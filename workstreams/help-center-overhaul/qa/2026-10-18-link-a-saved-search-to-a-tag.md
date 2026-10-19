# QA: Link a Saved Search to a Tag

- **Article:** Link a Saved Search to a Tag
- **Old title:** How to Link a Saved Search to a Tag
- **Old Notion page:** none used; the rewrite started from the live article
- **Intercom:** article 16221382, content 19552161, collection Tags, Baldwin only (no CRMLS counterpart)
- **Mirror:** `docs/help-center/baldwin/how-to-link-a-saved-search-to-a-tag.md`, checked against `get_article` on October 18, 2026; the body matches
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-10-18-link-a-saved-search-to-a-tag-rewrite.md`
- **Notion draft:** https://app.notion.com/p/3fd8b9e0143881499020df4b5b281008
- **Scored by:** Claude for Tara, October 18, 2026, scorecard revision 2

## Golden questions

| # | Factor | Old | New | Note |
|---|---|---|---|---|
| 1 | disambiguation | Pass | Pass | |
| 2 | visual_content_text | Pass | Pass | Live article has no images; every placeholder carries alt text |
| 3 | undefined_terms | Fail | Pass | Tag defined in the opening |
| 4 | structured_enumeration | Pass | Pass | |
| 5 | query_answer_symmetry | Fail | Pass | "Considerations" replaced |
| 6 | self_contained_sections | Pass | Pass | |
| 7 | audience_specification | Pass | Pass | No role gate; Roles records All Except Client |
| 8 | entity_distribution | Pass | Pass | |
| 9 | semantic_chunk_boundaries | Fail | Pass | Saved search sharing bullet cut |
| 10 | restate_questions | Pass | Pass | No tables |
| 11 | overview_jtbd | Fail | Pass | Live article had no opening |
| 12 | instruction_completeness | Fail | Pass | Neither live Steps block said what happens next |
| 13 | limitations_workarounds | Pass | Pass | Saved search listings cannot be removed one by one; route given |
| 14 | numerical_clarity | Pass | Pass | |

Old: 9 of 14. New: 14 of 14.

## Plain language gate

Pass. No do-not list terms. "Unlink" is the article's verb for the x under Saved searches; the unlink lead also says "remove its listings", the word members are likely to type.

## Dimension scores

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 12.9 (3/7: 170-character "you will learn" description, no opening, "Considerations" heading and no echo) | 30.0 | +17.1 |
| Chunk independence (25) | 16.7 (4/6: mixed Considerations section, truncated "Your client can" paragraph) | 25.0 | +8.3 |
| Answer completeness (25) | 10.7 (3/7: no outcomes, no defaults, Tag undefined, related articles named in italics without links) | 25.0 | +14.3 |
| Fin-parsable formatting (10) | 6.3 (5/8: terminal periods and bold in steps, horizontal rules) | 10.0 | +3.7 |
| Accuracy and confidence (10) | 10.0 | 10.0 | 0 |
| **Total** | **56.5, Needs rewrite** | **100.0, Fin-ready** | **+43.5** |

The old score understates the problem: both live procedures describe a window that no longer exists (Tag Name, Contacts dropdown, Next, Add search results to Tag, Alerts, Save). The scorecard has no check for stale steps.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I add a saved search to a tag? | Yes, with stale steps | Yes |
| Can I link more than one saved search to a tag? | Partly | Yes |
| Why did a listing disappear from my tag? | Partly, under Considerations | Yes, though the heading says "update", not "disappear"; test this one first after port |
| How do I keep a listing in my tag if it drops out of the search? | Yes | Yes |
| Why can't I delete a listing from my tag? | No | Yes |
| How do I remove a saved search from a tag? | No | Yes |
| Will I get an email when new listings come into my tag from a saved search? | No | Yes |
| Can my client see the saved search listings on the tag? | No | Yes |

## Source differences and what won

- The live article and its Loom both describe the old Tag window. Tara's October 18 screenshots won: Saved searches section with Add in Create a new tag and Edit Tag; the Add saved search window ("Display search results in real time.") with a Saved searches field, a card per selected search with its listing count, and Cancel and Add; chips with an x under Saved searches; a "Tag updated." message after Save.
- Listings and notes window: Added by you group first, then one group per saved search under its name. Saved search listings have no trash can or reorder arrows; every listing has a Note for client field. Jira PWEB-23465 spells the label "Added by You"; the screenshot shows "Added by you", which the draft follows.
- Tara, October 18: only the agent's own saved searches are listed; the Search by name or contact field matches search and contact names; a saved search can be linked to more than one Tag; changing a linked search's filters updated the Tag's count right away; liked and disliked listings stay; unlinking removes listings right away; a saved search listing sends the Tag notifications email; the public page labels listings From Saved Search or Shared by the agent; no Tag option exists in the New Search or Edit Search windows.
- Live Tags Page Overview says the Save Search dialog links a saved search to a Tag. Tara found no such option; that article needs the line removed in its rewrite.

## Open items

- Resolved October 18, 2026 (Tara's test): listings a contact liked or disliked stay in the Tag after their saved search is unlinked. The Unlink outcome now says so.
- Possible bug, kept out of the article per the bug rule: after unlinking, the Listings and notes count in the Edit Tag window includes the reacted listings, but the Listings and notes window (Edit) shows only listings added individually. Recommend a Jira ticket. Still to check: whether the liked listing shows on the public Tag page after unlinking, and whether removing the like takes it out of the Tag.
- Resolved October 18, 2026 (Tara's test): removing the reaction took the listing out of the Tag and lowered the count. The draft says the listing stays until the contact removes the reaction. Tara tested as both the client and the agent; removing the reaction worked either way. The agent removes it on the Tag's public page (Tara, October 18, 2026). Tara also confirmed the hide route with a reaction: a liked saved search listing stays in the Tag after it is hidden and the search saved, and leaves once the like is removed. Original marker was `[confirm: how to remove a saved search listing a contact liked or disliked]`. A reviewer noted on October 18, 2026 that changing the search's filters cannot remove it, since reacted listings stay after they stop matching. One test answers both markers: on a Tag with a contact, like one listing that comes from a saved search, unlink that search, click Save, and check whether the listing is still under Listings and notes.
- Tara is confirming with the team whether there is a limit on how many saved searches or listings one Tag can hold. The draft states no limit.
- Saved searches a client created or edited do not appear in the Add saved search list. Tara thinks this may be a bug and is confirming; the draft says nothing about it.
- The pencil icon on each card in the Add saved search window edits the saved search ("Manage saved search contacts and their alert preferences by editing the search"). Left out: what it opens has not been checked, and the window's own text covers it.
- Cut from the live article: "Filters you've added just for your own tracking stay visible to you only, even if the search is shared." It belongs to saved search sharing, not Tags.
- Video: the live Loom (ac5b7a3c722f4cd88ef0e26bbf758bb8) shows the old window. Replaced with a video placeholder.
- Set: How to Tag Individual Listings has its own "Synchronize your Tags page with the listings in a Saved Search" section that duplicates this article; cut it to a link in that rewrite. Create and Edit a Tag said "connect" for linking a saved search; changed to "link" on October 18, 2026, as Tara confirmed. Its link text still reads "How to Link a Saved Search to a Tag" and should follow the new title at port.
- Removing one saved search listing: Tara confirmed October 18, 2026 that hiding the listing in the saved search and saving the search removes it from the Tag right away; without saving, it stays in both the search and the Tag. There is no remove option on the Listing Detail Page or the public Tag page. This replaced "change the search's filters to exclude it". The link to Actions Menu Options on the Search Page uses the live URL (13623271), which still shows the old Multi-Listing Actions article until that draft is ported.
- Tracker ID: TRK-097 (Tara, October 18, 2026). Added to the Production Tracker the same day with Article, Visual, and Video Due set to October 22, 2026; reviewer and visual owner copied from Create and Edit a Tag.
- MLS: the live article is Baldwin only; Tara scoped the draft to Baldwin and CRMLS.
