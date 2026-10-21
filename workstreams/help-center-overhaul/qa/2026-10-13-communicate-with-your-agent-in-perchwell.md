# QA: Communicate with Your Agent in Perchwell

- Article name: Communicate with Your Agent in Perchwell (title unchanged)
- Old Notion page: https://app.notion.com/p/1e78b9e01438802c9bd5ddf4b8001945
- Intercom article ID 11373888, content ID 12304874
- Mirror: `docs/help-center/baldwin/communicate-with-your-agent-in-perchwell.md` and `docs/help-center/crmls/communicate-with-your-agent-in-perchwell.md` (shared article)
- New Notion page: https://app.notion.com/p/3f88b9e014388192a12df9410d9877db
- Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-10-13-communicate-with-your-agent-in-perchwell-rewrite.md`
- Scored by Claude for Kevin, October 13, 2026, against scorecard revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Pass | Pass | Old had no images; new placeholders carry alt text |
| 3 undefined_terms | Pass | Pass | Client portal defined on first use |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | "Messages access" and "Listing reactions" were bare nouns |
| 6 self_contained_sections | Fail | Pass | Old reactions section never said where to react |
| 7 audience_specification | Fail | Pass | Now states the article is for invited clients |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | "Use this article" opening added |
| 12 instruction_completeness | Fail | Pass | Old steps ended at "Send your message"; every Steps block now ends at the outcome |
| 13 limitations_workarounds | Pass | Pass | No notification on reactions, stated with the route forward |
| 14 numerical_clarity | Pass | Pass | No numbers |

## Plain language gate

Pass on the rewrite. No do-not-list terms. "Shared properties" is the on-screen label and named only where the client has to find it; "chat" replaces "send a message in Messages" to avoid a feature-name echo.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 17.1 | 30.0 | +12.9 |
| Chunk independence (25) | 20.8 | 25.0 | +4.2 |
| Answer completeness (25) | 10.7 | 25.0 | +14.3 |
| Fin-parsable formatting (10) | 3.8 | 10.0 | +6.2 |
| Accuracy and confidence (10) | 8.0 | 10.0 | +2.0 |
| Total | 60.4 | 100.0 | +39.6 |

Old: Needs rewrite. New: Fin-ready, 14 of 14 golden questions, plain language gate passed.

Old failures: "In this article, you will learn" opening, bare-noun headings with no heading echo, an H1 section heading, steps that stop at "Send your message", no audience, no links, bold UI labels, an emoji tip, a horizontal rule, and "Use Messages" and "Use reactions" leads.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I message my agent in Perchwell? | Partly, steps vague | Yes |
| How do I like a listing my agent sent me? | No, never says where to react | Yes |
| Can I change my reaction to a listing? | No | Yes |
| Does my agent get notified when I react to a listing? | Partly | Yes |
| Can I reply to my agent's email instead of logging in? | No | Yes |
| What does Maybe mean on a listing? | Yes | Yes |
| Can I message my agent from the Perchwell app? | No | Yes |
| How do I send my agent a listing? | No | Yes, by link to Share Listings with Your Agent |

## Open items

- Shared article: the same Intercom record sits in the Baldwin and CRMLS help centers. Row proposed as MLS/AOR Baldwin and CRLMS All; links point into the Baldwin help center.
- Reactions are written in on-screen order (Reject, Maybe, Like); the live article ran Like, Maybe, Reject. Confirm the team is happy with the product order.
- Whether a client can clear a reaction entirely, rather than switch to another, is unknown and left out.
- The Shared properties filters (All, Undecided, Maybe, Liked, Rejected) on the client side are unconfirmed and left out.
- The live How to Share a Tag article says clients can "like or dislike" listings and "undo a reaction at any time". That describes the public Tag page, but the vocabulary differs from Reject, Maybe, Like; check when that article is next touched.
- Two screenshot placeholders need captures from a test client account.
- Loom video confirmed current by Kevin, October 13, 2026; the reviewer should confirm its steps match the written ones.
