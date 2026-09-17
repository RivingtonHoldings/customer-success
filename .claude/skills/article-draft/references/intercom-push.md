# Intercom push

The rules that govern writing to Intercom. `/port-to-intercom` (`.claude/skills/port-to-intercom/SKILL.md`) implements them; this file is the policy those mechanics answer to, and the two must not drift.

Pushes were turned on September 17, 2026. The decision is in `workstreams/help-center-overhaul/docs/decisions.md`.

## Preconditions

1. Pushes are on and the decision is recorded in `docs/build-log.md` or `workstreams/help-center-overhaul/docs/decisions.md`.
2. `/sync-help-center` has run at least twice with a clean second run, so the mirror is trusted.
3. The Notion draft's `Article Status` in the Perchwell Help Center Database [Sep 2026] is `Ready to Transfer`. A `Draft` or `New Article Request` page is never pushed, and a row already `Live in Intercom` is never overwritten.
4. The collection (and section, if any) the article belongs to has been identified in the mirror, so `parent_id` and `parent_type` are known rather than guessed.
5. An `author_id` for the pushing teammate is known. The Intercom connector does not expose an admin lookup, so this comes from an existing article's `author` field in the mirror. An update omits `author_id` and keeps the original author, so this precondition binds on new articles only.

## New article (ladder rung 2)

- Convert the approved draft to Intercom HTML with no whitespace between block tags (the tool description explains why).
- Show the user a summary: title, collection, description, `state: draft`, author. Wait for an explicit yes.
- Call `create_article` with `state: "draft"`. Never `published`. Publishing is a human action inside Intercom.
- Record the returned article ID in the draft's metadata comment, and the public URL in the Notion row's `Intercom URL`.
- Run `/sync-help-center` so the mirror picks up the new draft article.

## Update to a live article (ladder rung 3)

- Fetch the current body with `get_article` and diff it against the proposed body. Show the full before-and-after in the conversation.
- Ask for confirmation for this one article. "Yes to all" is not accepted; when a change sheet touches several articles, confirm each separately.
- Call `update_article` with the body, and the title or description if they changed. Pass nothing else. Omitting `state` leaves the publish state alone; omitting `author_id` leaves authorship alone; omitting `parent_id` and `parent_type` leaves collection membership alone, which matters because an article shared between two help centers loses a collection if they are passed.
- Prepend a line to `docs/help-center/changelog.md` under the header. The file is newest first, so a new entry goes at the top, not at the end.
- Move the Notion row to `Live in Intercom` and fill its `Intercom URL`.
- Run `/sync-help-center`.

## Resolving the article ID

An Intercom admin URL carries `activeContentId=`, which is the **content ID**, the number Fin cites. It is not the article ID the API takes. Resolve one to the other with `search_articles` on the title and match the `content_id` field. Getting this wrong fails loudly when the number matches nothing and quietly when it matches something else, which is why the Notion row carries `Intercom URL` and that is the preferred source.

## What this file will never do

No conversation writes, no contact or company writes, no macro writes, no deletes. Those are not part of the push and the connector does not offer most of them anyway. Claude never sets an article to `published`.
