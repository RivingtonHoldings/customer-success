# Search collection port report

The record of the October 23, 2026 port of the Search collection from the Perchwell Help Center Database [Sep 2026] in Notion to Intercom. All 19 articles replaced their existing Intercom articles in place, by ID, using `/port-to-intercom`. Every article stayed published, and every update had its own before-and-after diff and its own confirmation from Tara. Per-article detail is in `docs/help-center/changelog.md`.

**Result:** 19 of 19 articles are live and match Notion. Every Notion screenshot and video landed where Notion places it. Nothing from Notion failed to port. The only elements left out were the ones left out on purpose: alt text, captions, and the "Baldwin |" screenshot labels.

## Rules applied to every article

- Notion is the source of truth. When a live article had edits newer than the Notion draft, the Notion version won.
- No alt text and no captions, because Intercom does not support alt text (Tara, October 23).
- A blank line goes between paragraphs, images, headings, and videos, matching the spacing Tara added by hand to the pilot.
- Notion page links were replaced with the Intercom article they stand for, at `/baldwin/en/`.
- In the eight articles shared with CRMLS, the "Baldwin |" labels were stripped and the images kept, so CRMLS readers see Baldwin screenshots for now (Tara, October 23).
- New screenshots were re-hosted in Intercom through scratch draft 17720766. Screenshots already on the live article were reused at their current sizes.

## Per-article results

Live URLs follow `https://support.perchwell.com/baldwin/en/articles/<ID>`. Shared articles also open under `/crmls/en/`.

| Article | ID | Help centers | Video | Screenshots | Missing or open |
|---|---|---|---|---|---|
| Create a Search with Filters | 13903380 | Baldwin | Loom 9113eeac | 7 spots from 6 images | None |
| Actions Menu Options on the Search Page | 13623271 | Baldwin | Loom 9167ae89 | 3 | Split sentence from the pilot edit, which Tara is fixing |
| Create a Template Search | 13903342 | Baldwin | Arcade Z87zQnzd | 3 (2 new, 1 kept) | No CRMLS version |
| Filter Your Search by Keyword | 16053548 | Baldwin | None (Video Status Not Needed) | 3 | None; CRMLS has its own article, 11011163 |
| Filter Your Search by Property Type and Subtype | 13922158 | Baldwin | Loom c007a141 | 3 | None |
| Filter Your Search with Map Tools | 14744497 | Baldwin | Loom 2d0310b3 | 5 | No CRMLS version |
| Print or Save Search Results as a PDF | 16302253 | Baldwin | Loom f856f080 | 3 | The Notion placeholder for the Actions menu screenshot has no image yet; no CRMLS version |
| Search FAQ | 15200328 | Baldwin | None | 4 | The Search Page Overview link points to the mobile article 14786263 |
| Search for Condos, Subdivisions, and Communities | 15363551 | Baldwin, default | Loom f7d6f466 | 3 (1 new, 2 kept) | None |
| Search Page Overview | 13903243 | Baldwin, default | None (Video Status Not Needed) | 4 | The link to 8955876 does not open in Baldwin |
| Share Listings with Clients from Search | 13903326 | Baldwin, default | Loom a7151424 | 6 | Facts to confirm, listed below |
| Customize Your Search Results View | 11962073 | Baldwin, CRMLS, default | Loom efee8a99 | 13 (4 new, 9 kept) | Baldwin screenshots in CRMLS |
| Export Listings to a CSV File | 11776740 | Baldwin, CRMLS, default | Loom 1214b6e8 | 4 | Baldwin screenshots in CRMLS |
| Filter Your Search by Open House Date | 11517245 | Baldwin, CRMLS, default | Loom 2a6c0e75 | 2 | Link text still says "Customize Your Search View" |
| Filter Your Search by Status and Price Changes | 11010696 | Baldwin, CRMLS, default | Loom 62ae5727 | 5 | Duplicate 16170546 waiting to be archived |
| Manage Your Saved Searches | 8955646 | Baldwin, CRMLS, default | Arcade axXBGfeZ | 7 | Baldwin screenshots in CRMLS |
| Set Up Email Alerts for Saved Searches | 11112420 | Baldwin, CRMLS, default | Loom e5c96277 | 4 | Facts to confirm, listed below |
| Share a Saved Search with a Client | 8955682 | Baldwin, CRMLS, default | Arcade 2JEF0FWK | 3 | Facts to confirm, listed below |
| Universal Search Bar | 11002620 | Baldwin, CRMLS | Loom d83f9879 | 2 (both kept) | Baldwin screenshots in CRMLS |

Every Notion row is now set to Live in Intercom.

## Removed on purpose, per Notion as the source of truth

These were on the live articles and are gone now. If any of them should come back, add it in Notion and re-port.

