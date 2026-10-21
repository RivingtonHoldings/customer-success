# QA: What Changed When You Moved to Perchwell

- Old title: Key Workflow Changes
- Old Notion page: https://app.notion.com/p/3378b9e0143880048044f4f654c08890 (Master Article List, read only)
- Intercom article ID 14459729, content ID 16905641, Baldwin only, collection Then vs. Now
- Mirror: `docs/help-center/baldwin/key-workflow-changes.md` (live body confirmed identical with `get_article`, October 19, 2026)
- Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-10-19-key-workflow-changes-rewrite.md`
- Notion: https://app.notion.com/p/3fe8b9e0143881e3b27bee043407c3c3
- Scored by Claude for Kevin, October 19, 2026, against scorecard revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Pass | Pass | No images |
| 3 undefined_terms | Fail | Pass | FKA, FHA, BR, CMA, CollabLink were undefined; the undefined Listing Integrity review sentence was cut |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | One bare heading over a 15-row table; now one heading per change |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | Every member except invited clients; nothing gated |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Fail | Pass | 15 topics in one block |
| 10 restate_questions | Fail | Pass | Table had no intro; table removed |
| 11 overview_jtbd | Fail | Pass | |
| 12 instruction_completeness | Pass | Pass | No steps |
| 13 limitations_workarounds | Fail | Pass | "Cross-field OR not yet supported" stated plainly without "not yet" |
| 14 numerical_clarity | Fail | Pass | "~25 calculators" dropped; Hot Sheet 998-day maximum stated |

## Plain language gate

New: pass. Old: fail on "Navigate to" (open), "Leverage" (open, check), "third-party" (free calculator sites), and "FKA".

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 8.6 (2/7) | 30.0 (7/7) | +21.4 |
| Chunk independence (25) | 16.7 (4/6) | 25.0 (6/6) | +8.3 |
| Answer completeness (25) | 7.1 (2/7) | 25.0 (7/7) | +17.9 |
| Fin-parsable formatting (10) | 5.0 (4/8) | 10.0 (8/8) | +5.0 |
| Accuracy and confidence (10) | 2.0 (1/5) | 10.0 (5/5) | +8.0 |
| Total | 39.4, Not retrievable as written | 100.0, Fin-ready | +60.6 |

The new draft passes every check. Answer completeness 6 passed once the undefined Listing Integrity review sentence was cut (Kevin, October 19, 2026).

## Fin test questions

| Question | Old, one section | New, one section |
|---|---|---|
| Where is Quick Search in Perchwell? | Partly, wrong equivalent | Yes |
| What happened to Class in search? | Partly, said one type only | Yes |
| Why can't I see Print until I select listings? | Partly, said all actions hidden | Yes |
| Where did CollabLink go? | Yes | Yes |
| Why can't I edit my client's email address? | Yes | Yes |
| Where is the Market Monitor? | Yes | Yes |
| Where is the mortgage calculator? | No, pointed to outside sites only | Yes |
| Where are BR Announcements and the Message Center? | Split across two rows | Yes |

## Source differences and decisions

- Live article and old Notion page match apart from the retired "In this article" heading and support footer.
- Legacy platform genericized to "a legacy platform", Paragon feature names kept (Kevin, October 19, 2026).
- Table replaced by one section per change, linking to the article that teaches it. Title changed to a task-led form; old title kept in metadata.
- Corrected from Kevin's answers, October 19, 2026: Quick Search equivalent is the Template Search, one at a time (live said multiple templates); Property Type allows one or more types from the Quick Filter (live said one); with no listings selected only Export CSV is available (live said all actions hidden); CollabLink became Messages, and public links still need no login; contact details rule confirmed for invited clients; agents are not copied on every email (saved search alerts follow the Recipient setting); a saved search must be linked to a Hot Sheet first; Mortgage & Tax covers payment estimates; Features rule kept as a plain fact; FHA is the Fair Housing Act; the bulletin board is BR Announcements.

## Open items

- Resolved October 19, 2026: Kevin confirmed the agent receives a copy of every email Messages sends to a client. No `[confirm: ...]` markers remain.
- Sibling fixes done October 19, 2026: Actions Menu Options on the Search Page now says only Export CSV is available with no listings selected. Print or Save Search Results as a PDF now has the member select a listing first; Kevin tested that Print still includes every search result with 2 selected.
- Seven other Then vs. Now articles are unmigrated, including New Terminology, which overlaps this one. CRMLS applicability of the collection is still open in `project-status.md`.
- Fin labels and audience set manually at port.
