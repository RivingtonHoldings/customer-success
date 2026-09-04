# Intercom push (NOT IMPLEMENTED)

**Status: stub. Nothing in this file runs today.** The `/article-draft` skill stops at the Notion draft. This file records how the push will work so it can be built without redesigning the flow, and so the write rules are visible before anyone turns them on.

Do not add a call to `mcp__eff8e27b-83eb-43ee-befe-90e26bf3b57b__create_article` or `mcp__eff8e27b-83eb-43ee-befe-90e26bf3b57b__update_article` to the skill until every precondition below is met and Leo has removed this banner.

## Preconditions

1. The team has turned pushes on (target September 11, 2026) and `docs/build-log.md` or `workstreams/help-center-overhaul/docs/decisions.md` records the decision.
2. `/sync-help-center` has run at least twice with a clean second run, so the mirror is trusted.
3. The Notion draft's `Article Status` in the Perchwell Help Center Database [Sep 2026] is `Ready to Transfer`. A `Draft` or `New Article Request` page is never pushed.
4. The collection (and section, if any) the article belongs to has been identified in the mirror, so `parent_id` and `parent_type` are known rather than guessed.
5. An `author_id` for the pushing teammate is known. The Intercom connector does not expose an admin lookup, so this comes from an existing article's `author` field in the mirror.

## New article (ladder rung 2)

- Convert the approved draft to Intercom HTML with no whitespace between block tags (the tool description explains why).
- Show the user a summary: title, collection, description, `state: draft`, author. Wait for an explicit yes.
- Call `create_article` with `state: "draft"`. Never `published`. Publishing is a human action inside Intercom.
- Record the returned article ID in the draft's metadata comment.
- Run `/sync-help-center` so the mirror picks up the new draft article.

## Update to a live article (ladder rung 3)

- Fetch the current body with `get_article` and diff it against the proposed body. Show the full before-and-after in the conversation.
- Ask for confirmation for this one article. "Yes to all" is not accepted; when a change sheet touches several articles, confirm each separately.
- Call `update_article` with the body (and title or description if they changed). Omit `state` so the publish state is left as is.
- Append a line to `docs/help-center/changelog.md`: date, MLS, article title, what changed, who confirmed.
- Run `/sync-help-center`.

## What this file will never do

No conversation writes, no contact or company writes, no macro writes, no deletes. Those are not part of the push and the connector does not offer most of them anyway.
