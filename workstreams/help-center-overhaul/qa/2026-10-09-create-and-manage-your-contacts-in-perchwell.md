# QA: Create and Manage Your Contacts in Perchwell

- **Article:** Create and Manage Your Contacts in Perchwell (title kept by the teammate's choice; a task-led alternative, "Add, Edit, and Organize Contacts into Groups", was offered and declined)
- **Sources:** old Notion row https://app.notion.com/p/21d8b9e0143880819e77c6253810bb29; Intercom article 14790755, content 17388981; mirror `docs/help-center/baldwin/create-and-manage-your-contacts-in-perchwell.md`; Arcade `BafoJr1xmezMuPsnvDuC` step captions; teammate answers and three screenshots, October 9, 2026; set drafts Contacts Page Overview and Invite Clients to Perchwell and Resend Invitations (Notion)
- **Scored by:** Claude, for Kevin, October 9, 2026, using the scorecard check set revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Pass | Pass | Old had no images; new placeholders carry alt text |
| 3 undefined_terms | Pass | Pass | CSV defined |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | Old headings were bare nouns: "Contact creation", "Group organization" |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | No role gates the workflow |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | Old opened with "What a contact is" |
| 12 instruction_completeness | Fail | Pass | Add Group, rename, and delete now run to Save or Delete group, confirmed October 9 |
| 13 limitations_workarounds | Pass | Pass | Locked fields with the Support route; deleting a group keeps its contacts |
| 14 numerical_clarity | Pass | Pass | Five additional emails stated |

## Plain language gate

New: Pass. No term from the do-not list. "Create" and "add" both appear: Create is the window and button label on the Contacts page, and Add contact is the icon's hover label and the listing-share window's button.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 12.9 (3/7: description over 140 characters, no jobs-to-be-done opening, bare-noun headings, no heading echo) | 30.0 | +17.1 |
| Chunk independence (25) | 16.7 (4/6: H1 sections with H2 Steps, additional emails stated twice) | 25.0 | +8.3 |
| Answer completeness (25) | 14.3 (4/7: no outcomes after group and edit steps, deletion not stated as irreversible, invite and bulk upload not linked) | 25.0 | +10.7 |
| Fin-parsable formatting (10) | 3.8 (3/8: multi-action steps with stale labels, emoji callouts, bold throughout, horizontal rules) | 10.0 | +6.2 |
| Accuracy and confidence (10) | 6.0 (3/5: four stale labels, "Use the contact profile") | 10.0 | +4.0 |
| **Total** | **53.6, Needs rewrite** | **100.0, Fin-ready, both gates passed** | +46.4 |

## Fin test questions

| Question | Old, one section | New, one section |
|---|---|---|
| How do I add a new contact in Perchwell? | Yes | Yes |
| How do I create a new contact group? | Yes | Yes |
| If I delete a group, do I lose the contacts in it? | No | Yes |
| Can a contact be in more than one group? | No | Yes |
| How do I move a contact to a different group? | Partly | Yes |
| How do I delete a contact, and can I undo it? | Partly | Yes |
| Why can't I change my client's email address? | Yes | Yes |
| How do I add more email addresses to a contact? | Yes | Yes |

## Source differences and how they were settled

- Live and old Notion bodies match. The Notion row links a different Arcade (`yT6yJOFw…`) and a Loom, and its Help Center URL names article 8955819, not 14790755. All three videos are retired: the teammate says a new Loom is needed.
- Live labels that were wrong, settled by the teammate on October 9: Edit Grouping became the Edit groups people icon and window; Invite Contact to Perchwell became Invite to Perchwell; Edit Profile and Save Profile are Edit profile and Save profile.
- The Contacts page opens the Create New Contact window (Create button, Create Tag toggle). The Add Contact window (Company, Title, Group, Add contact button) opens from the listing-share flow. The live article merged the two windows.
- One group per contact, confirmed. This contradicts the live Contacts Page Overview mirror, which says "one or more groups".
- Delete contact is on the profile outside edit mode and asks for confirmation; the dialog says deletion is permanent and irreversible.

## Set findings for other drafts

- **Contacts Page Overview:** under scope A its Add a contact section now duplicates this article's steps. Cut it to one or two sentences and a link here. Its links to this article use the default `/en/` help center.
- **Invite Clients to Perchwell and Resend Invitations:** says a saved invitation template is added when Invite to Perchwell is on in the Create New Contact window. The teammate says the template appears only in the listing-share Add Contact window.
- **Contacts Page Overview:** its "Add a contact while sharing listings" route (Select a Tag, + Create New Tag, + New Contact) differs from the teammate's route (Listing Actions, then the text share option). Both may exist; confirm.

## Open items

- All five `[confirm: ...]` markers were resolved by the teammate on October 9: Create returns you to the Contacts page; the listing-share route ends at Add contact; Add Group opens a required Group name field with Discard and Save; a selected group shows Group name, Delete group, Discard, and Save; Delete contact sits at the bottom of the Contact Details tab.
- Not stated in the article, because no source covers it: whether Delete group asks for confirmation, and what happens to listings and Tags shared with a deleted contact.
- Screenshots still needed: the Create New Contact window and a profile in edit mode. Captured October 9 and saved in `outputs/drafts/images/`: Edit groups window, a group open for editing, Contact Details with Delete contact, Delete contact confirmation, listing-share Add Contact window. None show member data.
- New Loom needed.
- Link titles point at the draft titles of Invite Clients and Bulk Upload Contacts; check them at port.
