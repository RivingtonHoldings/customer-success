# Proposal for Leo's review: `/publish` commands built on `/port-to-intercom`

Status: revision 2, November 6, 2026. Proposal only. Nothing in the existing skills, Notion, or Intercom is changed by this document, and nothing is implemented. Tara approved the direction; Leo's explicit approval of section 10 is required before any implementation.

Revision 3 (November 6, 2026) adds Tara's three follow-ups: one safe rule for updating live articles without changing `Article Status` (section 5), a per-link workflow for missing MLS links (section 6), and how the readiness table is found and read without blocking routine updates (section 4). Revision 2 incorporated Leo's answers to the first review and Tara's seven decisions: every MLS is a peer; readiness lives in Notion, in the simplest existing place; `Live in Intercom` is left alone until its dependencies are confirmed; missing cross-MLS links are flagged, never substituted; Leo approves before implementation; testing is approved in principle but not yet run.

## 1. Commands

One article per run. Notion is the single source of truth; every run fetches the row fresh.

| Command | Means |
|---|---|
| `/publish baldwin <article>` | The Baldwin Intercom record only |
| `/publish crmls <article>` | The CRMLS Intercom record only |
| `/publish both <article>` | Always exactly Baldwin and CRMLS, in that order |
| `/publish <slug> <article>` | Any registered MLS, for example `/publish stellar` |
| `/publish all <article>` | Every MLS that is registered, applicable to the article, and marked ready (section 4) |

Conversion, the push, the changelog, the Notion close-out, and the mirror re-sync stay in `/port-to-intercom`. `/publish` adds no second way to write to Intercom.

## 2. What already works, and what is added

Kept as is: live Notion fetch; the `Baldwin |` and `CRMLS |` caption and placeholder labels; unlabeled images shared; update-versus-create from the row's Intercom URL fields (no duplicates); the five preconditions (the status precondition is replaced by the single update rule in section 5); one confirmation and one changelog line per record; Intercom write tools always prompt; `state` never set to published; no `parent_id`, `parent_type`, or `author_id` on an update.

Added: a combined plain-language preview (section 8); a media record and change check (section 7); a "Needs your attention" outcome for conflicting or ambiguous media and for missing links; an MLS registry; MLS readiness read from Notion; and the thin `/publish` wrapper.

## 3. Peer MLS architecture

Leo's concern was that making Baldwin the "home" and other MLSs "secondary" would cause problems. Revision 2 treats every MLS as a registry row and runs one flow for all, with no default flow and no secondary mode. The CRMLS-mode section of `port-to-intercom` is replaced by that single flow. Baldwin and CRMLS keep their exact current behavior because every difference between them moves into a registry field, not into code that knows their names.

Current behaviors that assume Baldwin is the home, and how each is expressed for peers:

| Today | For peers |
|---|---|
| The unsuffixed `Intercom URL` field is Baldwin | Registry field "URL field": Baldwin maps to `Intercom URL`, CRMLS to `Intercom URL CRMLS`, a new MLS to `Intercom URL <MLS>`. No Notion field is renamed |
| "Default flow" is Baldwin; "CRMLS mode" is everything else | One flow, MLS looked up in the registry |
| Unlabeled video is kept for Baldwin; for another MLS only when its `Video Status` is `Complete` | Registry field "unlabeled video counts as this MLS": Baldwin yes, others no. Preserves the rule exactly |
| Updating an existing Baldwin record needs row status `Ready to Transfer`; updating an existing CRMLS record accepts `Live in Intercom` or `Ready to Transfer` | One update rule for every MLS (section 5), so no registry field is needed |
| Hosted images are reused from the Baldwin record | Reuse by media identity from any record that already hosts that image (section 7) |
| CRMLS links fall back to the Baldwin URL and are flagged | Removed. See section 6 |
| `both` and Baldwin-first ordering | Registry order; `both` is fixed to Baldwin then CRMLS |
| The retire list names the "shared Baldwin record" | Names whichever record sits in the target MLS's collection and is not that MLS's own |

Registry file: `docs/help-center/mls-registry.md`, one row per MLS, technical facts only: slug; display name used in captions and placeholders; Notion `MLS` option; Intercom help center ID; public URL path; the Notion field names for its Intercom URL, Visual Status, and Video Status; mirror folder; the one behavior field above. Adding an MLS means a registry row, its three Notion fields and `MLS` option, a collection-map refresh, and a mirror folder. No skill edit. Readiness is not in the registry (section 4).

