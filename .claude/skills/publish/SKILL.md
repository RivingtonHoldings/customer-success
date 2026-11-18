---
name: publish
description: Publish one approved Perchwell help center article to one or more MLS help centers in Intercom, with a plain-language preview first. Use whenever a teammate types /publish, or says "publish this to Baldwin," "publish to CRMLS," "publish to both," "publish to all MLSs," "update the live article for Baldwin and CRMLS," or names an MLS and an article to push. Resolves which MLSs are meant, checks readiness, shows what would change in plain words (text, screenshots, video, links, anything needing attention), then runs /port-to-intercom for each MLS with its own confirmations. Adds no way to write to Intercom of its own and never sets an article to published.
---

# Publish

A thin wrapper around `/port-to-intercom` (`.claude/skills/port-to-intercom/SKILL.md`). It decides which MLSs a run covers, checks what would happen for each, shows Tara or the teammate a plain-language preview, and then hands each MLS to `/port-to-intercom`, which does every conversion, push, changelog line, Notion close-out, media record, and mirror sync. `/publish` writes nothing to Intercom, Notion, or the repo itself. If a rule here and a rule in `/port-to-intercom` ever differ, `/port-to-intercom` wins, because it is the only skill that writes.

Notion is the source of truth. Every run fetches the Notion row fresh.

## Inputs

`/publish <scope> <article>`, one article per run.

- **Scope** (required):
  - `baldwin`, `crmls`, or any slug in `docs/help-center/mls-registry.md`: that MLS's record only.
  - `both`: always exactly Baldwin, then CRMLS, in that order, regardless of what else is registered.
  - `all`: every MLS that is registered, listed on the article's Notion `MLS` field, and marked `Yes` in the readiness table. Each MLS skipped is listed with the reason (not on the row, not registered, readiness `No` or `Paused`).
  - No scope: ask which; never assume one.
- **Article** (required): a Tracker ID (such as TRK-095), a Notion page URL, or an exact title. More than one article is refused: "`/publish` takes one article per run. Which one first?" A title that matches more than one row is refused and the matching Tracker IDs are listed.
- **Hints** (optional): "preview" shows the preview and stops, so nothing is written.

Each Notion row is its own article. If the scope names an MLS the row's `MLS` field does not list (for example `/publish baldwin TRK-127`, a CRMLS-only row), refuse and say so. For `both`, the row must list both; if it lists only one, say which is missing and offer that one MLS instead.

## Workflow

1. **Resolve the row and the MLS list.** Fetch the Notion row. Resolve the scope to a list of MLS slugs from the registry, in registry order (`both` is fixed to Baldwin then CRMLS). Read the readiness table as `/port-to-intercom` step 3 describes. Under `all`, drop any MLS that fails the three conditions and list it.

2. **Check each MLS without writing.** For every MLS in the list, run `/port-to-intercom` steps 1 to 5 as a preflight, including its preconditions, the update-or-create decision (a filled URL field is an update and is never created again), the media classification against the media record, and the link sort. A precondition failure for one MLS is reported with its plain reason and that MLS is dropped from this run; the others continue. A refusal that names a fix (for example a `Draft` row with its article already published) says what to change in Notion and that this command never changes the status itself.

