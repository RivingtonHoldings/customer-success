# QA: Analytics Page Overview

- Article name: Analytics Page Overview
- Old title: Analytics Tab Overview. It was retitled because "Analytics Tab" competes with Analytics Tab Walkthrough, which covers the Analytics view on the Search page, and because Analytics is a page in the top navigation, not a tab.
- Sources: live Intercom article 13623210 (content ID 15695161), mirrored at `docs/help-center/baldwin/analytics-tab-overview.md`. Old Notion page: [Analytics Page Overview](https://app.notion.com/p/34b8b9e0143880fd8f04f5f389a33641) (Master Article List). Also the Agent/Office/Brokerage (Firm) Ranking Report and Team Ranking Report release notes, the internal Market Analytics troubleshooting page, and the June 2026 Agent Ranking screenshot from the old page.
- Teammate answers and screenshots, October 14, 2026:
  - Agents and brokers can both open Analytics.
  - Closed Date starts at "on or after 1 years ago".
  - Clicking a ranking value opens a menu: Drill into Individual Closed Listings, Copy value, Expand.
  - Export Dashboard is on every report. Its Format options are PNG (Image), PDF, XLSX (Excel), and CSVs (in ZIP file).
  - Office Ranking has these filters and columns (screenshot provided). Team Ranking has these columns (screenshot provided).
  - Decimal unit counts come from co-agent splits.
  - Market Activity statuses, the Market Analytics Field dropdown, and Absorption Rate and Months of Supply are all current.
- Scored by Claude (article-rewrite), October 14, 2026, against scorecard revision 2.

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Pass | Pass | Old had no images. New has six placeholders, each with alt text |
| 3 undefined_terms | Fail | Pass | Old used "MLS#" and left Total Volume and the columns undefined. New defines each column and CSV |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | Old used bare nouns ("Report Types", "Agent Ranking Report"). New headings are task-led |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | Agents and brokers both have access, confirmed, so the body says nothing |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Fail | Pass | Old used multiple H1s and repeated the same "Things to Know" block under each report |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | Old opened with "When to Use" and had no "Use this article to" opening |
| 12 instruction_completeness | Fail | Pass | Old steps stopped at "Choose the report". New steps end with the outcome |
| 13 limitations_workarounds | Pass | Pass | Include Zero Volume is still open; see Open items |
| 14 numerical_clarity | Fail | Pass | Old stated the default date as the prior calendar year; the product shows "on or after 1 years ago" |

Old: 7 of 14. New: 14 of 14, with no `[confirm: ...]` markers open.

## Plain language gate

New: pass. The draft has no do-not terms. "Drill into Individual Closed Listings" is a control's exact on-screen label. The prose says "the closed listings behind a ranking", not "drill down".

Old: fail.
- "MLS#" should be "MLS ID".
- "Sort by available criteria" should be "filters", since the controls filter and do not sort.
- "Great for", "makes it easy", and "curated" are marketing phrasing. Drop them and state the function.

## Scores

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 8.6 (2 of 7) | 30.0 | +21.4 |
| Chunk independence (25) | 16.7 (4 of 6) | 25.0 | +8.3 |
| Answer completeness (25) | 14.3 (4 of 7) | 25.0 | +10.7 |
| Fin-parsable formatting (10) | 6.3 (5 of 8) | 10.0 | +3.7 |
| Accuracy and confidence (10) | 4.0 (2 of 5) | 10.0 | +6.0 |
| **Total** | 49.9, Not retrievable as written | 100.0, Fin-ready | +50.1 |

Checks the old article failed:
- Retrieval: a title that clashes with Analytics Tab Walkthrough, a 186-character description, no jobs opening, bare-noun headings, and no heading echo.
- Chunk independence: H1 used for sections, and filter lists and default-date facts repeated under every report.
- Answer completeness: steps with no outcome, an unstated default, and no link to the Search Analytics view.
- Formatting: terminal periods on steps, bold labels, and horizontal rules.
- Accuracy: a default date that contradicts the product, marketing phrasing, and "you can" / "Use the".

Include Zero Volume is the one product question still open; see Decisions.

## Fin test questions

| Question | Old, one section | New, one section |
|---|---|---|
| How do I see which agents sold the most this year? | Partly (Agent Ranking, no column meanings) | Yes |
| Why does an agent show 4.5 sales? | No | Yes |
| How do I see the listings behind an agent's volume? | Partly ("click any ranking stat") | Yes |
| Can I export the agent ranking to Excel? | No | Yes |
| What date range does the ranking report use by default? | Yes, but wrong | Yes |
| Is there a team ranking report? | No | Yes |
| What do Absorption Rate and Months of Supply mean? | Yes | Yes |
| How do I see recent price drops on a map? | Partly | Yes |

## Open items

Confirm markers resolved October 14, 2026, from the teammate's answers and screenshots:
- Agent Ranking uses the Units and Volume columns.
- Agent Status and Office Status values are Active and Inactive.
- Structure Style values are Condo and Other. Agent Ranking also has this filter.
- A firm's totals combine all of its offices.
- Drill into Individual Closed Listings opens a window titled "Drill - <column>" with a row count and Download.
- Expand shows the value in a label.
- The Export Dashboard name field is labeled File name.

Resolved in the second round, October 14, 2026, from the Firm and Team Ranking screenshots and the teammate's answers:
- Firm Ranking has the same columns as the other ranking reports, with Firm MLS ID and Firm Name.
- Inactive agents appear when Agent Status is set to Inactive. The live article's "only active agents appear" claim is dropped as wrong.
- All four ranking reports share Closed Date, County, City, Subdivision, Property Type, Property Sub Type, Structure Style, and Limit Number of Results. Each adds its own filters: Agent Status and Agent Office; Office Status and Office Firm; Firm Office Status; Team Status.

No confirm markers remain. The values of Firm Office Status and Team Status were not given, so the draft names the filters without listing values.

Product issue to report: the Drill window's Filters (14) section and its column headings show internal data names, such as "Dbt Perchwell Marts Baldwin Ranking Office Closed Date". Members may ask what these mean. The article does not describe that section.

Decisions for the team:
- **Include Zero Volume.** The live article says Agent and Office Ranking have an Include Zero Volume option that adds agents or offices with no sales. Neither the June Agent Ranking screenshot nor the October Office Ranking screenshot shows it. The draft leaves it out. If the option is gone, add one sentence under the bare-deficit exception so Fin unlearns it. If it still exists, add it to the ranking filters list.
- **Market Activity statuses.** New, Coming Soon, Price Drop, Sold, Under Contract, and Active Under Contract are kept as a sentence, not a labeled list. Defining each status would need sources the draft does not have. A reviewer may want the list.
- **Market Analytics Closed Date.** The live article labels this filter Close Date. The draft uses Closed Date to match the ranking report screenshots. This is unverified on the Market Analytics screen.
- **Scope.** Option A was taken: one Overview covering all six reports. The teammate did not choose a scope, so this was the recommended default. The old row's note asks to separate ranking reports from market analytics, which the draft does with two H2 groups.
- **Screenshots must not reuse the June 2026 images as they stand.** The Agent Ranking image shows real agent names, and so will any new capture of a ranking report. Decide whether to blur names or accept roster data that members can already see in Perchwell.
- **Link check at port.** The Analytics Tab Walkthrough mirror URL is a default help center `/en/` link. The draft points at `/baldwin/en/`; confirm it resolves.
- **Retitle redirect.** The old title Analytics Tab Overview should redirect or be retired in Intercom when the new article is ported.