Caption labels are matched against the registry. An unrecognized label (a typo, or an MLS not yet registered) goes to Needs your attention instead of being guessed.

## 4. MLS readiness lives in Notion

Requirement: `/publish all` targets an MLS only when it is registered, listed on the article's Notion `MLS` field, and explicitly marked ready. Being listed in Notion is not enough.

This is a fact about the MLS, not about one article, so it does not belong on every article row. Options checked against the existing Notion structure:

| Option | Verdict |
|---|---|
| A short "MLS publishing readiness" table on the existing Help Center Production Tracker page, which the team already uses for per-MLS visual and video status | **Recommended.** No new database, no schema change, visible to the team, one place |
| Text in the `MLS` option description | Hidden in property settings; easy to lose, which is Leo's concern |
| A new per-article property | Wrong level: a column on every row to say something true of the whole MLS |
| The September project page | That page is slated for archive; wrong long-term home |
| A new Notion database | Works, but is the heaviest option and not needed for a few rows |

Recommended table (columns: MLS, Ready to publish, Owner, Notes), one row per MLS, created only after Tara approves. The skill reads it fresh each run.

How the table is found and read: the registry file holds one constant, the Production Tracker page ID (`3dd8b9e0143881bbbaf4ea0964bd34f9`). Each run fetches that page and reads the table whose heading is "MLS publishing readiness." Columns are matched by header name (MLS, Ready to publish, Owner, Notes) and rows by MLS display name from the registry, ignoring case. A simple Notion table comes back in the page markdown as plain table rows, as the project page's tables do, so no special access is needed. The page is read-only for the skills. Before Phase 1 ships, a dry run reads the real table once to prove it parses.

Values: `Yes`, `No`, `Paused`.
- `Yes`: ready for first records, `all`, and updates.
- `No` (not yet ready): blocks creating that MLS's first record for an article and excludes it from `all`. It never blocks an update to a record that already exists.
- `Paused`: blocks everything for that MLS, updates included. An explicit freeze, for example around a cutover.
- Missing row, blank, an unreadable page, or a table that cannot be found counts as `No` for first records and `all`, and has no effect on updates. The preview says "readiness table could not be read; this update continues because the record already exists."

Effect on routine work: Baldwin and CRMLS are seeded `Yes`, and updates to existing records are never gated by anything short of `Paused`, so a table problem cannot interrupt routine Baldwin or CRMLS updates. A direct command to an MLS marked `No` (for example `/publish stellar` before Stellar is ready) is refused for a first record with the reason.

## 5. Updating articles already live, without changing the Notion status

Goal: `/publish` updates existing live articles for either MLS, and nobody changes `Article Status` each time an article is edited.

How it works today (checked in `port-to-intercom` and `intercom-push.md`): updating an existing Baldwin record requires the row to be `Ready to Transfer`, and a port then sets it back to `Live in Intercom`. Updating an existing CRMLS record accepts either status and leaves the status alone. On Baldwin that status step does two real jobs: it is the team's signal that Notion edits are approved, and it stops the same article being pushed twice over someone's later edit. Dropping it for Baldwin needs replacement protections, below.

Proposed single rule for updating an existing record, the same for every MLS. It replaces both current rules. All of it is checked before the preview, and any failure stops the run with the reason in plain words.

Eligibility
1. Row `Article Status` is `Ready to Transfer` or `Live in Intercom`. `Draft`, `New Article Request`, and `Deprecated` never publish.
2. `Article Review Status` is `Review Finished` or `Complete`. This becomes the approval signal for edits, and it is a field reviewers already own. If an edit needs review, a reviewer moves it back to `In Review` and `/publish` holds. CRMLS already requires this.
3. The MLS's URL field is filled. A filled field always means update; it is never a create.

