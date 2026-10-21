# QA: Manage People FAQ

- Article name: Manage People FAQ (title unchanged)
- Old Notion page: https://app.notion.com/p/3668b9e0143880a39e4ffdaaf3056b31 (titled Manage People FAQs)
- Intercom article ID 15201140, content ID 17971228
- Mirror: `docs/help-center/baldwin/manage-people-faq.md` (Baldwin only, not shared with CRMLS)
- Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-10-15-manage-people-faq-rewrite.md`
- New Notion page: https://app.notion.com/p/3fa8b9e0143881bca141cd468e1ef664
- Scored by Claude for Kevin, October 15, 2026, against scorecard revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Pass | Pass | No images in either version |
| 3 undefined_terms | Fail | Pass | Old body never named Assume Identity or Manage People; the new one defines assuming an agent's identity with a which-means clause |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Pass | Pass | Question headings |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | Opening names brokers and admins; Manage People is an admin and broker page |
| 8 entity_distribution | Fail | Pass | Feature name now in every section |
| 9 semantic_chunk_boundaries | Fail | Pass | Old question was bold text, not a heading |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | "Use this article" opening added |
| 12 instruction_completeness | Pass | Pass | No Steps blocks; the one-click stop action is in its lead |
| 13 limitations_workarounds | Pass | Pass | |
| 14 numerical_clarity | Pass | Pass | |

## Plain language gate

Pass on the rewrite. No do-not-list terms. "Assume Identity" and "Can login as me" are on-screen labels, confirmed from the live Assume Identity screenshots; the body otherwise says "log in as an agent", the words a member would type.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 12.9 | 30.0 | +17.1 |
| Chunk independence (25) | 16.7 | 25.0 | +8.3 |
| Answer completeness (25) | 14.3 | 25.0 | +10.7 |
| Fin-parsable formatting (10) | 8.8 | 10.0 | +1.2 |
| Accuracy and confidence (10) | 6.0 | 10.0 | +4.0 |
| Total | 58.7 | 100.0 | +41.3 |

Old: Needs rewrite. New: Fin-ready, 14 of 14 golden questions, plain language gate passed. No `[confirm: ...]` markers.

Old failures: description 86 characters, no opening, bold question instead of a heading, no feature name in the body, "Yes" answered what the admin can do rather than what the agent experiences, the agent's session not stated, Assume Identity not linked, an unsourced forward-looking sentence about guardrails, "you will be able to".

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| If I log in as my agent while they're logged in, will it kick them out? | No | Yes |
| Do changes I make in an agent's account show up for them? | Partly | Yes |
| Does the agent get notified when I assume their identity? | No | Yes |
| Who can assume identity in Perchwell? | No | Yes |
| As an admin, how do I get permission to log in as an agent? | No | Yes |
| How do I get back to my own account after assuming identity? | No | Yes |
| Where is the Roster in Perchwell? | No | Yes |
| How do I find an agent in my office? | No | Yes |

## Open items

- Agent experience during a concurrent session confirmed by Kevin, October 15, 2026: the agent stays logged in and sees the changes. Agent is not notified at login, also confirmed by Kevin.
- The live guardrails sentence ("The team is looking into adding guardrails around adding and editing listings") was dropped at Kevin's direction.
- Scope widened at Kevin's direction: four questions added, each sourced from the live Assume Identity (16053168) and Perchwell Teams (14742099) articles, with links out. Assume Identity is unmigrated; when it is rewritten, keep its admin and broker routes consistent with the two sentences here.
- The old Notion row's second question, about listings when an agent moves offices, stays out. Kelly's comment on that row (May 29, 2026) splits it into three FAQs, two under Add/Edit and one under Analytics.
- "Perchwell will track all history" (Assume Identity) left out: it is unclear whether the agent or broker can see that history.
- Privacy, replace now: the live Assume Identity screenshot of the agent details page (Assume Identity button) shows what looks like a real agent's first and last name in Contact information. The image is already published.
- Labels checked against live Assume Identity screenshots (captured July 30, 2026): Assume Identity button on the agent details page, Stop assuming identity in the profile menu, Can login as me dropdown under Features in profile settings. The admin route's Log in As label was not used in this FAQ.
- Roles set to Admin/Broker; the old row had none. MLS/AOR Baldwin from the old row. Collection Manage People (the live subcollection is Manage People / FAQs; Analytics FAQ set the same precedent).
- Title collision: "Manage People" is also the page name and the collection name. Kept, since FAQ titles follow the "\<Area\> FAQ" pattern, as Dashboard FAQ, Reports FAQ, and Analytics FAQ do.
- Who can assume an agent's identity, revised October 15, 2026 to match the Log In as an Agent with Assume Identity rewrite and Kevin's product answers: office admins and MLS staff also use the Manage People route; the admin route runs through Log in as, which lists only agents who added the admin under Can login as me; Can login as me is office-only; MLS address corrected to mls@baldwinrealtors.com; link text updated to the new title.
- Set check, October 15, 2026: the Manage People collection holds only an empty [Placeholder] Manage People row. No sibling draft mentions Manage People or Assume Identity.
