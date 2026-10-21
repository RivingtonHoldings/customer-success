# QA: Set Up Your Clients in Perchwell

- **Article name:** Set Up Your Clients in Perchwell
- **Old title:** Quick Guide: Getting Clients Started in Perchwell
- **Sources:** live Intercom article 15521779 (content ID 18497734), checked with `get_article` on October 9, 2026 and matching the mirror at `docs/help-center/baldwin/quick-guide-getting-clients-started-in-perchwell.md`; the five live screenshots, read at full resolution; the Notion drafts of the sibling articles listed under Source differences. No old Master Article List page was supplied.
- **Scored by:** Claude, for Kevin, October 9, 2026
- **Scorecard:** revision 2 (September 10, 2026 check set)
- **Scope decision:** short hub, chosen by Kevin October 9, 2026. Each section gives one or two sentences, keeps the fact that controls the order, and links the sibling article that owns the workflow. No Steps blocks.

## Golden questions

| # | Factor | Old | New | Note |
|---|---|---|---|---|
| 1 | disambiguation | Fail | Pass | Old: emoji pointers; "the invite option", "the Contacts section" |
| 2 | visual_content_text | Fail | Pass | Old: five images with no alt text. New: one screenshot placeholder, carrying its alt text |
| 3 | undefined_terms | Fail | Pass | Client portal and CSV now defined on first use |
| 4 | structured_enumeration | Pass | Pass | |
| 5 | query_answer_symmetry | Fail | Pass | Old: "Step 3:", "View Contact list", "Add contacts" headings |
| 6 | self_contained_sections | Fail | Pass | Old: alert steps began "Click the Settings icon on the saved search", depending on the section before |
| 7 | audience_specification | Pass | Pass | No role gates the workflow; Roles property is All Except Client |
| 8 | entity_distribution | Pass | Pass | |
| 9 | semantic_chunk_boundaries | Fail | Pass | Old: "Saved Search Alerts and Messaging Clients" covered alerts only |
| 10 | restate_questions | Pass | Pass | No tables |
| 11 | overview_jtbd | Fail | Pass | Old: "In this article, you will learn how to ..." |
| 12 | instruction_completeness | Fail | Pass | Old: no Steps block said what happens next. New: no Steps blocks |
| 13 | limitations_workarounds | Pass | Pass | Invitation requirement stated as the route forward |
| 14 | numerical_clarity | Fail | Pass | Old: "in the morning", "in the evening" with no times |

Old: 5 of 14. New: 14 of 14.

## Plain language gate

New: pass. No term from the do-not list; real things named (contacts, saved searches, listings); the title, description, opening, and headings use words an agent would say; no sentence restates a Steps block; each section carries the member's verb (add, invite, share, turn on, start).

## Dimension scores

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 8.6 (2 of 7) | 30.0 (7 of 7) | +21.4 |
| Chunk independence (25) | 12.5 (3 of 6) | 25.0 (6 of 6) | +12.5 |
| Answer completeness (25) | 7.1 (2 of 7) | 25.0 (7 of 7) | +17.9 |
| Fin-parsable formatting (10) | 2.5 (2 of 8) | 10.0 (8 of 8) | +7.5 |
| Accuracy and confidence (10) | 4.0 (2 of 5) | 10.0 (5 of 5) | +6.0 |
| **Total** | **34.7, Not retrievable as written** | **100.0, Fin-ready** | **+65.3** |

Old failures by dimension:

- Retrieval: title near-collides with Getting Started in Perchwell; empty description; "In this article" opening; numbered and bare-noun headings; no heading echo.
- Chunk independence: alert steps depend on the section before; one heading mixes alerts and messaging; H1 used for sections.
- Answer completeness: no outcome after any Steps block; no defaults; alert times vague; client portal undefined; alerts article named without a link.
- Formatting: combined steps (step 4 of the invite and contact blocks); emoji tips; bold throughout; emoji reactions; no alt text; horizontal rules.
- Accuracy: five statements contradicted by the article's own screenshots or confirmed sibling drafts (see Source differences); "you can" throughout.

Caveat on the new score: the hub's facts trace to sibling Notion drafts, most not yet live. If a sibling changes in review, the matching sentence here changes with it.

## Source differences

The live article lost on each of these. The hub keeps only the corrected fact where it needs one, and links out for the rest.

| Live article said | Corrected by | Hub now |
|---|---|---|
| Click Add New Contact | Live screenshot: Add contact pencil icon, Add Contact window; Contacts Page Overview draft | Links Contacts Page Overview |
| Select Reinvite Client under Account Status | Live screenshot: Reinvite contact to Perchwell under Account status; Invite Clients draft | Links Invite Clients to Perchwell |
| Invite by starting a new message in Messages | Message Clients draft: Messages is for invited clients only | States that Messages works only with invited clients |
| Shared-search clients cannot save changes | Live screenshot's on-screen text and the Share a Saved Search draft: clients can edit filters, and saved changes update your search | States that clients can edit and that changes update your search |
| Alerts under Notifications, with Immediately, Mornings, Nights, and Mornings and Nights | Set Up Email Alerts draft: Alerts toggle, Recipient and Frequency dropdowns, Immediately, Daily, Weekly, Monthly | States the Recipient default and links the alerts article |
| Share from the Tags page | Message Clients draft cut the Tag route; How to Share a Tag owns it | Not mentioned |
| Email Templates tip, linking Agent-to-Client Transition Email Templates | Invite Clients draft leaves open whether a saved template is added to invitations | Dropped; see open items |

## Fin test questions

| Question | Old, one section? | New, one section? |
|---|---|---|
| How do I get my clients set up in Perchwell? | No, spread over five steps | Yes, opening plus section links |
| Do my clients need to accept the invite before I can share a saved search? | Partly, "needs an account" | Yes, Invite clients section |
| Why can't I message my client in Messages? | No | Yes, Invite clients section |
| Can my client change a saved search I shared? | Yes, but wrong | Yes, Share saved searches section |
| How do I make saved search alerts go to my client? | Partly, outdated options | Yes, Turn on alerts section |
| Does my client need a Perchwell account to get alerts? | No | Yes, Turn on alerts section |
| How do clients react to listings I send them? | Yes, as emoji | Yes, Messages section |
| Were my contacts brought over from my old system? | Yes | Yes, Add clients section |

## Open items

- **Link text follows the live titles.** Bulk Upload Contacts, Invite Clients to Perchwell, and Add an Invited Client to a Saved Search are being retitled in their drafts. Update the link text here when those ports land.
- **Inbound link.** Agent-to-Client Transition Email Templates links to this article through an old Notion URL that members cannot open. It needs fixing when that article is next touched.
- **Email templates tip dropped.** Confirm whether agents should still be pointed to email templates when inviting several clients. If so, add one sentence to the Invite section once the Invite Clients draft resolves its template marker.
- **Screenshots.** The live images show contacts with @test.com emails, so they appear to be test data, not member data. They are being retired either way.
- **Redirect.** Record the old title for the Intercom redirect and audit.
