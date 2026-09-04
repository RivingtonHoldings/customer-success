#!/usr/bin/env python3
"""Help center mirror tooling for /sync-help-center.

Read-only toward Intercom. Subcommands:

  probe     Build docs/help-center/collections.md by asking the public help center
            which help center owns each collection (200 = owner, 401 = not owner).
  plan      Diff the article inventory (list_articles JSON files) against the
            mirror's sync-state.json for one MLS and write a work plan.
  fetch     Fetch public article pages for the plan's published articles in small
            batches with backoff; resumable.
  ingest    Save a get_article JSON result (from the connector) for a draft or a
            fallback article into the work folder.
  build     Convert fetched bodies to markdown, write article files, README.md
            index, sync-state.json, and print the added/updated/removed/unchanged
            summary.
  verify    Compare a fetched public body against a get_article JSON body.

Run from the repo root. Work files live under the scratch folder passed with
--work (never inside the repo).
"""
import argparse, json, os, re, sys, time, hashlib, html, subprocess
from datetime import datetime, timezone
from html.parser import HTMLParser

REPO = os.getcwd()
HC = {
    'baldwin': {'id': 4755399, 'base': 'https://support.perchwell.com/baldwin/en', 'label': 'Baldwin'},
    'crmls':   {'id': 4767477, 'base': 'https://support.perchwell.com/crmls/en',   'label': 'CRMLS'},
    'default': {'id': 279383,  'base': 'https://support.perchwell.com/en',         'label': 'Default (NYC and brokerage)'},
}
COLL_MD = os.path.join(REPO, 'docs', 'help-center', 'collections.md')

