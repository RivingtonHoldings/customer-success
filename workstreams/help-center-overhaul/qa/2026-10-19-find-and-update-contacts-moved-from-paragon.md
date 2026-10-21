# QA: Find and Update Contacts Moved from Paragon

- **Article:** Find and Update Contacts Moved from Paragon
- **Old title:** Your Data: Contacts from Paragon
- **Old Notion page:** https://app.notion.com/p/34a8b9e0143880a5a377dc2baf5574b1 (Master Article List, read only)
- **Intercom:** article 14726035, content 17293244, Baldwin help center, collection Then vs. Now
- **Mirror:** `docs/help-center/baldwin/your-data-contacts-from-paragon.md` (synced September 4, 2026); live body also read with `get_article` on October 19, 2026
- **New Notion page:** https://app.notion.com/p/3fe8b9e014388161b320f2bb02f9b7a8 (Draft; Tara asked in a page comment, October 19, 2026, to approve the Paragon title)
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-10-19-find-and-update-contacts-moved-from-paragon-rewrite.md`
- **Scored by:** Claude for Kevin, October 19, 2026, scorecard revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Fail | Pass | Old pointed at "the following message" with no image; that message does not exist (an email is required to add a contact) |
| 2 visual_content_text | Fail | Pass | Old referenced a missing image; new placeholder carries alt text |
| 3 undefined_terms | Pass | Pass | |
| 4 structured_enumeration | Fail | Pass | The four email workflows were prose; now a bullet list |
| 5 query_answer_symmetry | Fail | Pass | Old had one bold sentence as its only heading |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | Every member except invited clients; nothing gates it |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Fail | Pass | Old mixed migration timing, email rules, and invitations in one block |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | "You will learn how" replaced with "Use this article to" |
| 12 instruction_completeness | Fail | Pass | Old said to add an email with no steps; new has steps and an outcome |
| 13 limitations_workarounds | Fail | Pass | Old stated the exclusion with no route; new gives the steps to add an email |
| 14 numerical_clarity | Fail | Pass | "Approximately 20%" cut on Kevin's approval; it described Paragon before the move |

Old: 5 of 14 pass. New: 14 of 14.

## Plain language gate

Pass. No do-not-list terms. Old failed on "workflows", "data integrity", and "inputs", all cut.

## Dimensions

| Dimension | Weight | Old | New | Delta |
|---|---|---|---|---|
| Retrieval signals | 30 | 8.6 (2/7) | 25.7 (6/7) | +17.1 |
| Chunk independence | 25 | 8.3 (2/6) | 25.0 (6/6) | +16.7 |
| Answer completeness | 25 | 7.1 (2/7) | 25.0 (7/7) | +17.9 |
| Fin-parsable formatting | 10 | 3.8 (3/8) | 10.0 (8/8) | +6.2 |
| Accuracy and confidence | 10 | 2.0 (1/5) | 8.0 (4/5) | +6.0 |
| **Total** | 100 | 29.8, Not retrievable as written | 93.7, Fin-ready | +63.9 |

New failures, both from the title Kevin chose: Retrieval signals check 1 (the title names a legacy platform) and Accuracy and confidence check 4 (no legacy platform is named). These are a rule exception pending Tara's decision, not a drafting defect; see Open items. With a generic title the score would be 100.

## Fin test questions

| Question | Old, one section | New, one section |
|---|---|---|
| Where are my contacts from Paragon? | Partly (names the Contacts page in passing) | Yes |
| Why can't I pick a client when I share a listing by email? | Yes | Yes |
| How do I add an email to a contact that doesn't have one? | No | Yes |
| Did all my contact details come over from Paragon? | Yes | Yes |
| I edited a contact in Paragon after the switch, why isn't it updated? | Yes | Yes |
| Are my Paragon contacts already invited to Perchwell? | No | Yes |
| Can I change a client's email after I invite them? | Yes | Yes |

## Source differences and decisions

- The live article and the old Notion page carry the same text; the live one adds the email templates link.
- Both promised a screenshot of a message prompting for an email. Kevin confirmed no such message exists, since an email is required to add a contact; the sentence is cut.
- Live text said contacts without email are both "excluded" and "prompted". Kevin confirmed they are left out of the contact list when sharing a listing by email, sharing a saved search, sharing a report, or sending a message.
- Future tense ("will be migrated") rewritten as past; the cutover was August 3, 2026.
- Migrated contacts arrived uninvited, from the live Your Data: Perchwell Best Practices article, confirmed by Kevin.
- "Every field moved over" confirmed by Kevin.
- Left out on Kevin's instruction: incomplete migrations and the closed re-import path (Baldwin keeps these in Support conversations), and spouse contacts.
- The locked-fields rule is linked to Create and Manage Your Contacts in Perchwell rather than restated; that draft locks first name, last name, email, and phone, where the live article named email only.
- "Members may know their contacts from the Collaboration Center in Paragon" comes from the Baldwin new-terminology mapping (Collaboration Center / CollabLink to Contacts and Messages).

## Open items

- **Title names Paragon.** Kevin chose "Find and Update Contacts Moved from Paragon". CLAUDE.md and the content standard say articles never name a legacy platform; the Then vs. Now siblings write "a legacy platform". The article is Baldwin-only, which removes the rule's main reason, but the exception needs Tara's sign-off. Fallback: "Find and Update Contacts Moved from a Legacy Platform", with the body genericized to match.
- Link titles use the draft names "Invite Clients to Perchwell and Resend Invitations" and "Sample Emails to Tell Clients About Perchwell"; the live titles are still "Invite Clients to Perchwell" and "Agent-to-Client Transition Email Templates". Recheck at port.
- The live "Your Data: Perchwell Best Practices" (14725404) links to this article by its old URL and claims 100 percent contact completeness. Intercom keeps the URL, but that article needs its own rewrite.
- The Export Contacts to a CSV File draft has an open `[confirm:]` on whether contacts carried over from a legacy platform are in the export.
- Screenshot placeholder must use a test contact, with no real member or client names.
