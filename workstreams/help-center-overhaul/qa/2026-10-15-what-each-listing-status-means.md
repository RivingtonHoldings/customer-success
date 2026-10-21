# QA: What Each Listing Status Means

- **Article:** What Each Listing Status Means
- **Old title:** Listing Statuses in Perchwell
- **Sources:** old Notion page [Listing Statuses in Perchwell](https://app.notion.com/p/3498b9e014388026befedfcbe1868014); Intercom article 14709241, content 17268243; mirror `docs/help-center/baldwin/listing-statuses-in-perchwell.md` (Baldwin only, not shared). Live body confirmed with `get_article` on October 15, 2026, since the mirror was 16 days old; it matched.
- **Cross-checked against:** Top Compliance Questions, Most Common Questions Asked to MLS Staff, New Terminology, and the Listing Maintenance FAQ, Manage Listings Page Overview, and Filter Your Search by Status and Price Changes drafts.
- **Notion draft:** https://app.notion.com/p/3fa8b9e0143881b79c55f591bbacdd6a
- **Scored by:** Claude for Kevin, October 15, 2026, scorecard revision 2.

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Pass | Pass | No images in either version |
| 3 undefined_terms | Pass | Pass | Temp off mkt now defined |
| 4 structured_enumeration | Pass | Pass | Table became two labeled lists |
| 5 query_answer_symmetry | Fail | Pass | Old article had one empty H2 |
| 6 self_contained_sections | Fail | Pass | Old table had no heading or intro |
| 7 audience_specification | Pass | Pass | Canceled role corrected to brokers and MLS staff, confirmed |
| 8 entity_distribution | Fail | Pass | "Listing status" now in every heading and lead |
| 9 semantic_chunk_boundaries | Fail | Pass | Current, off-market, and legacy statuses split |
| 10 restate_questions | Fail | Pass | Old table had no intro sentence |
| 11 overview_jtbd | Fail | Pass | |
| 12 instruction_completeness | Pass | Pass | No procedures |
| 13 limitations_workarounds | Pass | Pass | |
| 14 numerical_clarity | Pass | Pass | Old 365-day rule conflicted with two sources that say 180; dropped |

Old: 8 of 14. New: 14 of 14.

## Plain language gate

Pass. No do-not list terms. Status names follow the Search filter's on-screen spelling, and Temp off mkt is spelled out on first use.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 8.6 (2/7) | 30.0 (7/7) | +21.4 |
| Chunk independence (25) | 12.5 (3/6) | 25.0 (6/6) | +12.5 |
| Answer completeness (25) | 17.9 (5/7) | 25.0 (7/7) | +7.1 |
| Fin-parsable formatting (10) | 7.5 (6/8) | 10.0 (8/8) | +2.5 |
| Accuracy and confidence (10) | 4.0 (2/5) | 10.0 (5/5) | +6.0 |
| **Total** | **50.4, Needs rewrite** | **100.0, Fin-ready** | **+49.6** |

Old failures: bare title, 69-character description, no opening, empty heading, no echo, legacy rows mixed with current ones, Coming Soon duplicating Closed's definition, bold header row, no table intro, no links, Paragon named, and the 365-day conflict left unmarked.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| What does active under contract mean? | Yes | Yes |
| Can I show a coming soon listing? | No, definition was wrong | Yes |
| How long can a listing stay coming soon? | No | Yes |
| What does temp off mkt mean? | No, label did not match | Yes |
| What is the difference between withdrawn and canceled? | Yes | Yes |
| Who can change a listing to canceled? | Yes, but named the wrong role | Yes |
| Why don't I see my closed listings in Manage Listings? | No | Yes |
| What happened to Contingent on Sale? | Yes | Yes |

## Decisions taken (Kevin, October 15, 2026)

- Title changed to What Each Listing Status Means.
- Coming soon takes the old Notion page's definition plus the 30-day limit from the Listing Maintenance FAQ. The live article had copied Closed's definition into it.
- Syndication of Coming soon listings left out: Top Compliance Questions says they are not syndicated to public websites, the Listing Maintenance FAQ says they syndicate through normal channels. Unresolved; belongs to those articles.
- Active New Construction day rule dropped (live said 365 days, old Notion page and Most Common Questions say 180, and the live text named Paragon). Only the legacy-name mapping from New Terminology is kept.
- Active under contract uses the Top Compliance wording on backup offers and seller-optional showings.
- Changing a listing's status is out of scope; it is a separate task with its own old draft (Baldwin| Changing and Updating your Listing Status).
- Canceled: only brokers and MLS staff can change a listing to Canceled, and agents cannot. The live article said brokers and office administrators. Kevin confirmed on October 15, 2026, and the draft adds the route for agents: ask their broker.
- Roles: All Except Client. Collection: FAQs (old row FAQs & What's Coming; Intercom collection FAQs & Cheat Sheets).

## Open items

- Status spelling comes from the Search filter (Filter Your Search by Status and Price Changes draft). The Listing status dropdown in Add/Edit has not been checked against it; a screenshot would settle it.
- The Filter Your Search by Status and Price Changes link points at its Notion page; replace with the Intercom URL once that article is ported.
- Manage Listings Page Overview is stored in Intercom under a default help center URL (`/en/`); confirm the `/baldwin/en/` link resolves at transfer.
- The Coming soon syndication conflict between Top Compliance Questions and the Listing Maintenance FAQ should be resolved in those articles.
