# Support ops

Evergreen support content that outlives any single project. Nothing here has an end date.

## What lives here

- `macros/` - Paste-ready Intercom macro drafts, one file per feature, named `YYYY-MM-DD-<feature-slug>-macros.md`. Every file is listed in `macros/README.md`, which is the index the `/intercom-macros` skill reads before drafting so it updates an existing macro instead of duplicating it.

## Rules

- Claude never creates, edits, or deletes macros in Intercom. Drafts are saved here; a teammate creates the macro in Intercom by hand (New macro, paste, set availability, save).
- Macros use the conversation register from the root `CLAUDE.md`: friendly, one click at a time, screenshot placeholders telling the teammate what to capture.
- When a macro references a help center article, link the public URL from the mirror in `docs/help-center/`. If the article is not in the mirror, run `/sync-help-center` first or leave a `[link: <article title>]` placeholder.
- Keep the index current. A macro that is retired in Intercom gets its line removed here, not marked "old."
