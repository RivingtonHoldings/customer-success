---
name: port-to-intercom
description: Transfer an approved Perchwell help center article from its Notion draft to the live Intercom help center, then mark the Notion row Live in Intercom. Use whenever a teammate types /port-to-intercom, pastes a Notion page URL or an Intercom admin URL and says "port this," "transfer this to Intercom," "push this live," "publish this article," "move this to Intercom," "update the live article," "replace the Intercom article with the Notion one," or asks what is left before an approved draft reaches members. Converts the Notion body to Intercom HTML, shows a full before-and-after diff, takes one confirmation per article, writes the changelog, and re-syncs the mirror. Never sets an article to published and never writes conversations, contacts, companies, or macros.
---

# Port to Intercom

The last step of the article pipeline. An article has been drafted or rewritten, reviewed by the team in Notion, and scored; this skill carries it into Intercom, where members and Fin actually read it, and closes the Notion row. Since November 4, 2026 it also carries the same row into the CRMLS help center as a separate record with the CRMLS screenshots and videos (see CRMLS mode).

This skill owns transfer mechanics only. It does not rewrite, score, or re-review: if the draft is not ready, stop and say so rather than fixing it here. The policy it answers to is `.claude/skills/article-draft/references/intercom-push.md` and the write-rules ladder in the root `CLAUDE.md`.

## Inputs

- **The article** (required). A Notion page URL from the Perchwell Help Center Database [Sep 2026], an Intercom admin URL, an article title, or a mirror path under `docs/help-center/`.
- **Mode hints** (optional). "dry run" converts and diffs but writes nothing. "preflight" checks the preconditions and stops. "new article" forces rung 2 when no live article exists.
- **Target** (optional). "port to CRMLS", "CRMLS", or `--mls crmls` runs the CRMLS mode described below: the same Notion row produces a second Intercom record for the CRMLS help center, carrying the CRMLS screenshots and videos. With no target the skill ports to the help centers the live article already reaches, which today means Baldwin.

## Workflow

1. **Resolve the Notion row.** Fetch the page and read `Article Name`, `Article Status`, `Article Review Status`, `MLS` (multi-select: Baldwin, CRMLS), `Collection`, `Roles`, `Intercom URL`, `Intercom URL CRMLS`, `Visual Status CRMLS`, and `Video Status CRMLS`. The data source is `3d18b9e0-1438-80cc-ab0f-000bf0fc1389`. The property was renamed from `MLS/AOR` and its CRMLS option from `CRLMS All` before November 4, 2026; older docs that use the old names are describing this field.

2. **Resolve the Intercom article ID.** Prefer `Intercom URL` on the Notion row and take the number from the slug (`.../articles/11002620-universal-search-bar` is article **11002620**). With no URL, call `search_articles` on the title. **Never treat a number from an Intercom admin URL as the article ID.** An admin URL reads `activeContentId=11821319`, and that is the *content ID*, the number Fin cites, not the API ID. To go from one to the other, search by title and match the `content_id` field. Passing a content ID to `get_article` returns `not_found`, which is the good case; the bad case is that it matches some other article.

3. **Check the preconditions**, all five from `intercom-push.md`. Report each as pass or fail and **stop on any failure**. The one that fails most often is status: a row must be `Ready to Transfer`. A `Draft` row means the review has not happened, and a row already `Live in Intercom` means someone else did this. Neither is pushed.

4. **Check who the article actually reaches.** Call `get_article` and read **`parent_ids`**, then map every ID through `docs/help-center/collections.md` to its owning help center. Report the full list before the diff.

   **Do not decide this from the mirror.** The mirror is the wrong instrument: it covers Baldwin and CRMLS only, because the default help center (NYC and brokerages) is deliberately not mirrored. An article in a default collection looks single-audience in the mirror and is not. This is exactly what happened on the Dashboard Overview port, 2026-09-18: the mirror recorded one collection, `parent_ids` held two, and the second was the default help center. The rewrite reached an audience outside the project's scope and nothing in the repo would have shown it.

   When more than one help center is in the list, say so plainly and check every cross-link: a link into one help center is wrong for readers of the other. Name those links and let the teammate decide. Do not silently rewrite or drop them.

