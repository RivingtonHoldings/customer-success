# QA: Share a Saved Search with a Client

- **Article name:** Share a Saved Search with a Client
- **Old title:** Add an Invited Client to a Saved Search
- **Old Notion page:** https://app.notion.com/p/1db8b9e014388092a384de78d013da3f
- **Intercom article ID:** 8955682, content ID 9098973
- **Mirror paths:** `docs/help-center/baldwin/add-an-invited-client-to-a-saved-search.md`, `docs/help-center/crmls/add-an-invited-client-to-a-saved-search.md` (shared article)
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-10-08-share-a-saved-search-with-a-client-rewrite.md`
- **Scored by:** Claude, with Tara's product answers and two current screenshots, October 8, 2026
- **Check set:** revision 2 (September 10, 2026)

## Golden questions

| # | Factor | Old | New | Note |
|---|---|---|---|---|
| 1 | disambiguation | Fail | Pass | Old step "Click into the search bar"; new names the Search contacts field |
| 2 | visual_content_text | Fail | Pass | Old images had no alt text; new placeholders carry alt text |
| 3 | undefined_terms | Pass | Pass | |
| 4 | structured_enumeration | Pass | Pass | Toggle states are now a labeled list |
| 5 | query_answer_symmetry | Fail | Pass | Bare "Tips" heading removed |
| 6 | self_contained_sections | Fail | Pass | Old "Turn on client access" depended on the window opened in an earlier section; each procedure now opens the window itself |
| 7 | audience_specification | Fail | Pass | Invitation requirement now stated before the steps |
| 8 | entity_distribution | Pass | Pass | "saved search" in every section |
| 9 | semantic_chunk_boundaries | Pass | Pass | |
| 10 | restate_questions | Pass | Pass | No tables |
| 11 | overview_jtbd | Fail | Pass | No opening paragraph in the live article |
| 12 | instruction_completeness | Fail | Pass | Every Steps block ends with what happens next |
| 13 | limitations_workarounds | Fail | Pass | Contacts without an accepted invitation get alerts only; route to Invite Clients to Perchwell |
| 14 | numerical_clarity | Pass | Pass | No numbers stated; the contact limit is unknown and not claimed |

## Plain language gate

Pass. Grep hits reviewed: "several" replaced with "multiple". No term from the do-not list in the sense it bans. "Contacts dropdown", "Search contacts", and the toggle name are exact on-screen control labels.

## Dimension scores

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 12.9 (3/7) | 30.0 (7/7) | +17.1 |
| Chunk independence (25) | 12.5 (3/6) | 25.0 (6/6) | +12.5 |
| Answer completeness (25) | 10.7 (3/7) | 25.0 (7/7) | +14.3 |
| Fin-parsable formatting (10) | 5.0 (4/8) | 10.0 (8/8) | +5.0 |
| Accuracy and confidence (10) | 6.0 (3/5) | 10.0 (5/5) | +4.0 |
| **Total** | **47.1** | **100.0** | **+52.9** |

Old band: Not retrievable as written. New band: Fin-ready, both gates passed.

Old failures: description in "In this article" form; no opening paragraph; H1 section headings and a bare "Tips" heading; wrong toggle label ("view and edit"); "Settings icon" and "the search bar" do not match the screen; no alt text; horizontal rules; bold UI labels; no related links; no account requirement; copy-on-edit and tag filter behavior missing.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I share a saved search with my client? | Partly (split across three sections) | Yes |
| Can my client change my saved search? | No | Yes |
| Why can't my client see the search I shared? | No | Yes |
| Will my client get notified when I share a search? | No | Yes |
| Can I add more than one client to a saved search? | No | Yes |
| How do I remove a client from a saved search? | No (Tips mentions it, no steps) | Yes |
| Can I add someone who isn't in my contacts? | No | Yes |
| Will my client get email alerts from the shared search? | No | Yes |

## Review, October 9, 2026

A reviewer's structural edit was merged: the toggle section now explains what the setting controls instead of repeating the instruction to turn it on, and the alerts section points to its own article. Eight fixes were applied on top of the reviewer's version: the alerts section now names the Recipient step, since Recipient defaults to Only me and turning on Alerts alone does not email the client; a repeated invitation fact and "However" removed; the feature name restored to the toggle heading; Step 1 and the toggle wording matched to the sibling drafts; the Note says whose tag filters; the contraction removed; and the email description restored. The tip about removing a client after the transaction closes was dropped. The score holds at 100 and both gates pass.

**Correction, October 9, 2026.** Client edits update the agent's saved search; they do not go to a copy. Tara corrected her October 8 answer. The live Manage Your Saved Searches article says the opposite and needs the same fix. The confirm marker about a client's copy after removal no longer applies and was removed. Client portal is now defined in the share section, and the Off state says the search does not appear in the client portal, confirmed by Tara.

## Open items

- Manage Your Saved Searches (live) says "client edits create a new saved search under the client's account. Your original saved search stays the same." That is wrong as of October 9, 2026; fix when that article is rewritten, or sooner, since agents may rely on it.
- Removal is written as the X next to the client's name in the Contacts field, from Tara's October 8 screenshot. Clearing the client's checkbox in the open dropdown may also work; the article documents one way.
- The "added you to the search" email is described from a test email screenshot; its sender name and search name vary, so the article says only that you added them and that it has an Open saved search button.
- Maximum number of contacts on one saved search is unknown; the article makes no claim.
- Shared article (Baldwin and CRMLS); links point at the Baldwin help center.
- Retitle: the Set Up Email Alerts for Saved Searches draft links to this article under its old title; update the link text when this is ported.
- Manage Your Saved Searches (live) says the Contacts dropdown lets you "create a new one". The current screen has no create option; fix when that article is rewritten.
- Dropped from the live article: the tip "Delete saved searches you no longer use", which belongs to Manage Your Saved Searches.
- Both live images show an older Edit Search window and are replaced with placeholders. The first also shows a contact's name.
- Arcade video is marked Update Required on the old row; it may show the older window.
