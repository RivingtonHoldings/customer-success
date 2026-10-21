# QA: Add and Edit Listings in the Perchwell Mobile App

- **Old title:** My Listings Overview
- **Sources:** live Intercom article 14785355 (content ID 17380619), mirror `docs/help-center/baldwin/my-listings-overview.md`, confirmed unchanged against `get_article` on October 21, 2026. No old Master Article List page. The article's four live screenshots (dated April 2026, Training Mode). Teammate product answers, October 21, 2026. Sibling drafts in Notion: Add and Edit Listings (TRK-044), Listing Detail Page in the Perchwell Mobile App (TRK-054), Manage Contacts in the Perchwell Mobile App (TRK-053).
- **Scored by:** Claude for Kevin Liang, October 21, 2026
- **Scorecard:** September 10, 2026 check set, revision 2
- **Article type:** Workflow (was an Overview by title). Scope option A: mobile-specific steps only, with AI Scribe, syndication, and documents given one line each and linked to the browser articles.

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Fail | Pass | Old: "Here, there are trash icons", "Click the Edit button" with no surface |
| 2 visual_content_text | Fail | Pass | Old: four images with no alt text. New: alt text written from the screenshots |
| 3 undefined_terms | Fail | Pass | PPIN now defined |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Pass | Pass | |
| 6 self_contained_sections | Fail | Pass | Old: "You can also reorder via up/down arrows" detached from its section |
| 7 audience_specification | Fail | Pass | Agents see their own listings; MLS staff see every listing and draft |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | Old had no opening paragraph |
| 12 instruction_completeness | Fail | Pass | Old: Create the Listing stopped at "enter the listing information". New: every procedure ends with its outcome, including the message after submitting |
| 13 limitations_workarounds | Pass | Pass | No drag to reorder stated where the member meets it |
| 14 numerical_clarity | Pass | Pass | Old numbers were exact but wrong (5 MB, 10 MB); now 15 MB and 50 MB |

Old: 7 of 14. New: 14 of 14.

## Plain language gate

Pass. Check 1 flagged "records" in "tax records and other public records", which is the real-world term the standard exempts. "Syndication Settings" is the on-screen section label and a word agents use.

## Dimension scores

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 8.6 (2/7) | 30.0 (7/7) | +21.4 |
| Chunk independence (25) | 8.3 (2/6) | 25.0 (6/6) | +16.7 |
| Answer completeness (25) | 7.1 (2/7) | 25.0 (7/7) | +17.9 |
| Fin-parsable formatting (10) | 2.5 (2/8) | 10.0 (8/8) | +7.5 |
| Accuracy and confidence (10) | 4.0 (2/5) | 10.0 (5/5) | +6.0 |
| **Total** | **30.5** | **100.0** | **+69.5** |

Old band: Not retrievable as written. New band: Fin-ready, both gates passed.

Old failures, for the record: the title names the wrong page (the tab is My Listings, the page is titled Manage Listings); the description is over 140 characters and opens with "In this article"; no opening paragraph; four H1s and an H4; required fields covered in three places; bold on every UI label; an emoji tip; horizontal rules; "you can" and "Use Filters"; button labels and upload limits that do not match the product.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I add a listing in the Perchwell app? | Yes | Yes |
| Why can't I submit my listing on my phone? | Yes | Yes |
| How do I reorder listing photos on mobile? | Partly, in a bullet under Remove or Re-Arrange Images | Yes |
| What's the photo size limit in the mobile app? | Yes, but wrong (5 MB) | Yes (15 MB) |
| Can I use a PPIN for Autofill on my phone? | Yes | Yes |
| How do I edit a live listing from the app? | No; no Submit updates | Yes, across the Edit and Save sections |
| How do I delete a draft listing in the app? | No | Yes |
| Why do I only see my own listings in the app? | No | Yes |

## Open items

- Resolved October 21, 2026: the teammate gave the on-screen spelling of all 11 filters, including Expiration date, which was missing from the first list. The live article's "Address" filter does not exist and was dropped.
- Resolved October 21, 2026: the teammate says the message is "Listing updated successfully" and the listing goes straight to Live or Coming Soon on the MLS. The draft applies the message to both Submit listing and Submit updates. The browser draft says Submit listing shows "Listing successfully uploaded". Check whether a new listing's message differs on mobile, and check the browser draft's wording.
- Not carried, as sibling inferences: the browser draft's warning that Autofill replaces fields already filled in, and accepted photo formats (PNG, JPG/JPEG). Both are likely the same on mobile; confirm before adding them.
- The live mobile article said videos upload as files. The browser draft says videos and virtual tours are links. The rewrite drops videos and links to the browser article for virtual tours.
- **Conflict with a sibling:** the Add and Edit Listings draft (TRK-044) says to enter a PPIN in the Tax PPIN # field, "not in Autofill". The teammate confirmed the mobile Autofill accepts a PPIN through Search by Tax ID/PPIN. Check the browser behavior and fix whichever article is wrong.
- Role: the teammate says permissions match the browser. The browser draft opens "as an agent with the right permissions", and an open Notion comment questions it. This article states no role until that is settled.
- The Public visibility dropdown on each photo is left out, at the teammate's request.
- Screenshots are from April 2026 in Training Mode. They show the current labels, but a reshoot outside Training Mode would be cleaner. The listing addresses visible in them are public listing data, not member identifiers.
- The live article also sits in Intercom collection 19637741, which returns 401 for every help center. Check where it lives before porting.
- Title overlap: the title contains the browser article's name, Add and Edit Listings. Each names its own surface and the two link to each other, which the naming standard allows.
- The live Listing Maintenance FAQ answers "Where can I manage my listings ... in the mobile app?" with "tapping My Listings". That is still correct.
