# QA: Manage Contacts in the Perchwell Mobile App

- **Old title:** Contacts Page Overview- Mobile
- **Sources:** live Intercom article 14785957 (content ID 17381257), mirror `docs/help-center/baldwin/contacts-page-overview-mobile.md`, the stored body via `get_article`, the article's four screenshots, and the teammate's answers on October 20, 2026. No old Master Article List row exists for this article. Not shared with CRMLS.
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-10-20-manage-contacts-in-the-perchwell-mobile-app-rewrite.md`
- **Scored by:** Claude for Kevin Liang, October 20, 2026, scorecard revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Fail | Pass | Old tip led with an emoji |
| 2 visual_content_text | Fail | Pass | Old images had empty alt text; new alt text written from the screenshots |
| 3 undefined_terms | Fail | Pass | Client portal and CC now defined |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | "Tips" and "Access Contacts" replaced with task headings carrying "mobile app" |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | Every member except invited clients; nothing stated, Roles property records it |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | |
| 12 instruction_completeness | Fail | Pass | Old steps had no outcomes and skipped the Add new contact tap. New: every procedure ends with its outcome, including the delete confirmation |
| 13 limitations_workarounds | Pass | Pass | Locked fields stated with the route to Perchwell Support; deletion stated as permanent |
| 14 numerical_clarity | Pass | Pass | Up to 5 additional addresses, matching the on-screen text |

## Plain language gate

Pass. No do-not-list terms. "Contact details" is the screen's title and is named after the tap that opens it.

## Dimension scores

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 8.6 (2/7) | 30.0 (7/7) | +21.4 |
| Chunk independence (25) | 12.5 (3/6) | 25.0 (6/6) | +12.5 |
| Answer completeness (25) | 10.7 (3/7) | 25.0 (7/7) | +14.3 |
| Fin-parsable formatting (10) | 2.5 (2/8) | 10.0 (8/8) | +7.5 |
| Accuracy and confidence (10) | 8.0 (4/5) | 10.0 (5/5) | +2.0 |
| **Total** | **42.3, Not retrievable as written** | **100.0, Fin-ready, both gates passed** | **+57.7** |

Old failures: a bare-noun title that collides with Contacts Page Overview; a 186-character description; no "Use this article to" opening; the Home-then-Contacts route repeated in four procedures; H4 headings and a bolded duplicate H1; no outcomes; no links; bold UI labels, an emoji callout, horizontal rules, empty alt text; "you can" and "Use" outside the exceptions.

## Fin test questions

| Question | Old, one section | New, one section |
|---|---|---|
| How do I add a contact on the Perchwell app? | Partly (missing the Add new contact tap) | Yes |
| How do I put a contact in a group on my phone? | Yes | Yes |
| How do I invite a client to Perchwell from the mobile app? | No (toggle only, at creation) | Yes |
| Why can't I change my client's email in the app? | Partly (tip, no route) | Yes |
| How do I find contacts in a group on my phone? | Partly (tip only) | Yes |
| How do I see what searches I shared with a client on mobile? | Yes | Yes |
| How do I delete a contact in the Perchwell app? | No | Yes |
| What does the Email button on a contact do? | No | Yes |

## Open items

- All three confirm markers resolved by the teammate on October 20, 2026: the magnifying glass searches by contact name and the two-arrow icon filters by group; Delete Contact opens a confirmation window and a deleted contact cannot be recovered; locked fields are changed through Perchwell Support.
- The teammate confirmed the locked fields are first name, last name, and email, so phone is not locked. The web Contacts Page Overview and Create and Manage Your Contacts drafts list phone as locked and need a check. `key-workflow-changes.md` says only the client can edit their email and phone, which also disagrees.
- The confirmation window's title and button labels after Delete Contact were not captured; the draft says "confirm in the window that opens".
- Teammate answered "yes" to the question covering both a Create Tag toggle and setting Grouping in the Add contact window; the draft reads it as yes to both.
- Whether the sort control's label changes from First Name to Last Name after switching was not asked.
- Images are from April 2026. The contact names and phone number in them are test data, confirmed by the teammate.
- Retitled from a page-style title. The old URL slug carries "contacts-page-overview-mobile"; Intercom keeps the article ID, so links resolve.
- Links point at the default help center (`/en/`); flag at port.
