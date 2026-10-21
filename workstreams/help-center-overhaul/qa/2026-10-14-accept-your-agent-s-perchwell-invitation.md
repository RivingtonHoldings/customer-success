# QA: Accept Your Agent's Perchwell Invitation

- Article name: Accept Your Agent's Perchwell Invitation (title unchanged)
- Old Notion page: none; migrated from the live article
- Intercom article ID 15521326, content ID 18497092
- Mirror: `docs/help-center/baldwin/accept-your-agent-s-perchwell-invitation.md`
- Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-10-14-accept-your-agent-s-perchwell-invitation-rewrite.md`
- Scored by Claude for Kevin, October 14, 2026, against scorecard revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Fail | Pass | Live images carry "image" as alt text; the rewrite has alt text on the image and both placeholders |
| 3 undefined_terms | Pass | Pass | Client portal defined on first use |
| 4 structured_enumeration | Fail | Pass | The flow was spread across one-line headings; now two Steps blocks |
| 5 query_answer_symmetry | Fail | Pass | "Preparation", "Password creation", "Getting started", "Tips" replaced with task headings |
| 6 self_contained_sections | Fail | Pass | "A new webpage will open" depended on the section before it |
| 7 audience_specification | Pass | Pass | The title and opening address the invited client; Roles: Invited Client |
| 8 entity_distribution | Fail | Pass | Perchwell named in every section |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | "Use this article to" opening replaces "You will learn how" |
| 12 instruction_completeness | Fail | Pass | Each Steps block ends at the outcome; the client login page URL, www.perchwell.com/accounts/sign_in, confirmed by Kevin October 14, 2026 |
| 13 limitations_workarounds | Pass | Pass | Missing email and forgotten password each give the route forward |
| 14 numerical_clarity | Fail | Pass | Password requirements now stated: 8 characters, one capital letter, one number, one special character |

## Plain language gate

Pass on the rewrite. No do-not-list terms. "Client portal" is the settled term from `docs/product-context.md`, defined in the section that uses it.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 8.6 | 30.0 | +21.4 |
| Chunk independence (25) | 20.8 | 25.0 | +4.2 |
| Answer completeness (25) | 14.3 | 25.0 | +10.7 |
| Fin-parsable formatting (10) | 3.8 | 10.0 | +6.2 |
| Accuracy and confidence (10) | 6.0 | 10.0 | +4.0 |
| Total | 53.5 | 100.0 | +46.5 |

Old: Needs rewrite. New: Fin-ready, 14 of 14 golden questions, plain language gate passed, no open confirm markers.

Old failures: description in the retired "In this article: You will learn" form; no "Use this article to" opening; bare-noun headings; capability list in the opening with no sections behind it; no outcome after the password step; password requirements missing; "You can" and "where you can"; emoji callouts and bold UI labels; images with no alt text; Next Steps links into intercom.help with one saying "your client has shard with you". Three facts the live article has wrong: the subject line (now "Start your home search on Perchwell"), the sender (the agent's name from no-reply@perchwell.com, not "Perchwell"), and the link label (Forgot your password?, not Forgot Password).

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| I can't find the invitation my agent sent me | Partly, the spam tip and the resend tip sit in two sections | Yes |
| What is the subject line of the Perchwell invite email? | No, the subject is out of date | Yes |
| What are the password requirements for Perchwell? | No | Yes |
| How do I accept my agent's invitation? | Partly, spread across four headings | Yes |
| I forgot my Perchwell password | Yes, in Tips, with the wrong label | Yes |
| Can I use Perchwell on my phone? | Yes | Yes |
| Where do I see the saved searches my agent shared? | Partly, a link with the wrong subject | Yes |
| How do I log in to Perchwell as a client? | Partly | Yes |

## Open items

- Resolved October 14, 2026: clients sign in at www.perchwell.com/accounts/sign_in, a different route from the agent login; the password page Accept Invitation opens is `perchwell.com/onboard?reset_password_token=<token>`.
- Privacy, replace now: the live email screenshot and password screenshot, and the Arcade, show what read as a person's full name, a client's first name, an email address, and a saved search named for a client. Replace the live images in Intercom now; the draft carries placeholders asking for demo names. The Arcade needs re-recording or confirmation that the names are demo personas.
- Invitation expiry left out: Kevin's answer was that the link "should not expire", which is not firm enough to publish.
- CRMLS has its own separate article on the same topic (Intercom 11373210, Client Collaboration / Invited Clients). It is not shared with this one, and it carries the same out-of-date subject line and label. It could be ported from this rewrite.
- Set consistency: the Invite Clients to Perchwell and Resend Invitations draft gives the old subject line in its Tip and says "Forgot Password". Both need updating to match this article.