def iso(ts):
    if not ts: return ''
    return datetime.fromtimestamp(int(ts), tz=timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

def now_iso():
    return datetime.now(tz=timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

def curl(url, out=None, retries=5):
    """GET with backoff on 429 and 5xx. Returns (code, body_text)."""
    for attempt in range(retries):
        args = ['curl', '-sS', '-L', '--max-time', '30', '-w', '\n%{http_code}', url]
        r = subprocess.run(args, capture_output=True, text=True)
        body, _, code = r.stdout.rpartition('\n')
        code = code.strip()
        if code in ('429',) or code.startswith('5'):
            time.sleep(min(60, 2 ** attempt * 2)); continue
        if out and code == '200':
            open(out, 'w').write(body)
        return code, body
    return code, body

# ---------- inventory ----------
def load_inventory(paths):
    arts = {}
    for p in paths:
        raw = open(p, errors='ignore').read()
        start = raw.find('{'); end = raw.rfind('}')
        data = json.loads(raw[start:end + 1])
        if isinstance(data, list):  # persisted tool-result wrapper
            data = json.loads(data[0]['text'])
        for a in data.get('articles', data.get('data', {}).get('articles', [])):
            arts[str(a['id'])] = a
    return arts

# ---------- collections.md ----------
def read_collections():
    """Parse collections.md into {collection_id: {'owner','name','parent'}}."""
    if not os.path.exists(COLL_MD):
        sys.exit('collections.md missing; run: probe')
    out = {}
    for line in open(COLL_MD):
        m = re.match(r'\|\s*(\d+)\s*\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|', line)
        if not m: continue
        cid, name, owner, parent, count = [x.strip() for x in m.groups()]
        out[cid] = {'name': name, 'owner': owner, 'parent': parent, 'count': count}
    return out

def cmd_probe(args):
    """Crawl each public help center home page and collection pages.
    Ownership comes from the 200/401 response; names from the collection page h1."""
    inv = load_inventory(args.inventory) if args.inventory else {}
    known = {p for a in inv.values() for p in (a.get('parent_ids') or [])}
    rows = {}
    for mls, cfg in HC.items():
        code, home = curl(cfg['base'] + '/')
        if code != '200':
            print(f'{mls}: home page returned {code}', file=sys.stderr); continue
        top = re.findall(r'/collections/(\d+)', home)
        queue = list(dict.fromkeys(top))
        seen = set()
        while queue:
            cid = queue.pop(0)
            if cid in seen: continue
            seen.add(cid)
            code, page = curl(f"{cfg['base']}/collections/{cid}")
            if code != '200': continue
            name = re.search(r'<h1[^>]*>(.*?)</h1>', page, re.S)
            name = html.unescape(re.sub(r'<[^>]+>', '', name.group(1))).strip() if name else ''
            arts = sorted(set(re.findall(r'/articles/(\d+)', page)))
            children = [c for c in dict.fromkeys(re.findall(r'/collections/(\d+)', page)) if c != cid and c not in seen]
            rows.setdefault(cid, {'name': name, 'owner': mls, 'parent': '', 'articles': set(), 'children': []})
            rows[cid]['articles'] |= set(arts)
            for ch in children:
                rows.setdefault(ch, {'name': '', 'owner': mls, 'parent': cid, 'articles': set(), 'children': []})
                if not rows[ch]['parent']: rows[ch]['parent'] = cid
                queue.append(ch)
            time.sleep(0.3)
    # collections referenced by articles but not reachable from any public home page
    for cid in sorted(known - set(map(int, rows.keys()))):
        owners = []
        for mls, cfg in HC.items():
            code, _ = curl(f"{cfg['base']}/collections/{cid}")
            if code == '200': owners.append(mls)
        rows[str(cid)] = {'name': '', 'owner': owners[0] if owners else 'none (401 everywhere)', 'parent': '', 'articles': set(), 'children': []}
    # write
    lines = ['# Help center collections', '',
             f'Generated by `/sync-help-center probe` on {now_iso()} from the public help center pages. '
             'Ownership rule: the owning help center returns 200 for `<base>/collections/<id>`, the others return 401. '
             'An article belongs to every help center that owns one of its collections. '
             'The sync reads this file; regenerate it with the probe subcommand when collections change.', '',
             '| Collection ID | Name | Owner | Parent collection | Published articles |', '|---|---|---|---|---|']
    order = sorted(rows.items(), key=lambda kv: (kv[1]['owner'], kv[1]['parent'] or '0', kv[1]['name']))
    for cid, r in order:
        lines.append(f"| {cid} | {r['name']} | {r['owner']} | {r['parent']} | {len(r['articles'])} |")
    lines += ['', 'Help center IDs: Baldwin 4755399, CRMLS 4767477, default 279383.']
    open(COLL_MD, 'w').write('\n'.join(lines) + '\n')
    json.dump({cid: {**r, 'articles': sorted(r['articles'])} for cid, r in rows.items()},
              open(os.path.join(args.work, 'collections_probe.json'), 'w'), indent=1)
    print(f'wrote {COLL_MD} with {len(rows)} collections')
    for mls in HC:
        ids = set()
        for r in rows.values():
            if r['owner'] == mls: ids |= r['articles']
        print(f'  {mls}: {sum(1 for r in rows.values() if r["owner"]==mls)} collections, {len(ids)} distinct published articles on the public site')

# ---------- membership ----------
def membership(inv, colls, mls):
    """Articles that belong to this MLS: any parent collection owned by it."""
    owned = {cid for cid, c in colls.items() if c['owner'] == mls}
    out = {}
    for aid, a in inv.items():
        pids = {str(p) for p in (a.get('parent_ids') or [])}
        mine = pids & owned
        if mine:
            out[aid] = sorted(mine)
    return out

def slugify(s):
    s = re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')
    return s[:80] or 'untitled'

def article_slug(a):
    u = a.get('url') or ''
    m = re.search(r'/articles/\d+-([a-z0-9-]+)', u)
    return m.group(1) if m else slugify(a.get('title') or '')

def state_path(mls):
    return os.path.join(REPO, 'docs', 'help-center', mls, 'sync-state.json')

def load_state(mls):
    p = state_path(mls)
    return json.load(open(p)) if os.path.exists(p) else {'last_run': None, 'help_center_id': HC[mls]['id'], 'articles': {}}

def cmd_plan(args):
    inv = load_inventory(args.inventory)
    colls = read_collections()
    mls = args.mls
    mem = membership(inv, colls, mls)
    state = load_state(mls)
    plan = {'mls': mls, 'generated': now_iso(), 'articles': {}, 'removed': []}
    for aid, cids in mem.items():
        a = inv[aid]
        prev = state['articles'].get(aid)
        if prev and prev.get('updated_at') == a['updated_at'] and prev.get('state') == a['state'] and os.path.exists(os.path.join(REPO, 'docs', 'help-center', mls, prev['file'])):
            action = 'unchanged'
        elif prev:
            action = 'updated'
        else:
            action = 'added'
        plan['articles'][aid] = {'action': action, 'state': a['state'], 'title': a['title'], 'updated_at': a['updated_at'], 'collections': cids, 'url': a.get('url')}
    for aid in state['articles']:
        if aid not in mem: plan['removed'].append(aid)
    os.makedirs(args.work, exist_ok=True)
    json.dump(plan, open(os.path.join(args.work, f'plan-{mls}.json'), 'w'), indent=1)
    json.dump({aid: inv[aid] for aid in mem}, open(os.path.join(args.work, f'inventory-{mls}.json'), 'w'), indent=1)
    c = {k: sum(1 for v in plan['articles'].values() if v['action'] == k) for k in ('added', 'updated', 'unchanged')}
    need_pub = [aid for aid, v in plan['articles'].items() if v['action'] != 'unchanged' and v['state'] == 'published']
    need_draft = [aid for aid, v in plan['articles'].items() if v['action'] != 'unchanged' and v['state'] == 'draft']
    print(f"{mls}: members={len(mem)} added={c['added']} updated={c['updated']} unchanged={c['unchanged']} removed={len(plan['removed'])}")
    print(f"  published bodies to fetch from the public site: {len(need_pub)}")
    print(f"  draft bodies to read with get_article (no public page): {len(need_draft)}")
    if need_draft:
        print('  draft ids: ' + ' '.join(need_draft))
    print(f"  total members by state: published={sum(1 for v in plan['articles'].values() if v['state']=='published')} draft={sum(1 for v in plan['articles'].values() if v['state']=='draft')}")

def cmd_fetch(args):
    mls = args.mls
    plan = json.load(open(os.path.join(args.work, f'plan-{mls}.json')))
    bodies = os.path.join(args.work, 'bodies'); os.makedirs(bodies, exist_ok=True)
    todo = [aid for aid, v in plan['articles'].items() if v['action'] != 'unchanged' and v['state'] == 'published']
    done = 0; failed = []
    for i in range(0, len(todo), args.batch):
        batch = todo[i:i + args.batch]
        for aid in batch:
            out = os.path.join(bodies, f'{aid}.public.html')
            if os.path.exists(out) and os.path.getsize(out) > 0:
                continue  # resume
            url = f"{HC[mls]['base']}/articles/{aid}"
            code, body = curl(url, out)
            if code != '200':
                failed.append((aid, code))
            else:
                done += 1
        time.sleep(args.pause)
        print(f'  fetched {min(i+args.batch, len(todo))}/{len(todo)}', flush=True)
    print(f'fetched {done} new bodies; already had {len(todo)-done-len(failed)}; failed {len(failed)}')
    for aid, code in failed:
        print(f'  FAILED {aid} ({code}): read it with get_article and save with: ingest {aid} <json file>')

def cmd_ingest(args):
    raw = open(args.file, errors='ignore').read()
    data = json.loads(raw[raw.find('{'):raw.rfind('}') + 1])
    if isinstance(data, list): data = json.loads(data[0]['text'])
    body = data.get('body')
    if isinstance(body, dict): body = body.get('value', '')
    bodies = os.path.join(args.work, 'bodies'); os.makedirs(bodies, exist_ok=True)
    open(os.path.join(bodies, f'{args.id}.api.html'), 'w').write(body or '')
    print(f'ingested {args.id} ({len(body or "")} chars)')

# ---------- HTML to markdown ----------
class MD(HTMLParser):
    BLOCK = {'p', 'div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol', 'li', 'blockquote', 'table', 'tr', 'pre', 'hr', 'article', 'section', 'iframe'}
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []; self.lists = []; self.callout = 0; self.href = None; self.link_text = []
        self.in_table = False; self.row = None; self.cell = None; self.table = []; self.pre = False; self.skip = 0; self.divs = []
    def text(self, s):
        if self.skip: return
        if self.cell is not None: self.cell.append(s); return
        if self.href is not None: self.link_text.append(s); return
        self.out.append(s)
    def nl(self, n=1):
        if self.cell is not None or self.href is not None: return
        joined = ''.join(self.out)
        while joined.endswith('\n' * (n + 1)): joined = joined[:-1]
        self.out = [joined.rstrip(' ')]
        if not joined.endswith('\n' * n): self.out.append('\n' * (n - (len(joined) - len(joined.rstrip('\n')))))
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ('script', 'style', 'svg', 'button'): self.skip += 1; return
        if self.skip: return
        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self.nl(2); self.text('#' * int(tag[1]) + ' ')
        elif tag == 'p':
            if self.lists and self.out and not ''.join(self.out).endswith(('\n', '. ', '- ', '> ')): self.text(' ')
            elif not self.lists:
                if self.callout:
                    j = ''.join(self.out)
                    if not j.endswith('> '):
                        self.nl(1); self.text('>\n> ')
                else:
                    self.nl(2)
        elif tag == 'br': self.text('  \n' + ('> ' if self.callout else ''))
        elif tag in ('ul', 'ol'):
            self.nl(2 if not self.lists else 1); self.lists.append([tag, 0])
        elif tag == 'li':
            self.nl(1)
            if self.callout: self.text('> ')
            if self.lists:
                self.lists[-1][1] += 1
                indent = '  ' * (len(self.lists) - 1)
                marker = '- ' if self.lists[-1][0] == 'ul' else f'{self.lists[-1][1]}. '
                self.text(indent + marker)
        elif tag in ('b', 'strong'): self.text('**')
        elif tag in ('i', 'em'): self.text('*')
        elif tag == 'code' and not self.pre: self.text('`')
        elif tag == 'pre': self.nl(2); self.text('```\n'); self.pre = True
        elif tag == 'a':
            self.href = a.get('href'); self.link_text = []
        elif tag == 'img':
            src = re.sub(r'\?expires=.*$', '', a.get('src', ''))
            alt = a.get('alt', '') or 'image'
            self.nl(2); self.text(f'![{alt}]({src})'); self.nl(2)
        elif tag == 'iframe':
            src = a.get('src', ''); self.nl(2); self.text(f'[Embedded video]({src})'); self.nl(2)
        elif tag == 'div':
            cls = a.get('class', '')
            is_callout = 'intercom-interblocks-callout' in cls
            self.divs.append(is_callout)
            if is_callout:
                self.nl(2); self.callout += 1; self.text('> ')
        elif tag == 'blockquote':
            self.nl(2); self.callout += 1; self.text('> ')
        elif tag == 'hr': self.nl(2)
        elif tag == 'table': self.in_table = True; self.table = []; self.nl(2)
        elif tag == 'tr': self.row = []
        elif tag in ('td', 'th'): self.cell = []
    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'svg', 'button'): self.skip = max(0, self.skip - 1); return
        if self.skip: return
        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'): self.nl(2)
        elif tag == 'p':
            if not self.lists: self.nl(2)
        elif tag in ('ul', 'ol'):
            if self.lists: self.lists.pop()
            self.nl(2 if not self.lists else 1)
        elif tag == 'li': self.nl(1)
        elif tag in ('b', 'strong'): self.text('**')
        elif tag in ('i', 'em'): self.text('*')
        elif tag == 'code' and not self.pre: self.text('`')
        elif tag == 'pre': self.text('\n```'); self.pre = False; self.nl(2)
        elif tag == 'a':
            txt = ''.join(self.link_text).strip(); href = self.href; self.href = None
            if href and txt: self.text(f'[{txt}]({href})')
            elif txt: self.text(txt)
        elif tag == 'div':
            was = self.divs.pop() if self.divs else False
            if was and self.callout: self.callout -= 1; self.nl(2)
        elif tag == 'blockquote':
            if self.callout: self.callout -= 1
            self.nl(2)
        elif tag in ('td', 'th'):
            self.row.append(' '.join(''.join(self.cell).split())); self.cell = None
        elif tag == 'tr':
            if self.row is not None: self.table.append(self.row); self.row = None
        elif tag == 'table':
            self.in_table = False
            if self.table:
                w = max(len(r) for r in self.table)
                rows = [r + [''] * (w - len(r)) for r in self.table]
                lines = ['| ' + ' | '.join(rows[0]) + ' |', '|' + '---|' * w] + ['| ' + ' | '.join(r) + ' |' for r in rows[1:]]
                self.text('\n'.join(lines)); self.nl(2)
    def handle_data(self, data):
        if self.pre: self.text(data); return
        s = re.sub(r'\s+', ' ', data)
        if s.strip() == '' and not self.out: return
        self.text(s)

def html_to_md(h):
    # Intercom callouts are divs; make them explicit so the parser can close them.
    p = MD(); p.feed(h); p.close()
    md = ''.join(p.out)
    md = re.sub(r'[ \t]+\n', '\n', md)
    md = re.sub(r'\n{3,}', '\n\n', md)
    md = md.replace(' ', ' ')
    return md.strip() + '\n'

def extract_public_body(page):
    m = re.search(r'<article[^>]*>(.*?)</article>', page, re.S)
    if not m: return None
    body = m.group(1)
    # drop Intercom's "Related Articles" block, which is navigation, not article content
    body = re.split(r'<section[^>]*related_articles', body)[0]
    return body

def yaml_str(s):
    return json.dumps(s if s is not None else '')

def cmd_build(args):
    mls = args.mls
    folder = os.path.join(REPO, 'docs', 'help-center', mls)
    os.makedirs(folder, exist_ok=True)
    plan = json.load(open(os.path.join(args.work, f'plan-{mls}.json')))
    inv = json.load(open(os.path.join(args.work, f'inventory-{mls}.json')))
    colls = read_collections()
    state = load_state(mls)
    bodies = os.path.join(args.work, 'bodies')
    used = {}
    for aid, prev in state['articles'].items():
        if aid in plan['articles'] and plan['articles'][aid]['action'] == 'unchanged':
            used[prev['file']] = aid
    summary = {'added': [], 'updated': [], 'removed': [], 'unchanged': [], 'missing_body': []}
    new_state = {'last_run': now_iso(), 'help_center_id': HC[mls]['id'], 'source': 'metadata from Intercom list_articles; bodies from the public help center (published) and get_article (drafts)', 'articles': {}}
    for aid, item in plan['articles'].items():
        a = inv[aid]
        if item['action'] == 'unchanged':
            new_state['articles'][aid] = state['articles'][aid]; summary['unchanged'].append(aid); continue
        src = None; kind = None
        for suffix, k in (('.api.html', 'intercom-api'), ('.public.html', 'public-help-center')):
            p = os.path.join(bodies, f'{aid}{suffix}')
            if os.path.exists(p):
                src = open(p, errors='ignore').read(); kind = k
                if k == 'public-help-center':
                    src = extract_public_body(src) or ''
                break
        if src is None:
            summary['missing_body'].append(aid)
            if aid in state['articles']:
                new_state['articles'][aid] = state['articles'][aid]
            continue
        body_md = html_to_md(src)
        # filename
        base = article_slug(a)
        fname = base + '.md'
        if fname in used and used[fname] != aid: fname = f'{base}-{aid}.md'
        used[fname] = aid
        cnames = [colls.get(c, {}).get('name', '') or c for c in item['collections']]
        labels = [t['name'] for t in (a.get('tags') or {}).get('tags', [])]
        fm = [
            '---',
            f'intercom_id: "{aid}"',
            f'content_id: "{a.get("content_id", "")}"',
            f'title: {yaml_str(a.get("title"))}',
            f'description: {yaml_str(a.get("description") or "")}',
            f'url: {yaml_str(a.get("url") or "")}',
            f'help_center: {mls}',
            f'help_center_id: {HC[mls]["id"]}',
            f'collection: {yaml_str(cnames[0] if cnames else "")}',
            f'collection_ids: [{", ".join(item["collections"])}]',
            f'collections: [{", ".join(yaml_str(c) for c in cnames)}]',
            f'state: {a.get("state")}',
            f'author_id: {a.get("author_id")}',
            f'created_at: {iso(a.get("created_at"))}',
            f'updated_at: {iso(a.get("updated_at"))}',
            f'labels: [{", ".join(yaml_str(l) for l in labels)}]',
            f'body_source: {kind}',
            f'synced_at: {new_state["last_run"]}',
            '---', '',
            f'# {a.get("title")}', '', '',
        ]
        content = '\n'.join(fm) + body_md
        open(os.path.join(folder, fname), 'w').write(content)
        new_state['articles'][aid] = {'file': fname, 'updated_at': a['updated_at'], 'state': a['state'], 'title': a['title'], 'content_id': a.get('content_id'), 'body_sha1': hashlib.sha1(body_md.encode()).hexdigest()}
        summary[item['action']].append(aid)
    for aid in plan['removed']:
        prev = state['articles'].get(aid)
        if prev:
            p = os.path.join(folder, prev['file'])
            if os.path.exists(p): os.remove(p)
        summary['removed'].append(aid)
    # README index grouped by collection
    groups = {}
    for aid, st in new_state['articles'].items():
        a = inv.get(aid)
        if not a: continue
        cids = plan['articles'][aid]['collections'] if aid in plan['articles'] else []
        for c in (cids or ['none']):
            groups.setdefault(c, []).append((a['title'], st['file'], a['state'], iso(a['updated_at'])[:10]))
    lines = [f"# {HC[mls]['label']} help center mirror", '',
             f"Read-only mirror of the live Intercom help center (help center ID {HC[mls]['id']}). Refreshed by `/sync-help-center`; do not edit these files by hand. Last sync: {new_state['last_run']}. Articles: {len(new_state['articles'])} ({sum(1 for s in new_state['articles'].values() if s['state']=='published')} published, {sum(1 for s in new_state['articles'].values() if s['state']=='draft')} draft).", '',
             'Each file carries frontmatter with the Intercom article ID, the content ID Fin cites, title, public URL, collections, state, author ID, timestamps, and labels. Image links point at Intercom\'s CDN without the expiring signature, so they may need an Intercom login to open.', '']
    def cname(c): return colls.get(c, {}).get('name') or f'Collection {c}'
    for c in sorted(groups, key=lambda x: (colls.get(x, {}).get('parent') or '', cname(x))):
        parent = colls.get(c, {}).get('parent')
        title = cname(c) + (f' (under {cname(parent)})' if parent else '')
        lines += [f'## {title}', '', f'Collection ID {c}. {len(groups[c])} articles.', '']
        for t, f, s, u in sorted(groups[c]):
            lines.append(f'- [{t}]({f}){"" if s == "published" else " (draft)"}, updated {u}')
        lines.append('')
    open(os.path.join(folder, 'README.md'), 'w').write('\n'.join(lines))
    json.dump(new_state, open(state_path(mls), 'w'), indent=1)
    print(f"{HC[mls]['label']}: added {len(summary['added'])}, updated {len(summary['updated'])}, removed {len(summary['removed'])}, unchanged {len(summary['unchanged'])}, missing body {len(summary['missing_body'])}; total {len(new_state['articles'])}")
    if summary['missing_body']:
        print('  missing bodies (not written): ' + ' '.join(summary['missing_body']))
    json.dump(summary, open(os.path.join(args.work, f'summary-{mls}.json'), 'w'), indent=1)

def norm_text(h):
    t = re.sub(r'<[^>]+>', ' ', h); t = html.unescape(t); return re.sub(r'\s+', ' ', t).strip()

def cmd_verify(args):
    pub = extract_public_body(open(os.path.join(args.work, 'bodies', f'{args.id}.public.html')).read()) or ''
    raw = open(args.file).read(); data = json.loads(raw[raw.find('{'):raw.rfind('}') + 1])
    if isinstance(data, list): data = json.loads(data[0]['text'])
    api = data['body']['value'] if isinstance(data.get('body'), dict) else data.get('body', '')
    a, b = norm_text(pub), norm_text(api)
    print(f'{args.id}: public {len(a)} chars, api {len(b)} chars, identical text: {a == b}')
    if a != b:
        import difflib
        for l in list(difflib.unified_diff(b.split('. '), a.split('. '), 'api', 'public', lineterm=''))[:30]: print(l)

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('probe'); p.add_argument('--work', required=True); p.add_argument('--inventory', nargs='*'); p.set_defaults(f=cmd_probe)
    p = sub.add_parser('plan'); p.add_argument('--mls', required=True, choices=list(HC)); p.add_argument('--work', required=True); p.add_argument('--inventory', nargs='+', required=True); p.set_defaults(f=cmd_plan)
    p = sub.add_parser('fetch'); p.add_argument('--mls', required=True, choices=list(HC)); p.add_argument('--work', required=True); p.add_argument('--batch', type=int, default=10); p.add_argument('--pause', type=float, default=1.0); p.set_defaults(f=cmd_fetch)
    p = sub.add_parser('ingest'); p.add_argument('id'); p.add_argument('file'); p.add_argument('--work', required=True); p.set_defaults(f=cmd_ingest)
    p = sub.add_parser('build'); p.add_argument('--mls', required=True, choices=list(HC)); p.add_argument('--work', required=True); p.set_defaults(f=cmd_build)
    p = sub.add_parser('verify'); p.add_argument('id'); p.add_argument('file'); p.add_argument('--work', required=True); p.set_defaults(f=cmd_verify)
    a = ap.parse_args(); a.f(a)