Guards against the wrong article or a duplicate
4. The article ID comes from the URL slug and `get_article` must return it. A content ID returns `not_found` and stops the run (existing rule).
5. The live title must equal the row's `Article Name` or the title recorded at the last publish. Otherwise stop: "The Intercom article with this ID is titled X; this Notion row is Y."
6. The live article's collections must include one owned by the target MLS's help center (`docs/help-center/collections.md`). Otherwise stop.
7. Publish state is untouched: a published article stays published, a draft stays a draft.
8. Create path (URL field empty): search the target help center by the row's title and any old title first. A same-titled article stops the run and asks whether to link it to this row or create anyway. Nothing is created silently.

Guards against overwriting or repeating work (these replace "never overwrite a `Live in Intercom` row")
9. Nothing-to-publish check: if Notion has not changed since the recorded publish and the live article still matches what was published, say "Nothing to publish" and stop.
10. Edited-in-Intercom check: if the live article was changed in Intercom after the last publish (its `updated_at` is later than the one recorded; for a first publish, later than the article's last changelog date), the preview says so in plain words, for example "Edited in Intercom on Nov 3 after the last publish; publishing will replace that edit," and the existing diff against the live article shows what would be replaced. It needs an explicit yes.
11. The preview shows who edited the Notion page since the last publish and when, from Notion's version history.
12. Unchanged: one confirmation per record, the full diff at confirmation, a changelog line, no `parent_id`, `parent_type`, or `author_id` on an update.

Status handling: an update never changes `Article Status`. A first publish from a `Ready to Transfer` row sets it to `Live in Intercom`, as today. The drafting skills' rule "never overwrite a `Live in Intercom` page" is a different guard (it protects the Notion page from a drafting skill, not from a person editing it) and is untouched.

Effect: Baldwin gains update-from-`Live in Intercom`; CRMLS behaves as today; `Ready to Transfer` still works for both. Remaining risk: Review Status is not reset automatically when someone edits, so a half-finished edit on a live row could be offered for publishing. The protections are the review-status check, the who-edited line, and your per-article confirmation of the diff. A Notion automation that moves Review Status back on edit would close the gap but is outside this proposal.

Not part of this change: whether the status field should later be split into a per-MLS state. Leo and Tara can decide that separately after the Notion views and automations that use `Live in Intercom` are checked (they were not visible to this review).

## 6. Missing cross-MLS links: flag, explain, let Tara decide

Rule for every MLS: a link must go to that MLS's own article. Nothing is ever substituted automatically, in either direction. One missing link does not block an otherwise valid update; each one is a decision for Tara.

Each link in the body is sorted before the preview:
- Resolved: the linked row's URL field for the target MLS is filled and that article is published.
- Shared: the linked record already sits in a collection owned by the target MLS's help center. It is labeled "shared article" in the preview.
- Missing: no article for the target MLS, or one that exists but is still a draft.

A missing link shows in plain language, one entry per link, for example: "The CRMLS version of Universal Search Bar links to Search FAQ in the section 'Find several listings at once.' Search FAQ has no CRMLS article yet, so there is nothing in the CRMLS help center to link to." Tara then chooses for that link:

1. **Stop.** Nothing is written for that MLS.
2. **Publish without the link.** The link text stays as plain text and everything else publishes.
3. **Approve a named exception.** Tara names the exact destination (title, MLS, URL), such as "use the Baldwin Search FAQ." The confirmation repeats it with a warning that CRMLS readers would leave the CRMLS help center. It is the only way another MLS's article can appear, and only the one named.

Exceptions are recorded in a new `docs/help-center/link-exceptions.md` (article, MLS, link text, named destination, who approved, date, status). An exception applies to that one link and that one destination only. Each later publish of the article lists it again as a reminder, and when the missing article is created the exception is offered for replacement with the correct link. If the destination changes, Tara is asked again. Approvals are per link; "approve all" is not accepted for exceptions. For `both`, link decisions are made per MLS.

Change from today: CRMLS mode currently keeps the Baldwin URL and notes it for the link pass. That stops. Never emits a Notion URL (unchanged).

## 7. Media record and replaced-screenshot detection

The media record is a receipt of what was last pushed, not a content store. It never holds article text or image files, is never read to draft or edit anything, and if it disagrees with Notion, Notion is right and the record is rewritten after the confirmed push. Location: `docs/help-center/media-record/<tracker-id>.json` (Leo approved), written only by the publishing skill after a confirmed push.

Per article it records the Intercom article ID, the title, and the article's `updated_at` at publish (used by the checks in section 5). Per MLS and media slot it records: position (section heading plus order), kind, caption label as read, identity, the Intercom CDN or video URL it became, and the Notion page's last-edited time at publish.

Identity (from the live Universal Search Bar row):
- Uploaded image: the file ID inside `notion-file-block://<block>/<fileId>?name=...`. A new upload gets a new file ID even with the same filename, so a replaced screenshot is detected. Block ID is not used: a replacement showed in Notion history as a removed block plus a new one.
- External image (many Baldwin images are Intercom CDN links in Notion): the URL path without any signature.
- Video: the Loom or Arcade URL.
- Signed download URLs expire in 5 minutes and are never recorded.

Cross-check: `notion-get-version-changes` lists block-level added, removed, and edited records since a given time; disagreement with the identity comparison is flagged.

First publish of an article already live (no record yet). Never silently reuse an old screenshot. Each media item is one of:

| State | How reached | What publishing does |
|---|---|---|
| Verified unchanged | External image whose URL path equals the live Intercom body's; or Notion history since the last publish date shows no change to that block | Keeps the Intercom copy |
| Changed | Different identity, or history shows it added, removed, or replaced | Uploads the current Notion image or video link |
| Cannot be verified | Uploaded image with nothing to compare against and no usable history | Listed under Needs your attention; on Tara's confirmation the current Notion image is uploaded fresh |

After the first confirmed push the record exists and later runs classify automatically as unchanged, replaced, added, removed, moved, or label changed. No backfill of existing articles. Needs-your-attention triggers for media: a label that conflicts with the filename or the MLS Visual/Video Status, an unrecognized label, a slot whose identity and label both changed, or an item that cannot be verified. Unlabeled images remain shared and never trigger it. Unlabeled videos follow the existing status rule.

Still to confirm, not yet run: on a "<Article> - Claude Copy" row, how Notion's Replace on an image appears (same block with a new file ID, or a new block). Both outcomes are handled; this only documents which.

## 8. What Tara sees before anything is written

Plain language, no HTML or technical diff; the full diff is shown only at confirmation, as today. Sample for `/publish both Universal Search Bar`:

```
Publish: Universal Search Bar   (Notion row TRK-095, Review Complete)

Ready to publish: Baldwin yes, CRMLS yes (from the readiness table)

Will update in Intercom
  Baldwin  Universal Search Bar   existing article 11002620   (no new article created)
  CRMLS    Universal Search Bar   existing article 18234136   (no new article created)

What changed since each was last published
  Baldwin
    Text: 1 paragraph reworded (Things to Know)
    Screenshots: 1 replaced (top navigation, Step 1); 2 unchanged
    Video: unchanged
  CRMLS
    Text: same 1 paragraph
    Screenshots: 1 replaced (search window, "What you find"); 1 unchanged
    Video: not included (CRMLS video not marked Complete)

Left out on purpose
  Baldwin: the 2 CRMLS screenshots.  CRMLS: the 2 Baldwin screenshots and the Baldwin video.

Links: 6 links go to this MLS's own articles. 1 link has no CRMLS article yet.

Needs your attention
  1. The CRMLS version links to Search FAQ ("Find several listings at once"), and Search FAQ has no CRMLS article yet, so there is nothing in the CRMLS help center to link to. Choose: stop, publish without that link, or name an exception.

Edits since the last publish: a reviewer (Nov 5), Tara (Nov 4). Intercom has not been edited since the last publish.

Next: your choice on item 1; then I ask you to confirm Baldwin, then separately CRMLS. A missing link never blocks the rest of the update.
```

The preview names every record by MLS, title, and ID; says update or create; groups changes into Text, Screenshots, Video, and Links; always ends with an explicit Needs-your-attention section; and lists any MLS skipped under `all` with the reason.

## 9. Proposed changes by file

None is touched until Leo approves.

- `.claude/skills/port-to-intercom/SKILL.md`: replace the default-flow and CRMLS-mode split with one registry-driven flow; the single update rule in section 5 (replacing the Baldwin and CRMLS status preconditions and the "never overwrite a Live row" rule); the link workflow in section 6; media classification and the first-publish rule in step 5; the plain-language summary before the existing diff in step 6; write the media record in step 9.
- `.claude/skills/port-to-intercom/references/intercom-html.md`: replace "reuse the CDN URL whenever the draft points at the same image" with the identity comparison; link handling follows section 6.
- `.claude/skills/article-draft/references/intercom-push.md`: precondition 3 and the CRMLS section become the single update rule and the general MLS section.
- New: `.claude/skills/publish/SKILL.md`, `.claude/commands/publish.md`, `docs/help-center/mls-registry.md`, `docs/help-center/link-exceptions.md`, `docs/help-center/media-record/`.
- Notion (after Tara's approval): one readiness table on the Help Center Production Tracker page.
- Small updates: `docs/build-log.md`, the commands list in the root `CLAUDE.md`, a pointer in `docs/help-center/crmls-port-map.md`.

Not changed: `/sync-help-center`, the mirror, `.claude/settings.json`, `docs/standards/` (label, placement, and order rules kept verbatim), the Notion database schema, `Article Status` values, the drafting skills' rule against overwriting a live Notion page, and the media itself, which stays in Notion.

Preserved rules: filenames and captions as the convention reads today; images after the step they illustrate, Baldwin first; Intercom body media order equals Notion order per MLS; a step with no image for an MLS gets none, never another MLS's; a Baldwin-only video is never a stand-in; one confirmation and one changelog line per record; Intercom write tools always prompt.

## 10. For Leo to approve explicitly

1. **One registry-driven flow** replaces the CRMLS-mode section, with MLS differences held in registry fields (section 3). The one behavior field left is whether unlabeled video counts for an MLS.
2. **One rule for updating existing records, for every MLS** (section 5): `Ready to Transfer` or `Live in Intercom`, review finished, plus the identity, nothing-to-publish, and edited-in-Intercom guards. This lets Baldwin update from `Live in Intercom` without a status change, replaces the Baldwin `Ready to Transfer` requirement and the "never overwrite a Live row" guard, and leaves `Article Status` untouched on updates.
3. **Review Status as the edit-approval signal**, and whether a Notion automation to reset it on edit is wanted later.
4. **Links** (section 6): missing links are flagged per link with stop, publish without the link, or a named exception; exceptions live in `link-exceptions.md`; no automatic fallback. This changes today's CRMLS behavior and the order of collection waves.
5. **Readiness table** on the Production Tracker page (section 4): how it is read, that it gates only `all` and the creation of an MLS's first record, never routine updates, and that `Paused` is the only value that blocks updates.
6. **Media record**: location and receipt-only role (section 7), now also holding the article ID, title, and Intercom `updated_at` at publish.
7. **Notion views and automations** that use `Live in Intercom` need a check before any later change to that status; this proposal does not change it.
8. **Build order**: registry and Notion table, then the `port-to-intercom` generalization, then the media record and link exceptions, then `/publish`.

## 11. Testing

Run only after approval; none has been run.

- Before any edit, dry-run the current `/port-to-intercom` on three live articles: a Baldwin-only one, a shared one, and Universal Search Bar (TRK-095). Save what each would change. After the edit, the same dry runs must match, except for the intended link and update-rule changes.
- Update rule, on "Claude Copy" rows and dry runs: a `Live in Intercom` Baldwin row with edits updates without a status change; a `Draft` row is refused; Review Status `In Review` holds; a wrong ID, a title mismatch, and a record in the wrong help center each stop; an empty URL field with a same-titled article in Intercom stops and asks; an unedited row reports nothing to publish; an article edited in Intercom after the last publish shows the warning.
- Links: a missing destination appears in plain language; each of stop, publish without the link, and a named exception behaves as described; the exception is recorded and re-listed on the next publish; no other MLS's article ever appears unnamed.
- Media: replace a screenshot keeping the filename (reported replaced); add and remove media; a mistyped label and a label/status mismatch (Needs your attention); unlabeled images (not flagged); first publish of a live article with an uploaded image and no history (reported cannot be verified, never silently reused).
- Readiness: with the table in place, `/publish baldwin` and `/publish crmls` updates run normally; a `No` row blocks `all` and first-record creation but not updates; `Paused` blocks everything; a missing or unreadable table never blocks an update and says so; a scratch registry row for a fake MLS resolves.
- Real publish of one article: state and collections unchanged, changelog line, media record written, second `/sync-help-center` shows zero changes, rendered image order matches Notion.
