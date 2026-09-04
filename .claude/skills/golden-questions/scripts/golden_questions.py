#!/usr/bin/env python3
"""Golden questions tooling for /golden-questions. Read-only toward Intercom.

Subcommands (run from the repo root):
  pool     Filter search_conversations result files down to Baldwin Fin conversations in a date window.
  sample   Pick N conversations spread across the window.
  ingest   Store one get_conversation result (reduced to the parts that matter) in the confidential run folder.
  extract  Per conversation: member question(s), topic, Fin answered, teammate stepped in, cited articles,
           Intercom resolution state, Perchwell resolution. Writes raw + scrubbed views (both confidential).
  check    Scan a committed file for emails, phone numbers, and every member or teammate name seen in the run.

Everything this script writes goes under workstreams/help-center-overhaul/confidential/golden-questions/<run>/.
The committed golden-question-set.md is written by Claude from the scrubbed extract, then verified with `check`.
"""
import argparse, json, os, re, sys, html, random, glob
from datetime import datetime, timezone, timedelta

REPO = os.getcwd()
CONF = os.path.join(REPO, 'workstreams', 'help-center-overhaul', 'confidential', 'golden-questions')
MIRROR = os.path.join(REPO, 'docs', 'help-center')
BALDWIN_WORKFLOW = '(Members) Baldwin | Support Bot Workflow NEW'

def ts(s):
    return int(datetime.strptime(s, '%Y-%m-%d').replace(tzinfo=timezone.utc).timestamp())

