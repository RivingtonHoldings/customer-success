# QA: Message Clients in the Perchwell Mobile App

- **Old title:** Messages Overview
- **Sources:** live Intercom article 14786130 (content ID 17381504), mirror `docs/help-center/baldwin/messages-overview.md`, confirmed unchanged against `get_article` on October 20, 2026. No old Master Article List page. The article's two live screenshots (April 2026; the teammate says the screens have not changed). Teammate product answers, October 20 and 21, 2026. Sibling drafts in Notion: Message Clients in Perchwell (TRK-011), Listing Detail Page in the Perchwell Mobile App (TRK-054), Manage Contacts in the Perchwell Mobile App (TRK-053).
- **Scored by:** Claude for Kevin Liang, October 21, 2026
- **Scorecard:** September 10, 2026 check set, revision 2
- **Article type:** Workflow (was an Overview by title). Sharing from Search and the Listing Detail Page merged into one section with one Steps block; the Tags route cut to one linking sentence.

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Fail | Pass | Old: two images with empty alt text. New: placeholders carry alt text written from the screenshots |
| 3 undefined_terms | Pass | Pass | |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | Old: "Share from Search", "Share from Tags" did not name Messages or clients |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | Invited clients only, stated with the route to invite |
| 8 entity_distribution | Fail | Pass | Old: Messages absent from the three share sections' headings and leads |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | Old opened by describing the feature, not the jobs |
| 12 instruction_completeness | Fail | Pass | Old: no outcome after any Steps block |
| 13 limitations_workarounds | Fail | Pass | Old: invited-only stated with no route forward. New: invite link and Share externally |
| 14 numerical_clarity | Pass | Pass | 1,000-character message limit added |

Old: 8 of 14. New: 14 of 14.

## Plain language gate

Pass. No term from the do-not list. "Undecided", "Liked", and "Rejected" are the group headings on screen and words an agent would say.

## Dimension scores

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 8.6 (2/7) | 30.0 (7/7) | +21.4 |
| Chunk independence (25) | 12.5 (3/6) | 25.0 (6/6) | +12.5 |
| Answer completeness (25) | 10.7 (3/7) | 25.0 (7/7) | +14.3 |
| Fin-parsable formatting (10) | 6.3 (5/8) | 10.0 (8/8) | +3.7 |
| Accuracy and confidence (10) | 6.0 (3/5) | 10.0 (5/5) | +4.0 |
| **Total** | **44.0** | **100.0** | **+56.0** |

Old band: Not retrievable as written. New band: Fin-ready, both gates passed, no `[confirm: ...]` markers left.

Old failures, for the record: bare-noun title with no surface; description opens "In this article" and does not name Messages; no "Use this article to" opening; H1s for sections; push notifications stated twice; bold on every UI label; horizontal rules; empty alt text; "You can send"; "quickly gauge", "never miss", "stay on top of every conversation"; and labels that no longer match the product (Actions and Send via Messages on Search, the Share icon on the Listing Detail Page).

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I send a listing to my client from the Perchwell app? | Yes, with outdated labels | Yes |
| Why is my client grayed out when I try to send listings on my phone? | No | Yes |
| How do I start a new message in the Perchwell app? | No | Yes |
| How do I see which listings my client liked on mobile? | No; one bullet says reactions exist | Yes |
| Is there a character limit on messages in the app? | No | Yes |
| How do I share a listing with someone who isn't invited? | No | Yes |
| How do I turn on push notifications for messages? | No, and implied they exist | Yes: they are not available |

## Open items

- **Replace now, not at port:** both live screenshots show a contact's full name in the conversation header and another person's name beside a message. The teammate asked for the reshoot to come from a test account; every placeholder says so. Replace the published images in Intercom now if the names are real people.
- **Bare-deficit exception, a deliberate choice:** the live article promised push notifications for new messages. The teammate confirmed October 21, 2026 that they are not available (the profile toggles are Daily Sales Market Pulse and Daily Rental Market Pulse, which are market reports). The rewrite states the absence once, as a yes-or-no question, because Fin learned the wrong answer from the live article.
- Resolved October 21, 2026: the browser draft Message Clients in Perchwell (TRK-011) said the mobile app sends push notifications. The bullet was replaced in Notion and the repo copy with a sentence saying they are not available, linking this article by its new title.
- Resolved October 21, 2026: the message sends with the paper-plane icon, which has no label. All three markers are resolved.
- Resolved October 21, 2026: mobile Shared listings has a Maybe group. The live screenshot showed none because that conversation had no Maybe reactions. The order Liked, Maybe, Rejected, Undecided is assumed from the screenshot's order with Maybe after Liked; check it in the reshoot. "Undecided: not reacted to" follows the browser draft's definition.
- Whether there is a Share step between choosing the contact and the message, as in the browser, is unconfirmed; the teammate's answer described picking a contact and then sending.
- Tags route: the live article documented sharing from a Tag with checkboxes and Actions. Search now uses the three-dots icon instead of Actions; confirm Tag listings work the same way before anyone writes those steps back in.
- Not carried, as sibling inferences from the browser draft: conversations cannot be deleted, the no-reply email to the client, and email replies landing in Messages. Likely the same on mobile; confirm before adding.
- Uninvited contacts are confirmed grayed out when sharing listings. Whether the New conversation picker does the same is unconfirmed, so the draft states it for sharing only.
- Link text uses the new title "Manage Contacts in the Perchwell Mobile App" with the live URL of Contacts Page Overview- Mobile (14785957), which that draft replaces. Update the link text if that title changes.
- The live article also sits in Intercom collection 19637741, as the other mobile articles do. Check where it lives before porting.
- Title overlap with the browser article Message Clients in Perchwell. Each names its own surface and the two link to each other through Manage Contacts and the browser article's push notification bullet, which links this article by its old title; update that link text at port.
