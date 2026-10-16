# QA: Create and Edit a Tag

- **Article:** Create and Edit a Tag
- **Old title:** How to Create a Tag
- **Old Notion page:** https://app.notion.com/p/3b28b9e0143881afb7c7e8656f4c495e (Master Article List, read only)
- **Intercom:** article 16221240, content 19551948, collection Tags, Baldwin
- **Mirror:** `docs/help-center/baldwin/how-to-create-a-tag.md`
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-10-15-create-and-edit-a-tag-rewrite.md`
- **Scored by:** Claude for Tara, October 15, 2026, scorecard revision 2

## Golden questions

| # | Factor | Old | New | Note |
|---|---|---|---|---|
| 1 | disambiguation | Pass | Pass | |
| 2 | visual_content_text | Fail | Pass | Both live images had "image" as alt text; every placeholder now carries alt text |
| 3 | undefined_terms | Fail | Pass | Tag defined in the opening; "public Tags page" was undefined |
| 4 | structured_enumeration | Fail | Pass | Rename steps were prose; a Note was nested inside step 4 |
| 5 | query_answer_symmetry | Pass | Pass | |
| 6 | self_contained_sections | Pass | Pass | |
| 7 | audience_specification | Pass | Pass | No role gate; Roles records All Except Client |
| 8 | entity_distribution | Pass | Pass | |
| 9 | semantic_chunk_boundaries | Fail | Pass | Rename section also carried contact removal and deletion |
| 10 | restate_questions | Pass | Pass | No tables |
| 11 | overview_jtbd | Fail | Pass | Live article had no opening paragraph |
| 12 | instruction_completeness | Fail | Pass | No Steps block said what happens after the last step |
| 13 | limitations_workarounds | Pass | Pass | Contact removal now stated with the route (delete the Tag) |
| 14 | numerical_clarity | Pass | Pass | |

Old: 8 of 14. New: 14 of 14.

## Plain language gate

Pass. "Client Tag" is the Create New Contact window's own wording and appears once, where the member turns the toggle on. "My Tag" appears once, as the Status column value the member sees.

## Dimension scores

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 21.4 (5/7: description is the weak "you will learn" form at 113 characters, no opening) | 30.0 | +8.6 |
| Chunk independence (25) | 12.5 (3/6: mixed rename section, `## Steps:` at H2, contact removal stated twice) | 25.0 | +12.5 |
| Answer completeness (25) | 10.7 (3/7: no outcomes, no which-means, Tag undefined, no related links) | 25.0 | +14.3 |
| Fin-parsable formatting (10) | 5.0 (4/8: bold labels, terminal periods in steps, nested Note, no alt text) | 10.0 | +5.0 |
| Accuracy and confidence (10) | 8.0 (4/5: "you can always add a client") | 10.0 | +2.0 |
| **Total** | **57.6, Needs rewrite** | **100.0, Fin-ready** | **+42.4** |

The old score understates the problem: the live New Tag steps describe a window that no longer exists (Tag Name, a Contacts dropdown, Save). The scorecard has no check for a stale screen.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I create a tag? | Yes, with stale steps | Yes |
| How do I add a client to a tag? | Yes, with stale steps | Yes, with a link to How to Share a Tag |
| How do I remove a client from a tag? | Yes | Yes, from the Important callout; the heading no longer says "remove", so test this one first after port |
| How do I rename a tag? | Yes, in prose | Yes |
| How do I delete a tag? | Partly, inside a Note | Yes |
| How do I turn off tag notifications? | No | Yes |
| Why can't my client like or dislike listings on my tag? | No | Yes |
| Can I create a tag when I add a new contact? | No | Yes |

## Source differences and what won

