# QA: Add and Edit Listings

- Article name: Add and Edit Listings (title unchanged)
- Old Notion page: https://app.notion.com/p/27e8b9e01438809997dee4c519f5566f
- Intercom article ID 13627189, content ID 15700488
- Mirror: `docs/help-center/baldwin/add-and-edit-listings.md` (Baldwin only, not shared)
- Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-10-13-add-and-edit-listings-rewrite.md`
- New Notion page: https://app.notion.com/p/3f88b9e01438816581e8c763a35944c0
- Evidence: the Arcade walkthrough's 17 screenshots (captured March 10, 2026, in Training Mode), a current screenshot of a live listing in Add/Edit from Kevin, and Kevin's product answers, October 13, 2026
- Scored by Claude for Kevin, October 13, 2026, against scorecard revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Pass | Pass | No images in the live article; every placeholder in the draft carries alt text |
| 3 undefined_terms | Fail | Pass | IDX, VOW, AVM, and PPIN (Parcel/Property Index Number) defined on first use |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | "Listing creation", "Listing selection", and "Missing field resolution" were bare nouns |
| 6 self_contained_sections | Fail | Pass | "Listing form sections" and "Missing field resolution" did not name the form or the listing |
| 7 audience_specification | Fail | Pass | Brokers and agents with full access, stated in the opening; confirmed by Kevin |
| 8 entity_distribution | Fail | Pass | Add/Edit form named in every section |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | "Use this article to" opening added |
| 12 instruction_completeness | Fail | Pass | Each Steps block ends at the outcome; Submit listing and Submit updates outcomes confirmed |
| 13 limitations_workarounds | Pass | Pass | Autofill overwrite and virtual tour links stated as the route forward |
| 14 numerical_clarity | Pass | Pass | Old numbers were exact but wrong for photos (5 MB) and documents (10 MB); now 15 MB and 50 MB, confirmed by Kevin |

## Plain language gate

Pass on the rewrite. "public records" is the real-world term, not a hit. "Syndication" is the on-screen section name and the word agents use.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 12.9 | 30.0 | +17.1 |
| Chunk independence (25) | 8.3 | 25.0 | +16.7 |
| Answer completeness (25) | 7.1 | 25.0 | +17.9 |
| Fin-parsable formatting (10) | 3.8 | 10.0 | +6.2 |
| Accuracy and confidence (10) | 6.0 | 10.0 | +4.0 |
| Total | 38.1 | 100.0 | +61.9 |

Old: Not retrievable as written. New: Fin-ready, 14 of 14 golden questions, plain language gate passed. No `[confirm: ...]` markers remain.

Old failures: description over 140 characters and in "In this article" form; no opening; sections at H1; bare-noun headings with no echo; required-field rule stated twice; Steps blocks with no outcome; no role; PPIN undefined; AI Scribe re-explained instead of linked; bold UI labels and an emoji callout with no label; horizontal rules; "Use" three times. Wrong facts in the live article: Manage Listings "on your dashboard" (it is in the top navigation), "+ Add New Listing" (no plus), required fields "in red" (orange), "Save Draft"/"Submit Listing" (Save draft, Submit listing), photo and video upload (photos only, video as a Virtual Tour link), photo limit 5 MB (15 MB), document limit 10 MB (50 MB), and no mention of Submit updates for a live listing.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I add a new listing in Perchwell? | Partly, wrong location for Manage Listings | Yes |
| Why can't I click Submit listing? | Partly | Yes |
| What is the max file size for listing photos? | No, wrong number | Yes |
| Can I upload a video to my listing? | No, says videos upload | Yes |
| How do I change a listing that's already active? | Partly, no Submit updates | Yes |
| Autofill erased what I typed, why? | No | Yes |
| How do I fix the map pin on my listing? | Partly | Yes |
| Where did my saved draft listing go? | No | Yes |

## Open items

- Resolved October 13, 2026 by Kevin: brokers and agents with full access add listings; PPIN is Parcel/Property Index Number, entered in the Tax PPIN # field; Submit listing shows "Listing successfully uploaded"
- Agents without full access: the article does not say how to get it. Add a sentence if the team knows the route
- Video: the Arcade (https://app.arcade.software/share/q8cqAyPuAnqnPRjIZdlD) shows the March Autofill panel (County, Submit), a 5 MB photo note, and Training Mode. Replaced with a video placeholder; re-record
- Listings Widget Overview link: the Notion draft is retitled Find Listings in the Listings Widget; update the link text when it ports
- Sibling fixes outside this draft: AI Scribe says "Create New Listing", "from your dashboard", and "Listing Description section" (the field is Public remarks); My Listings Overview (mobile) says 5 MB photos and 10 MB documents; Manage Listings Page Overview says "Click Filter" and has bold UI labels. Confirm the mobile limits match the web before changing them
- Keyboard shortcuts section added October 19, 2026 from the Add/Edit Shortcuts release note, after review finished; reviewer flagged by Notion comment. Hold the port until the feature is confirmed live for Baldwin (October 22 release). [confirm: on-screen spelling of Property sub-type in Add/Edit] [confirm: on-screen names of the Agent and Unit fields]
