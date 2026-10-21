# QA: Create a CMA with a Subject Property

- Article: Create a CMA with a Subject Property (title unchanged)
- Sources: live Intercom article 15216797 (content ID 17993797), mirror `docs/help-center/baldwin/create-a-cma-with-a-subject-property.md`; old Notion page https://app.notion.com/p/3658b9e0143880c39f4fdc563885715d; the article's Arcade walkthrough (sB2LuiL7y0c67q5UxvjG), captured after March 27, 2026 and before cutover; teammate product answers, October 12, 2026
- Scored by Claude with `/article-rewrite`, October 12, 2026, against the scorecard check set revision 2

## Golden questions

| # | Factor | Live | Rewrite | Note |
|---|---|---|---|---|
| 1 | disambiguation | Fail | Pass | Live used emoji pointers and "the listing action button" |
| 2 | visual_content_text | Pass | Pass | Live has no images; rewrite placeholders carry alt text |
| 3 | undefined_terms | Fail | Pass | CMA and comps now defined in the opening |
| 4 | structured_enumeration | Pass | Pass | |
| 5 | query_answer_symmetry | Pass | Pass | |
| 6 | self_contained_sections | Fail | Pass | Live opened a section with "Once you are satisfied with your results" |
| 7 | audience_specification | Pass | Pass | No role gate |
| 8 | entity_distribution | Pass | Pass | |
| 9 | semantic_chunk_boundaries | Pass | Pass | |
| 10 | restate_questions | Pass | Pass | No tables |
| 11 | overview_jtbd | Fail | Pass | Live has no opening paragraph in the body |
| 12 | instruction_completeness | Fail | Pass | Live first procedure skipped selecting CMA Subject Property and ended before the outcome |
| 13 | limitations_workarounds | Fail | Pass | Live said "Listing Detail pages only" while documenting a Preview path. Confirmed October 12, 2026: CMA Subject Property is Listing Detail Page only, and Preview offers Actions, then Quick CMA; the rewrite states that as the route forward |
| 14 | numerical_clarity | Pass | Pass | Defaults confirmed: 1 mile, up to 20 miles, plus or minus 1 bed and bath, plus or minus 10% living area, Closed within 180 days |

Live: 8 of 14. Rewrite: 14 of 14.

## Plain language gate

Pass. "Comps" is the member's own word and is defined on first use. Apx living area, Distance (miles), and the other criteria are named by their on-screen labels only in the labeled list, where the member looks at the controls.

## Dimension scores

| Dimension | Weight | Live | Rewrite | Delta |
|---|---|---|---|---|
| Retrieval signals | 30 | 12.9 (3/7) | 30.0 (7/7) | +17.1 |
| Chunk independence | 25 | 12.5 (3/6) | 25.0 (6/6) | +12.5 |
| Answer completeness | 25 | 14.3 (4/7) | 25.0 (7/7) | +10.7 |
| Fin-parsable formatting | 10 | 3.8 (3/8) | 10.0 (8/8) | +6.2 |
| Accuracy and confidence | 10 | 6.0 (3/5) | 10.0 (5/5) | +4.0 |
| Total | 100 | 49.4 | 100.0 | +50.6 |

Live band: Not retrievable as written. Rewrite band: Fin-ready, no `[confirm]` markers.

Live failures, in short: description over 140 characters and in "In this article" form; no opening paragraph; H1 section headings; one heading without the feature name; emoji callouts, bold UI labels, and horizontal rules; "you can" and "allows you to"; a missing step; a constraint contradicted by the article's own steps.

## Fin test questions

| Question | Live answers from one section | Rewrite answers from one section |
|---|---|---|
| How do I run comps for a specific address? | Yes, but the steps skip selecting CMA Subject Property | Yes |
| Which listings does the comps search look at? Does it include sold listings? | No | Yes |
| How far out can I set the distance for comps? | Yes | Yes |
| How do I widen the square footage range for my comps? | Partly; no range stated | Yes |
| Can I start CMA Subject Property from a search preview? | Contradictory | Yes: Listing Detail Page only, with Quick CMA as the route from Preview |
| Where does my subject property go in the CMA? | Partly; pinned in results only | Yes |
| How do I get back to my search without running comps? | No | Yes |
| How do I email or print the CMA? | Link only | Link only, with the step names |

## Open items

- Resolved October 12, 2026: CMA Subject Property starts from the Listing Detail Page only; from a listing preview, members click Actions, then select Quick CMA.
- The Arcade walkthrough is out of date: it shows a three-dot icon rather than Listing Actions, and an Auto CMA option the product no longer has. The video needs re-recording so the written steps match it. The Listing Detail Page frames also show the listing agent's team name, email, and phone; replace them when the video is re-recorded.
- Auto CMA is gone, per the teammate on October 12, 2026, but the live Baldwin Listing Detail Page Overview articles (`listing-detail-page-overview.md`, `listing-detail-page-overview-14784837.md`) and CRMLS `navigating-the-listing-detail-page.md` still describe it.
- The live link to Create a Quick CMA Report pointed at `intercom.help/perchwell-help-center-baldwin/...` with the text "Create a CMA Report"; the rewrite links the public Baldwin URL with the article's real title. Check at port that it resolves for Baldwin members.
- Roles: the old row has no Roles value; `All Except Client` was proposed to match Create a Listing Report.
- Two screenshot placeholders need current captures.
