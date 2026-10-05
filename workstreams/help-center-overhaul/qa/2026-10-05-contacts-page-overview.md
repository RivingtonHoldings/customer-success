# QA: Contacts Page Overview

Article name: Contacts Page Overview (title unchanged)
Scored by: Claude, for Tara, 2026-10-05
Scorecard set: September 10, 2026, revision 2

## Sources

- New Notion draft: https://app.notion.com/p/3f08b9e0143881a88e56c522774b0833 (created 2026-10-05)
- Old Notion page: https://app.notion.com/p/2f08b9e014388089b318c1eacd7ac10b (Master Article List, read only, left unchanged)
- Intercom article ID: 13975194, content ID: 16256222
- Mirror: `docs/help-center/baldwin/contacts-page-overview.md`. Live stored body read with `get_article` on 2026-10-02; unchanged since July 28, 2026
- Three current product screenshots supplied by Tara, 2026-10-02: the My Contacts tab, the Create New Contact modal, and the My MLS tab
- Tara's answers to 13 product questions, 2026-10-05, and a second round the same day with three more screenshots: the contact profile (Contact Details tab and its full field list) and the Create Tag Learn more modal

## Scope decision

Tara chose orientation only (option A, 2026-10-05). Contact creation, Bulk Upload, invitations, group management, and export are handed to the articles that already own them. The My MLS roster, the list columns, the toolbar icons, and the Create New Contact modal's options have no other home and are documented here in full.

| Live section | Now owned by |
|---|---|
| Contact creation steps | Create and Manage Your Contacts in Perchwell |
| Import contacts with Bulk Upload | Bulk Upload Contacts |
| Invite to Perchwell | Invite Clients to Perchwell |
| Group assignment steps | Create and Manage Your Contacts in Perchwell |
| Export | Export Your Contact List |
| Find your agent roster | This article |

## Golden questions

| # | Factor | Old | New | Note |
|---|---|---|---|---|
| 1 | disambiguation | Fail | Pass | Old said "You can find the list ... here" and used emoji callouts. New names each icon by its hover label and position |
| 2 | visual_content_text | Fail | Pass | Old had two images with no alt text after trailing colons. New has three placeholders carrying alt text |
| 3 | undefined_terms | Fail | Pass | CSV and Client Tag defined on first use; "client portal" dropped |
| 4 | structured_enumeration | Fail | Pass | Old numbered a list of options and bulleted the Bulk Upload steps. New uses labeled bullets for every set |
| 5 | query_answer_symmetry | Fail | Pass | Old headings were bare nouns ("Contact creation", "Group assignment") |
| 6 | self_contained_sections | Pass | Pass | |
| 7 | audience_specification | Pass | Pass | New states the one gate: invited clients do not see My MLS |
| 8 | entity_distribution | Pass | Pass | |
| 9 | semantic_chunk_boundaries | Fail | Pass | Old nested the agent roster under shared activity and put sections at H1 |
| 10 | restate_questions | Pass | Pass | No tables in either |
| 11 | overview_jtbd | Fail | Pass | Old opened on a topic ("your hub") and its description read "In this article, you will learn" |
| 12 | instruction_completeness | Fail | Pass | Old stopped at "Click Add Contact" and "Click Save Profile". New's two Steps blocks end with what opens and what the roster shows |
| 13 | limitations_workarounds | Fail | Pass | Old said the email cannot be updated with no route forward. New names all four locked fields and the route (Support), the name-only roster search, and that My MLS does not export |
| 14 | numerical_clarity | Pass | Pass | Five additional emails, confirmed |

Old: 5 of 14. New: 14 of 14, gate passed.

## Plain language gate

**Pass.** No term from the do-not list in the sense it bans. "Modal" was retired October 1, 2026, after this draft was first written; the three uses were changed to "the Create New Contact window", the name on screen, before the first commit. "Look up" appears only as a verb. "Roster" and "agent roster" are the words a member types, and the live article's own heading used them. Icon labels (Add contact, Export contacts, Edit groups, Filters) are hover labels on controls and are named once each, where the member reaches for them.

## Dimensions

| Dimension | Weight | Old | New | Delta |
|---|---|---|---|---|
| Retrieval signals | 30 | 8.6 (2/7) | 30.0 (7/7) | +21.4 |
| Chunk independence | 25 | 12.5 (3/6) | 25.0 (6/6) | +12.5 |
| Answer completeness | 25 | 7.1 (2/7) | 25.0 (7/7) | +17.9 |
| Fin-parsable formatting | 10 | 2.5 (2/8) | 10.0 (8/8) | +7.5 |
| Accuracy and confidence | 10 | 8.0 (4/5) | 10.0 (5/5) | +2.0 |
| **Total** | **100** | **38.7** | **100.0** | **+61.3** |

Old band: Not retrievable as written. New band: Fin-ready, gate passed, no open markers.