- The live article and the old Notion page agree almost word for word, and both describe the New Tag window wrongly. Tara's October 15 screenshots won: the window is titled Create a new tag, has Name, Description, Reactions, Saved searches, Listings, and Tag notifications, and ends with Create. It has no Contacts field.
- The live article's August 19 images show an older Edit Tag window (Name (Public), Greeting Message, Add search results to Tag) and a two-icon Actions column. Superseded by the current Edit Tag screenshot. Neither image carried member names.
- Contacts can't be removed after saving (Tara, October 15). The x beside a contact in the Invited section of Share via Tag only appears before saving.
- Reaction icons need both the Reactions toggle on and at least one contact on the Tag (Tara).
- Tag notification emails go to the agent with the Tag's contacts copied (Tara).
- Deleting cannot be undone, and the public link returns a 404 afterward (Tara, Delete Tag screenshot).
- Legacy name: Listing Carts, for Baldwin and CRMLS (Tara; `new-terminology.md`).

## Open items

- Listings and notes, Edit: resolved by Tara, October 15. Notes for contacts, drag or up and down arrows to reorder, open the full listing, trash can removes the listing from the Tag. Still open: whether the box-with-arrow icon has a hover label, and whether notes attach to each listing or the whole Tag.
- Duplicate: resolved by Tara, October 16, 2026, from a Duplicate Tag screenshot. It copies listings and settings into a new Tag with a new public link; contacts and client reactions are not copied ("A new link will be created for this Tag. Client reactions are not copied."). A second window opens after Duplicate to add contacts. Now its own section, Duplicate a Tag.
- Duplicate a Tag, step 5: resolved October 16, 2026 from Tara's screenshot after clicking Duplicate. A "Tag duplicated." message appears and the copy is listed with My Tag in the Status column, so no contacts carry over; no contact window appeared, so step 5 was cut and the outcome points to sending the copy. In that screenshot the Duplicate Tag window was still open behind the message; worth checking whether it stays open or closes.
- Tags FAQ: when it is migrated, add "Can I remove a contact from a Tag?" answered "No. A contact cannot be removed from a Tag after you save it. To stop a contact from viewing the Tag, delete the Tag." Neither heading in this article says "remove", so the FAQ question heading is the strongest Fin match for that question.
- Duplicate-then-delete as a second route for removing a contact: Tara decided October 16, 2026 to leave it out. The callout names deleting the Tag only.
- The Duplicate Tag window spells the notification options Price increase, Price decrease, and Status change; the Create a new tag window capitalizes them. The article does not name them in the Duplicate section. Possible product inconsistency to report.
- Clear All Listings: resolved by Tara, October 16, 2026, from screenshots. A Clear all listings window warns it removes all listings, saved searches, and client reactions and cannot be undone; Clear All confirms, an "All listings have been cleared." message appears, and the Tag stays with 0 listings and its other settings. Now its own section, Clear all listings from a Tag.
- Duplicate and Clear All Listings each became their own H2 on October 16, 2026, as a reviewer suggested.
- Create New Tag in the Search Share window opens a different window than New Tag on the Tags page; Tara reports it as a bug. The draft says only where the option is.
- Tag notifications: Tara confirmed October 16, 2026 that adding a listing to a Tag also sends an email. The article now names that alongside the three change types.
- Video: the live Loom (0cc1fcba5b3b480f8d57e5b6eca525bf) and the old row's `videos.perchwell.com/#video=create-public-tag-page` both predate the current window. Replaced with a video placeholder.
- Scope (option A, inferred from Tara's answers): sending, inviting, the public page, and the Tags table were left to their own articles. Tara's screenshot notes for them, kept for those rewrites:
  - Tags table icons have hover labels: Copy public link, Open public link, Edit tag. Send and Resend have none.
  - Columns menu: every column checked by default; clicking one unchecks it and closes the menu.
  - Filters button offers Contacts, Status, and Name; the same three filter from their column headers.
  - Sorting: first header click ascending, second descending, third removes it; the number shows sort order; no limit on sorted columns.
  - Tags with contacts show the contact's initials in a circle; manually named Tags do not. Status reads My Tag for a Tag with no contacts.
- CRMLS: this draft serves both MLSs. The live CRMLS article Creating and Editing Tags (14324175, and its default help center copy 14324147) describes a different UI and should be retired or redirected when this one ports.
- Tracker ID: TRK-096, from the master sheet, set in Notion October 16, 2026.
- How to Tag Individual Listings and How to Link a Saved Search to a Tag still describe the old New Tag window (Tag Name, Contacts, Next, Alerts, Save); both need fixing in their own rewrites.