def iso(t):
    return datetime.fromtimestamp(int(t), tz=timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ') if t else ''

def load_json_file(p):
    raw = open(p, errors='ignore').read().strip()
    if raw.startswith('['):  # persisted tool-result wrapper: [{"type": "text", "text": "<json>"}]
        return json.loads(json.loads(raw)[0]['text'])
    start = raw.find('{'); end = raw.rfind('}')
    data = json.loads(raw[start:end + 1])
    if isinstance(data, dict) and data.get('type') == 'text' and 'text' in data: return json.loads(data['text'])
    return data

def run_dir(run):
    d = os.path.join(CONF, run); os.makedirs(os.path.join(d, 'conversations'), exist_ok=True); return d

def strip_html(h):
    t = re.sub(r'<br\s*/?>', '\n', h or ''); t = re.sub(r'</p>', '\n', t); t = re.sub(r'<[^>]+>', '', t)
    return re.sub(r'\n{2,}', '\n', html.unescape(t)).strip()

# ---------- pool ----------
def cmd_pool(args):
    since, until = ts(args.since), ts(args.until) + 86400  # until is inclusive
    pool = {}
    for f in args.search_results:
        data = load_json_file(f)
        # compact rows from the `search` DSL tool (id, text, url only; the query itself bounded the window and workflow)
        for r in data.get('results', []):
            cid = r['id'].replace('conversation_', '')
            txt = r.get('text', '')
            m = re.search(r'Author: (.*?) \((.*?)\)', txt); st = re.search(r'State: (\w+)', txt)
            body = re.search(r'Body: (.*)', txt); tags = re.search(r'Tags: (.*)', txt)
            if m and m.group(2).lower().endswith('@perchwell.com'): continue  # internal test traffic
            pool[cid] = {'id': cid, 'created_at': None, 'created': '', 'state': st.group(1) if st else None,
                         'member_name': m.group(1) if m else None, 'member_email': m.group(2) if m else None,
                         'contact_ids': re.findall(r'Contact IDs: (.*)', txt)[:1], 'first_message': strip_html(body.group(1)) if body else '',
                         'page_url': None, 'tags': [t.strip() for t in tags.group(1).split(',')] if tags else [],
                         'ai_title': None, 'part_of_platform': None, 'type_of_request': None, 'fin_resolution_state_attr': None,
                         'fin_escalated_reason': None, 'ai_agent': {'resolution_state': None, 'source_title': BALDWIN_WORKFLOW},
                         'content_sources': [], 'first_admin_reply_at': None, 'teammate_ids': [], 'shape': 'search-dsl'}
        for c in data.get('conversations', []):
            ca = c.get('custom_attributes') or {}
            ag = c.get('ai_agent') or {}
            if ca.get('MLS') != 'Baldwin' and ag.get('source_title') != BALDWIN_WORKFLOW: continue
            if ca.get('MLS') == 'Test / Internal' or ca.get('Type of Request') == 'Internal / Test / Spam': continue
            if ((src.get('author') or {}).get('email') or '').lower().endswith('@perchwell.com'): continue
            if not c.get('ai_agent_participated'): continue
            if not (since <= c['created_at'] < until): continue
            src = c.get('source') or {}
            pool[c['id']] = {
                'id': c['id'], 'created_at': c['created_at'], 'created': iso(c['created_at']), 'state': c['state'],
                'member_name': (src.get('author') or {}).get('name'), 'member_email': (src.get('author') or {}).get('email'),
                'contact_ids': [x.get('id') for x in (c.get('contacts') or {}).get('contacts', [])],
                'first_message': strip_html(src.get('body')), 'page_url': src.get('url'),
                'tags': [t['name'] for t in (c.get('tags') or {}).get('tags', [])],
                'ai_title': ca.get('AI Title'), 'part_of_platform': ca.get('Part of the Platform'), 'type_of_request': ca.get('Type of Request'),
                'fin_resolution_state_attr': ca.get('Fin AI Agent resolution state'), 'fin_escalated_reason': ca.get('Fin AI Agent escalated reason'),
                'ai_agent': {k: ag.get(k) for k in ('resolution_state', 'last_answer_type', 'rating', 'source_title')},
                'content_sources': [(s.get('url', '').split('id=')[-1], s.get('title')) for s in (ag.get('content_sources') or {}).get('content_sources', [])],
                'first_admin_reply_at': (c.get('statistics') or {}).get('first_admin_reply_at'),
                'teammate_ids': [a['id'] for a in (c.get('teammates') or {}).get('admins', [])],
            }
    d = run_dir(args.run)
    json.dump({'since': args.since, 'until': args.until, 'built': iso(datetime.now(tz=timezone.utc).timestamp()), 'conversations': pool}, open(os.path.join(d, 'pool.json'), 'w'), indent=1)
    from collections import Counter
    print(f'pool: {len(pool)} Baldwin Fin conversations created {args.since} to {args.until} (inclusive)')
    print('  by Intercom resolution_state:', dict(Counter(v['ai_agent']['resolution_state'] for v in pool.values())))
    print('  by part of platform:', dict(Counter(v['part_of_platform'] for v in pool.values()).most_common(12)))
    days = Counter(v['created'][:10] or 'unknown (compact rows)' for v in pool.values()); print('  by day:', dict(sorted(days.items())))
    print('  tagged FIN unsuccessful:', sum(1 for v in pool.values() if any('Unsuccessfully' in t for t in v['tags'])))

# ---------- sample ----------
def cmd_sample(args):
    d = run_dir(args.run)
    pool = json.load(open(os.path.join(d, 'pool.json')))['conversations']
    rnd = random.Random(args.seed)
    by_day = {}
    if all(not v.get('created') for v in pool.values()):
        ordered = sorted(pool, key=int); k = max(1, len(ordered) // args.n)
        for i, cid in enumerate(ordered): by_day.setdefault(f'bucket-{i // k:02d}', []).append(cid)
    else:
        for v in pool.values(): by_day.setdefault(v['created'][:10], []).append(v['id'])
    days = sorted(by_day); picks = []
    sp = os.path.join(d, 'sample.json')
    if args.top_up and os.path.exists(sp):
        picks = [i for i in json.load(open(sp))['ids'] if i in pool]
        for day in by_day: by_day[day] = [i for i in by_day[day] if i not in picks]
    # round-robin across days so the sample spans the window instead of clustering on the busiest day
    order = {day: rnd.sample(ids, len(ids)) for day, ids in by_day.items()}
    while len(picks) < args.n and any(order.values()):
        for day in days:
            if order[day] and len(picks) < args.n: picks.append(order[day].pop())
    json.dump({'n': len(picks), 'seed': args.seed, 'ids': picks}, open(os.path.join(d, 'sample.json'), 'w'), indent=1)
    print(f'sampled {len(picks)} of {len(pool)}:')
    print(' '.join(picks))

# ---------- ingest ----------
KEEP_TYPES = {'comment', 'assignment', 'close', 'open', 'note', 'snoozed', 'unsnoozed', 'conversation_tags_updated', 'fin_guidance_applied'}
def cmd_ingest(args):
    d = run_dir(args.run)
    c = load_json_file(args.file)
    parts = []
    for p in (c.get('conversation_parts') or {}).get('conversation_parts', []):
        if p.get('part_type') not in KEEP_TYPES and not p.get('body'): continue
        au = p.get('author') or {}
        parts.append({'id': p.get('id'), 'part_type': p.get('part_type'), 'created_at': p.get('created_at'),
                      'author_type': au.get('type'), 'author_name': au.get('name'), 'author_id': au.get('id'),
                      'from_ai_agent': au.get('from_ai_agent'), 'is_ai_answer': au.get('is_ai_answer'),
                      'body_html': p.get('body'), 'body_text': strip_html(p.get('body')),
                      'quick_reply_option_uuid': (p.get('metadata') or {}).get('quick_reply_option_uuid'),
                      'event_details': p.get('event_details') or {}})
    src = c.get('source') or {}
    out = {'id': c['id'], 'created_at': c['created_at'], 'state': c['state'], 'tags': [t['name'] for t in (c.get('tags') or {}).get('tags', [])],
           'source': {'body': src.get('body'), 'url': src.get('url'), 'author': src.get('author')},
           'contacts': (c.get('contacts') or {}).get('contacts', []), 'custom_attributes': c.get('custom_attributes') or {},
           'ai_agent': c.get('ai_agent') or {}, 'ai_agent_participated': c.get('ai_agent_participated'),
           'statistics': c.get('statistics') or {}, 'teammates': (c.get('teammates') or {}).get('admins', []),
           'conversation_parts': parts, 'part_count_total': (c.get('conversation_parts') or {}).get('total_count')}
    json.dump(out, open(os.path.join(d, 'conversations', f"{c['id']}.json"), 'w'), indent=1)
    print(f"ingested {c['id']}: {len(parts)} parts kept of {out['part_count_total']}")

# ---------- extract ----------
def mirror_index():
    idx = {}
    for mls in ('baldwin', 'crmls'):
        p = os.path.join(MIRROR, mls, 'sync-state.json')
        if not os.path.exists(p): continue
        for aid, st in json.load(open(p))['articles'].items():
            idx.setdefault(str(st.get('content_id')), {})[mls] = {'id': aid, 'title': st['title'], 'file': f'docs/help-center/{mls}/{st["file"]}'}
            idx.setdefault('title:' + st['title'].strip().lower(), {})[mls] = {'id': aid, 'title': st['title'], 'file': f'docs/help-center/{mls}/{st["file"]}'}
    return idx

ACK_WORDS = {'thanks', 'thank', 'you', 'got', 'it', 'ok', 'okay', 'perfect', 'great', 'yes', 'yep', 'yrs', 'yea', 'awesome', 'will', 'do', 'that', 'helped', 'helps', 'sounds', 'good', 'so', 'much', 'ty', 'thx', 'appreciate', 'i'}
def is_ack(text):
    words = re.findall(r"[a-z']+", text.lower())
    return bool(words) and len(words) <= 8 and all(w in ACK_WORDS for w in words)
QUICK_REPLIES = {"let's get started", 'how to use perchwell', 'paragon vs. perchwell', 'migrating my data to perchwell', 'report an issue', 'integrations', 'idx & data syndication', 'mls rules or violations', 'share feedback', 'call mls team', 'something else', 'yes', 'no', 'that helped', 'wait for the team'}

def cmd_extract(args):
    d = run_dir(args.run)
    idx = mirror_index()
    files = sorted(glob.glob(os.path.join(d, 'conversations', '*.json')))
    rows = []; names = set(); skipped = []
    for f in files:
        c = json.load(open(f))
        ca0 = c.get('custom_attributes') or {}
        if ca0.get('MLS') == 'Test / Internal' or ca0.get('Type of Request') == 'Internal / Test / Spam' or (((c.get('source') or {}).get('author') or {}).get('email') or '').lower().endswith('@perchwell.com'):
            skipped.append(c['id']); continue
        parts = c['conversation_parts']
        member_msgs = [p for p in parts if p['author_type'] == 'user' and p['part_type'] == 'comment' and p['body_text'] and not p['quick_reply_option_uuid'] and p['body_text'].strip().lower() not in QUICK_REPLIES]
        fin_answers = [p for p in parts if p.get('is_ai_answer')]
        teammate_msgs = [p for p in parts if p['author_type'] == 'admin' and p['body_text'] and p['part_type'] in ('comment', 'assignment', 'note')]
        for p in parts:
            if p['author_type'] == 'user' and p['author_name']: names.add(p['author_name'])
            if p['author_type'] == 'admin' and p['author_name']: names.add(p['author_name'])
        au = (c['source'] or {}).get('author') or {}
        if au.get('name'): names.add(au['name'])
        # citations: content_sources (content ids) + inline links in Fin answers
        cited = []
        for s in (c['ai_agent'].get('content_sources') or {}).get('content_sources', []):
            cid = s.get('url', '').split('id=')[-1]; cited.append({'content_id': cid, 'title': s.get('title'), 'mirror': idx.get(cid)})
        inline = set()
        for p in fin_answers:
            for m in re.finditer(r'data-entity-id="(\d+)"', p['body_html'] or ''): inline.add(m.group(1))
        # Perchwell resolution: Fin answered, no teammate message after Fin's last answer, no member follow-up within 48h after it
        last_fin = max((p['created_at'] for p in fin_answers), default=None)
        perch = None; reason = ''
        if not fin_answers:
            perch = False; reason = 'Fin gave no answer'
        else:
            tm_after = [p for p in teammate_msgs if p['created_at'] > last_fin]
            # a bare acknowledgement ("thanks", "yes", "got it") is not a same-topic follow-up
            member_after = [p for p in member_msgs if last_fin < p['created_at'] <= last_fin + 48 * 3600 and not is_ack(p['body_text'])]
            if tm_after: perch = False; reason = 'teammate messaged after Fin'
            elif member_after: perch = False; reason = 'member followed up within 48h'
            else: perch = True; reason = 'Fin answered, no teammate message, no member follow-up within 48h'
        rows.append({
            'id': c['id'], 'created': iso(c['created_at']), 'state': c['state'], 'tags': c['tags'],
            'topic': {'ai_title': c['custom_attributes'].get('AI Title'), 'part_of_platform': c['custom_attributes'].get('Part of the Platform'), 'type_of_request': c['custom_attributes'].get('Type of Request')},
            'member_questions': [{'at': iso(p['created_at']), 'text': p['body_text']} for p in member_msgs],
            'fin_answered': bool(fin_answers), 'fin_answer_count': len(fin_answers),
            'fin_answers': [{'at': iso(p['created_at']), 'text': p['body_text'][:1200]} for p in fin_answers],
            'teammate_stepped_in': bool(teammate_msgs), 'teammate_message_count': len(teammate_msgs),
            'teammate_messages': [{'at': iso(p['created_at']), 'text': p['body_text'][:600]} for p in teammate_msgs],
            'cited_articles': cited, 'inline_cited_content_ids': sorted(inline),
            'intercom_resolution_state': c['ai_agent'].get('resolution_state'), 'intercom_resolution_attr': c['custom_attributes'].get('Fin AI Agent resolution state'),
            'perchwell_resolved': perch, 'perchwell_resolution_reason': reason,
        })
    json.dump({'rows': rows, 'names_seen': sorted(names)}, open(os.path.join(d, 'extracted.json'), 'w'), indent=1)
    # scrubbed view for clustering
    scrub = make_scrubber(names)
    lines = [f'# Scrubbed extract for run {args.run} (still confidential; do not commit)', '']
    for r in rows:
        lines += [f"## {r['id']} | {r['created'][:10]} | {r['topic']['part_of_platform']} | AI title: {r['topic']['ai_title']} | Intercom: {r['intercom_resolution_state']} | Perchwell resolved: {r['perchwell_resolved']} ({r['perchwell_resolution_reason']})", '']
        for q in r['member_questions']: lines.append(f"- MEMBER: {scrub(q['text'])}")
        for a in r['fin_answers']: lines.append(f"- FIN: {scrub(a['text'])[:500]}")
        for t in r['teammate_messages']: lines.append(f"- TEAMMATE: {scrub(t['text'])[:300]}")
        cites = ', '.join(f"{c['title']} [{c['content_id']}" + (f" -> {c['mirror']['baldwin']['file']}" if c.get('mirror') and c['mirror'].get('baldwin') else ' -> not in Baldwin mirror') + ']' for c in r['cited_articles']) or 'none'
        lines.append(f'- CITED: {cites}'); lines.append('')
    open(os.path.join(d, 'extract-scrubbed.md'), 'w').write('\n'.join(lines))
    from collections import Counter
    print(f'extracted {len(rows)} conversations; names seen: {len(names)}; skipped as internal test traffic: {skipped}')
    print('  Fin answered:', sum(r['fin_answered'] for r in rows), '| teammate stepped in:', sum(r['teammate_stepped_in'] for r in rows))
    print('  Intercom resolution:', dict(Counter(r['intercom_resolution_state'] for r in rows)))
    print('  Perchwell resolved:', dict(Counter(r['perchwell_resolved'] for r in rows)))
    print(f"  scrubbed view: {os.path.relpath(os.path.join(d, 'extract-scrubbed.md'), REPO)}")

EMAIL = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')
PHONE = re.compile(r'(?<!\d)(?:\+?1[\s.-]?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}(?!\d)')
ADDRESS = re.compile(r'\b\d{1,6}\s+(?:[A-Z][a-z]+\s){1,4}(?:St|Street|Ave|Avenue|Rd|Road|Dr|Drive|Ln|Lane|Blvd|Ct|Court|Cir|Circle|Way|Hwy|Pl|Place|Pkwy|Trail|Trl|Loop)\b\.?', re.I)
MLSID = re.compile(r'\b(?:MLS\s*(?:#|ID|number)?\s*:?\s*)?\d{6,8}\b')

def make_scrubber(names):
    ordered = sorted({n for n in names if n and len(n) > 2}, key=len, reverse=True)
    firsts = sorted({n.split()[0] for n in ordered if len(n.split()[0]) > 2}, key=len, reverse=True)
    def scrub(t):
        t = EMAIL.sub('[email]', t); t = PHONE.sub('[phone]', t); t = ADDRESS.sub('[address]', t); t = MLSID.sub('[mls id]', t)
        for n in ordered: t = re.sub(re.escape(n), 'the member', t, flags=re.I)
        for n in firsts: t = re.sub(r'\b' + re.escape(n) + r'\b', 'the member', t)
        return t
    return scrub

COMMON_WORD_NAMES = {'will', 'hope', 'grace', 'faith', 'chase', 'mark', 'bill', 'dawn', 'rose', 'summer', 'dean', 'gene', 'june', 'april', 'august', 'grant', 'sandy', 'candy', 'penny', 'holly', 'brook', 'lane', 'mike', 'rich', 'jack', 'jimmy', 'chip', 'buck', 'wade', 'reed', 'cliff', 'clay', 'frank', 'earl', 'duke', 'king', 'young', 'long', 'field', 'fields', 'hunter', 'carter', 'baker', 'cook', 'mason', 'miles', 'page', 'pierce', 'price', 'sharp', 'stone', 'wells', 'west', 'north', 'south', 'east', 'major', 'sterling', 'star', 'sky', 'storm', 'river', 'rain', 'may', 'sue', 'don', 'joy', 'pat', 'kelly', 'ray', 'art', 'guy'}

def cmd_check(args):
    d = run_dir(args.run)
    names = set()
    p = os.path.join(d, 'extracted.json')
    if os.path.exists(p): names |= set(json.load(open(p)).get('names_seen', []))
    pp = os.path.join(d, 'pool.json')
    if os.path.exists(pp):
        for v in json.load(open(pp))['conversations'].values():
            if v.get('member_name'): names.add(v['member_name'])
    text = open(args.file).read()
    hits = []
    for m in EMAIL.finditer(text): hits.append(('email', m.group(0)))
    for m in PHONE.finditer(text): hits.append(('phone', m.group(0)))
    for n in sorted(names, key=len, reverse=True):
        if n and re.search(re.escape(n), text, re.I): hits.append(('name', n))
        first = n.split()[0] if n else ''
        # first names that are also ordinary English words produce false positives on their own
        if len(first) > 3 and first.lower() not in COMMON_WORD_NAMES and re.search(r'\b' + re.escape(first) + r'\b', text): hits.append(('first name', first))
    if hits:
        print(f'{len(hits)} possible identifier(s) in {args.file}:')
        for k, v in hits: print(f'  {k}: {v}')
        sys.exit(1)
    print(f'clean: no emails, phone numbers, or names from this run found in {args.file}')

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('pool'); p.add_argument('--run', required=True); p.add_argument('--since', required=True); p.add_argument('--until', required=True); p.add_argument('--search-results', nargs='+', required=True); p.set_defaults(f=cmd_pool)
    p = sub.add_parser('sample'); p.add_argument('--run', required=True); p.add_argument('--n', type=int, default=25); p.add_argument('--seed', type=int, default=2026); p.add_argument('--top-up', action='store_true', help='keep the existing sample and add picks until n'); p.set_defaults(f=cmd_sample)
    p = sub.add_parser('ingest'); p.add_argument('--run', required=True); p.add_argument('file'); p.set_defaults(f=cmd_ingest)
    p = sub.add_parser('extract'); p.add_argument('--run', required=True); p.set_defaults(f=cmd_extract)
    p = sub.add_parser('check'); p.add_argument('--run', required=True); p.add_argument('file'); p.set_defaults(f=cmd_check)
    a = ap.parse_args(); a.f(a)
