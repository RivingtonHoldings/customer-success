# QA: Mobile App FAQ

- **Article name:** Mobile App FAQ
- **Old title:** Mobile FAQ
- **Sources:** live Intercom article 15201164 (content ID 17971267), mirror `docs/help-center/baldwin/mobile-faq.md` (synced September 4, 2026; body checked against `get_article` on October 20, 2026, unchanged); old Notion page https://app.notion.com/p/3658b9e014388060bd1ddbcc3f232829; product answers from the teammate, October 20, 2026
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-10-20-mobile-app-faq-rewrite.md`
- **Notion:** https://app.notion.com/p/3ff8b9e014388136b9b8d0b70ce466a6
- **Scored by:** Claude, with Kevin, October 20, 2026. Scorecard check set revision 2.

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Pass | Pass | No images |
| 3 undefined_terms | Pass | Pass | |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Pass | Pass | Question headings |
| 6 self_contained_sections | Fail | Pass | Old answers ("Not at this time") made no sense without the heading |
| 7 audience_specification | Pass | Pass | Brokers and admins named in the Assume Identity answer |
| 8 entity_distribution | Fail | Pass | Each answer now names the Perchwell mobile app |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | |
| 11 overview_jtbd | Fail | Pass | Added the "Use this article to" opening |
| 12 instruction_completeness | Pass | Pass | No steps |
| 13 limitations_workarounds | Fail | Pass | Each "no" now gives the route: a web browser on an iPad, the listing in the app, a browser on a computer |
| 14 numerical_clarity | Pass | Pass | |

Old: 10 of 14. New: 14 of 14.

## Plain language gate

Pass. No term from the do-not list. "Assume Identity" is the on-screen label and is named once, at the point the member looks for it; the heading and answer otherwise say "assume an agent's identity", the member's phrasing from the live article.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 12.9 (3/7: no opening, 56-character description, no heading echo, iPad heading lacks Perchwell) | 30.0 | +17.1 |
| Chunk independence (25) | 16.7 (4/6: answers depend on the heading, feature name missing) | 25.0 | +8.3 |
| Answer completeness (25) | 14.3 (4/7: no system behavior stated, no route forward, no related links) | 25.0 | +10.7 |
| Fin-parsable formatting (10) | 10.0 | 10.0 | 0 |
| Accuracy and confidence (10) | 8.0 (4/5: "use your default browser") | 10.0 | +2.0 |
| **Total** | **61.9, Needs rewrite** | **100.0, Fin-ready** | **+38.1** |

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| Is there a Perchwell app for my iPad? | Yes | Yes |
| What browser should I use for Perchwell on my iPad? | No | Yes |
| Where do I download the Perchwell app for my phone? | No | Yes, with a link to the login article |
| Why don't the notes I added on my phone show up on my computer? | Partly, no route forward | Yes |
| Can other agents see my listing notes? | No | Yes |
| How do I log in as one of my agents from my phone? | Partly, no route forward | Yes |
| Can I assume an agent's identity in a phone browser? | No | Yes |

## Source differences

The old Notion page and the live article match, apart from "works the same as" (Notion) against "works just like" (live) in the iPad answer. Both were replaced by the teammate's product answers.

## Decisions taken

- Title changed from Mobile FAQ to Mobile App FAQ, so the title carries "app", the word members type.
- Collection: Mobile. The live article sits in the Mobile / FAQs sub-collection, which maps to its parent area.
- Roles: All, since the iPad answer applies to invited clients too.
- Cut "that feedback has been shared with the product team" from two answers, per the teammate.
- Cut "It works just like the desktop version" from the iPad answer. The browser and app differ (Dashboard, contact export, and bulk upload are browser-only), so the claim was not safe.
- Cut "If you previously downloaded the iPad app, please uninstall it". The teammate's answer covers pointing members to the phone app or a browser and did not keep this step.
- Questions reordered: iPad first, then notes, then Assume Identity.

## Open items

- Confirm that deleting an old Perchwell iPad app no longer needs mentioning. Restore one sentence to the iPad answer if members still have it installed.
- No legacy-platform sentence. new-terminology.md shows the legacy name for Assume Identity is also Assume Identity. The legacy mobile app's name includes the platform name, so it cannot go in an article.
- Link targets are live articles that drafts will replace: the notes link points at live article 14784837 under its new draft title, Listing Detail Page in the Perchwell Mobile App, and the iPad link points at 15280170 under its draft title, Log In to the Perchwell Mobile App. Check both titles at port.
- Set consistency: the Log In as an Agent with Assume Identity draft says "Open Perchwell in a browser to log in as an agent". The teammate confirmed it works only on a computer, so that line should say "a browser on a computer".