5. **Convert the body to Intercom HTML** using `references/intercom-html.md`. The title and the `**Description:**` line leave the body and become the `title` and `description` fields.

   **Keep only this help center's screenshots.** A caption that starts `Baldwin |` or `CRMLS |` marks an image for that MLS only, and a placeholder labeled `(Baldwin)` or `(CRMLS)` likewise. Take the target help center from step 4: keep the unlabeled images and the ones labeled for that help center, strip the label, and drop the rest. List what was dropped in the diff, so a reviewer can see each step still has its image. If step 4 found the article in both Baldwin and CRMLS and the draft has labeled images, stop: one article cannot show each MLS its own screenshot, and keeping either set shows the wrong one to the other MLS. Ask the teammate whether to split the article or pick one image per step.

   **Replace every link to a Notion page with the Intercom article it stands for.** Drafts link sibling articles as Notion page mentions (`<mention-page url="…">`) or `app.notion.com` / `notion.so` URLs while those siblings are still drafts. Members cannot open a Notion page, so none may reach Intercom. For each one:

   - Fetch the linked page. If it is a row in the Perchwell Help Center Database [Sep 2026], take its `Intercom URL`. If that is empty, find the Intercom article the row will replace: the `Intercom article ID` in its QA file under `workstreams/help-center-overhaul/qa/`, or `search_articles` on its `Article Name` and old title.
   - Call `get_article` on that ID. Use the public `url` it returns, with the target help center from step 4 in the path (`/baldwin/en/` or the CRMLS equivalent), never a bare `/en/` link.
   - Keep the row's `Article Name` as the link text. If the target has not been ported yet, its live title still differs; say so in the report, because the link text matches only once that article ports.
   - **Stop on that link** if the target has no Intercom article, is `draft` in Intercom, or does not sit in the target help center. Name the link and let the teammate decide. Do not drop it, and do not link the Notion page.

   List every replacement in the diff (link text, Notion page, Intercom URL). Added October 23, 2026, after the Search collection review found Notion links in five articles.

6. **Diff and confirm.** Fetch the live body with `get_article` and show the full before-and-after in the conversation: title, description, then the body section by section. Ask for confirmation **for this one article**. "Yes to all" is not accepted, and a batch of articles is confirmed one at a time.

   **Diff against `get_article`, never against the mirror.** The mirror holds the page Intercom renders for a reader, and the rendering differs from the stored HTML: a cross-link stored as `/en/` is served as `/baldwin/en/`, so the mirror shows a path the article does not contain. Diffing the Notion draft against the mirror on 2026-09-23 produced a seven-link regression that did not exist, and the "fix" for it was an unrequested change to a reviewed page. The same trap as step 4's, one field over.

7. **Push.** On an update call `update_article` with `id`, `body`, and `title` or `description` only when they changed. On a new article call `create_article` with `state: "draft"` and the `parent_id` and `parent_type` read from the mirror. Nothing else in either call. See the Rules.

8. **Verify.** Call `get_article` and confirm `state` is unchanged and `parent_ids` still holds every collection it held before. Then open the public URL and check what a member sees: every image loaded, the video playing, and no blank gaps from whitespace between block tags. Expect the stored HTML to differ from what was sent in the ways `references/intercom-html.md` lists under "What Intercom changes on save"; anything beyond that list is a real defect.

9. **Close the loop.** Prepend a line to `docs/help-center/changelog.md` under the header, newest first: date, MLS, article title, what changed, who confirmed. Set the Notion row to `Article Status: Live in Intercom` and fill `Intercom URL`. Run `/sync-help-center` with a **fresh work folder**, then run it again and confirm the second run reports zero changes.

   Then grep the rebuilt mirror file for one fact you just changed and confirm it is there. The counts and the clean second run can both look right over a stale body, so this is the only check that proves the mirror caught the push.

