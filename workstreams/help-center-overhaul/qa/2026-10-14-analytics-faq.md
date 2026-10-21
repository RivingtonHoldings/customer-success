# QA: Analytics FAQ

- Article name: Analytics FAQ (title unchanged)
- Old Notion page: https://app.notion.com/p/3658b9e01438800b97d2ccc999061ce2
- Intercom article ID 15200594, content ID 17970407
- Mirror: `docs/help-center/baldwin/analytics-faq.md` (matches the stored Intercom body, checked October 14, 2026)
- Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-10-14-analytics-faq-rewrite.md`
- New Notion page: https://app.notion.com/p/3f98b9e01438813888d6f8496a4df714
- Scored by Claude for Kevin, October 14, 2026, against scorecard revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Pass | Pass | No images in either version |
| 3 undefined_terms | Fail | Pass | "Search Analytics" never distinguished from the Analytics page; now a question of its own. PDF defined |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Pass | Pass | Question headings |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | Agent access to all six reports confirmed by Kevin |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | "Use this article to" opening added |
| 12 instruction_completeness | Pass | Pass | No Steps blocks |
| 13 limitations_workarounds | Fail | Pass | 8-chart limit now has the route forward: delete a chart first |
| 14 numerical_clarity | Pass | Pass | 8 charts, six reports |

## Plain language gate

Pass on the rewrite. No do-not-list terms. "AI-generated" and "PDF" are words members use.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 17.1 | 30.0 | +12.9 |
| Chunk independence (25) | 16.7 | 25.0 | +8.3 |
| Answer completeness (25) | 10.7 | 25.0 | +14.3 |
| Fin-parsable formatting (10) | 8.8 | 10.0 | +1.2 |
| Accuracy and confidence (10) | 6.0 | 10.0 | +4.0 |
| Total | 59.3 | 100.0 | +40.7 |

Old: Needs rewrite. New: Fin-ready, 14 of 14 golden questions, plain language gate passed. No `[confirm: ...]` markers remain.

Old failures: description 55 characters, no opening, the chart answer never names Analytics, one-sentence answers, bold "8 charts", no links, chart saving unclear on what is kept, 8-chart limit with no route forward, "Search Analytics" undefined, Paragon named, "You can".

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| Can agents run the Agent Ranking report or is it broker only? | Partly, no report named | Yes |
| What reports are in Analytics? | No | Yes |
| What is the max number of charts in analytics? | Yes | Yes |
| I have 8 charts and can't add another, what do I do? | No | Yes |
| Do my charts stay when I save my search? | Yes | Yes |
| Why don't my analytics charts show the whole market? | No | Yes |
| How do I email my analytics charts to a client? | No | Yes |
| Where is Statistical Reporting in Perchwell? | No | Yes |

## Open items

- Resolved October 14, 2026 from Kevin's screenshots: the Analytics option sits next to View, above the search results, among the view icons (not a dropdown). The live Analytics Tab Walkthrough still says View dropdown, then Analytics; flag for that article's rewrite.
- Resolved October 14, 2026 from Kevin's screenshot: a chart is deleted with the x icon in its upper right, whose hover label reads Delete and the chart name (Delete Price).
- Share scope: Analytics Tab Walkthrough describes one Share icon for the view, while Share and Export Analytics Charts says to click Share on the chart you want. The draft says "Click Share in the Analytics view" and does not claim one chart or all.
- Six reports confirmed from Kevin's screenshot, October 14, 2026: Agent, Office, Firm, and Team Ranking (labeled Broker), Market Activity and Market Analytics (labeled Market). The live Analytics Tab Overview lists only four; the Analytics Page Overview draft covers all six.
- Invited clients editing charts on a shared saved search left out at Kevin's direction.
- Roles set to All Except Client; the old row had none. Kevin did not object, but did not confirm.
- Links to Analytics Tab Walkthrough, Share and Export Analytics Charts, and Manage Your Saved Searches use Baldwin paths, but the mirror records those three at the default help center (`/en/`). Confirm they resolve at transfer.
- Visuals: none. The six-report list and the Analytics page screenshot placeholder were cut after the set check found the Analytics Page Overview draft owns both; the FAQ names the reports in two sentences and links it. The link is to the Notion page and needs replacing with the Intercom URL at transfer.
- Set check, October 14, 2026: the Analytics collection holds this FAQ, Analytics Page Overview (Draft), and an empty [Placeholder] Analytics row. Legacy sentence matched to the Overview's wording, "may know Analytics as Statistical Reporting"; "the Analytics view on the Search page" matches the Overview's term.
