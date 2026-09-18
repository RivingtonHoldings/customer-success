---
name: port-to-intercom
description: Transfer an approved Perchwell help center article from its Notion draft to the live Intercom help center, then mark the Notion row Live in Intercom. Use whenever a teammate types /port-to-intercom, pastes a Notion page URL or an Intercom admin URL and says "port this," "transfer this to Intercom," "push this live," "publish this article," "move this to Intercom," "update the live article," "replace the Intercom article with the Notion one," or asks what is left before an approved draft reaches members. Converts the Notion body to Intercom HTML, shows a full before-and-after diff, takes one confirmation per article, writes the changelog, and re-syncs the mirror. Never sets an article to published and never writes conversations, contacts, companies, or macros.
---

# Port to Intercom

The last step of the article pipeline. An article has been drafted or rewritten, reviewed by the team in Notion, and scored; this skill carries it into Intercom, where members and Fin actually read it, and closes the Notion row.

This skill owns transfer mechanics only. It does not rewrite, score, or re-review: if the draft is not ready, stop and say so rather than fixing it here. The policy it answers to is `.claude/skills/article-draft/references/intercom-push.md` and the write-rules ladder in the root `CLAUDE.md`.

## Inputs

- **The article** (required). A Notion page URL from the Perchwell Help Center Database [Sep 2026], an Intercom admin URL, an article title, or a mirror path under `docs/help-center/`.
- **Mode hints** (optional). "dry run" converts and diffs but writes nothing. "preflight" checks the preconditions and stops. "new article" forces rung 2 when no live article exists.

## Workflow

1. **Resolve the Notion row.** Fetch the page and read `Article Name`, `Article Status`, `MLS/AOR`, `Collection`, `Roles`, and `Intercom URL`. The data source is `3d18b9e0-1438-80cc-ab0f-000bf0fc1389`.

2. **Resolve the Intercom article ID.** Prefer `Intercom URL` on the Notion row and take the number from the slug (`.../articles/11002620-universal-search-bar` is article **11002620**). With no URL, call `search_articles` on the title. **Never treat a number from an Intercom admin URL as the article ID.** An admin URL reads `activeContentId=11821319`, and that is the *content ID*, the number Fin cites, not the API ID. To go from one to the other, search by title and match the `content_id` field. Passing a content ID to `get_article` returns `not_found`, which is the good case; the bad case is that it matches some other article.

3. **Check the preconditions**, all five from `intercom-push.md`. Report each as pass or fail and **stop on any failure**. The one that fails most often is status: a row must be `Ready to Transfer`. A `Draft` row means the review has not happened, and a row already `Live in Intercom` means someone else did this. Neither is pushed.

4. **Check who the article actually reaches.** Call `get_article` and read **`parent_ids`**, then map every ID through `docs/help-center/collections.md` to its owning help center. Report the full list before the diff.

   **Do not decide this from the mirror.** The mirror is the wrong instrument: it covers Baldwin and CRMLS only, because the default help center (NYC and brokerages) is deliberately not mirrored. An article in a default collection looks single-audience in the mirror and is not. This is exactly what happened on the Dashboard Overview port, 2026-09-18: the mirror recorded one collection, `parent_ids` held two, and the second was the default help center. The rewrite reached an audience outside the project's scope and nothing in the repo would have shown it.

   When more than one help center is in the list, say so plainly and check every cross-link: a link into one help center is wrong for readers of the other. Name those links and let the teammate decide. Do not silently rewrite or drop them.

5. **Convert the body to Intercom HTML** using `references/intercom-html.md`. The title and the `**Description:**` line leave the body and become the `title` and `description` fields.

6. **Diff and confirm.** Fetch the live body with `get_article` and show the full before-and-after in the conversation: title, description, then the body section by section. Ask for confirmation **for this one article**. "Yes to all" is not accepted, and a batch of articles is confirmed one at a time.

7. **Push.** On an update call `update_article` with `id`, `body`, and `title` or `description` only when they changed. On a new article call `create_article` with `state: "draft"` and the `parent_id` and `parent_type` read from the mirror. Nothing else in either call. See the Rules.

8. **Verify.** Call `get_article` and confirm `state` is unchanged and `parent_ids` still holds every collection it held before. Then open the public URL and check what a member sees: every image loaded, the video playing, and no blank gaps from whitespace between block tags. Expect the stored HTML to differ from what was sent in the ways `references/intercom-html.md` lists under "What Intercom changes on save"; anything beyond that list is a real defect.

9. **Close the loop.** Prepend a line to `docs/help-center/changelog.md` under the header, newest first: date, MLS, article title, what changed, who confirmed. Set the Notion row to `Article Status: Live in Intercom` and fill `Intercom URL`. Run `/sync-help-center` with a **fresh work folder**, then run it again and confirm the second run reports zero changes.

   Then grep the rebuilt mirror file for one fact you just changed and confirm it is there. The counts and the clean second run can both look right over a stale body, so this is the only check that proves the mirror caught the push.

10. **Report.** The article ID and public URL, what changed in title, description, and body, the changelog line, the Notion row's new status, the mirror files the sync touched, and anything left for a human: Fin labels per `docs/standards/fin-labeling.md`, MLS audience, new screenshots or video, and any cross-link flagged in step 4.

## Rules

- **Never set `state: "published"`.** Publishing is a human action inside Intercom. On an update, omit `state` entirely; omitting it leaves a published article published, which is what an update to a live article wants.
- **Never pass `parent_id` or `parent_type` on an update.** They move the article. An article shared between two help centers can lose a collection, and it will not be obvious that it did. Pass them on a create, where there is nothing to lose.
- **Never pass `author_id` on an update**, and say in the report that the byline moved anyway. Unlike `state`, omitting `author_id` does not preserve the original author: Intercom stamps the acting admin. Passing one would only pick a different wrong answer.
- **Never push a row that is not `Ready to Transfer`, and never overwrite a row already `Live in Intercom`.** The second is the guard against porting the same article twice over someone else's later edit.
- **Never hand-edit a file in `docs/help-center/`.** The mirror follows Intercom; only `/sync-help-center` writes there.
- **No conversation, contact, company, or macro writes.** Macros are drafted in the repo and a human creates them in Intercom.
- **Labels and audience are not settable here.** `update_article` cannot touch tags, so existing Fin labels survive a push untouched. Setting them stays a human step.
- **One article, one confirmation, one changelog line.** A release that touches six articles is six of each.

## Reference

- `.claude/skills/port-to-intercom/references/intercom-html.md` - the Notion markdown to Intercom HTML mapping.
- `.claude/skills/article-draft/references/intercom-push.md` - the policy, including the five preconditions.
- `.claude/skills/article-draft/references/notion-publishing.md` - the database schema and the manual steps that remain after a push.
- `docs/help-center/collections.md` - which help center owns a collection ID.

## Related skills

`/article-draft` and `/article-rewrite` produce the Notion draft this skill transfers. `/sync-help-center` refreshes the mirror before and after.