10. **Report.** The article ID and public URL, what changed in title, description, and body, the changelog line, the Notion row's new status, the mirror files the sync touched, and anything left for a human: Fin labels per `docs/standards/fin-labeling.md`, MLS audience, new screenshots or video, and any cross-link flagged in step 4.

## CRMLS mode

One Notion row, two Intercom records. The Baldwin record is the one `Intercom URL` points at and the default flow above maintains it. The CRMLS record lives in the CRMLS help center (ID 4767477), in the collection with the same name as the Baldwin one, and `Intercom URL CRMLS` points at it. The Baldwin record is never changed by a CRMLS port. Decided with Leo on November 4, 2026; the decision record is in `workstreams/help-center-overhaul/docs/decisions.md`.

Each numbered step above applies with these differences:

- **Step 2.** `Intercom URL CRMLS` filled means this is an **update** of that record; take the ID from its slug. Empty means a **create**. Read the Baldwin ID from `Intercom URL` as well: its stored body supplies CDN URLs for unlabeled images that are already hosted, and its `parent_ids` tell you whether the Baldwin record still sits in a CRMLS collection.
- **Step 3, preconditions.** The row's `Article Status` is `Live in Intercom` (the Baldwin port already happened) or `Ready to Transfer`. `Article Review Status` is `Review Finished` or `Complete`. `MLS` contains CRMLS. `docs/help-center/collections.md` has a crmls-owned collection whose name matches the Baldwin collection the live article sits in (read that from the Baldwin mirror file's `collections` field; a sub-collection matches on its full `Parent / Child` name). A missing match is a failure that names the collection. `Visual Status CRMLS` and `Video Status CRMLS` are reported, never gating: a `Blocked` or `Not Started` value changes what the body carries, not whether it ports.
- **Step 4, what it replaces.** Call `search_articles` with `help_center_id: 4767477` on the article's title and any old title in its QA file, and `get_article` on each hit. Report a **retire list**: CRMLS-only legacy records with the same subject, and the Baldwin record itself when its `parent_ids` still include a CRMLS collection. Nothing on the list is touched during the port; see Retirement below.
- **Step 5, convert for CRMLS.**
  - Images: keep unlabeled images and `CRMLS |` images; drop `Baldwin |` images. When a step's only image is Baldwin-labeled, the step carries no image. List every omitted step in the diff and the report so the visual owner can add the CRMLS screenshot; do not substitute the Baldwin one (Leo, November 4, 2026).
  - Videos: a video whose caption starts `CRMLS |` is kept and `Baldwin |` is dropped, as with images. An **unlabeled** video is kept only when `Video Status CRMLS` is `Complete`; otherwise drop it and log it. Every recording made before November 4 is unlabeled and was shot in Baldwin, so the status field is what says a shared recording also serves CRMLS. Never embed a Baldwin-only video as a stand-in (Leo, November 4, 2026).
  - Cross-links: resolve each linked row as in step 5 above, then pick the CRMLS destination. Use the row's `Intercom URL CRMLS` when it is filled. Otherwise, if the linked Baldwin record's `parent_ids` include a CRMLS collection, the shared record serves CRMLS readers, so rewrite the link to `https://support.perchwell.com/crmls/en/articles/<id>-<slug>`. Otherwise keep the Baldwin URL and flag the link in the report; it gets fixed on the link pass when that article ports to CRMLS. Never emit a Notion URL.
  - Image hosting: the scratch-draft method in `references/intercom-html.md`. Reuse a CDN URL already on the Baldwin record only for an unlabeled image. Every CRMLS-labeled image is new to Intercom and goes through the scratch draft.
