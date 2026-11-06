# Proposal for Leo's review: `/publish` commands built on `/port-to-intercom`

Status: revision 2, November 6, 2026. Proposal only. Nothing in the existing skills, Notion, or Intercom is changed by this document, and nothing is implemented. Tara approved the direction; Leo's explicit approval of section 10 is required before any implementation.

Revision 2 incorporates Leo's answers to the first review and Tara's seven decisions: every MLS is a peer; readiness lives in Notion, in the simplest existing place; `Live in Intercom` is left alone until its dependencies are confirmed; missing cross-MLS links are flagged, never substituted; Leo approves before implementation; testing is approved in principle but not yet run.

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

Kept as is: live Notion fetch; the `Baldwin |` and `CRMLS |` caption and placeholder labels; unlabeled images shared; update-versus-create from the row's Intercom URL fields (no duplicates); the five preconditions; one confirmation and one changelog line per record; Intercom write tools always prompt; `state` never set to published; no `parent_id`, `parent_type`, or `author_id` on an update.

Added: a combined plain-language preview (section 8); a media record and change check (section 7); a "Needs your attention" outcome for conflicting or ambiguous media and for missing links; an MLS registry; MLS readiness read from Notion; and the thin `/publish` wrapper.

## 3. Peer MLS architecture

Leo's concern was that making Baldwin the "home" and other MLSs "secondary" would cause problems. Revision 2 treats every MLS as a registry row and runs one flow for all, with no default flow and no secondary mode. The CRMLS-mode section of `port-to-intercom` is replaced by that single flow. Baldwin and CRMLS keep their exact current behavior because every difference between them moves into a registry field, not into code that knows their names.

Current behaviors that assume Baldwin is the home, and how each is expressed for peers:

| Today | For peers |
|---|---|
| The unsuffixed `Intercom URL` field is Baldwin | Registry field "URL field": Baldwin maps to `Intercom URL`, CRMLS to `Intercom URL CRMLS`, a new MLS to `Intercom URL <MLS>`. No Notion field is renamed |
| "Default flow" is Baldwin; "CRMLS mode" is everything else | One flow, MLS looked up in the registry |
| Unlabeled video is kept for Baldwin; for another MLS only when its `Video Status` is `Complete` | Registry field "unlabeled video counts as this MLS": Baldwin yes, others no. Preserves the rule exactly |
| Updating an existing Baldwin record needs row status `Ready to Transfer`; updating an existing CRMLS record accepts `Live in Intercom` or `Ready to Transfer` | Registry field "row status required to update an existing record," preserving each rule as is. This asymmetry is real today; see section 5 and the question for Leo |
| Hosted images are reused from the Baldwin record | Reuse by media identity from any record that already hosts that image (section 7) |
| CRMLS links fall back to the Baldwin URL and are flagged | Removed. See section 6 |
| `both` and Baldwin-first ordering | Registry order; `both` is fixed to Baldwin then CRMLS |
| The retire list names the "shared Baldwin record" | Names whichever record sits in the target MLS's collection and is not that MLS's own |

Registry file: `docs/help-center/mls-registry.md`, one row per MLS, technical facts only: slug; display name used in captions and placeholders; Notion `MLS` option; Intercom help center ID; public URL path; the Notion field names for its Intercom URL, Visual Status, and Video Status; mirror folder; the two behavior fields above. Adding an MLS means a registry row, its three Notion fields and `MLS` option, a collection-map refresh, and a mirror folder. No skill edit. Readiness is not in the registry (section 4).

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

Recommended table (columns: MLS, Ready to publish, Owner, Notes), one row per MLS. The skill reads it fresh each run. An MLS is ready only when its cell reads exactly `Yes`; a missing row, a blank, or anything else means not ready, and the preview says so by name. If the table later proves too loose, a database can replace it without touching the skills' logic. Creating the table is a Notion write and waits for Tara's approval.

Open point: should the readiness gate also apply when an MLS is named directly (`/publish stellar`)? Recommendation: yes, one rule for every command. Baldwin and CRMLS would both be marked `Yes`, so nothing changes for them today.

## 5. `Live in Intercom`: current purpose and impact (no behavior change proposed)

Checked against the repo. The `Article Status` value is read or written in these places:

- `port-to-intercom` step 3 and rules: the default flow refuses a row that is not `Ready to Transfer` and never overwrites a row already `Live in Intercom`; CRMLS mode accepts either. Step 9 sets the row to `Live in Intercom` after a Baldwin port; a CRMLS port leaves it alone.
- `article-draft` and `notion-publishing.md`: drafting never overwrites a row that is `Live in Intercom`, which protects the Notion working copy of a live article.
- `intercom-push.md` precondition 3 and the update-to-a-live-article steps.
- Notion: the status belongs to the `complete` group (with `Deprecated`), so team views grouped or filtered by status group may depend on it. The view filters and any automations were not visible to this review.

In practice the one field does three jobs: "a Baldwin record is live," a lock against overwriting, and a pipeline stage for team views. Per-MLS truth already lives in which Intercom URL fields are filled. The 42-article link fix of November 4 moved rows off and back to `Live in Intercom` around each update, so the team already treats the status as the signal that edits are approved to publish.

Impact for `/publish`: a live Baldwin article edited in Notion cannot be updated until a person sets the row back to `Ready to Transfer`, while an existing CRMLS record of the same row can be updated while the row is still `Live in Intercom`.

