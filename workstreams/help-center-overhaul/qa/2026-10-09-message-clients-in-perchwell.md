# QA: Message Clients in Perchwell

- **Article name:** Message Clients in Perchwell (title unchanged)
- **Notion draft:** https://app.notion.com/p/3f38b9e0143881f48642e7efb960e033 (reference copy: "(COPY)Message Clients in Perchwell")
- **Intercom article ID:** 12541968, content ID 14014573
- **Mirror paths:** `docs/help-center/baldwin/message-clients-in-perchwell.md`, `docs/help-center/crmls/message-clients-in-perchwell.md` (shared article)
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-10-08-message-clients-in-perchwell-rewrite.md`
- **Scored by:** Claude, against the Notion draft as of October 9, 2026, after Tara's October 8 to 9 review with current screenshots
- **Check set:** revision 2 (September 10, 2026)

## Golden questions

| # | Factor | Old | New | Note |
|---|---|---|---|---|
| 1 | disambiguation | Pass | Pass | |
| 2 | visual_content_text | Pass | Pass | Old had no images; new placeholders carry alt text |
| 3 | undefined_terms | Fail | Pass | Old: "client portal" undefined. New defines it, and the Preview starting point says how to open Preview |
| 4 | structured_enumeration | Pass | Pass | |
| 5 | query_answer_symmetry | Fail | Pass | Old "New message creation", "New message identification", "Tips" |
| 6 | self_contained_sections | Pass | Pass | |
| 7 | audience_specification | Pass | Pass | Invited-client requirement stated before the procedures |
| 8 | entity_distribution | Fail | Pass | Old "From Tags" section never named Messages |
| 9 | semantic_chunk_boundaries | Pass | Pass | |
| 10 | restate_questions | Pass | Pass | No tables |
| 11 | overview_jtbd | Pass | Pass | Old opening listed jobs under a "What Messaging lets you do" heading |
| 12 | instruction_completeness | Fail | Pass | Old Contacts, Listing Detail Page, Tags, filter, and notification steps had no outcome |
| 13 | limitations_workarounds | Fail | Pass | Old said "Message only invited clients" with no route; new links Invite Clients to Perchwell and states that uninvited contacts receive shared listings by email |
| 14 | numerical_clarity | Pass | Pass | New states the 1,000-character message limit |

## Plain language gate

Pass. No em dashes, no "you can", "allows you to", or "able to". The one "use" is the "Use this article to" opening, an accepted exception. No term from the plain language do-not list. Messages panel, Shared properties, Listing Actions, Share via Message, Send as in-app message, and Invite this contact to Perchwell are exact on-screen control labels.

## Dimension scores

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 12.9 (3/7) | 30.0 (7/7) | +17.1 |
| Chunk independence (25) | 8.3 (2/6) | 25.0 (6/6) | +16.7 |
| Answer completeness (25) | 10.7 (3/7) | 25.0 (7/7) | +14.3 |
| Fin-parsable formatting (10) | 7.5 (6/8) | 10.0 (8/8) | +2.5 |
| Accuracy and confidence (10) | 6.0 (3/5) | 10.0 (5/5) | +4.0 |
| **Total** | **45.4** | **100.0** | **+54.6** |

Old band: Not retrievable as written. New band: Fin-ready, both gates passed.

Old failures: description in "In this article" form at about 200 characters; no "Use this article to" opening; H1 section headings; bare-noun headings; From Tags never names Messages; invited-only stated twice; steps with no outcome; no related links; "client portal" undefined; bold UI labels; "Share via Messages" and the Listing Detail Page and Contacts steps do not match the screen; "Use Messages", "Use notifications", "Use the option".

New failures and fixes:

- **Fixed October 9, 2026: Preview.** The Preview starting point now opens with "Click a listing in your search results to preview it."
- **Fixed October 9, 2026: email replies.** Tara confirmed that a client's reply to the email appears in the Messages conversation and in the member's email inbox; Things to Know now says both.

Both fixed; the article scores 100.0.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I message my client in Perchwell? | Yes | Yes |
| Why can't I message my client? | Partly (no route to invite) | Yes |
| How do I send a listing to my client in Messages? | Partly (step labels wrong) | Yes |
| Can I share several listings in one message? | Yes | Yes |
| What happens if I share a listing with a contact I haven't invited? | No | Yes |
| How do I see which listings my client liked? | Partly (no outcome) | Yes |
| How do I know when my client messages me? | Yes | Yes |
| Can I delete a conversation? | Yes (in Tips) | Yes |
| Is there a character limit on messages? | No | Yes |

## Open items

- Port with Contacts Page Overview: Start a conversation links there for the Contacts page route, and the live Contacts Page Overview does not mention the chat icon yet.
- Shared article (Baldwin and CRMLS); links point at the Baldwin help center.
- Screenshot placeholders: three, owned by the Visual Owner. The Listing Detail Page shot from the old draft is gone; the remaining share placeholder shows the Actions menu above the search results.
- Arcade video is carried over from the live article and may show the older Listing Detail Page and Tags flows.
- Dropped from the live article: the From Tags procedure (sharing a Tag is covered by How to Share a Tag) and the tip "Messages stay linked to the listings you reference".
- UX note for the product team: Preview offers both Actions (shares every selected listing) and Listing Actions (shares only the previewed listing), and the full Listing Detail Page labels the same action Send as in-app message.
