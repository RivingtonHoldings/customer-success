# QA: Actions Menu Options on the Search Page

- **Article:** Actions Menu Options on the Search Page
- **Old title:** Multi-Listing Actions on the Search Page
- **Old Notion page:** https://app.notion.com/p/2ef8b9e0143880868709d4df9d3c6cef (Master Article List, read only)
- **Intercom:** two separate articles, not one shared record. Baldwin 13623271, content 15695301, published. CRMLS 13933104, content 16202346, unpublished draft with different text
- **Mirror:** `docs/help-center/baldwin/multi-listing-actions-on-the-search-page.md`, `docs/help-center/crmls/multi-listing-actions-on-the-search-page.md`
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-10-13-actions-menu-options-on-the-search-page-rewrite.md`
- **New Notion draft:** https://app.notion.com/p/3f88b9e0143881679eb2d314628ca70b
- **Scored by:** Claude for Tara, October 13, 2026, against scorecard revision 2. Old column scores the Baldwin live article
- **Evidence:** two current screenshots from Tara (three listings selected with the Actions menu open; no listings selected with the menu open), and the live Arcade, which still shows the retired bottom action bar
- **Product answers:** Tara, October 13, 2026: the header checkbox selects only loaded listings (60 load on their own, then 30 per scroll); with nothing selected, Export CSV and Print include every result, loaded or not; Contact Agent opens one window listing every agent on each selected listing, with template, Subject, message, and up to 5 extra email addresses; Open in New Tab opens one tab with a carousel; Driving Directions accepts up to 9 listings and opens Google Maps from the member's current location; Schedule a Showing opens the ShowingTime integration; Baldwin only for now; remove the Arcade
- **Title:** Tara chose Actions Menu Options on the Search Page, October 13, 2026, over Take Action on Selected Listings from Search (near-repeat of a Search Page Overview heading) and Use the Actions Menu on the Search Page (the standard bans "use" as a stand-in verb)
- **Review edits:** October 13, 2026: selection scope moved into the first section lead, description and opening made complementary, option descriptions made consistent, repeated "from the Actions menu on the Search page" cut from section leads, the 9-listing limit moved into the Driving Directions item
- **Scope decision:** Tara, October 13, 2026: a hub with one sentence per Actions menu option and a link to its article. Contact Agent, Open in New Tab, and Driving Directions have no other article, so they are covered here

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Pass | Pass | Old had no images; placeholders now carry alt text |
| 3 undefined_terms | Fail | Pass | CMA, CSV, and cc (carbon copy) defined on first use |
| 4 structured_enumeration | Pass | Pass | Tables became labeled lists |
| 5 query_answer_symmetry | Fail | Pass | "Tips" was a bare heading |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Fail | Pass | "Some actions depend on your permissions" named no role; no role gates the menu |
| 8 entity_distribution | Pass | Pass | Actions menu and Search page named in every section |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | |
| 11 overview_jtbd | Fail | Pass | Old had no opening paragraph |
| 12 instruction_completeness | Fail | Pass | Old steps stopped at opening the dropdown |
| 13 limitations_workarounds | Fail | Pass | Greyed-out options and Driving Directions location sharing now give the route forward |
| 14 numerical_clarity | Pass | Pass | |
| **Total** | 8 of 14 | 14 of 14 | |

## Plain language gate

Pass. No terms from the do-not list. "Actions", "Keep", "Hide", "Share via Text", and the other option names are on-screen control labels. "integration" is accurate for ShowingTime.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 8.6 (2 of 7) | 30.0 (7 of 7) | +21.4 |
| Chunk independence (25) | 20.8 (5 of 6) | 25.0 (6 of 6) | +4.2 |
| Answer completeness (25) | 3.6 (1 of 7) | 25.0 (7 of 7) | +21.4 |
| Fin-parsable formatting (10) | 5.0 (4 of 8) | 10.0 (8 of 8) | +5.0 |
| Accuracy and confidence (10) | 4.0 (2 of 5) | 10.0 (5 of 5) | +6.0 |
| **Total** | **42.0, Not retrievable as written** | **100.0, Fin-ready, no confirm markers open** | **+58.0** |

What the old article failed:
- Retrieval: bare-noun title, an "In this article" description over 140 characters, no opening paragraph, and a bare "Tips" heading
- Chunk independence: sections were H1
- Answer completeness: no outcome after the steps, a vague permissions line, CMA undefined, constraints left as "some actions depend on", and option workflows described rather than linked
- Formatting: wrong UI labels in the steps, an emoji callout, and bold throughout
- Accuracy: Action Panel, Tag, and Select All labels no longer match the product; "Use these actions" headed both tables

## Source differences and which side won

| Point | Baldwin live and old Notion | CRMLS draft | Resolution |
|---|---|---|---|
| Where the options sit | Action Panel / Actions drop down | Action Panel at the bottom of the page | Screenshots: Actions button in the upper right of the results, with a count such as 3 of 29 |
| Select all | Select All in the Action Panel | Same | Tara: checkbox in the column header, selects loaded listings only |
| Tag | Its own option | Tag Selected | Gone from the menu. Share, then via Tag, per Search Page Overview |
| Open in New Tab | Carousel (table) vs. listing detail pages in a new tab (Tips) | View Listings | Tara: one new tab with a carousel |
| Missing from both | | | Share via Text, Keep, Hide, Driving Directions, Export CSV, Print added from the screenshots and sibling drafts |
| Listing Presentations, Cloud CMA | Not listed | Listed | Dropped. Listing Presentations is removed for both MLSs per `docs/product-context.md`; Cloud CMA dropped with CRMLS out of scope for now |
| Tips: "Some actions depend on your permissions and connected services" | Present | Present | Cut: names no action and no route forward |
| Arcade walkthrough | Embedded | None | Replaced with a video placeholder; it shows the retired bottom action bar |

## Fin test questions

| Question | Old, one section | New, one section |
|---|---|---|
| How do I select multiple listings on the search page? | Yes | Yes |
| How do I select all the listings in my search? | Partly, wrong label | Yes |
| Why are most of the options in the Actions menu greyed out? | No | Yes |
| How do I add several listings to a tag from my search? | Yes, wrong option | Yes |
| Can I email the listing agents for several listings at once? | Yes | Yes |
| How do I get driving directions to the listings I picked? | No | Yes |
| How do I text listings to a client from search? | No | Yes |
| How do I hide listings from my search results? | Partly, in Tips | Yes |
| How many listings can I get driving directions for? | No | Yes |

## Open items

- No `[confirm: ...]` markers left. Tara confirmed October 13, 2026, with screenshots of the Contact Agent window: the button is Send Email, each agent receives a separate email per listing, additional recipients are cc'd (up to 5, added with Add Email), the Message field has default text, {listing} works in the subject and message, and "Your email has been sent successfully." appears after sending
- Not answered, left out of the draft rather than marked: whether the header checkbox has a hover label, how to clear a selection, whether Schedule a Showing needs a ShowingTime account, and what it does with multiple listings selected
- MLS: Baldwin only for now, per Tara. The separate CRMLS Intercom draft (13933104) is left alone; it still lists Listing Presentations, which is removed
- Fixed October 13, 2026, with Tara's approval: Export Listings to a CSV File now says that with nothing selected, Export CSV includes every result, and it no longer tells members to scroll to load every listing. Still open: Map Tools in Search (live) says multi-select driving directions are "coming soon"
- Load count: Tara confirmed 30 load, 30 more a few seconds later, then 30 per scroll. After a reviewer flagged "60" against the set, the article says "30 listings at a time as you scroll" to match Search Page Overview, October 13, 2026
- Search Page Overview links here by the old title and URL; update the link text at port
- Links to Notion drafts (Share Listings with Clients from Search, Export Listings to a CSV File, Print or Save Search Results as a PDF, Search Page Overview) need public URLs at port. Message Clients in Perchwell and Create a Listing Report point at the default help center and are flagged for transfer
- Arcade removed per Tara; new video and screenshots are placeholders
- One Pager added to Create a Report, October 13, 2026, per Tara; the on-screen label is One Pager. The linked Create One Page Reports article (live, default help center) calls it One Page Report and its Search steps still use the retired footer action bar; fix both when it is migrated
- Final standards pass, October 13, 2026, after Tara's section-by-section edits: cc defined (golden question 3), four echo fixes, and Create a Report cut to 22 words. Rewrite holds at 100.0 and 14 of 14; plain language gate passes
