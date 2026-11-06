# Proposal for Leo's review: `/publish` commands built on `/port-to-intercom`

Status: Phase 0 only. Nothing in the existing skills, Notion, Intercom, or GitHub is changed by this document. Approved by Tara: overall direction and Phase 0. Needs Leo's review before Phase 1.

Saved November 6, 2026 as a new file for Leo to read. No existing file was touched, and nothing is committed or pushed yet.

## 1. What is being proposed

Three commands, one new thin skill, one small registry file, and a media record, all layered on `/port-to-intercom`:

| Command | Means |
|---|---|
| `/publish baldwin <article>` | Update or create the Baldwin Intercom record only |
| `/publish crmls <article>` | Update or create the CRMLS Intercom record only |
| `/publish both <article>` | Always exactly Baldwin and CRMLS, in that order |
| `/publish all <article>` | Every MLS that is registered, applicable to the article, and marked ready (see 4). Used once a third MLS exists |
| `/publish <slug> <article>` | Any registered MLS, for example `/publish stellar` |

One article per run. Notion is the single source of truth; every run fetches the row fresh. Conversion, the push, the changelog, the Notion close-out, and the mirror re-sync all stay in `/port-to-intercom`; `/publish` adds no second way to write to Intercom.

## 2. What already works, and what is added

Already in `/port-to-intercom` (kept as is): live Notion fetch; `Baldwin |` / `CRMLS |` caption and placeholder labels; keep unlabeled images; unlabeled video kept for Baldwin and for another MLS only when its `Video Status` is `Complete`; never substitute the other MLS's screenshot or video; update-vs-create from the row's Intercom URL fields (so no duplicates); five preconditions; per-article confirmation; `update_article` and `create_article` always prompt; never sets `published`; changelog; mirror re-sync.

Added:

1. A combined, plain-language preview before any write (section 5).
2. A media record and change check, including a safe first-publish rule for live articles (sections 3 and 4).
3. A "Needs your attention" outcome for conflicting or ambiguous media only.
4. An MLS registry so a new MLS needs no skill edit (section 6).
5. The `/publish` wrapper (section 7).

## 3. Media record (tracks what was published, nothing else)

- Purpose: remember what was last pushed to each MLS record so the next run can say what changed. It is a receipt, not a source. It never holds article text, never holds image files, and is never read to draft or edit anything. Notion always wins: if the receipt and Notion disagree, Notion is right and the receipt is rewritten after the confirmed push.
- Location: `docs/help-center/media-record/<tracker-id>.json`, written only by the publishing skill after a confirmed push (like the mirror, never hand-edited).
- Per MLS, per media slot: position among that MLS's media (section heading plus order), kind, the caption label as read, the identity, and the Intercom CDN URL or video URL it became, plus the Notion page's last-edited time at publish.
- Identity of a media item (from investigation of the live Universal Search Bar row):
  - Uploaded image: the file ID inside `notion-file-block://<block>/<fileId>?name=...`. A new upload always gets a new file ID even with an identical filename, so a replaced screenshot is detected even when the name does not change. Block ID is not used (a replacement shows up in Notion history as a removed block plus a new one).
  - External image (many Baldwin images are Intercom CDN links in Notion): the URL path, minus any signature.
  - Video: the Loom or Arcade URL.
  - Signed download URLs expire in 5 minutes and are never recorded.
- Second signal: `notion-get-version-changes` gives block-level added, removed, and edited records between two times. Used as a cross-check; disagreement with the first signal is flagged.

## 4. First publish of an article already live in Intercom (no record yet)

Rule: never silently reuse an old screenshot. Each media item ends in one of three states, shown in the preview:

| State | How it is reached | What publishing does |
|---|---|---|
| Verified unchanged | External image whose URL path equals the one in the live Intercom body; or Notion history since the article's last publish date shows no change to that media block | Keeps the Intercom copy |
| Changed | Different identity, or Notion history shows the block added, removed, or replaced | Uploads the current Notion image (or video link) |
| Cannot be verified | Uploaded image with no way to compare to the live copy and no usable history | Shown under "Needs your attention." If Tara confirms, the current Notion image is uploaded fresh, since Notion is the truth; nothing is reused on a guess |

After the first confirmed push the record exists and later runs are fully automatic. No bulk backfill of the ~70 live articles; each gets its record when it is next published.

One check to run before Phase 1 (needs a throwaway edit, so it waits for approval): on a "<Article> - Claude Copy" row, confirm how Notion's Replace on an existing image shows up (same block with a new file ID, or a new block). Both are handled; this only documents which.

## 5. What Tara sees before anything is written

Plain language, no HTML, no technical diff. The technical diff stays available only on request. Sample for `/publish both Universal Search Bar`:

```
Publish: Universal Search Bar   (Notion row TRK-095, Complete)

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
  Baldwin: the 2 CRMLS screenshots.   CRMLS: the 2 Baldwin screenshots and the Baldwin video.

Needs your attention (none)  |  or a short list, one line each, with the reason

Links: 4 links to other articles will point to the Baldwin versions; 2 to CRMLS.

Next: I will ask you to confirm Baldwin, then separately CRMLS.
```

