# QA: Export Contacts to a CSV File

Old title: Export Your Contact List

## Sources

- Old Notion page (Master Article List, read only): https://app.notion.com/p/2b28b9e014388036b6afeb4a491dc31e
- Intercom article ID 12896093, content ID 14593607
- Mirror: `docs/help-center/baldwin/export-your-contact-list.md` and `docs/help-center/crmls/export-your-contact-list.md` (shared article)
- New Notion draft: https://app.notion.com/p/3f48b9e01438815d890ce71b71457ba5
- Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-10-09-export-contacts-to-a-csv-file-rewrite.md`
- Live screenshot (Intercom CDN, captured about May 2026): the My Contacts tab with the export icon's hover tooltip. Settled the icon's shape and position and that the click downloads directly
- Product answers from the teammate, October 9, 2026: the export includes the contacts the member added to Perchwell, not the entire contact list; the CSV fields are First Name, Last Name, Email, Cell phone, Group, and Status; the mobile app cannot export contacts; the hover label is Export contacts, lowercase c
- Set read from the new database (Client Collaboration): Contacts Page Overview, Bulk Upload Contacts from a CSV File, Invite Clients to Perchwell and Resend Invitations, Message Clients in Perchwell; plus Export Listings to a CSV File (Search) for the export pattern

Scored by Claude with /article-rewrite on October 9, 2026, against the scorecard check set revision 2.

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Fail | Pass | Live image has no alt text; the draft's placeholder carries it |
| 3 undefined_terms | Fail | Pass | CSV and CRM defined on first use |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | "Export use cases", "CSV export", "Tips" replaced with task headings |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | No role gate; Roles property records All Except Client |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Fail | Pass | Delete-a-contact tip removed; it belongs to Create and Manage Your Contacts |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | "Use this article to" opening added |
| 12 instruction_completeness | Pass | Pass | |
| 13 limitations_workarounds | Fail | Pass | Browser-only stated where the member starts the export; scope of the file stated |
| 14 numerical_clarity | Pass | Pass | |

Old: 8 of 14. New: 14 of 14.

## Plain language gate

New: Pass. No term from the do-not list. "Cell phone" kept as the CSV field name. "Export contacts" appears as the icon's hover label at the point of use only.

## Scores

| Dimension | Weight | Old | New | Delta |
|---|---|---|---|---|
| Retrieval signals | 30 | 12.9 (3/7) | 30.0 (7/7) | +17.1 |
| Chunk independence | 25 | 12.5 (3/6) | 25.0 (6/6) | +12.5 |
| Answer completeness | 25 | 7.1 (2/7) | 25.0 (7/7) | +17.9 |
| Fin-parsable formatting | 10 | 5.0 (4/8) | 10.0 (8/8) | +5.0 |
| Accuracy and confidence | 10 | 8.0 (4/5) | 10.0 (5/5) | +2.0 |
| Total | 100 | 45.5 | 100.0 | +54.5 |

Old band: Not retrievable as written. New band: Fin-ready, gate passed, with one open `[confirm: ...]` marker.

Old failures: description in the "In this article, you will learn" form and under 120 characters; no opening paragraph; bare-noun headings at H1; the CSV export section has no lead sentence; the Tips list mixes in deleting a contact; the download location is stated twice; "all visible contacts" is vague and, per the teammate, inaccurate; mobile not covered; CSV undefined; UI labels bolded and the icon called "Export" rather than its hover label; image with no alt text; a horizontal rule.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I export my contacts? | Yes | Yes |
| Can I export my contacts from the Perchwell app on my phone? | No | Yes |
| What columns are in the contacts export? | No | Yes |
| Does the contact export include agents from my MLS? | No | Yes |
| Where did my exported contacts file go? | Yes | Yes |
| How do I get my Perchwell contacts into my CRM? | No | Partly: the use case is named; the steps sit in the next section |
| Why aren't all my contacts in the export? | No | Partly, until the confirm marker is resolved |

## Open items

- `[confirm: which contacts on the My Contacts tab the export leaves out, such as contacts carried over from a legacy platform]`. The teammate's answer says the export holds contacts the member added personally; which contacts that excludes is not yet named
- Replace the live article's screenshot now, not at port: it shows seven contact rows with names, emails, and phone numbers, including a personal Gmail address and two perchwell.com staff addresses
- The live screenshot's tooltip reads "Export Contacts"; the teammate confirmed the current label is "Export contacts", matching the Contacts Page Overview draft
- "such as your CRM" is an example added to the source's "another platform", matching the Bulk Upload sibling's CRM wording; cut it if the team prefers the source phrasing
- The export is two steps (open Contacts, click the icon). It is kept as a Steps block because this is the dedicated workflow article; the Contacts Page Overview carries the same action as one sentence
- Shared article: one row with both Baldwin and CRLMS All, per the September 17, 2026 rule; the teammate approved
- The Bulk Upload link points at the live article in the default help center (`/en/`); flag at transfer, and update the link text once that article is retitled Bulk Upload Contacts from a CSV File
- The Contacts Page Overview draft links this article as "Export Your Contact List"; update that link text when this title goes live
