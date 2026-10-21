# QA: Unsubscribe from Saved Search Alert Emails

Old title: Unsubscribe from Notifications (For Invited Clients)

## Sources

- Old Notion page (Master Article List, read only): https://app.notion.com/p/2b28b9e01438802d88a1d496e0cd0582
- Intercom article ID 13602428, content ID 15664447
- Mirror: `docs/help-center/baldwin/unsubscribe-from-notifications-for-invited-clients.md` and `docs/help-center/crmls/unsubscribe-from-notifications-for-invited-clients.md` (shared article)
- New Notion draft: https://app.notion.com/p/3f48b9e01438816fa5a0cfbf6c84acda
- Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-10-09-unsubscribe-from-saved-search-alert-emails-rewrite.md`
- Live screenshot (Intercom CDN, captured about February 2026): an NYC saved search alert email. Showed that the footer link reads "Click here to unsubscribe." rather than "Unsubscribe"
- Screenshots from the teammate, October 9, 2026: a Baldwin saved search alert email with the same footer label, and the Unsubscribe from notifications page the link opens (Email address field, Unsubscribe button, "shared search email notifications from" the agent)
- Product answers from the teammate, October 9, 2026: the unsubscribe stops every saved search alert email from the agent, not only the one search named; it does not stop other Perchwell emails; to get alerts again, the agent re-shares the saved search or the client accepts a new invitation; tag alerts go to agents only and clients do not receive them (settled after an earlier answer said they did)
- Set read: the new database's Client Collaboration rows (all agent-facing); the mirror's Client Experience articles (Receive Alerts About New Listings, View Shared Saved Searches, Accept Your Agent's Perchwell Invitation); Client Collaboration FAQ; CRMLS Managing Tag Alerts

Scored by Claude with /article-rewrite on October 9, 2026, against the scorecard check set revision 2.

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Fail | Pass | Live image has no alt text; both placeholders carry it |
| 3 undefined_terms | Pass | Pass | |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | "Email alert unsubscribe", "Tag alert toggle", "Tips" replaced with task headings |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | Invited clients named in the opening |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | "Use this article to" opening added |
| 12 instruction_completeness | Fail | Pass | Steps now run through the Unsubscribe from notifications page and end with the outcome |
| 13 limitations_workarounds | Pass | Pass | Getting alerts again is stated, and the tag alert question is answered |
| 14 numerical_clarity | Pass | Pass | |

Old: 10 of 14. New: 14 of 14.

## Plain language gate

New: Pass. No term from the do-not list. "Click here to unsubscribe" is the footer link's exact label and appears only in the step that clicks it.

## Scores

| Dimension | Weight | Old | New | Delta |
|---|---|---|---|---|
| Retrieval signals | 30 | 17.1 (4/7) | 30.0 (7/7) | +12.9 |
| Chunk independence | 25 | 20.8 (5/6) | 25.0 (6/6) | +4.2 |
| Answer completeness | 25 | 14.3 (4/7) | 25.0 (7/7) | +10.7 |
| Fin-parsable formatting | 10 | 2.5 (2/8) | 10.0 (8/8) | +7.5 |
| Accuracy and confidence | 10 | 4.0 (2/5) | 10.0 (5/5) | +6.0 |
| Total | 100 | 58.7 | 100.0 | +41.3 |

Old band: Needs rewrite. New band: Fin-ready, gate passed, with one open `[confirm: ...]` marker.

Old failures: description in the "In this article, you will learn" form and under 120 characters; no "Use this article to" opening; bare-noun headings, one of them an H1 in the body; the steps stop at the email link and miss the unsubscribe page; the link is named "Unsubscribe" when the footer reads "Click here to unsubscribe."; "Perchwell stops sending email notifications" overstates the scope; a tag alert section for clients, who do not receive tag alerts, built on a bell icon they do not have; UI labels bolded; emoji callout; image with no alt text; horizontal rules; "Use the Unsubscribe link".

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I stop getting listing alert emails? | Partly, missing the unsubscribe page | Yes |
| If I unsubscribe from one search, do I stop getting all of them? | No | Yes |
| How do I turn off tag alerts? | Yes, but wrong (bell icon) | Yes: clients do not receive them |
| I unsubscribed by mistake. How do I get my alerts back? | Partly, in Tips | Yes |
| Will I still get messages from my agent after I unsubscribe? | No | Yes |
| How do I delete my Perchwell account? | Yes, in Tips | Yes |

## Open items

- `[confirm: what the client sees after clicking Unsubscribe, such as a confirmation message]`
- Retitled from the working title "Unsubscribe from Saved Search and Tag Alerts" once tag alerts were confirmed agent-only. Title collision check: no other title uses "unsubscribe"; "Set Up Email Alerts for Saved Searches" shares "email alerts" and "saved search" but covers the agent's side, so the two name different jobs
- Replace the live article's screenshot now, not at port: its greeting shows a named person, and the listing is an NYC condo. The teammate's Baldwin capture, cropped below the recipient line, is at `workstreams/help-center-overhaul/outputs/drafts/images/2026-10-09-saved-search-alert-email-footer.png`
- The unsubscribe page screenshot shows the teammate's own name as the agent; reshoot from a test agent account
- CRMLS Managing Tag Alerts is correct that clients do not receive tag alerts; no change needed there
- Collection: Client Experience, approved by the teammate, where the other client-facing articles live
- MLS: shared article, one row with Baldwin and CRLMS All, approved by the teammate