Rules for this preview: it names every Intercom record by MLS, title, and ID; says update or create; groups changes into Text, Screenshots, Video, Links; and always ends with an explicit Needs-your-attention section. A skipped MLS (under `all`) is listed with the reason.

## 6. MLS registry

New file `docs/help-center/mls-registry.md`, one row per MLS, read by the skills instead of hardcoded names:

| Field | Baldwin | CRMLS |
|---|---|---|
| slug | baldwin | crmls |
| display name (captions, placeholders) | Baldwin | CRMLS |
| Notion `MLS` option | Baldwin | CRMLS |
| Intercom help center ID | 4755399 | 4767477 |
| public URL path | /baldwin/en/ | /crmls/en/ |
| Notion fields | Intercom URL, Visual Status Baldwin, Video Status Baldwin | Intercom URL CRMLS, Visual Status CRMLS, Video Status CRMLS |
| mirror folder | docs/help-center/baldwin | docs/help-center/crmls |
| unlabeled video counts as this MLS | yes (existing rule) | only when Video Status is Complete |
| **ready to publish** | yes | yes |

Adding an MLS = a registry row, its Notion fields and `MLS` option, a collection-map refresh, a mirror folder. No skill edit.

- **`both`** is fixed: Baldwin and CRMLS.
- **`all`** targets an MLS only when all three hold: it is in the registry, it appears in the article's Notion `MLS` field, and its registry row says ready to publish = yes. An MLS that is merely tagged in Notion but not yet configured is skipped and reported by name.
- Caption labels are matched against the registry. An unrecognized label (a typo, or an MLS not yet registered) goes to Needs your attention instead of being guessed.

## 7. Proposed changes by file (for Leo's review)

No file below is touched in Phase 0.

`.claude/skills/port-to-intercom/SKILL.md` (Leo's skill; changes kept minimal):
- Replace the Baldwin-default / "CRMLS mode" split with a target parameter looked up in the registry. Baldwin and CRMLS keep their current behavior, including URL fields, collection matching, retire list, and the rule that a port never writes another MLS's record. The CRMLS section becomes the "secondary MLS" section, MLS names replaced by registry lookups.
- Step 5: classify media per section 3, apply the first-publish rule in section 4, and add the "Needs your attention" outcome. It triggers only on conflicting or ambiguous media: label disagrees with the filename or the MLS Visual/Video Status; unrecognized label; a slot whose identity and label both changed; an item that cannot be verified under the first-publish rule. Unlabeled images remain shared and never trigger it. Unlabeled video follows the existing status rule.
- Step 6: add the plain-language summary above the existing full diff (diff still shown at confirmation, as today).
- Step 9: write the media record after a confirmed push.

`.claude/skills/port-to-intercom/references/intercom-html.md`: replace "reuse the CDN URL whenever the draft points at the same image" (line 90) with the identity comparison in section 3.

New: `.claude/skills/publish/SKILL.md`, `.claude/commands/publish.md`, `docs/help-center/mls-registry.md`, `docs/help-center/media-record/` (empty until first publish).

Small doc updates: `docs/build-log.md`, the commands list in the root `CLAUDE.md`, a pointer in `docs/help-center/crmls-port-map.md`.

Not changed: `/sync-help-center`, the mirror, `.claude/settings.json` (Intercom write tools stay on the ask list), `docs/standards/` (the label, placement, and order rules in `content-standards.md` lines 355 and 356 are preserved verbatim), the Notion database schema, and the media content itself, which stays in Notion.

## 8. Existing rules preserved

Filenames and captions as the convention reads them today (`Baldwin | Alt text: ...`, `CRMLS | Alt text: ...`, `(Baldwin)` / `(CRMLS)` placeholders); images placed after the step they illustrate, Baldwin first; media order in the Intercom body equals Notion order per MLS; a step with no image for an MLS gets none, never the other MLS's; a Baldwin-only video is never a stand-in; one confirmation and one changelog line per record; Intercom `state` untouched; updates never pass `parent_id`, `parent_type`, or `author_id`.

## 9. Questions for Leo

1. Is replacing the "CRMLS mode" section with a registry-driven secondary-MLS section acceptable, or does he prefer to keep CRMLS mode and add the registry beside it?
2. Is `docs/help-center/media-record/` in the repo the right home for the receipt, or would he rather keep it elsewhere?
3. Should "ready to publish" live in the registry (proposed) or as a Notion field per MLS?
4. Any dependency on the current CRMLS mode, such as the port map or retirement steps, that the generalization could break?

## 10. Verification once Phase 1 is approved

- Dry run of baldwin, crmls, and both on Universal Search Bar: correct records and plain-language preview; zero write calls.
- On a "Claude Copy" row: replace a screenshot keeping the filename (reported Changed); add and remove media (reported); a mistyped label and a label/status mismatch (reported under Needs your attention); unlabeled images (not flagged).
- First publish of a live article with an uploaded image and no history: reported Cannot be verified, never silently reused.
- A scratch registry row for a fake MLS: `/publish <slug>` resolves; a not-ready MLS is skipped by `/publish all` and named.
- Real publish of one article: state and collections unchanged, changelog line, media record written, second `/sync-help-center` shows zero changes, rendered image order matches Notion.