- **Step 6.** On a create there is no live CRMLS body, so show the whole proposed body, plus the title, description, collection name and ID, and the retire list. On an update, diff against `get_article` of the CRMLS record.
- **Step 7.** Create: `create_article` with `state: "draft"`, `parent_id` set to the CRMLS collection ID, and the Baldwin record's exact title and description. Update: `update_article` with `id`, `body`, and `title` or `description` only when they changed. The Rules below apply unchanged.
- **Step 8.** On a create, `parent_ids` holds exactly the one CRMLS collection and `state` is `draft`. A draft has no public page, so the member-view check waits until a teammate publishes it; say so in the report.
- **Step 9.** The changelog line starts `CRMLS` and names the new ID, the collection, the Baldwin ID it pairs with, what it replaces, and the omitted images and video. In Notion, fill `Intercom URL CRMLS` with the public URL under `/crmls/en/`, and leave `Article Status` and `Intercom URL` alone. Add or update the article's row in `docs/help-center/crmls-port-map.md` (Tracker ID, Baldwin ID, CRMLS ID, CRMLS collection, retire list, image and video gaps, flagged links, retirement status). Then the double sync.
- **Step 10.** The human steps for a CRMLS create are: publish the draft in Intercom, set the Fin labels with `MLS: CRMLS`, remove the shared Baldwin record from the CRMLS collection if it is still there (name the collection and the record), delete the scratch draft, and come back for Retirement.

**Link pass.** After every article in a collection has a CRMLS record, run the CRMLS mode once more over each of them as an update. The only change should be flagged links turning into `/crmls/en/` links to the new records. Confirm each article as usual.

**Retirement.** Runs after a teammate publishes the CRMLS record, never before, so CRMLS readers are not left without an article. For each CRMLS-only legacy record on the retire list, call `update_article` with `id` and `state: "draft"` and nothing else. This is a rung 3 change: show the record's title, ID, collection, and current state, take one confirmation for that record, and write one changelog line (precedent: commit 3e4a4d8, two replaced articles unpublished). Deleting a record stays a human step. A shared Baldwin record leaves the CRMLS collection by a human in Intercom, because `update_article` takes a single `parent_id` and would drop its other collections; after that, re-probe `collections.md` and re-sync.

## Rules

- **Never set `state: "published"`.** Publishing is a human action inside Intercom. On an update, omit `state` entirely; omitting it leaves a published article published, which is what an update to a live article wants.
- **Never pass `parent_id` or `parent_type` on an update.** They move the article. An article shared between two help centers can lose a collection, and it will not be obvious that it did. Pass them on a create, where there is nothing to lose.
- **Never pass `author_id` on an update**, and say in the report that the byline moved anyway. Unlike `state`, omitting `author_id` does not preserve the original author: Intercom stamps the acting admin. Passing one would only pick a different wrong answer.
- **Never push a row that is not `Ready to Transfer`, and never overwrite a row already `Live in Intercom`.** The second is the guard against porting the same article twice over someone else's later edit.
- **Never hand-edit a file in `docs/help-center/`.** The mirror follows Intercom; only `/sync-help-center` writes there.
- **No conversation, contact, company, or macro writes.** Macros are drafted in the repo and a human creates them in Intercom.
- **Labels and audience are not settable here.** `update_article` cannot touch tags, so existing Fin labels survive a push untouched. Setting them stays a human step.
- **One article, one confirmation, one changelog line.** A release that touches six articles is six of each. A CRMLS port of a row that is already live in Baldwin is a second article and gets its own.
- **A CRMLS port never writes to the Baldwin record.** Not its body, not its collections. If the Baldwin body also needs a change, that is a separate default-mode port with its own confirmation.
- **Never substitute the other MLS's screenshot or video.** A missing CRMLS asset is a gap in the report, not a Baldwin image in a CRMLS article.

## Reference

- `.claude/skills/port-to-intercom/references/intercom-html.md` - the Notion markdown to Intercom HTML mapping.
- `.claude/skills/article-draft/references/intercom-push.md` - the policy, including the five preconditions.
- `.claude/skills/article-draft/references/notion-publishing.md` - the database schema and the manual steps that remain after a push.
- `docs/help-center/collections.md` - which help center owns a collection ID.
- `docs/help-center/crmls-port-map.md` - one row per article the CRMLS mode has ported: both Intercom IDs, the collection, what it replaced, and what is still missing.

## Related skills

`/article-draft` and `/article-rewrite` produce the Notion draft this skill transfers. `/sync-help-center` refreshes the mirror before and after.
