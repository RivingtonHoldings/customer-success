# QA: Create Brokerage Email Templates

- **Old title:** Create Communication Templates for your Brokerage
- **Sources:** live Intercom article 15653156 (content ID 18692554), mirror `docs/help-center/baldwin/create-communication-templates-for-your-brokerage.md`; Notion draft https://app.notion.com/p/3fb8b9e014388102bb4bf5388e80e5a5; the stored body from `get_article`; the article's three images; sibling live articles Add Branding to a Brokerage (14057465) and Create Communication Templates (14549167); product answers from Kevin, October 16, 2026. No old Notion page; the run started from the public URL.
- **Scored by:** Claude for Kevin, October 16, 2026. Scorecard revision 2.

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Fail | Pass | Old used 💡 and → as pointers |
| 2 visual_content_text | Fail | Pass | No alt text on any of three images; new image and placeholder carry alt text |
| 3 undefined_terms | Fail | Pass | Dynamic text and CMA now defined |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | "Email template creation", "Tips", "Email Signatures" replaced |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Fail | Pass | Brokers and MLS staff stated; agents cannot open My brokerage |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Fail | Pass | Old signature section mixed dynamic text with signatures |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | |
| 12 instruction_completeness | Fail | Pass | Delete outcome confirmed October 16, 2026 |
| 13 limitations_workarounds | Fail | Pass | One Reports template in use per report type |
| 14 numerical_clarity | Pass | Pass | |

## Plain language gate

Pass. No do-not-list term in the banned sense. "in use" in the Reports item is the screen's own wording, not the verb "use".

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 4.3 (1/7) | 30.0 (7/7) | +25.7 |
| Chunk independence (25) | 12.5 (3/6) | 25.0 (6/6) | +12.5 |
| Answer completeness (25) | 3.6 (1/7) | 25.0 (7/7) | +21.4 |
| Fin-parsable formatting (10) | 2.5 (2/8) | 10.0 (8/8) | +7.5 |
| Accuracy and confidence (10) | 2.0 (1/5) | 10.0 (5/5) | +8.0 |
| **Total** | **24.9, Not retrievable as written** | **100.0, Fin-ready** | **+75.1** |

Old failures, for the record: title collides with Create Communication Templates (14549167); description over 140 characters and opens "In this article"; H1s inside the body and `Steps:` at H2; wrong labels (Email Templates for Email copy templates, Edit Dynamic Text for Insert Dynamic Text); the claim that a brokerage template appears when inviting a client, which product says is wrong; Tips listed Invited Clients and Contact Agent types that are not on the page; bold throughout; horizontal rules; "Navigate to" and "you can".

## Fin test questions

| Question | Old, one section | New, one section |
|---|---|---|
| How do I create an email template for my whole brokerage? | Partly, wrong labels | Yes |
| Why can't I see My brokerage? | No | Yes |
| How do I add the agent's name to a brokerage template? | Partly, wrong button name | Yes |
| How many email templates can I have for reports? | No | Yes |
| Can my agents edit the brokerage templates? | No | Yes |
| Will the agent's signature show on brokerage template emails? | No | Yes |
| How do I delete a brokerage email template? | No | Yes |
| Where do agents find the brokerage templates? | No | Yes |

## Open items

- All four `[confirm: ...]` markers resolved by Kevin, October 16, 2026: {listing} inserts a link to the listing; Insert Dynamic Text adds the option at the cursor; Delete opens a confirmation window and removes the template from every agent's Settings; with Default on, the template fills in automatically for that type of email.
- Resolved October 16, 2026: agents cannot edit brokerage templates. A broker's edit in My brokerage does not reach agents, who keep the version already in their Settings; to change the wording agents get, the broker deletes the template and creates a new one. (An earlier answer the same day said edits applied brokerage-wide; Kevin corrected it.) The note below is kept for history. Product had said agents "pick and customize" brokerage templates in Settings and also have no access to brokerage templates. The draft reads this as: agents work with their copy in Settings and cannot open My brokerage. Confirm an agent's edits do not change the template for other agents.
- **Replace now:** the live article's first image (the profile menu with My brokerage) shows a named account and MLS ID while assuming identity. If that is a real agent, replace the image in Intercom now. The draft drops it.
- The live third image (Edit Template with the dynamic text list) is headed "Communication templates" in lowercase and shows Default toggles, which suggests it was taken in an agent's Settings, not My brokerage. The draft uses a screenshot placeholder instead.
- Label conflict with siblings: Add Branding to a Brokerage says Edit Templates, + Add Template, and Save Template; the agent article says Settings, Email Copy Templates. The June 11, 2026 screenshot and product answers support this draft. Both siblings need a follow-up, and Add Branding's template section should shrink to a sentence and a link here.
- The sample invitation message was cut, since My brokerage has no invite template type. It belongs in the agent article or Agent-to-Client Transition Email Templates.
- Title: the draft uses Create Brokerage Email Templates, the recommendation. The alternative was to keep the old title in title case. Teammate to confirm.
- Roles is Admin/Broker; the database has no MLS staff option, so MLS staff access lives in the body only.
