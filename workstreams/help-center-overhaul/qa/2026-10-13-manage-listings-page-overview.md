# QA: Manage Listings Page Overview

- **Article name:** Manage Listings Page Overview (title unchanged)
- **Sources:** old Notion page https://app.notion.com/p/30c8b9e0143880058446f3e0fa0f2a53; Intercom article 13623016, content 15694685; mirror `docs/help-center/baldwin/manage-listings-page-overview.md`; teammate screenshots of the Manage Listings page and the Open Houses window, October 13, 2026 (kept in `confidential/`); live article screenshots of the Search filters panel, August 10, 2026
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-10-13-manage-listings-page-overview-rewrite.md`; Notion page https://app.notion.com/p/3f88b9e014388104a17fe50f01c193c8
- **Scored by:** Claude (/article-rewrite), October 13, 2026, for Kevin Liang
- **Scorecard:** September 10, 2026 set, revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1. disambiguation | Fail | Pass | Old used a 📖 emoji pointer |
| 2. visual_content_text | Fail | Pass | Both live images now carry alt text; placeholders carry alt text |
| 3. undefined_terms | Pass | Pass | |
| 4. structured_enumeration | Fail | Pass | Old wrote add and edit steps as nested bullets |
| 5. query_answer_symmetry | Fail | Pass | "Listing filters", "Open house scheduling", and "Tips" replaced with task-led headings |
| 6. self_contained_sections | Pass | Pass | |
| 7. audience_specification | Pass | Pass | New states the role gate and what admins and agents see, from the teammate's answer |
| 8. entity_distribution | Fail | Pass | Manage Listings now in every heading |
| 9. semantic_chunk_boundaries | Pass | Pass | |
| 10. restate_questions | Pass | Pass | No tables |
| 11. overview_jtbd | Fail | Pass | Old had no opening paragraph |
| 12. instruction_completeness | Fail | Pass | Open house steps now end with where the open house appears |
| 13. limitations_workarounds | Pass | Pass | Expired listings cannot be duplicated; required open house fields |
| 14. numerical_clarity | Pass | Pass | |

Old: 7 of 14 pass. New: 14 of 14 pass.

## Plain language gate

Pass. No term from the do-not list in a banned sense. "Search filters panel" is the panel's on-screen title and is named only after the Filters click that opens it.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 12.9 (3/7) | 30.0 (7/7) | +17.1 |
| Chunk independence (25) | 16.7 (4/6) | 25.0 (6/6) | +8.3 |
| Answer completeness (25) | 17.9 (5/7) | 25.0 (7/7) | +7.1 |
| Fin-parsable formatting (10) | 2.5 (2/8) | 10.0 (8/8) | +7.5 |
| Accuracy and confidence (10) | 8.0 (4/5) | 10.0 (5/5) | +2.0 |
| **Total** | **58.0, Needs rewrite** | **100.0, Fin-ready** | **+42.0** |

Old failures: description 155 characters and in "In this article" form; no opening; bare-noun headings; heading echo missing in filters; feature name missing from the filters section; H1 used for sections; no outcome after open house steps; default statuses not stated; emoji callouts; bold throughout; horizontal rules; images without alt text; "You can use". All eight `[confirm: ...]` markers were resolved October 13, 2026.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| Where do I find my draft listings? | Yes | Yes |
| How do I add an open house to my listing? | Yes | Yes |
| How do I delete an open house? | No | Yes |
| Can clients see my open house remarks? | Yes | Yes |
| Why don't my closed listings show in Manage Listings? | No | Yes |
| Why can't I see other agents' listings in Manage Listings? | No | Yes |
| How do I duplicate a listing? | No | Yes |
| Where is Manage Listings? | Yes | Yes |

## Open items

- Resolved October 13, 2026, by Kevin: the list sorts by column heading and starts sorted by Updated; Export exports the selected listings; Public is the default open house type; an open house is changed by deleting and re-adding it; Visibility offers Public, suspended, and Public & suspended (lowercase on screen), with Public & suspended as the default; Media narrows to listings with that media; the date filters take a start and end date; Reset filters returns every filter to its default. No `[confirm: ...]` markers remain.
- Ask: the export file format, if the team wants it named.
- Set: the live Listing Maintenance FAQ says open house remarks can be edited or cleared from the calendar icon; the Open Houses window only deletes and re-adds, confirmed October 13, 2026. Fix when the FAQ is migrated.
- Ask: do the pencil and trash can icons have hover labels? The calendar icon has none, confirmed October 13, 2026.
- Ask: what brokers who are not brokerage admins see in the list; the teammate's answer covered brokerage admins and agents.
- Ask: what the dark square icon to the left of the calendar and pencil icons in each row does. The article does not mention it.
- Video: no video exists; a video placeholder is in the draft.
- Media: the August 10, 2026 Search filters screenshot cuts off at Next open house and does not show Expiration Date or Showing start date. Recapture it with the full filter list. The page and Open Houses screenshots need a test account or crops: the teammate's captures show listing agent names and a remark naming a person.
- Link: the live article's Add and Edit link points to the default help center (`intercom.help/perchwell-help-center-baldwin/...`); the draft uses `support.perchwell.com/baldwin/en/...`. `/port-to-intercom` checks the stored links.
- Set: the Add and Edit Listings draft says "as a broker or an agent with full access" and carries the Maintain Listings legacy sentence. This draft uses "with permission to manage listings", from the teammate's answer, and holds the legacy sentence as the Overview. Align the two.
- Set: the live Listing Detail Page Overview names open house types Public or Agent Only; the Open Houses window offers Public, Broker Only, and By Appointment.
