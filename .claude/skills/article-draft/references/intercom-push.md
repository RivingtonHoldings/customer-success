# Intercom push

The rules that govern writing to Intercom. `/port-to-intercom` (`.claude/skills/port-to-intercom/SKILL.md`) implements them; this file is the policy those mechanics answer to, and the two must not drift.

Pushes were turned on September 17, 2026. The decision is in `workstreams/help-center-overhaul/docs/decisions.md`.

## Preconditions

1. Pushes are on and the decision is recorded in `docs/build-log.md` or `workstreams/help-center-overhaul/docs/decisions.md`.
2. `/sync-help-center` has run at least twice with a clean second run, so the mirror is trusted.
3. The Notion row's `Article Status` in the Perchwell Help Center Database [Sep 2026] is `Ready to Transfer` or `Live in Intercom`, its `Article Review Status` is `Review Finished` or `Complete`, and the update rule in the next section holds. A `Draft`, `New Article Request`, or `Deprecated` page is never pushed. A push from a `Live in Intercom` row never changes `Article Status`; a push from a `Ready to Transfer` row sets it to `Live in Intercom`.
4. The collection (and section, if any) the article belongs to has been identified in the mirror, so `parent_id` and `parent_type` are known rather than guessed.
5. An `author_id` for the pushing teammate is known. The Intercom connector does not expose an admin lookup, so this comes from an existing article's `author` field in the mirror. An update omits `author_id` and keeps the original author, so this precondition binds on new articles only.

## One record per MLS (ladder rung 2 for a create, rung 3 for an update)

A Notion row whose `MLS` field lists several MLSs produces one Intercom record per MLS, each in that MLS's help center (the registry in `docs/help-center/mls-registry.md` names each one and the Notion URL field that points at its record). `/port-to-intercom` ports to one MLS per run. Since November 4, 2026 this has applied to Baldwin and CRMLS; any MLS added to the registry follows the same rule. The preconditions for the target MLS, in addition to numbers 1, 2, 4, and 5 above:

- The row's `Article Status` is `Ready to Transfer` or `Live in Intercom`, and `Article Review Status` is `Review Finished` or `Complete`. Review Status is a required check, not proof that recent edits were reviewed; the confirmed diff is the approval. A create for a second MLS normally happens from a row that is already live for the first; that is not an overwrite, because it writes a different record.
- The target MLS's URL field is empty for a create and holds the record for an update. A filled field is never a create. Before a create, the target help center is searched for a same-titled article, which stops the run.
- On an update, the live article's title matches the row's `Article Name` (a trailing MLS suffix removed) or the title in its latest changelog line, and its collections include one owned by the target MLS's help center in `docs/help-center/collections.md`.
- On a create, `collections.md` has a collection owned by the target MLS's help center whose name matches the row's `Collection`.
- The MLS's `Ready to publish` value in the readiness table on the Help Center Production Tracker allows it: `No` blocks a create, `Paused` blocks everything, and an unreadable table never blocks an update.

- The edited-in-Intercom check compares the live `updated_at` with the one stored in the article's media record (`docs/help-center/media-record/<Tracker ID>.json`), and falls back to the newest changelog date when there is no record yet. A later live value needs its own confirmation, asked first.
- A link with no published article for the target MLS is decided one link at a time: stop, publish without the link, or a named exception recorded in `docs/help-center/link-exceptions.md`. Another MLS's article is never substituted automatically.
- A push writes the target MLS's entry in the media record, a receipt of the media it carried. It is never a content source; Notion wins.

Everything else in the two sections below applies. A port never writes another MLS's record; a change to it is a separate port with its own confirmation.

**Retiring what a new record replaces.** Only after a teammate publishes the new record. A legacy record in the target help center is set to `draft` with `update_article` carrying `id` and `state` and nothing else, under the rung 3 rules: shown, confirmed one record at a time, one changelog line each. Another MLS's shared record leaves the target collection by a human in Intercom, because `update_article` takes a single `parent_id` and would drop its other collections. Deleting a record stays human.

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
