# QA: Bulk Upload Contacts from a CSV File

Old title: Bulk Upload Contacts

## Sources

- Old Notion page (Master Article List, read only): https://app.notion.com/p/25a8b9e0143880fda464d362ec41cf56
- Intercom article ID 10732227, content ID 11478300
- Mirror: `docs/help-center/baldwin/bulk-upload-contacts.md` and `docs/help-center/crmls/bulk-upload-contacts.md` (shared article)
- New Notion draft: https://app.notion.com/p/3f38b9e0143881248962dad2da61891a
- Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-10-08-bulk-upload-contacts-from-a-csv-file-rewrite.md`
- Product answers from the teammate, October 8, 2026: no invite toggle in the Upload Contacts window, and the final button is Next; the import summary shows a count and error messages ("Email must be a valid email", "Email can't be blank", "Email already exists"); no apparent contact limit per file; the template's optional fields are Phone and Additional Email 1 to 5; Bulk upload is browser only; keep the Apple Pages tip. Current screenshot of the Upload Contacts window supplied.

Scored by Claude with /article-rewrite on October 8, 2026, against the scorecard check set revision 2.

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Pass | Pass | Live article has no images; the draft's two placeholders carry alt text |
| 3 undefined_terms | Fail | Pass | CSV and CRM now defined on first use |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | "CSV preparation", "Requirements and limits", "Tips" replaced with task headings |
| 6 self_contained_sections | Fail | Pass | Upload steps now name the Upload Contacts window |
| 7 audience_specification | Pass | Pass | No role gate; Roles property records All Except Client |
| 8 entity_distribution | Fail | Pass | Bulk upload or the Upload Contacts window named in every section |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | "Use this article to" opening added |
| 12 instruction_completeness | Pass | Pass | Every Steps block now ends with its outcome |
| 13 limitations_workarounds | Pass | Pass | Browser-only stated where the member opens Bulk upload |
| 14 numerical_clarity | Pass | Pass | "up to five additional emails" is exact |

Old: 9 of 14. New: 14 of 14.

## Plain language gate

New: Pass. Terms checked and kept: "import summary" (the screen the member reviews), "upload area" (the Browse or drag and drop area, named exactly in the step). "Must" appears only inside the on-screen error message "Email must be a valid email".

## Dimension scores

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 12.9 (3/7) | 30.0 (7/7) | +17.1 |
| Chunk independence (25) | 12.5 (3/6) | 25.0 (6/6) | +12.5 |
| Answer completeness (25) | 7.1 (2/7) | 25.0 (7/7) | +17.9 |
| Fin-parsable formatting (10) | 7.5 (6/8) | 10.0 (8/8) | +2.5 |
| Accuracy and confidence (10) | 4.0 (2/5) | 10.0 (5/5) | +6.0 |
| Total | 44.0 | 100.0 | +56.0 |

Old band: Not retrievable as written. New band: Fin-ready, gate passed, plain language passed, one `[confirm: ...]` marker open.

Old failures, for the record:

- Retrieval: description is 142 characters and uses the "In this article, you will learn" form; no opening paragraph; bare-noun headings; no heading echo.
- Chunk independence: sections fall back from the feature name; section headings are H1; First Name, Last Name, and Email Address listed in two sections.
- Answer completeness: the access and CSV preparation steps end without an outcome; the import summary is not explained; a "Requirements and limits" section instead of constraints where the member meets them; CSV and CRM undefined; no link to Invite Clients to Perchwell.
- Formatting: bold on every UI element; horizontal rules in the Intercom body.
- Accuracy: names Paragon; "Click Add Contact" and "Select Bulk Upload" no longer match the product; "use" as the verb in three places.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I upload a list of contacts at once? | Partial: access and upload are split across sections | Yes |
| Where do I get the CSV template for contacts? | Yes | Yes |
| What columns does the contact upload template need? | Yes, required fields only | Yes, required and optional fields |
| What does "Email already exists" mean when I upload contacts? | No | Yes |
| Can I bulk upload contacts from the mobile app? | No | Yes |
| Does bulk uploading contacts invite them to Perchwell? | No | Yes |
| How do I import my contacts from my CRM? | Partial: names the use case, no steps | Yes |
| My contact upload failed. What do I do? | Partial: one tip | Yes |

## Open items

- `[confirm: the exact name of this Apple Pages export option]`. The live tip says "Include header names". The team asked to keep the tip. The reviewer should confirm whether turning off header names conflicts with the rule to keep the template's column headers.
- Shared article: Intercom serves one record in both Baldwin (Client Collaboration) and CRMLS (Client Collaboration / Agents). The draft proposes MLS/AOR Baldwin and CRLMS All on one row, per the September 17, 2026 rule.
- Retitle: the Contacts Page Overview draft links this article as "Bulk Upload Contacts". Update that link text if the new title is approved, and set up the Intercom redirect for the old title.
- Sibling inaccuracy: the live Invite Clients to Perchwell article's "Client invitation (Bulk Upload)" section says to turn invitations on or off and click Upload. The teammate confirmed there is no invite toggle and the button is Next. Fix it when that article is migrated.
- Both screenshots need new captures. The old Notion images date from around April 2026 and show the retired Add Contact window name. The Upload Contacts screenshot the teammate supplied shows member emails in the background, so crop or blur them before it goes in the article.
- Position "lower left" for the Bulk upload button comes from the April 2026 image; confirm against the new capture.