- **Search FAQ:**
  - "How do I search for Listings sold as a buyer's agent?" (added live October 20) and its screenshot.
  - Three other questions.
- **Search Page Overview:**
  - The Search Analytics Loom (956e4116, added live October 8).
  - The Arcade demo.
  - The flood zone, share, and export walkthroughs.
- **Manage Your Saved Searches:**
  - Setting a Template Search with the star.
  - The Recently Viewed sort.
  - The alert frequency list.
  - "Clients must accept the invitation."
- **Set Up Email Alerts for Saved Searches:**
  - Both tables.
  - The rollout note about duplicate alert emails.
- Tips sections on several articles, horizontal rules, bold UI names, and emoji pointers.

## Facts to confirm

These were ported as Notion has them. Each one changes or adds a claim that nobody has checked against the product during the port.

- **Share Listings with Clients from Search:**
  - The texting sender number is now 332-241-3300; live said 332-240-3300.
  - The "texts send between 8 AM and 8 PM only" rule is gone.
- **Set Up Email Alerts for Saved Searches:** Monthly alerts now run on days 1 to 31, falling back to the last day of a shorter month. Live said 1 to 28.
- **Share a Saved Search with a Client:** "Changes a client saves also update the saved search in your account." The old Manage Your Saved Searches article said client edits create a separate saved search under the client's account.
- **Print or Save Search Results as a PDF:** "Photos are left out" and the tip to print 8 or fewer columns may predate the new printout.
- **Filter Your Search by Status and Price Changes:**
  - The 180-day default for closed and off-market statuses.
  - The 30-day default for price changes.
  - The day buttons on each date window tab.
- **Filter Your Search by Open House Date:** the 30, 60, 180, and 365 days buttons.

## Links members may not be able to open

Intercom finds articles by ID, so every link resolves. A link only fails when its target is not in the reader's help center.

- **Baldwin-only targets linked from shared articles:**
  - Create a Template Search (13903342)
  - Search Page Overview (13903243)
  - Map Tools (14744497)
  - Reverse Prospecting (16201667)
  - Contacts Page Overview (13975194)
  - Create and Manage Your Contacts in Perchwell (14790755)
  - View Shared Saved Searches (14743530)
  - Search FAQ (15200328)
  - Listing Statuses in Perchwell (14709241)
  - New Terminology (14459704)
  - Mobile FAQ (15201164)

  CRMLS readers may not be able to open these links, and neither may default help center readers where the article is also in the default help center.
- **Share Listings with Clients from Search:** How to Share a Tag (16221617) and Create Communication Templates (14549167) are Baldwin only, so default help center readers may not be able to open them.
- **Search Page Overview:** the Share and Export Analytics Charts link (8955876) is in CRMLS and the default help center only, so Baldwin readers may not be able to open it.
- **Search FAQ:** the Search Page Overview link points to the mobile article 14786263 instead of 13903243. Fix it in Notion, then re-port.

## Follow-ups

**For Tara in Intercom**
- Archive 16170546, the duplicate status and activity article. It has no collection but is published, so Fin may still answer from it.
- Delete scratch draft 17720766. It only held images for re-hosting, and every port copied its images out.
- Fix the split sentence on Actions Menu Options on the Search Page (13623271).

**CRMLS coverage**
- Several Notion rows list Baldwin and CRMLS, but the Intercom articles are Baldwin only: Create a Template Search, Filter Your Search with Map Tools, Print or Save Search Results as a PDF, and Actions Menu Options. CRMLS has a separate draft for Actions Menu Options, 13933104.
- Decide whether CRMLS gets its own versions of these articles, and of the eight shared articles that now show Baldwin screenshots.

**Fin labels**
- Manage Your Saved Searches, Set Up Email Alerts for Saved Searches, and Share a Saved Search with a Client have no Intercom tags.
- Several other articles still carry their pre-overhaul tags, such as "How to: Search (Open House)."
- Check all 19 articles against `docs/standards/` Fin labeling strategy.

**Mirror cleanup**
- Renaming an article leaves its old mirror file behind. There are now 14 leftover files in `docs/help-center/baldwin/` and 5 in `docs/help-center/crmls/`, each a second file for an article already mirrored under its new name.
  - Examples: `print-search-results.md`, `search-for-open-houses.md`, `understand-status-and-activity-filter.md`, `add-an-invited-client-to-a-saved-search.md`.
  - The sync script should delete a file when an article's slug changes.
- A second sync bug showed up during the port. When Baldwin removed 8955889 and added 17453999, both mapped to `analytics-tab-walkthrough.md`, and the build deleted the new file. A second run restored it.
- Both bugs are worth fixing in `sync_help_center.py` before the next large port.

**Notion**
- Open House Date: update the link text "Customize Your Search View" to "Customize Your Search Results View", then re-port, or leave it for the next edit.
