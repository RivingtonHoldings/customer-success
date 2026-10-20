# QA: Share a Tag with Clients

- **Article:** Share a Tag with Clients
- **Old title:** How to Share a Tag
- **Sources:** live Baldwin article, Intercom ID 16221617, content ID 19552537, mirror `docs/help-center/baldwin/how-to-share-a-tag.md`. No old Notion page. Related live CRMLS article Managing your Tag Alerts and Sharing Tags (12921217) read for comparison. Product facts confirmed by Tara with screenshots, October 19, 2026.
- **Scored by:** Claude, for Tara, October 19, 2026. Scorecard revision 2.

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Fail | Pass | Old image had no alt text; placeholders carry alt text |
| 3 undefined_terms | Fail | Pass | "Success toast" removed |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | "Share again" replaced |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | No role gate; Roles: All Except Client |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | No opening paragraph before |
| 12 instruction_completeness | Fail | Pass | Email steps stopped at Send; Resend outcome confirmed |
| 13 limitations_workarounds | Fail | Pass | Contacts cannot be removed, stated before the steps |
| 14 numerical_clarity | Pass | Pass | 225 and 10,000 character limits |

## Plain language gate

Old: fail on "toast" (replace with the message's text, "Copied to clipboard"). New: pass.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 17.1 | 30.0 | +12.9 |
| Chunk independence (25) | 25.0 | 25.0 | 0 |
| Answer completeness (25) | 7.1 | 25.0 | +17.9 |
| Fin-parsable formatting (10) | 5.0 | 10.0 | +5.0 |
| Accuracy and confidence (10) | 4.0 | 10.0 | +6.0 |
| **Total** | **58.2, Needs rewrite** | **100.0, Fin-ready** | **+41.8** |

Old failures: no opening; headings without the feature name ("Share again", "What your client sees"); no heading echo; email steps end at Send; no limit stated; toast undefined; no related links; bold and terminal periods in steps; image with no alt text; horizontal rules; "you can"; every control in the steps (Share, Copy Link, Share via Email, Re-Share) no longer exists; "Liked listings are added back to your Tag automatically" unsourced.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I share a tag with my client? | Partly, with controls that no longer exist | Yes |
| Does my client need a Perchwell account to see my tag? | Yes | Yes |
| How do I copy the link to my tag? | Partly, wrong control | Yes |
| Can I remove a client from a tag I already sent? | No | Yes |
| How do I resend a tag or add another client? | Partly, wrong control | Yes |
| Can I change the email that goes out with a tag? | No | Yes |
| How do my clients like or dislike listings in a tag? | Partly | Yes |
| Why does my tag show views when my client has not opened it? | No | Yes |

## Open items

- Resolved October 19, 2026, by Tara: Resend emails every contact; a template replaces the subject and message, and None clears both; Save and Close is not offered once contacts are invited.
- Save and Close bug: contacts do not stay added after Save and Close. Tara has filed it. The article describes the intended behavior per the standard.
- Reaction icons: the earlier screenshot without them was a Tag with Reactions turned off. With Reactions on, the public page shows the icons and All, From [agent], New to You, Liked, and Disliked.
- Left out on purpose: the All, From [agent], New to You, Liked, and Disliked view options and the status and sort dropdowns on the public page, since the page makes them obvious; the From Saved Search and Shared by labels, owned by Link a Saved Search to a Tag; mobile, per Tara.
- Video: the Loom shows the retired Share and Re-Share controls. Kept per Tara; replacement is planned.
- Live image: the published public-page image (captured August 5, 2026) shows a staff test account's email and phone number. It is replaced by a placeholder in this draft; it stays live until the port.
- Set: Create and Edit a Tag links "How to Share a Tag"; update the link text and URL when this article ports. Its contact callout reads "after you save it"; this draft reads "once you send or save it".
- Links point to live Baldwin URLs for How to Create a Tag and How to Link a Saved Search to a Tag; update them when those drafts port under new titles.
- Shared status: the article is in the Baldwin mirror only; the row is set to Baldwin and CRLMS All, matching the other Tag drafts.
- Tracker ID: TRK-098.
