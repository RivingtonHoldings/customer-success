# QA: Invite Clients to Perchwell and Resend Invitations

- **Article name:** Invite Clients to Perchwell and Resend Invitations
- **Old title:** Invite Clients to Perchwell
- **Intercom article ID:** 11373895, content ID 12304882
- **Mirror paths:** `docs/help-center/baldwin/invite-clients-to-perchwell.md` and `docs/help-center/crmls/invite-clients-to-perchwell.md` (shared article: Client Collaboration in Baldwin, Client Collaboration / Agents in CRMLS)
- **Old Notion row:** https://app.notion.com/1f18b9e0143880148fa4d4989136bd16 (Master Article List, read only, MLS All Regions, no video)
- **Notion draft:** https://app.notion.com/p/3f38b9e014388191b043fdcba6644b69
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-10-08-invite-clients-to-perchwell-rewrite.md`
- **Scored by:** Claude for Kevin, October 8, 2026, scorecard revision 2
- **Sources:** the live article body from Intercom `get_article` (matches the mirror), the live article's one screenshot (dated May 12, 2025), the Contacts Page Overview, Bulk Upload Contacts from a CSV File, and Message Clients in Perchwell Notion drafts, the live Accept Your Agent's Perchwell Invitation and Create and Manage Your Contacts articles, and Kevin's answers on the product (October 8, 2026)

## Revision, October 9, 2026

Rewritten against the content standard as of commit 489ed10, which added Tara's rules from Share Listings with Clients from Search and Message Clients in Perchwell. Score holds at 100.0 (14 of 14, plain language pass); every change below fixes something the new rules flag and that the October 8 scorecard did not check.

- **Second route to the same steps.** The resend section repeated the invite-from-profile steps with one different button. Merged into one section, "Invite a contact or resend an invitation from their profile", with the label difference inside step 2. The spam-folder tip and the Forgot Password route moved with it.
- **Leads name the page, not the route.** "Click Contacts in the top navigation" cut from all three `Steps:` blocks; each lead says "on the Contacts page" and step 1 starts on that page.
- **Outcome sentence states one result.** "Perchwell creates the contact and sends them an invitation email" became "The contact receives an invitation email." Bulk upload likewise.
- **Echo.** "workspace where an invited client collaborates with you in Perchwell" (Perchwell twice), "accepts the invitation from that inbox" after "each invitation", "invite them later ... invite each contact", and "messages ... in Messages" in the access list, all rephrased.
- **Link filler.** "To start a conversation ..., see [Message Clients]" became an article-subject sentence, and now points at the Share window's Invite this contact to Perchwell checkbox, a starting point that article owns (`docs/product-context.md`, Messages). "covers" became "explains how to" per the editorial read.
- **Description.** The Notion copy read "when you: add a contact, from a contact's profile ..."; the colon and the unparallel list were rewritten as "as you add or bulk upload contacts, or from a contact's profile, and resend an invitation a client cannot find" (139 characters).
- **Opening** reordered to match the merged sections: access, add a contact, profile (send or resend), bulk upload.

## Golden questions

| # | Factor | Old | New | Note |
|---|---|---|---|---|
| 1 | disambiguation | Pass | Pass | |
| 2 | visual_content_text | Fail | Pass | Old image had no alt text and sat under the wrong section. Every placeholder now carries alt text |
| 3 | undefined_terms | Fail | Pass | CSV now defined; client portal defined in the first section |
| 4 | structured_enumeration | Pass | Pass | |
| 5 | query_answer_symmetry | Fail | Pass | "Client invitation (existing contact)" and similar noun headings became task headings |
| 6 | self_contained_sections | Pass | Pass | |
| 7 | audience_specification | Pass | Pass | Silent; Roles is All Except Client |
| 8 | entity_distribution | Pass | Pass | |
| 9 | semantic_chunk_boundaries | Pass | Pass | |
| 10 | restate_questions | Pass | Pass | Old table had an intro sentence; the new draft has no table |
| 11 | overview_jtbd | Fail | Pass | Old article had no opening paragraph, and its description read "In this article, you will learn" |
| 12 | instruction_completeness | Fail | Pass | Old new-contact and bulk steps stopped at the last click |
| 13 | limitations_workarounds | Pass | Pass | |
| 14 | numerical_clarity | Pass | Pass | |

Old: 9 of 14. New: 14 of 14.

## Plain language gate

New: Pass. Nothing from the do-not list. "Status" and "Invite sent" are readouts the member reads in the contacts list, and they match the Contacts Page Overview draft. "client portal" is defined where it first appears.

## Dimension scores

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 17.1 (4/7) | 30.0 (7/7) | +12.9 |
| Chunk independence (25) | 16.7 (4/6) | 25.0 (6/6) | +8.3 |
| Answer completeness (25) | 10.7 (3/7) | 25.0 (7/7) | +14.3 |
| Fin-parsable formatting (10) | 6.3 (5/8) | 10.0 (8/8) | +3.7 |
| Accuracy and confidence (10) | 8.0 (4/5) | 10.0 (5/5) | +2.0 |
| **Total** | **58.8, Needs rewrite** | **100.0, Fin-ready** | **+41.2** |

Old failures: description over 140 characters and topic-led; no opening paragraph; bare-noun headings; H1 used for sections; the resend fact stated in three places; steps with no outcome; no defaults (locked fields, status change); CSV undefined; no links, and bulk upload re-explained; bold throughout; image without alt text; horizontal rules; "client-ready experience" and "secure workspace" as promotional framing.

The new score assumes the five `[confirm: ...]` items below are resolved as written. The band holds only once they are.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I invite my client to Perchwell? | Yes | Yes |
| My client never got the invite email. How do I resend it? | Partly. The button is named, but nothing on checking spam | Yes |
| Can I invite contacts when I bulk upload them? | Yes | Yes |
| Can my client see the listing agent's information? | Yes | Yes |
| Why can't I change my client's email address? | No | Yes |
| Can I add a personal message to the invitation? | Yes, but the answer is now wrong (the Create New Contact toggle has no message step) | Yes |
| Who does the invitation email come from? | Yes | Yes |
| My client accepted the invite but can't log in. What do they do? | No | Yes |

## Open items

- `[confirm: whether a saved invitation email template is added automatically when Invite to Perchwell is on]`. Create and Manage Your Contacts says a saved template shows above the toggle, but Kevin saw nothing appear.
- `[confirm: whether the message is optional, and whether Reinvite contact to Perchwell opens the same window as Invite contact to Perchwell]`. The October 9 merge depends on the second half; if Reinvite sends with no window, step 2's Reinvite case ends at the click and the section needs a sentence saying so.
- `[confirm: the exact label of the invitation toggle in the Upload Contacts window, and whether it appears before or after the import summary]`.
- **Conflict with a sibling draft.** Bulk Upload Contacts from a CSV File (Notion, Draft) says "The Upload Contacts window does not send invitations." Kevin confirmed there is an invitation toggle. One of the two drafts needs to change before either is ported.
- **Live screenshot is stale.** The May 2025 image shows Listing Presentations in the navigation and a Shared Buildings tab that the Contacts Page Overview draft does not list. It also shows a contact's name. It has been replaced with a placeholder, and the reshoot should use a test contact.
- **Shared article.** The same intercom_id is in both help centers. Following the September 17, 2026 rule, the row takes both MLS/AOR values, Baldwin and CRLMS All. Links point to the Baldwin help center.
- **Default help center links.** The Contacts Page Overview, Bulk Upload, and Message Clients drafts link to this article by ID, so the title change does not break them. Their link text still reads "Invite Clients to Perchwell", so update it when they are next edited.
- The old Master Article List row says MLS "All Regions", which does not map to the new database. Resolved by the shared-article rule above.
