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

1. **The title fails a scorecard check the naming standard requires it to fail.** Retrieval signals check 1 bans a title that repeats a Perchwell page name or a collection name. "Dashboard FAQ" does both, and so will all twelve Baldwin `<Area> FAQ` articles, because `content-standards.md` gives `<Area> FAQ` as the title pattern for the FAQ article type and Intercom derives the `<Area> / FAQs` collection from it. The rule and the standard contradict each other on every FAQ article in the backlog. Kelly and Rafe to rule: carve an FAQ exception into check 1, or change the FAQ title pattern. The title was kept either way, because breaking a set of twelve to satisfy one check is the worse trade.

2. **Both sources were wrong about the same fact, for the third time.** Notion said "search by office"; the live article said "search by agents". The answer is that brokerage and office are separate filters and the member picks the one matching what they want to watch. Neither document had it, and they disagreed in a way that made the live version look authoritative. This is the case `content-standards.md` records under "Agreement between sources is not verification", now extended to sources that disagree and are both wrong.

3. **`Add a Hot Sheet to the Dashboard` says "Monitor activity for up to 2+ years".** That is 998 days stated vaguely, and it fails numerical clarity on its own article. Recommend replacing it with "up to 998 days" when that article is next touched, so the set states the number one way.

4. **Brokerage and office filtering has no home in a workflow article.** `Add a Hot Sheet to the Dashboard` covers creating both Hot Sheet types and never mentions scoping a search to a brokerage or an office. This FAQ now carries the only copy. Recommend adding it there as a follow-up, with this article keeping the short answer and the link.

5. **Screenshot to place.** Tara has the image. The placeholder carries its alt text; at Intercom transfer that text goes into Intercom's alt field, not the caption.

6. **Manual after transfer:** Fin labels per `docs/standards/fin-labeling.md`, MLS audience, and publishing.