3. **Is there anything to publish?** For each MLS that is an update, compare the converted body, title, and description with the live article from `get_article`, ignoring whitespace-only differences (Baldwin live bodies have no empty spacer paragraphs and the converter's house spacing adds them). If nothing differs and the Notion page has not been edited since the media record's `notion_last_edited`, say "Nothing to publish for <MLS>" and drop that MLS. The converter's spacing is applied only when something real changed.

4. **Show the preview.** Plain language. No HTML, no raw diff, no field names. The full before-and-after diff comes later, in `/port-to-intercom`'s own confirmation. Use this shape, filling in only what applies:

   ```
   Publish: <Article Name>   (Notion row <Tracker ID>, Review <review status>)

   Ready to publish: <MLS> <yes/no/paused>, ... (from the readiness table)

   Will update in Intercom
     <MLS>  <title>   existing article <ID>   (no new article created)
   Will create in Intercom (as a draft)
     <MLS>  <title>   in <collection>   (a teammate publishes it in Intercom)

   What changed since each was last published
     <MLS>
       Text: <plain summary, for example 1 paragraph reworded (Things to Know)>
       Screenshots: <n replaced (where), n added, n removed, n unchanged>
       Video: <unchanged, added, replaced, or not included and why>

   Left out on purpose
     <MLS>: <the other MLSs' screenshots and videos that were not carried>

   Links: <n> go to this MLS's own articles. <n> have no <MLS> article yet.

   Needs your attention
     1. <one entry per missing link, per screenshot that cannot be verified, per odd caption>

   Edits since the last publish: <who edited the Notion page and when, from Notion's version history>. <Intercom has not been edited since the last publish, or: Intercom was edited on <date> after the last publish.>

   Next: <what happens next, in order>
   ```

   Rules for the preview:
   - Every record is named by MLS, title, and article ID, and says update or create.
   - Changes are grouped under Text, Screenshots, Video, and Links.
   - The Needs your attention section is always there. When it is empty, it says "Nothing."
   - Under `all`, list every MLS skipped and why.
   - A first publish with no media record says so, and lists each uploaded image that cannot be verified under Needs your attention. Nothing is silently reused.
   - Explain a system term in what the member sees, and hedge any prediction about members.
   - If the version history cannot name who edited, say so instead of guessing.

5. **Take the link decisions.** For each missing link in the preview, ask for the choice `/port-to-intercom` step 5 defines: stop, publish without the link, or a named exception. One link at a time, per MLS. A missing link never blocks the rest of the update. "Approve all" is not accepted for exceptions.

6. **Publish each MLS in turn.** For each MLS still in the run, in order, run `/port-to-intercom` for that MLS from step 6 on: the edited-in-Intercom confirmation first when it applies, then the full diff, then one confirmation for that record alone. A yes to Baldwin is not a yes to CRMLS; for `both`, ask each separately. If one MLS is declined, stops, or fails, say so and carry on with the next only if the teammate wants to; one MLS's outcome never changes another's record.

7. **Report once at the end.** Per MLS: the article ID and public URL, what was published or why it was not, the changelog line, and the Notion status. Then, across the run: every item still under Needs your attention, every Active link exception, and the human steps `/port-to-intercom` lists (publish a new draft in Intercom, Fin labels, scratch draft deletion). Never say an article is published when it was only created as a draft.

## Rules

- `/publish` has no write path of its own. Every Intercom write, changelog line, media record, link exception row, Notion update, and mirror sync happens inside `/port-to-intercom`, under its rules and prompts.
- Never set `state: "published"`. Never write to conversations, contacts, companies, or macros.
- Never substitute one MLS's screenshot, video, or link for another's.
- Never create a record when the MLS's URL field on the row is filled. Never change `Article Status` to get past a refusal.
- One article per run; one confirmation and one changelog line per record.
- Readiness: `No` blocks a first record and `all`, never an update; `Paused` blocks everything for that MLS; an unreadable table never blocks an update, and the preview says so.
- Output rules from the root `CLAUDE.md` apply to everything shown: no em dashes, no horizontal rules, no member names or emails.

## Reference

- `.claude/skills/port-to-intercom/SKILL.md` - the only skill that writes, and the rules this one defers to.
- `docs/help-center/mls-registry.md` - registered MLSs and where readiness is read.
- `docs/help-center/media-record/README.md` and `docs/help-center/link-exceptions.md` - the media receipt and the approved link exceptions.
- `workstreams/help-center-overhaul/docs/publish-commands-proposal.md` - the approved design, sections 1, 4, 5, 6, 7, and 8.
