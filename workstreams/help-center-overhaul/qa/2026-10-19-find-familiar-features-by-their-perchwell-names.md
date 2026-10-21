# QA: Find Familiar Features by Their Perchwell Names

- **Article:** Find Familiar Features by Their Perchwell Names
- **Old title:** New Terminology
- **Sources:** old Notion page https://app.notion.com/p/3378b9e0143880e396bce86cf265d2ab; Intercom article 14459704, content 16905403; mirror `docs/help-center/baldwin/new-terminology.md`. Baldwin only, not shared with CRMLS.
- **Scored by:** Claude, for Kevin Liang, October 19, 2026. Scorecard revision 2.

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Pass | Pass | No images |
| 3 undefined_terms | Fail | Pass | CRS now defined as Courthouse Retrieval System, confirmed by Kevin October 19, 2026. CollabLink is the member's own legacy term in the legacy column |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | Old article had no headings |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Fail | Pass | Old named staff-only masquerading with no role; row removed |
| 8 entity_distribution | Fail | Pass | |
| 9 semantic_chunk_boundaries | Fail | Pass | One 20-row table split into five areas |
| 10 restate_questions | Fail | Pass | Every table has an intro sentence |
| 11 overview_jtbd | Fail | Pass | |
| 12 instruction_completeness | Pass | Pass | No steps |
| 13 limitations_workarounds | Pass | Pass | |
| 14 numerical_clarity | Pass | Pass | |

## Plain language gate

Pass. No do-not-list terms. "Masquerading" (staff-only, product-context) and "Log in as user" were removed with the Assume Identity row.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 8.6 (2/7) | 30.0 (7/7) | +21.4 |
| Chunk independence (25) | 20.8 (5/6) | 25.0 (6/6) | +4.2 |
| Answer completeness (25) | 10.7 (3/7) | 25.0 (7/7) | +14.3 |
| Fin-parsable formatting (10) | 7.5 (6/8) | 10.0 (8/8) | +2.5 |
| Accuracy and confidence (10) | 6.0 (3/5) | 10.0 (5/5) | +4.0 |
| **Total** | **53.6, Needs rewrite** | **100.0, Fin-ready, both gates pass** | **+46.4** |

Old failures: bare-noun title; "In this article" description; no opening; no headings or echo; one table mixing every area; bold header cells; no table intro; Paragon named; staff-only term with no role; no links.

## Fin test questions

| Question | Old, one section | New, one section |
|---|---|---|
| What are Listing Carts called in Perchwell? | Yes | Yes |
| Where did Power Search go? | Yes | Yes |
| Where is the agent roster? | Yes | Yes |
| What happened to Class in search? | Yes | Yes |
| Where is Market Monitor in Perchwell? | Yes | Yes |
| How do I copy a listing? | Partly, names Duplicate only | Yes, plus the outcome and a link |
| Where are my partial listings? | Yes | Yes, plus a link |

The old article answers from one section only because it has one section; Fin retrieves it as a single unlabeled table chunk.

## Decisions taken

- Legacy platform genericized per the standard (option A, confirmed by Kevin). "Paragon Help" became "Help" and "Paragon Connect (mobile)" became "Connect mobile app" in the legacy column, since both carried the platform name.
- Title changed to the task-led proposal (confirmed by Kevin). Collision check: no matching article, collection, or page name.
- Grouped into five H2 areas (confirmed by Kevin).
- Assume Identity row removed. Baldwin has a live Assume Identity article for brokers and admins, so the name is unchanged in Perchwell, and "Masquerading" is staff-only per product-context. Removal confirmed by Kevin, October 19, 2026.
- "Spreadsheets" now maps to column templates in the Columns menu, the settled term (product-context, October 8, 2026), replacing "Templates (search results columns)".
- "Property Subtype" written as "Subtype", since the on-screen label is Property sub type and prose says subtype.

- Product answers from Kevin, October 19, 2026: the Listing Detail Page has a Mortgage & Tax section (replaces "Mortgage Calculator"); the Add/Edit button is labeled Autofill; Analytics is the only label ("Broker Analytics" dropped); Tags and public links belong in the Collaboration Center / CollabLink row; the About Me Page maps to User settings; Help sits at the far right of the top navigation; Maintain Listings maps to the Manage Listings page and the Add/Edit form.

## Open items

- No `[confirm: ...]` markers remain. CRS confirmed by Kevin as Courthouse Retrieval System, October 19, 2026.
- Default help center links (`/en/`) to flag at port: Customize Your Search View, Manage Listings Page Overview, Dashboard Overview, Add a Hot Sheet to the Dashboard, Messages Overview, Tags Overview.
- CRMLS: if CRMLS members also came from Paragon, this article could be shared; open question in project-status.
