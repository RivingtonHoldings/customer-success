# QA: Dashboard FAQ

Article name: Dashboard FAQ. Title unchanged.

Sources:

- Old Notion page: https://app.notion.com/p/3668b9e0143880a193dff60620e30801 (Master Article List, last edited July 17, 2026)
- Intercom article ID 15216626, content ID 17993546
- Mirror: `docs/help-center/baldwin/dashboard-faq.md` (Baldwin only; CRMLS has no Dashboard FAQ)
- Screenshot of a saved search hot sheet widget, supplied by Tara September 22, 2026
- New Notion draft: https://app.notion.com/p/3e48b9e014388136ba05ee2adf6955ed

Scored by Claude for Tara, September 22, 2026. Check set: September 10, 2026, revision 2.

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | Old said "home screen" for the Dashboard; corrected, but the old form was inconsistent rather than a dangling reference |
| 2 visual_content_text | Pass | Pass | Old had no images. New carries one screenshot placeholder with its alt text |
| 3 undefined_terms | **Fail** | Pass | Old never defined Hot Sheet, and put "Market Monitor" in the description with no legacy framing. New defines Hot Sheet at first use and gives the Market Monitor its own section |
| 4 structured_enumeration | **Fail** | Pass | Old described a four-step procedure in flowing prose. New uses a numbered `Steps:` block |
| 5 query_answer_symmetry | Pass | Pass | All headings are questions in both |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | No role gates the Dashboard among non-client roles, so silence is correct. `Roles: All - but client` records it |
| 8 entity_distribution | **Fail** | Pass | Old answer to "How many Hot Sheets can I add?" was "There is no limit. You can add as many as you'd like," which never names Hot Sheets |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables in either |
| 11 overview_jtbd | **Fail** | Pass | Old had no opening paragraph at all |
| 12 instruction_completeness | **Fail** | Pass | Old stopped at "use it as your Hot Sheet" and its related-article link had no destination in the live body |
| 13 limitations_workarounds | Pass | Pass | The mobile answer names the gap and the route forward in both |
| 14 numerical_clarity | Pass | Pass | 998 days and "no limit" are exact in both. New adds the five-timeframe cap |

Old: 9 of 14. New: 14 of 14.

## Plain language gate

Old: **Fail**, on check 3.

| Term flagged | Replacement |
|---|---|
| "home screen", in the first heading | "the Dashboard", the product's own name for the page and the word every other Dashboard article uses |
| "the Market Monitor", in the description, presented as a Perchwell feature | Moved into the body as a legacy platform comparison, per the transition voice rule |
| "off-market", hyphenated | "Off market", two words, which is how the Hot Sheet widget labels the row |

New: **Pass**. Checks 1 through 5 all clear. Check 5 in particular: "monitor", "save", "add", and "track" all appear in the sections that cover those tasks, not only inside link titles.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 12.86 | 25.71 | +12.86 |
| Chunk independence (25) | 20.83 | 25.00 | +4.17 |
| Answer completeness (25) | 17.86 | 25.00 | +7.14 |
| Fin-parsable formatting (10) | 8.75 | 10.00 | +1.25 |
| Accuracy and confidence (10) | 6.00 | 10.00 | +4.00 |
| **Total** | **66.30** | **95.71** | **+29.41** |

Old band: Needs rewrite. New band: Fin-ready.

The rewrite does not reach 100 because Retrieval signals check 1 fails on the title, and that failure is recorded rather than waived. See Open items.

## Fin test questions

| Question, as a member would type it | Old answers from one section | New answers from one section |
|---|---|---|
| how many hot sheets can I have | Yes | Yes |
| what's the longest timeframe for a hot sheet | Yes | Yes |
| how many days back can a hot sheet go | Yes | Yes |
| does off market include expired listings | No. The old answer named withdrawn and cancelled and never mentioned expired, so a member asking about expired got no ruling | Yes |
| how do I set up a hot sheet for my brokerage | No. The old answer described office or agent filtering, not brokerage | Yes |
| how do I track just my office's listings | Partial. "Search by agents and select the agents in your office" is not the office filter | Yes |
| can I see my dashboard on my phone | Yes | Yes |
| where did the market monitor go | No. "Market Monitor" appeared only in the description metadata, never in the body | Yes |

