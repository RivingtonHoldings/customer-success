# QA: Listing Detail Page in the Perchwell Mobile App

- **Old title:** Listing Detail Page Overview (retitled, because the browser article 14074994 and its Draft row TRK-046 carry the same name)
- **Sources:** Intercom article 14784837, content 17380040 (Baldwin, Mobile collection); mirror `docs/help-center/baldwin/listing-detail-page-overview-14784837.md`; old Notion rows [Apple](https://app.notion.com/p/34f8b9e014388096b8f4c92f3b786396) and [Android](https://app.notion.com/p/37c8b9e0143880c483acdcb8658a3868), both word for word the live text; the four live screenshots, captured late April 2026; teammate product answers, October 20, 2026
- **Scored by:** Claude for Kevin, October 20, 2026. Scorecard revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Fail | Pass | No alt text on any of the four live images; three are carried with alt text, the Admin image is dropped |
| 3 undefined_terms | Fail | Pass | CDOM, CMA, and RPR now defined |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | Bare-noun headings (Key Details, Collapsible Tiles, Action Window) replaced |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Fail | Pass | Admin tab and History now state who sees them; Listing Details states it is agent-only |
| 8 entity_distribution | Fail | Pass | Every section names the Listing Detail Page |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | |
| 12 instruction_completeness | Fail | Pass | Three-dots menu now says what each option does and where it leads |
| 13 limitations_workarounds | Pass | Pass | |
| 14 numerical_clarity | Pass | Pass | Mortgage defaults stated: 7% and 20% |

## Plain language gate

Pass. Searched for the do-not list: there are no hits. "Collapsible tiles" is gone; the article now says "sections".

## Dimension scores

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 4.3 (1/7) | 30.0 (7/7) | +25.7 |
| Chunk independence (25) | 16.7 (4/6) | 25.0 (6/6) | +8.3 |
| Answer completeness (25) | 7.1 (2/7) | 25.0 (7/7) | +17.9 |
| Fin-parsable formatting (10) | 3.75 (3/8) | 10.0 (8/8) | +6.25 |
| Accuracy and confidence (10) | 2.0 (1/5) | 10.0 (5/5) | +8.0 |
| **Total** | **33.9, Not retrievable as written** | **100.0, Fin-ready** | **+66.1** |

Old failures, for the record: the title duplicates the browser article's; the description is not 120 to 140 characters; there is no "Use this article to" opening; there are several H1s and an H4; bold and emoji appear throughout; there are horizontal rules; and "Down Payment Resource" is listed though it is not in the screenshot. Share externally is missing; "you can" and "Use" appear; and "instant directions" is used.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I share a listing from the Perchwell app? | Partly (Share externally missing) | Yes |
| If I add a note on my phone, will I see it on my computer? | No | Yes |
| How do I get directions to a listing in the app? | Yes | Yes |
| Where is the mortgage calculator in the mobile app? | Partly (no defaults) | Yes |
| How do I edit my listing from my phone? | Yes, but did not say who sees Admin | Yes |
| How do I run a CMA from a listing on my phone? | Yes | Yes |
| Can clients see a listing's History from a link I send? | No | Yes |
| How do I contact the listing agent from the app? | No | Yes |

## Open items

- Resolved October 20, 2026: the sections, top to bottom, are Description, Listing Details, Property Details, Features, Rooms, Map, Mortgage & Tax, and History. The live article's tile names (Property Information, Documents, Agents, Financials) and "Location" were wrong, which means the mirror and both old Notion pages agreed on labels the app no longer has.
- Resolved October 20, 2026: Directions opens Apple Maps on an iPhone. Google Maps on Android is carried from the live article.
- Resolved October 20, 2026: every member sees History; it is hidden from public links. The earlier answer about permissions referred to something else, so no role is stated.
- Resolved October 20, 2026: Mortgage & Tax is its own section. The Map and Mortgage & Tax sections now come before History, matching the page order.
- Down Payment Resource was dropped from the integration list. The April screenshot does not show it, and the answer did not confirm it.
- The screenshots date from late April 2026. They show the Admin tab, which now appears only on your own listings and for admins. The images are still accurate for an agent's own listing, but a refresh would remove the coach-mark tooltips.
- Mortgage field labels on mobile (Interest rate, Sale price, Down payment, Term) are not confirmed, so the article describes them in lowercase prose.
- Android has cosmetic differences only, per the teammate, so one article serves both. The old Android row (New Article Request) can be closed by whoever owns the Master Article List.
- The live article sits in two Intercom parents (19615962 Mobile and 19637741). Check 19637741 at port.
- This draft is set-consistent with the browser draft (TRK-046) on Listing Details being agent-only, Mortgage & Tax defaults, and the Financial Amortizer legacy name. The two link to each other once the browser draft adds its link back. The browser draft does not yet mention the mobile article.
