# QA: User Settings FAQ

- Article name: User Settings FAQ (old title: User Settings FAQs)
- Old Notion page: none; no Master Article List row found
- Intercom article ID 16180793, content ID 19483212
- Mirror: `docs/help-center/baldwin/user-settings-faqs.md`
- Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-10-16-user-settings-faq-rewrite.md`
- New Notion page: https://app.notion.com/p/3fb8b9e01438818b9eb9cb1f1a70362a
- Scored by Claude for Kevin, October 16, 2026, against scorecard revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Fail | Pass | "visit this Help Center article" replaced with the linked title |
| 2 visual_content_text | Fail | Pass | Three images behind trailing colons with no alt text; both kept images now carry alt text |
| 3 undefined_terms | Fail | Pass | "MMSI/Relevate" roster software dropped; PA/OA written out |
| 4 structured_enumeration | Fail | Pass | Profile picture steps were prose; now a numbered list |
| 5 query_answer_symmetry | Pass | Pass | Question headings |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | Assistant question names who it applies to |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Fail | Pass | Two email questions merged into one |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | "Use this article to" opening added |
| 12 instruction_completeness | Fail | Pass | Profile picture steps end with the automatic save, confirmed by Kevin October 16, 2026 |
| 13 limitations_workarounds | Pass | Pass | |
| 14 numerical_clarity | Pass | Pass | No file type or size limit to state, per Kevin |

## Plain language gate

Pass on the rewrite. No do-not-list terms. "pop-up" in the old article is gone with the wrong steps.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 17.1 | 30.0 | +12.9 |
| Chunk independence (25) | 20.8 | 25.0 | +4.2 |
| Answer completeness (25) | 14.3 | 25.0 | +10.7 |
| Fin-parsable formatting (10) | 5.0 | 10.0 | +5.0 |
| Accuracy and confidence (10) | 6.0 | 10.0 | +4.0 |
| Total | 63.2 | 100.0 | +36.8 |

Old: Needs rewrite. New: Fin-ready, 14 of 14 golden questions, plain language gate passed.

Old failures: description under 120 characters and led with "In this article", no opening, no heading echo under the profile picture question, email answered twice with two different routes, prose steps, bold UI labels, horizontal rules, images with no alt text, "please" and "You can reach out", an undefined vendor name, and profile picture steps that no longer work (clicking the photo on the User settings page does nothing, confirmed by Kevin October 16, 2026).

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I change my email in Perchwell? | Partly, two sections with different routes | Yes |
| The email on my listings is wrong, how do I fix it? | Yes | Yes |
| How do I update my phone number? | Yes | Yes |
| How do I change my profile picture? | No, the steps are wrong | Yes |
| Where is the About Me page? | No | Yes |
| I'm an assistant and only see the Dashboard, why? | Yes | Yes |
| Who do I contact to change my name? | Yes | Yes |

## Open items

- All confirm markers resolved October 16, 2026, by Kevin: on Edit profile, click the profile picture itself (no separate button), upload an image, and it saves automatically; no file type or size limit to state. "Upper left" for the picture on Edit profile comes from the old screenshot of the User settings page; check it when the placeholder is captured.
- Screenshot placeholder for the Edit profile view needs capturing.
- The profile menu screenshot shows Stop assuming identity, which appears only while assuming another account; retake it in a normal session. Both kept screenshots show a staff member's name and photo, not a member's.
- The old third screenshot (clicking the photo on the User settings page) was dropped, since that click does nothing.
- Source decisions, from Kevin October 16, 2026: MLS staff update name, email, and phone, or members contact Perchwell support; the live article's "update via the Baldwin portal" route was dropped. The agent or broker grants assistant permission, matching the live article; the Assume Identity draft's step of contacting the MLS with the broker was not carried here.
- Retitle: the Login and Troubleshooting FAQ draft links to "User Settings FAQs" by title; update its link text when this ports.
- Legacy sentence added from `new-terminology.md`: About Me Page maps to User Settings.