## Open items

No `[confirm: ...]` markers. Tara answered all nine product questions before drafting, and the screenshot settled the Off market and timeframe answers.

1. **The title fails Retrieval check 1, which is the open question already logged for September 18.** `project-status.md` tracks it as "Do the approved `<Page> Overview` and `<Area> FAQ` title patterns satisfy Fin-readiness Retrieval check 1", owned by Tara and Kelly Miragliotta, with 28 live articles exposed. Dashboard FAQ is a third data point and it scores the failure, siding with Listings Widget Overview against Dashboard Overview, which passed check 1 and scored 30.0 of 30. If the team rules the patterns pass, this article scores 100.0 rather than 95.7 and the band does not change. The title was kept either way, because breaking a set of twelve to satisfy one check is the worse trade.

2. **Both sources were wrong about the same fact, for the third time.** Notion said "search by office"; the live article said "search by agents". The answer is that brokerage and office are separate filters and the member picks the one matching what they want to watch. Neither document had it, and they disagreed in a way that made the live version look authoritative. This is the case `content-standards.md` records under "Agreement between sources is not verification", now extended to sources that disagree and are both wrong.

3. **The timeframe answer has two owners, and the set already disagreed before this article existed.** `Add a Hot Sheet to the Dashboard` (Notion draft, not yet ported) carries a Things to Know bullet that states the five-timeframe cap and the tab behavior in nearly the same words as this article's Q3, and its delegation line names only two things to look up here, withholding the timeframe. `Dashboard Overview`, which is live, delegates three and includes the timeframe. **Resolved September 22, 2026 by Tara:** the Add a Hot Sheet bullet is cut and this article owns the answer. That article already states the number inside both `Steps:` blocks, where the member meets it, and a question-form heading is the stronger retrieval target for a question-shaped query. Its delegation line now names three things and matches Dashboard Overview's.

4. **"off-market" keeps its hyphen, and the exact-label rule does not reach it.** The Hot Sheet widget renders the row as Off market, and this article was briefly changed to match on September 22, 2026, along with the Add a Hot Sheet delegation line. **Reverted the same day by Tara.** The rule requiring an exact on-screen label governs controls a member has to find and click: buttons, filters, menu items, navigation targets. A category in a readout is none of those. Against it stand the term members actually type, the live article's own heading, and nine other uses across the mirror. Consistency across eleven articles beats matching a chart row's sentence case. `Dashboard Overview` needs no change, so no live-article port is required. The screenshot's alt text still reads "Off market" because it transcribes what is visible in the image, which the standard's no-inventory exception allows.

5. **Brokerage and office filtering had no home in a workflow article. Resolved September 22, 2026 by Tara.** `Add a Hot Sheet to the Dashboard` covered creating both Hot Sheet types and never mentioned scoping a search to a brokerage or an office, in its live version or its draft, so this FAQ briefly held the only copy. One sentence was added to that draft's "Set up a saved search hot sheet" lead. This article keeps the four-step short answer and the link, which is the split the say-once rule wants: the capability is named in the workflow article, the question is answered here.

6. **Evidence for the open "you can" question.** `project-status.md` asks whether FAQ answers should be excepted from the "you can" ban, noting that 12 of 16 FAQ articles fail scorecard check 5 on it and citing this article's own "You can add as many as you'd like." The rewrite answers it without the exception: "Add as many Hot Sheets to the Perchwell Dashboard as you need." Reads naturally under a question-form heading, so the ban appears satisfiable without one.

7. **Screenshot to place.** Tara has the image. The placeholder carries its alt text; at Intercom transfer that text goes into Intercom's alt field, not the caption.

8. **Manual after transfer:** Fin labels per `docs/standards/fin-labeling.md`, MLS audience, and publishing.
