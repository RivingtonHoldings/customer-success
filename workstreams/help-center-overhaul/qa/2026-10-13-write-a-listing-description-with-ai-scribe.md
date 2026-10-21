# QA: Write a Listing Description with AI Scribe

- **Article:** Write a Listing Description with AI Scribe. Old title: AI Scribe
- **Sources:** Intercom article 11801815, content 12922702; mirror `docs/help-center/baldwin/ai-scribe.md` (Baldwin only, not shared); old Notion page https://app.notion.com/p/1dc8b9e01438808c982af7a5850035e5 with its April 20, 2026 screenshot; product screenshots captured October 13, 2026, and answers from Kevin, October 13, 2026
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-10-13-write-a-listing-description-with-ai-scribe-rewrite.md`; Notion https://app.notion.com/p/3f88b9e014388199bf4acf963f73ed6e
- **Scored by:** Claude for Kevin, October 13, 2026. Scorecard check set revision 2

## Golden questions

| # | Factor | Old | New | Note |
|---|---|---|---|---|
| 1 | disambiguation | Pass | Pass | |
| 2 | visual_content_text | Pass | Pass | Old had a video and no images; new placeholders carry alt text |
| 3 | undefined_terms | Fail | Pass | "Add/Edit Form" was never explained; new draft defines Add/Edit on first use |
| 4 | structured_enumeration | Pass | Pass | |
| 5 | query_answer_symmetry | Fail | Pass | "Listing description generation and refinement" and "Fair housing and accuracy" replaced by task headings carrying AI Scribe |
| 6 | self_contained_sections | Fail | Pass | Old Generate steps sat under "Highlight what you want to feature" and depended on the section before it |
| 7 | audience_specification | Pass | Pass | No role gate beyond listing entry; Roles property records All Except Client |
| 8 | entity_distribution | Fail | Pass | Old setting and fair housing sections never named AI Scribe |
| 9 | semantic_chunk_boundaries | Fail | Pass | Old emphasis options and Generate steps shared one block |
| 10 | restate_questions | Pass | Pass | No tables |
| 11 | overview_jtbd | Fail | Pass | Old article had no opening paragraph |
| 12 | instruction_completeness | Fail | Pass | Old steps stopped at turning on the toggle and at editing |
| 13 | limitations_workarounds | Fail | Pass | 2,000-character limit and the replace behavior now stated where the member meets them |
| 14 | numerical_clarity | Pass | Pass | |

Old: 6 of 14. New: 14 of 14.

## Plain language gate

Pass. "Public remarks" is the fair housing notice's own wording and the term members may type; Remarks/Directions, Listing description, Length, Tone, and Focus are named only where the member acts on them.

## Dimension scores

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 8.6 (2 of 7: bare-noun title, no opening, headings without the feature name, no heading echo, opening bullets out of section order) | 30.0 | +21.4 |
| Chunk independence (25) | 4.2 (1 of 6: Generate steps depend on the prior section, feature name missing, mixed topics, H1 sections, review-and-edit stated three times) | 25.0 | +20.8 |
| Answer completeness (25) | 7.1 (2 of 7: steps without outcomes, no defaults, no character limit, Add/Edit undefined, no link to submitting) | 25.0 | +17.9 |
| Fin-parsable formatting (10) | 6.3 (5 of 8: inexact labels, bolded UI, horizontal rules) | 10.0 | +3.7 |
| Accuracy and confidence (10) | 4.0 (2 of 5: "emphasis options", Generate, and Create New Listing do not match the product; "Use" and "lives in" verbs) | 10.0 | +6.0 |
| **Total** | **30.2, Not retrievable as written** | **100.0, Fin-ready** | **+69.8** |

No `[confirm: ...]` markers remain.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I use AI Scribe to write my listing description? | Partial, split across two sections | Yes |
| Where is AI Scribe in the listing form? | Partial, names Listing Description but not Remarks/Directions | Yes |
| What tones can AI Scribe write in? | Partial, three of five with "such as" | Yes |
| Can I regenerate the description with different settings? | No | Yes |
| Will AI Scribe overwrite what I already wrote? | No | Yes |
| Is there a character limit on the listing description? | No | Yes |
| Is the AI Scribe description fair housing compliant? | Partial | Yes |
| If I turn off AI Scribe, do I lose the text? | No | Yes |

## Open items

- Resolved October 13, 2026 by Kevin: the button is Apply changes (orange, with a refresh icon), not Generate as the live article says; every Focus option can be selected at once; the button is Add New Listing, not Create New Listing as the live article says. Add and Edit Listings ("+ Add New Listing") needs the same correction when it migrates
- The toggle-on screenshot lives only on the old Notion page; re-upload it or recapture it for the new row. A toggle-off capture is saved at `outputs/drafts/images/2026-10-13-ai-scribe-toggle-off.png` if the team prefers it
- Sibling cleanup: Add and Edit Listings and My Listings Overview both say AI Scribe can "draft or revise remarks and descriptions" and "rewrite text". AI Scribe writes only the public remarks in the Listing description field, so both claims need narrowing when those articles migrate
- Fin labels and MLS audience set by hand at port