Recommendation for Leo: change nothing now. `/publish` uses today's preconditions per MLS exactly as the registry fields describe. When it hits a `Live in Intercom` row it says so in plain words and reads Notion's history since the last publish: if the page was edited, it tells the user to set the row to `Ready to Transfer` to publish the edits; if not, it reports nothing to publish. Unifying the Baldwin and CRMLS rules, or splitting "live" into a per-MLS state, is a separate decision for Tara and Leo after checking Notion views and automations, and should not ship with this change.

## 6. Cross-MLS links

Rule for every MLS: a link in the article body must resolve to that MLS's own record. If the destination does not exist for the target MLS, the link is flagged under Needs your attention and nothing is substituted. No fallback to Baldwin or to any other MLS.

- Destination exists when the linked row's URL field for the target MLS is filled, or the linked record already sits in a collection owned by the target MLS's help center. A shared record counts, and the preview labels it "shared article" so it is visible.
- Missing destination: the port stops on that link, names it, and offers: wait until the destination exists; remove the link; or approve a named substitute for that one link. Tara decides each time. An approved exception is recorded in the port map as a flagged link.
- Change from today: CRMLS mode currently keeps the Baldwin URL and notes it for the link pass. That stops. Effect on waves: a collection ported before its siblings will stop on links to unported siblings, so order ports by dependency or approve the per-link exception.
- Never emits a Notion URL (unchanged).

## 7. Media record and replaced-screenshot detection

The media record is a receipt of what was last pushed, not a content store. It never holds article text or image files, is never read to draft or edit anything, and if it disagrees with Notion, Notion is right and the record is rewritten after the confirmed push. Location: `docs/help-center/media-record/<tracker-id>.json` (Leo approved), written only by the publishing skill after a confirmed push.

Per MLS and media slot it records: position (section heading plus order), kind, caption label as read, identity, the Intercom CDN or video URL it became, and the Notion page's last-edited time at publish.

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

Links: 6 links go to this MLS's own articles. 1 link has no CRMLS article yet: Search FAQ.

Needs your attention
  1. CRMLS link to Search FAQ has no CRMLS article. Wait, remove the link, or approve a named substitute?

Next: nothing is written until the items above are settled; then I ask you to confirm Baldwin, then separately CRMLS.
```

The preview names every record by MLS, title, and ID; says update or create; groups changes into Text, Screenshots, Video, and Links; always ends with an explicit Needs-your-attention section; and lists any MLS skipped under `all` with the reason.

## 9. Proposed changes by file

None is touched until Leo approves.

- `.claude/skills/port-to-intercom/SKILL.md`: replace the default-flow and CRMLS-mode split with one registry-driven flow; media classification and the first-publish rule in step 5; the link rule in section 6; the plain-language summary before the existing diff in step 6; write the media record in step 9. Behavior for Baldwin and CRMLS is unchanged except the link fallback in section 6.
- `.claude/skills/port-to-intercom/references/intercom-html.md`: replace "reuse the CDN URL whenever the draft points at the same image" with the identity comparison.
- `.claude/skills/article-draft/references/intercom-push.md`: the CRMLS section becomes the general MLS section.
- New: `.claude/skills/publish/SKILL.md`, `.claude/commands/publish.md`, `docs/help-center/mls-registry.md`, `docs/help-center/media-record/`.
- Notion (after Tara's approval): one readiness table on the Help Center Production Tracker page.
- Small updates: `docs/build-log.md`, the commands list in the root `CLAUDE.md`, a pointer in `docs/help-center/crmls-port-map.md`.

Not changed: `/sync-help-center`, the mirror, `.claude/settings.json`, `docs/standards/` (the label, placement, and order rules in `content-standards.md` are kept verbatim), the Notion database schema, the `Article Status` values and their behavior, and the media itself, which stays in Notion.

Preserved rules: filenames and captions as the convention reads today; images after the step they illustrate, Baldwin first; Intercom body media order equals Notion order per MLS; a step with no image for an MLS gets none, never another MLS's; a Baldwin-only video is never a stand-in; one confirmation and one changelog line per record.

## 10. For Leo to approve explicitly

1. One registry-driven flow replaces the CRMLS-mode section, with the behavior differences held in registry fields (section 3).
2. The registry keeps `Ready to publish` out and reads readiness from a Notion table on the Production Tracker page (section 4), and the gate applies to every command, including direct ones.
3. `Live in Intercom` and the per-MLS "row status required to update" rules stay exactly as they are today, with the plain-language message in section 5; any unification is a later, separate decision.
4. Missing cross-MLS links stop the port for review with no automatic fallback, which changes today's CRMLS behavior and affects the order of collection waves (section 6).
5. The media record location and its receipt-only role (section 7).
6. Whether the Notion views and automations that use the `Live in Intercom` status have been checked (they were not visible to this review).
7. Approval to build in this order: registry and Notion table, then the `port-to-intercom` generalization, then the media record, then `/publish`.

## 11. Testing

Run only after approval; none has been run.

- Before any edit, dry-run the current `/port-to-intercom` on three live articles: a Baldwin-only one, a shared one, and Universal Search Bar (TRK-095). Save what each would change. After the edit, the same dry runs must produce the same results, except for the intended link-rule change.
- On a "Claude Copy" row: replace a screenshot keeping the filename (reported replaced); add and remove media; a mistyped label and a label/status mismatch (reported under Needs your attention); unlabeled images (not flagged).
- First publish of a live article with an uploaded image and no history: reported cannot be verified, never silently reused.
- A scratch registry row for a fake MLS: `/publish <slug>` resolves; a not-ready MLS is skipped by `all` and named; a missing link stops the port.
- Real publish of one article: state and collections unchanged, changelog line, media record written, second `/sync-help-center` shows zero changes, rendered image order matches Notion.
