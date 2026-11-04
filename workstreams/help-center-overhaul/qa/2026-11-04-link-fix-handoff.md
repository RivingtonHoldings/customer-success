# Link-text fix handoff, November 4, 2026

This is a handoff for a session picking up the Baldwin link-text fixes partway through. Live Baldwin articles linked to sibling articles using their old titles. Each fix changes the link text to the target's current Intercom title. Tara set the scope as every affected Baldwin article except the monthly feature news articles. Each article ports one at a time, with a diff shown and Tara's yes before every push, under rung 3 of the root CLAUDE.md.

## Where things stand

- **Done:** 42 articles, live in Intercom. Each has a changelog line, a backup in `qa/port-backups/2026-11/<id>-2026-11-04-links.html`, and a Notion row set back to Live in Intercom.
- **Not yet done:** the mirror sync and the commit for the whole link batch. The changelog and backups are uncommitted.

## Prepared work

Every remaining article was prepared by two agents. Each one has these files in `/private/tmp/claude-501/-Users-tarabars-Documents-perchwell-customer-success/9dbf6c7c-2bef-4030-b3e8-6f7ce66a50a3/scratchpad/port/links/<intercom id>/`:

- `before.html`: the live body when it was prepared
- `after.html`: the body to push, with only link-text changes, image signatures stripped, and no newlines between tags
- `meta.json`: the TRK and the Notion row URL
- `diff.md`: the per-link changes to show Tara

In that folder, `close.py <folder> <id> <next id>` does three things:
- saves the backup
- prepends the changelog line
- prints the next article's diff

Run it from the repo root. `done.txt` lists the IDs already finished.

If that scratchpad folder is gone, re-prepare each article:
- `get_article` gives the live body.
- `docs/help-center/` gives the target titles; check targets in Intercom.
- Edit only the link text.

## Remaining, in order (Notion rows already set to Ready to Transfer)

| Intercom ID | TRK | Article | Note |
|---|---|---|---|
| 13903243 | TRK-091 | Search Page Overview | One sentence now repeats itself; suggested reword is in diff.md. One link goes to 8955876, which is not a Baldwin article (text already correct). Comment thread in Notion near an edited link |
| 11112420 | TRK-092 | Set Up Email Alerts for Saved Searches | Also in CRMLS and default |
| 15521779 | TRK-012 | Set Up Your Clients in Perchwell | "CSV file" twice in one sentence; suggested reword is in diff.md |
| 8955682 | TRK-076 | Share a Saved Search with a Client | Also in CRMLS and default |
| 16221617 | TRK-098 | Share a Tag with Clients | |
| 13903326 | TRK-093 | Share Listings with Clients from Search | One sentence now repeats itself; suggested reword is in diff.md |
| 11373849 | TRK-018 | Share Listings with Your Agent | Moved out of CRMLS today by someone else |
| 15216706 | TRK-100 | Tags FAQ | |
| 14465546 | TRK-101 | Tags Page Overview | |
| 11002620 | TRK-095 | Universal Search Bar | Also in CRMLS. Comment thread in Notion near an edited link |
| 14459729 | TRK-104 | What Changed When You Moved to Perchwell | |
| 11801815 | TRK-045 | Write a Listing Description with AI Scribe | No link changes. Removes the staff line "This video is applicable to all customers" |

## Per-article loop

1. Show Tara the diff from `diff.md`:
   - row status and who the article reaches
   - each link change with its section
   - the sentence as it will read
   - anything left as is

   Wait for her yes.
2. Push `after.html` with `update_article`, passing only `id` and `body`. Never pass `state`, `parent_id`, or `author_id`.
3. Run `close.py`. Then set the Notion row (`notion_url` in meta.json) to Article Status: Live in Intercom.

If Tara picks a reword, edit both `after.html` and the Notion page before you push.

## Held for Tara's decision

These rows are still set to Live in Intercom. Neither the link fixes nor the Notion edits have been applied.

- **Filter Your Search by Keyword (TRK-082, 16053548):** in Notion, step 3 is missing "under Listing Visibility & Access," which the live article has. Tara needs to say which version is right. The link fix is ready in `after.html`.
- **Listing Field Changes in Perchwell (TRK-103, 14459773):** the Notion page was edited at 17:50 UTC, after its re-port. Construction Status and Area are reworded. This needs Tara's check, then a full re-port.
- **Update Your Brokerage Logo and Colors (TRK-110, 14057465):** the live article has a third image after the Branding steps, and Notion doesn't have it.

## Finish

1. Run `/sync-help-center` with a fresh work folder. Run it a second time and confirm zero changes. Then grep the mirror for new link texts.
2. Commit with Tara's OK:
   - Leave out `docs/product-context.md`, which carries another session's edit, and anything under `confidential/`.
   - Push straight to main, with the sandbox off for her keychain token.

## Other open items found today

- **CRMLS collection moves:** someone moved three articles out of the CRMLS Invited Clients collection in Intercom: Share Listings with Your Agent, Communicate with Your Agent via Messages, and Receive Alerts About New Listings. If that wasn't intended, a human puts them back in Intercom.
- **intercom.help addresses:** ListTrac Integration (16777050) and Offer Manager Integration (16777012) still link to `intercom.help` addresses and use the old format. The Offer Manager item is logged in `docs/open-article-fixes.md`.
- **Split paragraph:** Create a Search with Filters (13903380) has a paragraph split mid-sentence after the Filter Your Search by Keyword link.
- **Orphaned comment:** TRK-008's Notion page has a comment thread that was left detached when its staff line was removed.
