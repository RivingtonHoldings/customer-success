# QA: Message Clients in Perchwell

Title kept. Scored October 8, 2026 by Claude for Kevin, against scorecard revision 2.

## Sources

- Old Notion page: https://app.notion.com/p/1f18b9e014388016ab52c55e083945d7 (Master Article List, read only). MLS: All Regions. Roles: empty. Text, Screenshot, and Video all marked Update Required
- Intercom article ID 12541968, content ID 14014573, last updated July 2, 2026
- Mirror: `docs/help-center/baldwin/message-clients-in-perchwell.md` and `docs/help-center/crmls/message-clients-in-perchwell.md` (shared article, same body; Client Collaboration in Baldwin, Client Collaboration / Agents in CRMLS)
- Live article images: none. The only media is the Arcade walkthrough
- Kevin's screenshot, October 8, 2026: the Actions menu on a Listing Detail Page, showing Contact agent, Share, Send as in-app message, and Share via Text under Share
- Kevin's answers, October 8, 2026: the Search Actions menu item is Share via Message; the Contacts icon is a chat bubble with the hover label Chat in Messages; Listing Detail Page sharing is now Send as in-app message in the Actions menu; the Tags page was redesigned, and a listing opened from a Tag must be opened in a new tab or with View within Perchwell before it can be sent; the Messages page flow (hover over Contacts, pencil icon) is current; Shared Properties, its filters, Undecided meaning no reaction yet, and clicking a listing to open its thread are all current; replies to the client email go to the Messages conversation; the chat icon is not greyed out for uninvited contacts; conversations still cannot be deleted
- Kevin's second round, October 8, 2026: uninvited contacts cannot be messaged (correcting the first answer); Send as in-app message opens the same fields as Share via Message on Search; a screenshot of the Share window message step, with a back arrow, the required Include a message field, a 1,000-character counter, and Send; the June comment left unresolved; the Arcade video left as is; the Contacts Page Overview draft not to be edited
- Notion comments on the old page: one open comment, June 22, 2026, "Reposition this article as the Message Page Overview". Two resolved inline comments on the invite sentence and the Send in Messages button
- Sibling articles checked: Invite Clients to Perchwell, Messages Overview (Mobile), Share Multiple Listings in Perchwell, Multi-Listing Actions on the Search Page, How to Share a Tag, Listing Detail Page Overview, and the drafts Contacts Page Overview, Search Page Overview, and Share Listings with Clients from Search
- Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-10-08-message-clients-in-perchwell-rewrite.md`
- Notion draft: https://app.notion.com/p/3f38b9e0143881f48642e7efb960e033

## Source differences and how they were settled

| Topic | Live | Old Notion | Settled by |
|---|---|---|---|
| Search Actions menu item | Share via Messages | Share via Messages | Kevin, and the Search Page Overview screenshots: Share via Message |
| Contacts page icon | message icon | message icon | Kevin: Chat in Messages chat bubble icon |
| Listing Detail Page | Share, Send in Messages button, Share | Same | Kevin's screenshot: Actions, then Send as in-app message |
| Tags | Select listings, footer action bar Share | Same | Kevin: Tags page redesigned; open the listing with View within Perchwell or in a new tab, then send it from the Listing Detail Page |
| Click a listing in Shared Properties | Not stated | Callout: opens the related message thread | Kevin: confirmed, carried |
| Email sender | no-reply@perchwell.com, replies directed to you | Not stated | Carried; Kevin: replies go to the Messages conversation |
| "Messages stay linked to the listings you reference" | Tip | Tip | Sharpened into Shared Properties; cut as a separate tip |
| "Messaging looks similar for clients in their client portal" | Tip | Tip | Sharpened, with client portal defined from Invite Clients to Perchwell |
| Scope | Workflow | Workflow, with a June comment asking for a Messages page Overview | Kept as a workflow under the current title; see Open items |

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Fail | Pass | Old: "the pencil icon", "the message icon", "the contact" with no surface named in the Tags steps |
| 2 visual_content_text | Pass | Pass | Old had no images; new placeholders carry alt text |
| 3 undefined_terms | Fail | Pass | Client portal and Shared Properties were undefined |
| 4 structured_enumeration | Pass | Pass | Filters and alert types are labeled lists |
| 5 query_answer_symmetry | Fail | Pass | Old headings: "From Contacts", "From Tags", "New message identification", "Tips" |
| 6 self_contained_sections | Fail | Pass | Old Tags and Contacts sections never named Messages |
| 7 audience_specification | Pass | Pass | Invited clients only, stated before the steps. Roles property: All Except Client |
| 8 entity_distribution | Fail | Pass | Messages named in every section |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | Old opened with "What Messaging lets you do" |
| 12 instruction_completeness | Fail | Pass | Every Steps block ends with its outcome |
| 13 limitations_workarounds | Fail | Pass | Invite requirement now carries the route: invite, or share by email, text, or public link |
| 14 numerical_clarity | Pass | Pass | |

## Plain language gate

Pass. No term from the do-not list. "in-app" appears only inside the on-screen label Send as in-app message.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 12.9 (3/7: description 190 characters and opens "In this article"; no opening paragraph; bare headings; no heading echo) | 30.0 | +17.1 |
| Chunk independence (25) | 12.5 (3/6: Tags section never names Messages; sections at H1; "only invited clients" and "conversations appear in Messages" each stated twice) | 25.0 | +12.5 |
| Answer completeness (25) | 7.1 (2/7: no Steps block ends with its outcome; Undecided and Shared Properties unexplained; invite requirement with no route; client portal undefined; no related links) | 25.0 | +17.9 |
| Fin-parsable formatting (10) | 6.25 (5/8: bold labels and a stray `****`, terminal periods in the filter steps, horizontal rules) | 10.0 | +3.75 |
| Accuracy and confidence (10) | 8.0 (4/5: "Use Messages", "Use notifications", "Use the option") | 10.0 | +2.0 |
| **Total** | **46.7** | **100.0** | **+53.3** |

Old band: Not retrievable as written. New band: Fin-ready, gate passed, no open markers.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I message my client in Perchwell? | Yes | Yes |
| Why can't I message my client? | Partly: says invite first, no route | Yes |
| How do I send a listing to my client in Messages from the listing page? | No: describes the retired Send in Messages flow | Yes |
| How do I share a listing from a Tag in Messages? | No: describes the retired footer action bar | Yes |
| How do I see which listings my client liked? | Yes | Yes |
| How do I know when a client has messaged me? | Yes | Yes |
| Can I delete a conversation in Messages? | Yes, in Tips | Yes |
| Where do my client's email replies go? | Partly: "directed to you" | Yes |

## Open items

- Labels not yet seen on screen: the contact step before the message step in the Share window (written as "Select a contact"); the Send icon on the Messages page; whether the pencil icon next to Contacts has a hover label; where View within Perchwell sits once a listing opens from a Tag.
- Scope: the open June 22 comment asks to reposition this as a Messages page Overview. Left unresolved on Kevin's instruction; the article stays a workflow under its current title.
- Shared article: one Notion row with MLS/AOR Baldwin and CRLMS All, per the September 17 decision. Cross-links point into the Baldwin help center.
- Video: the Arcade walkthrough predates Send as in-app message and the Tags redesign. Kevin accepted it as is for now.
- The Share Multiple Listings in Perchwell link uses the live title. Its draft retitles it Share Listings with Clients from Search; update the link text when that article is ported.
- The live Listing Detail Page Overview (Listing Maintenance) lists only Email, Text, Tags, and Public Link under Share and does not mention Send as in-app message. That article is stale.
