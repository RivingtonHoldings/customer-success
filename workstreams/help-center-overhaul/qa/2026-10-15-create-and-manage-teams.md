# QA: Create and Manage Teams

- Article name: Create and Manage Teams
- Old title: Perchwell Teams
- Old Notion URL: https://app.notion.com/p/3098b9e014388087ab24d0caa113c050
- Intercom article ID: 14742099; content ID: 17314260
- Mirror path: `docs/help-center/baldwin/perchwell-teams.md` (Baldwin only, not shared with CRMLS)
- Notion: https://app.notion.com/p/3fa8b9e01438817c87d7c3775e190640
- Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-10-15-create-and-manage-teams-rewrite.md`
- Scored by Claude for Kevin, October 15, 2026, scorecard revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Pass | Pass | Live article has no images; draft placeholders carry alt text |
| 3 undefined_terms | Fail | Pass | "Feature flag" and "roster management system" removed; Assume Identity linked |
| 4 structured_enumeration | Fail | Pass | Search criteria were a numbered list though they are not steps |
| 5 query_answer_symmetry | Fail | Pass | "Visible Team Fields", "Access and Permissions", "Tips" replaced with task headings |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | Roles stated per section: brokers, brokerage admins, MLS staff |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Fail | Pass | Old "Creating and Managing Teams" mixed access rules and two procedures |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | "In this article, you will learn" replaced with "Use this article to" |
| 12 instruction_completeness | Fail | Pass | Every Steps block ends with its outcome |
| 13 limitations_workarounds | Fail | Pass | Same-brokerage limit stated where the member meets it; "logo not available at launch" cut |
| 14 numerical_clarity | Pass | Pass | |

Old: 7 of 14. New: 14 of 14.

## Plain language gate

Pass. No terms from the plain language do-not list. "Feature flag" and "roster management system" from the live article are gone.

## Dimension scores

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 8.6 (2 of 7) | 30.0 (7 of 7) | +21.4 |
| Chunk independence (25) | 12.5 (3 of 6) | 25.0 (6 of 6) | +12.5 |
| Answer completeness (25) | 7.1 (2 of 7) | 25.0 (7 of 7) | +17.9 |
| Fin-parsable formatting (10) | 3.8 (3 of 8) | 10.0 (8 of 8) | +6.2 |
| Accuracy and confidence (10) | 4.0 (2 of 5) | 10.0 (5 of 5) | +6.0 |
| Total | 36.0, Not retrievable as written | 100.0, Fin-ready | +64.0 |

Old failures: a bare-noun title; an "In this article" description; an H1 used as a section heading; bold UI labels; an emoji callout; horizontal rules; "allows you to" and "ideal for"; the staff-only rule stated three times; the add-after-save rule stated twice; Steps blocks with no outcome; a stale "at launch" line.

All `[confirm: ...]` markers were resolved by October 21, 2026. The Roles property is the remaining open item.

## Fin test questions

| Question | Old, one section | New, one section |
|---|---|---|
| How do I find a team in Perchwell? | Yes | Yes |
| Who can create a team? | No, split across three sections | Yes |
| How do I add an agent to my team? | Partly, with no outcome | Yes |
| Can I add agents from a different brokerage to my team? | No, only in Tips | Yes |
| What does being on a team let me do with listings? | Yes | Yes |
| Can my teammate log in as me? | Partly, no link to Assume Identity | Yes |
| Who do I contact to change my team? | Yes | Yes |

## Open items

- Resolved October 15, 2026: a team is assigned from the Listing team dropdown in the listing form, below Listing office 3.
- Resolved October 15, 2026: the team form's General section has Team name, Status, and Brokerage, all three marked required, plus Website, Description, Team type, Agents, and Team leader. Team leader is greyed out until something is set. The Contact section holds Email and phone fields, and the Address section holds address fields. The live article's "Team Name, Lead, Email, and Contact Info" was incomplete.
- Resolved October 21, 2026: agents can be selected from the Agents dropdown while a team is being created. The live article's claim that agents cannot be added during creation was wrong. The Create section lists Agents as an optional field, and the Add agents section is now titled Add agents to an existing team.
- Resolved October 21, 2026: Team type is a free-text field.
- Resolved October 21, 2026: Team leader unlocks after agents are selected and is chosen from the team's agents. It was added to the Create section's optional fields and as an optional step in Add agents and choose a Team leader for an existing team.
- Resolved October 15, 2026 from the teammate's screenshots: Teams is a tab, and the last of People, Offices, Brokerages, and Teams. The button reads Add new, in lowercase, and on the Teams tab it offers Team. The form's save button reads Save Team. Agents are added from an Agents dropdown with an unlabeled search field. The Teams list also has a Status column, which neither source mentioned, and labels the member count Members.
- October 21, 2026: the teammate confirmed that only MLS staff add and manage teams. The opening, the description, and the Create and Add agents leads now say so. Request a change moved up so the sections for brokers and admins come before the MLS-staff-only ones.
- October 21, 2026: the reviewer's Notion description was replaced because it ran over 140 characters and used "able to". The teammate then confirmed the intent behind it: brokers and brokerage admins view the teams in their own office but cannot edit them. The Find a team section now says so. This also settles the earlier question of whether agents see the Teams tab, since the view is tied to the Admin/Broker role.
- Resolved October 21, 2026: brokerage admins and MLS staff assign a team to a listing from the Listing team dropdown.
- Open: the Roles property is Admin/Broker. The database has no MLS staff option, so the team should decide whether that value still fits.
- The visual owner added real screenshots inside the three screenshot callouts in Notion on October 20, 2026. The placeholder text is still there and comes out at port.
- Team logos are unsupported (confirmed October 14, 2026). The line was cut as a bare deficit, since the live article never promised logos. Restore it if members are asking.
- The Assume Identity article lists the Baldwin MLS email as mls@baldwinreatls.com, which looks like a typo. This draft does not include the email. Flag it on that article.
- The old Notion row's Video and Screenshot statuses are "New Video" and "New Screenshots", with no URLs. The draft carries one video placeholder and three screenshot placeholders.
