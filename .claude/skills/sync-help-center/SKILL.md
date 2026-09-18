---
name: sync-help-center
description: Keep docs/help-center/baldwin/ and docs/help-center/crmls/ as a faithful, read-only mirror of the live Intercom help centers, one markdown file per article with frontmatter, a README index per MLS, and a sync-state.json so re-runs only fetch what changed. Use whenever a teammate types /sync-help-center, asks to "refresh the help center," "pull the latest articles," "update the mirror," or when another skill notices the mirror is stale. Never writes to Intercom.
---

# Sync help center

The mirror lets every other skill search, cross-link, and diff articles without live Intercom calls, and it gives the team a version history of the help center in git. This skill refreshes it. It is read-only toward Intercom: it lists and reads, nothing else.

## How the mirror is built

Two sources, both authoritative, both read-only:

1. **Article metadata** comes from the Intercom connector: `mcp__eff8e27b-83eb-43ee-befe-90e26bf3b57b__list_articles`, paged at 150 per page. This gives every article's ID, content ID (the ID Fin cites), title, description, URL, parent collections, state, author, timestamps, and tags (the labels Fin uses).
2. **Help center membership** comes from `docs/help-center/collections.md`, which maps every collection ID to the help center that owns it (Baldwin 4755399, CRMLS 4767477, default 279383). An article belongs to every help center that owns one of its collections, so an article can appear in both mirrors. Do not infer membership from an article's URL; the URL shows the default help center whenever the article is also in a default collection.

Article bodies come from the public help center page for published articles (`support.perchwell.com/<mls>/en/articles/<id>`), which renders the same HTML the API returns, and from `get_article` for drafts, which have no public page. The script fetches public pages in small batches with backoff and resumes if interrupted.

## Steps

Work from the repo root. `WORK` is a folder in the session scratchpad (never inside the repo). **Use a new `WORK` folder for every run**, never one from an earlier sync: step 4 skips bodies it already has, so a reused folder serves this run a body captured before the article changed. See the warning under step 4. `SCRIPT` is `.claude/skills/sync-help-center/scripts/sync_help_center.py`.

1. **Pull the inventory.** Call `list_articles` with `per_page: 150` for page 1, read `pages.total_pages`, and call the remaining pages. Large results are saved to a file automatically and the result names the path; small results (usually the last page) arrive inline, so save those to `WORK/inventory/pageN.json` yourself. Collect the file paths.

   **Pagination is not stable.** Intercom orders articles so that a recently updated one moves position, which means an article can straddle a page boundary between two calls and come back twice while another comes back not at all. Observed 2026-09-17: two consecutive clean pulls each returned 463 rows but only 462 distinct IDs. So after collecting the pages, check two things before planning:

   - the count of **distinct** IDs against `total_count`, not the row count, which hides the duplicate;
   - that every article ID in both `sync-state.json` files appears in the inventory.

   The second check is the one that matters. A dropped article that the mirror holds would be planned as `removed` and its file deleted; a dropped article that the mirror never held is one of the roughly 200 uncollected drafts and costs nothing. If a mirrored article is missing, pull the pages again rather than building.
2. **Check the collection map.** If `docs/help-center/collections.md` is missing, or the inventory contains a collection ID that is not in it, regenerate it:
   `python3 SCRIPT probe --work WORK --inventory <inventory files>`
   The probe asks the public site which help center owns each collection (200 for the owner, 401 for the others) and reads collection names from the pages. Say in the report if the map changed.
3. **Plan each MLS.** For `baldwin` and then `crmls`:
   `python3 SCRIPT plan --mls <mls> --work WORK --inventory <inventory files>`
   It prints how many articles are added, updated, unchanged, and removed against `sync-state.json`, and lists any draft IDs whose bodies must come from the connector.
4. **Fetch published bodies.**
   `python3 SCRIPT fetch --mls <mls> --work WORK --batch 10 --pause 1`
   Backs off on 429 and 5xx responses, skips bodies already fetched, and reports any that failed.

   **"Already had" is for resuming an interrupted run, not for a second run.** The skip is keyed on the article ID alone, so a `WORK` folder left over from an earlier sync hands this run that folder's older body. This happened on 2026-09-17: a video was swapped on Universal Search Bar, the sync reported `updated 3` and looked clean, and the mirror kept the previous video because the body was served from the morning's cache. **The idempotency check in step 7 does not catch this**, because `sync-state.json` records the new `updated_at` next to the old body and a second run then sees nothing to do. A fresh `WORK` per run is the whole fix. When in doubt, confirm one changed fact in the rebuilt file rather than trusting the counts.
5. **Read drafts and failures through the connector.** For each draft ID from step 3 and each failed fetch from step 4, call `get_article`, then save the body: write the HTML `body.value` verbatim to `WORK/bodies/<id>.api.html` (or save the whole JSON result to a file and run `python3 SCRIPT ingest <id> <file> --work WORK`). Do not paraphrase or tidy the HTML; the mirror must be faithful.
6. **Build.**
   `python3 SCRIPT build --mls <mls> --work WORK`
   Writes one markdown file per article named from the URL slug (title slug for drafts, `-<id>` appended on collisions), the `README.md` index grouped by collection, and `sync-state.json`. Removed articles are deleted from the folder. Prints the per-MLS summary.
7. **Report** the summary for each MLS: added, updated, removed, unchanged, plus the total and the last sync time. If any body is missing, say which articles and why. Offer to commit the mirror.

A second run against the same inventory must report zero added, updated, or removed; if it does not, something is wrong with the state file and the run should be investigated before committing. A clean second run proves the state file agrees with the inventory. It does **not** prove the bodies are current, for the reason under step 4.

## What each article file contains

Frontmatter: `intercom_id`, `content_id`, `title`, `description`, `url`, `help_center`, `help_center_id`, `collection` (primary), `collection_ids`, `collections`, `state`, `author_id`, `created_at`, `updated_at`, `labels` (Intercom article tags), `body_source`, `synced_at`. Then the title as an H1 and the body as clean markdown: headings, lists, bold, links, tables, callouts as blockquotes, images as links to Intercom's CDN with the expiring signature removed, embedded videos as links. Horizontal rules from the source are dropped; headings carry the separation.

## Rules

- Never call `create_article`, `update_article`, or any other write. This skill reads.
- Never hand-edit files in `docs/help-center/`. If an article needs to change, that happens in Notion and Intercom; the mirror follows.
- `collections.md` is the membership source of truth. Regenerate it with the probe; do not edit ownership by hand unless Leo says a collection moved.
- The default help center (NYC and brokerages) is not mirrored. It is out of scope for the CS team.
- Articles with no collection at all (about 200 old drafts) belong to no help center and are not mirrored.
