# QA: Receive Alerts About New Listings

- **Article:** Receive Alerts About New Listings (title unchanged)
- **Old Notion page:** https://app.notion.com/p/1e58b9e01438805fbda9ccbea804fa5b
- **Intercom:** article 11373805, content 12304765
- **Mirror:** `docs/help-center/baldwin/receive-alerts-about-new-listings.md`, `docs/help-center/crmls/receive-alerts-about-new-listings.md` (shared article)
- **New Notion page:** https://app.notion.com/p/3f98b9e0143881e99770e03dad88be74
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-10-14-receive-alerts-about-new-listings-rewrite.md`
- **Scored by:** Claude, for Kevin, October 14, 2026, against scorecard revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Pass | Pass | Old had no images; new placeholders carry alt text |
| 3 undefined_terms | Pass | Pass | Client portal defined on first use |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | Old headings were bare nouns ("Alert contents", "Alert delivery channels") |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Fail | Pass | Old never said the article is for invited clients |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | Old opened with "In this article, you will learn" |
| 12 instruction_completeness | Fail | Pass | Old in-app steps stopped at the sort with no outcome. New sort step clicks the DOM column header and states the result and the status default |
| 13 limitations_workarounds | Pass | Pass | New adds the route for alerts without a visible saved search, and for messaging an agent |
| 14 numerical_clarity | Fail | Pass | Old "Some users" receive push notifications |

## Plain language gate

Pass. No term from the do-not list. "appears" in the last section has the saved search as its subject, so the system is the actor.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 12.9 (3/7) | 30.0 (7/7) | +17.1 |
| Chunk independence (25) | 16.7 (4/6) | 25.0 (6/6) | +8.3 |
| Answer completeness (25) | 7.1 (2/7) | 25.0 (7/7) | +17.9 |
| Fin-parsable formatting (10) | 7.5 (6/8) | 10.0 (8/8) | +2.5 |
| Accuracy and confidence (10) | 4.0 (2/5) | 10.0 (5/5) | +6.0 |
| **Total** | **48.2, Not retrievable as written** | **100.0, Fin-ready, gate passed** | **+51.8** |

Old failures: description 155 characters and not jobs-led; no "Use this article to" opening; bare-noun headings with no echo; H1 used for every section; bold UI labels; horizontal rules; "you can"; no role stated; "Some users"; no outcome after the in-app steps; no links; three unsourced or wrong claims (alerts start automatically, the email has a way to message the agent, reacting from any listing). New: chunk check 4 first failed on three one-sentence paragraphs; Kevin approved merging each with its neighbor, October 14, 2026. The remaining one-sentence paragraphs are section leads above a Steps block.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| Why am I getting emails about new listings? | Yes | Yes |
| How often will I get listing alerts? | Partly ("your agent sets the schedule") | Yes |
| Can I message my agent from the alert email? | Wrong (says yes) | Yes |
| Do I get alerts on my phone? | Partly ("some users") | Yes |
| How do I see the newest listings in my saved search? | Wrong (Newest First does not exist) | Yes |
| How do I stop getting these alert emails? | No | Yes, by link |
| Do I need an account to open listings from the email? | No | Yes |
| I get alerts but cannot find the saved search. Where is it? | No | Yes |

## Source differences and how they were settled

- Alerts "start automatically": replaced. Per Kevin, October 14, 2026, alerts start once the agent finishes saving the saved search; the reviewed Set Up Email Alerts draft adds that the agent turns on Alerts and picks a Recipient that includes contacts.
- Push notifications: kept, made definite. Kevin confirmed invited clients receive them.
- React or message from an alert listing: narrowed. The link opens the Listing Detail Page; reactions work only for listings in a Tag shared with the client (Kevin).
- "A way to message your agent" in the email: removed and stated as absent, with the route to Messages. Kevin's screenshot of an alert email shows no message option. This is the bare-deficit exception, since the live article promised it.
- Alert activity: widened from new listings to new matches, price, status, and open houses, hedged as "can include", per Kevin and the Set Up Email Alerts draft.
- "Email alerts and in-platform results reflect the same live data": cut. Alerts report activity since the last alert, so the sentence could not be stated precisely.

## Open items

- Sort step settled by Kevin, October 14, 2026: results sort by status by default, and clients click the DOM column header for the newest listings. "Newest First" does not exist. View Shared Saved Searches should be checked for the same wrong label when it is migrated. That one click putting the fewest days first follows the ascending-first sort in Create a Search with Filters; worth a glance in the screenshot.
- Shared article: live in Baldwin (Client Experience) and CRMLS (Client Collaboration / Invited Clients). Old row MLS is All Regions; proposed MLS/AOR is Baldwin and CRLMS All, matching the set.
- The unsubscribe link uses the draft title Unsubscribe from Saved Search Alert Emails over the live URL for Unsubscribe from Notifications (For Invited Clients). Recheck the title at port.
- Screenshots: alert email, Listing Detail Page from an alert, sorted saved search results; all from a test client account.
