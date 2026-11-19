# Link-text fix record, November 4, 2026

This is the record of the Baldwin link-text fixes, which are finished. Live Baldwin articles linked to sibling articles using their old titles, and each fix changed the link text to the target's current Intercom title. Tara set the scope as every affected Baldwin article except the monthly feature news articles. Each article was ported one at a time, with a diff shown and Tara's yes before every push, under rung 3 of the root CLAUDE.md.

## Where things stand

- **Done:** 56 articles, live in Intercom. Each has a changelog line, a backup in `qa/port-backups/2026-11/<id>-2026-11-04-links.html`, and a Notion row set back to Live in Intercom.
- **Mirror and commits:** the Baldwin mirror was re-synced and the work was committed and pushed to main on November 4, 2026. The CRMLS mirror was not synced in this batch.
- **Not in the batch:** the Baldwin monthly feature news articles.

## How the three held articles were resolved

- **Filter Your Search by Keyword (TRK-082, 16053548):** Tara chose the shorter Notion wording for step 3. The live step now reads "Enter a keyword in the Text Search field", and the link text was updated.
- **Listing Field Changes in Perchwell (TRK-103, 14459773):** no push was needed. A second re-port from Notion had already made the live article match the Notion page, link text included. Prepared files from earlier in the day were out of date and were not used.
- **Update Your Brokerage Logo and Colors (TRK-110, 14057465):** Tara chose to remove the live article's extra Reports customization screenshot so the article matches Notion. The link text was updated.

## Separate fix the same day

- **Create a Search with Filters (13903380, TRK-077):** a paragraph split mid-sentence after the Filter Your Search by Keyword link was joined into one paragraph, matching Notion. Backup: `qa/port-backups/2026-11/13903380-2026-11-04-split-paragraph.html`.

## Still open

- **CRMLS collection moves:** someone moved three articles out of the CRMLS Invited Clients collection in Intercom: Share Listings with Your Agent, Communicate with Your Agent via Messages, and Receive Alerts About New Listings. If that wasn't intended, a human puts them back in Intercom.
- **intercom.help addresses:** ListTrac Integration (16777050) and Offer Manager Integration (16777012) still link to `intercom.help` addresses and use the old format. The Offer Manager item is logged in `docs/open-article-fixes.md`.
- **CRMLS copy of Create a Search with Filters (18233998):** not checked for the same split paragraph.
- **Orphaned comment:** TRK-008's Notion page has a comment thread that was left detached when its staff line was removed. Tara resolves it in Notion.