Retrieval signals check 1 passes with a note: "Contacts Page Overview- Mobile" (14785957) is a near-identical title in the same help center. It names its own surface, so it is scored as a pass, but retitling it "Contacts Page Overview (Mobile)" when it is next touched would make the split cleaner.

## Fin test questions

| Question a member may type | Old answers from one section | New answers from one section |
|---|---|---|
| How do I find another agent's phone number? | Partial. "Search for an agent to find their details" | Yes, "Find an MLS member on the My MLS tab" |
| What does Invite sent mean on my contacts? | No | Yes, "What the Group, Last Shared, and Status columns show" |
| Can I export the agent roster? | No | Yes, "Export your contact list" |
| Why can't I change my client's email address? | Partial. Tip says it cannot change, with no fix | Yes, Important callout in "Add a contact" |
| What does Create Tag do when I add a contact? | No | Yes, same section |
| How do I see only my Actively Searching contacts? | Partial. "Use Filters" with no location | Yes, "Find, sort, and filter contacts" |
| Can my clients see the MLS roster? | No | Yes, "Open the Contacts page" |
| How do I stop other agents from seeing my client's saved searches? | No | Yes, "Message a contact or view their profile" |

## Open items

**No `[confirm: ...]` markers remain. Every fact in the draft is sourced.**

**Tara's review, 2026-10-05.** Tara rewrote the description, opening, and nine sections for directness and scannability, and her version is what stands. Claude's pre-review version is kept for comparison at `outputs/drafts/2026-10-05-contacts-page-overview-rewrite-v1-claude.md`, and the merged, reviewed version at `outputs/drafts/2026-10-05-contacts-page-overview-rewrite-v2-reviewed.md`. The Message Clients in Perchwell link, dropped in review, was added back at the end of the messaging section. Five standard fixes were applied on merge and agreed: the description extended from 79 to 138 characters; the Important callout on locked fields kept; CSV expanded on first use; link phrasing varied; and the add and rename options in Edit groups confirmed against a new screenshot of the Edit groups modal, which also shows reorder and delete. Three counter-proposals were agreed: the column section heading names the three columns rather than "contact details", which is also the name of a profile tab; the My MLS heading names the tab and its lead introduces "roster", which the section already used; and the Filters icon is named by shape like the other three. The Notion page was replaced with the merged version the same day. Rescored: 100.0, gate passed.

**Resolved 2026-10-05, second and third rounds**

- Adding a contact while sharing: select listings, Actions, Share, the Select a Tag dropdown, + Create New Tag, then + New Contact, which opens the regular Create New Contact modal. Added as a Steps block in the Add section. The draft does not name the share dialog or the client Tag modal, since neither title was confirmed.

- Group assignment: the group field was removed from the Create New Contact modal. A group is set after the contact is saved, from the profile's Edit profile, under Grouping. The draft says so where the member meets it (the Add section) and gives the path once (the groups section).
- The profile button reads Edit profile, lowercase p. Corrected from the live article's Edit Profile.
- The profile has four tabs on the left: Contact Details, Shared Listings, Shared Searches, Shared Reports. Added as a labeled list, with a placeholder for a profile screenshot.
- The profile carries a Reverse Prospecting toggle. Added from its on-screen text, with a link to the Reverse Prospecting article. Its default state is not stated, because one screenshot does not establish it.
- The Create Tag Learn more link opens a "What is a Tag?" modal. The Client Tag definition in the draft now follows that modal's wording.
- The Search my MLS result behavior, previously inferred, is confirmed.

**Decisions taken**

- Roles: the old row had none. Set to All Except Client, since invited clients do not see My MLS (Tara, answer 11).
- Video: the Arcade link is kept under the opening paragraph, and the video needs re-recording for the new workflow and UI (Tara, answer 12). `Media Update Needed: Yes`.
- Four screenshot placeholders. Tara's working screenshots carry real names, emails, and phone numbers and are not article assets.

**Corrections this rewrite found that outlive it**

The sibling articles this one now links to are stale against the October screenshots:

- Create and Manage Your Contacts in Perchwell says Add Contact, Edit Grouping, and Invite Contact to Perchwell, lists a group field in the modal, and lists four default groups that may not match.
- Bulk Upload Contacts names Paragon, and reaches Bulk Upload through Add Contact rather than the button on the modal.
- Invite Clients to Perchwell says Add Contact for the new-contact path.
- Contacts Page Overview- Mobile repeats the live web article's opening and is a near-identical title.
- Five links in the draft point into the default help center (`/en/`): Bulk Upload Contacts, Invite Clients to Perchwell, Create and Manage Your Contacts in Perchwell, Export Your Contact List, and Message Clients in Perchwell. Confirm at transfer that they resolve for Baldwin members.
- The old Notion page's open comment, asking whether additional emails are CC'd or BCC'd, is answered by the modal: notifications go to them in the same thread.
