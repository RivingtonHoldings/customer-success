# QA: Customize Your Dashboard

## Article and sources

- **Article name:** Customize Your Dashboard
- **Old title:** unchanged. Already task-led and matches the naming standard
- **Article type:** Workflow
- **Old Notion page:** https://app.notion.com/p/1c88b9e0143880318717f94e2d8335e9 (Master Article List, read only)
- **Intercom article ID:** 13623904 | **Content ID:** 15696089
- **Mirror path:** `docs/help-center/baldwin/customize-your-dashboard.md`
- **Shared across help centers:** no. Article 13623904 appears in `baldwin/` only. CRMLS has a separate article on the same subject, `Customizing your Dashboard`, ID 10159813
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-09-14-customize-your-dashboard-rewrite.md`
- **Notion draft:** https://app.notion.com/p/3db8b9e01438819b95c4f80b6b719fae

Scored by Claude for Tara, September 14, 2026, using the **September 10, 2026 check set, revision 2**.

**Mirror refreshed first.** The mirror was 10 days old, past the one-week threshold in the sync skill, so `/sync-help-center` ran before scoring. Baldwin picked up 1 new and 3 updated articles; CRMLS was unchanged. Customize Your Dashboard itself was unchanged, so the before-baseline is the current live article.

**Source note.** As with Dashboard Overview, the old Notion page is newer than the live article: Notion last edited 2026-07-17, live article 2026-07-02, with `Update Status: Transfer to Intercom`. A revision was written and never pushed. Notion wins on the facts it states; the mirror wins on the mobile constraint that the Notion revision dropped.

## Source differences and how each was resolved

| Fact | Live article | Old Notion page | Resolution |
|---|---|---|---|
| Arcade walkthrough | `demo.arcade.software/pgyIXO3DO8xMCsDYNahj` | `app.arcade.software/share/4DI3IhHDnSC1ad96xd8h` | **Notion.** A different, newer video, and the row reads `Video: Done` |
| Widgets in Manage Widgets | Hot Sheets, Contacts, Saved Searches, Tags | Hot Sheets, **Listings**, Contacts, Saved Searches, Tags | **Live article**, confirmed by Tara. The first draft took Notion, since CRMLS also lists Listings, and that was wrong. See below |
| Listings widget restriction | "cannot be removed or reordered" | "cannot be removed" | **Live article**, confirmed by Tara in the product. See below |
| Mobile constraint | stated | absent | **Live article.** Corroborated by `baldwin/dashboard-faq.md` |
| Listings widget link | Intercom 13903171, link text "in this article" | a Notion page | **Neither.** Repointed to the same article with its real title, `Listings Widget Overview` |

Dropped per the migration rules: the `In this article:` heading, the Click Script toggle, the trailing Perchwell banner image, horizontal rules, and the two emoji-led callouts.

**The reorder question was close and worth recording.** "Cannot be removed **or reordered**" appears in exactly one source, the live Baldwin article. Four sources mention only removal: the newer Notion revision of this same article, CRMLS's equivalent twice, and CRMLS's Listings widget article. The four-to-one majority was wrong. Tara confirmed in the product that the Listings widget cannot be reordered either, so the lone outlier was right and the Dashboard Overview draft, which asserts the same restriction, needed no change.

## Corrections from a product screenshot, September 14, 2026

Tara sent a screenshot of the Manage widgets panel. It corrected three things the written sources all had wrong, and it is the clearest evidence yet that no document in this repo is authoritative about the product.

**Hot Sheets is not a checkbox.** The panel holds an `Add hot sheet` action above a divider, then checkboxes for Contacts, Saved Search, and Tags. The draft had listed Hot Sheets among the toggleable widgets and told the member to check a box that does not exist. The section now describes the two controls separately, and Hot Sheets gets its own sentence routing to `Add a Hot Sheet to the Dashboard` rather than a third step, because it is a different mechanism with a different outcome and the green-confirmation line covers only the checkboxes.

**The button reads "Manage widgets", with a lowercase w.** Eight of the nine places the phrase appears across the Baldwin and CRMLS mirrors write it "Manage Widgets"; one writes it correctly. All eight are wrong. The draft used the capitalized form five times and now uses the on-screen one.

**The panel item reads "Saved Search", singular**, where the draft said "Saved Searches". The widget is still the Saved Searches widget elsewhere; the panel label is singular. Worth knowing that this is a product inconsistency rather than a writing choice.

**What this says about the sources.** Across this article and Dashboard Overview, the count is now five factual errors, every one of them sourced. Two came from preferring the newer Notion page, one from a majority of articles agreeing with each other, and three from the screenshot above. The only things that caught any of them were Tara checking the product and Tara sending a picture of it. The source-precedence rule added to `content-standards.md` on September 14 covers the first two; nothing in the standard or the scorecard covers the rest, because the failure is that written sources copy each other and drift together.

**Resolved, September 14, 2026.** Tara confirmed that Add hot sheet produces no green confirmation. The widget is added automatically, with no save step. So the panel behaves two ways: checking a box shows a green confirmation reading Widget added or Widget removed, and clicking Add hot sheet shows nothing at all.

The draft states the absence rather than staying silent on it, because the article tells the member to expect a confirmation two paragraphs earlier. Leaving it out would set up a member to click Add hot sheet and wonder whether it worked. This is the one place in these articles where naming what does not happen earns its place.

**Passage tightened on Tara's wording, September 14, 2026.** She proposed a version and asked whether it held up against the standard. It did, and it is better on two counts. "With nothing to save" was cut from both paragraphs: "updates as soon as you check" and "added immediately" already carry it, so the phrase was restating its own sentence. The related-article link moved to its own paragraph, which separates adding the widget from configuring the Hot Sheet inside it; those are different tasks and the model articles put such links in their own sentence anyway.

One change to her version. "Unlike other widgets, no confirmation message appears" became "Unlike the checkboxes", because the Listings widget is also an other widget and shows no confirmation either, having no add or remove behavior at all. The checkboxes are the thing that actually contrasts, and the phrase is shorter for being precise.

No check moves. Answer completeness check 3 still passes: system behavior is still stated, and the article's "which means" clause lives in the filter section. The score holds at 100.0.

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1. disambiguation | Fail | Pass | Two emoji-led callouts, one of them pointing at a link whose text is "in this article". New article has no emoji and names the linked article by title |
| 2. visual_content_text | Pass | Pass | Live article carries no images, so nothing is missing alt text. Two screenshots exist on the Notion page and were never transferred. New article carries two placeholders with their alt text |
| 3. undefined_terms | Fail | Pass | Live article never says what a widget is. New opening defines it as a tile that displays one kind of information |
| 4. structured_enumeration | Fail | Pass | Live article describes both procedures in flowing prose. New article has two numbered Steps blocks |
| 5. query_answer_symmetry | Pass | Pass | The live headings were already task-led and carried the feature name, which is unusual for a pre-standard article |
| 6. self_contained_sections | Pass | Pass | Neither article points backward. New steps restate where Manage Widgets sits |
| 7. audience_specification | Pass | Pass | No role gates this workflow, so silence passes under the house resolution |
| 8. entity_distribution | Pass | Pass | Both carry Dashboard and widget through every section |
| 9. semantic_chunk_boundaries | Fail | Pass | Live article combines reordering and filtering in one section, which are different jobs. New article splits them |
| 10. restate_questions | Pass | Pass | No tables in either. The widget list carries an intro line |
| 11. overview_jtbd | Fail | Pass | Live body has no opening paragraph; the description opens "In this article, you will learn how to" |
| 12. instruction_completeness | Fail | Pass | Live article never says what happens after a widget is checked or a layout is dragged. Both new Steps blocks end with the outcome, confirmed by Tara in the product |
| 13. limitations_workarounds | Pass | Pass | Both state the Listings restriction and the mobile constraint specifically, with the route forward |
| 14. numerical_clarity | Pass | Pass | Neither states a vague quantity |

**Old gate:** failed on 6 factors (1, 3, 4, 9, 11, 12).
**New gate:** all 14 pass, with no open confirm markers.

## Dimension scores

Revision 2 of the September 10, 2026 check set.

| Dimension | Weight | Old | New | Delta |
|---|---|---|---|---|
| Retrieval signals | 30 | 21.4 (5/7) | 30.0 (7/7) | +8.6 |
| Chunk independence | 25 | 16.7 (4/6) | 25.0 (6/6) | +8.3 |
| Answer completeness | 25 | 10.7 (3/7) | 25.0 (7/7) | +14.3 |
| Fin-parsable formatting | 10 | 5.0 (4/8) | 10.0 (8/8) | +5.0 |
| Accuracy and confidence | 10 | 8.0 (4/5) | 10.0 (5/5) | +2.0 |
| **Total** | **100** | **61.8** | **100.0** | **+38.2** |

| | Old | New |
|---|---|---|
| Score | 61.8 | 100.0 |
| Band | Needs rewrite | Fin-ready |
| Gate | Failed, 6 factors | Passed |

This is the highest starting score of the three articles migrated so far. Its headings were already task-led and its constraints were already specific, which is why retrieval signals started at 21.4 rather than the 4.3 and 10.0 of the other two. The gain is concentrated in Answer completeness, where the live article documents two procedures without ever saying what either one produces.

### Checks the old article failed

- **Retrieval signals:** description runs 152 characters, over Intercom's 140 cap; no "Use this article to" opening paragraph in the body
- **Chunk independence:** every section is an H1, competing with the title; reordering and filtering share one section with no H3 split
- **Answer completeness:** neither procedure says what happens after the last action; no "which means" clause anywhere; "widget" is never defined; the Listings widget link reads "in this article", which is the banned vague form
- **Fin-parsable formatting:** both procedures are prose rather than numbered lists; two callouts are emoji-led with no bold label; bold is applied throughout the body
- **Accuracy and confidence:** "You can only view and access these areas on desktop" uses "you can"

## Facts confirmed in the product by Tara, September 14, 2026

Neither is documented anywhere in the repo, so both are recorded here for traceability.

- Checking or unchecking a widget in Manage Widgets applies immediately, with no save step. A green confirmation appears at the bottom of the screen reading Widget added or Widget removed
- A reordered layout saves automatically and persists the next time the member opens the Dashboard
- The Listings widget cannot be reordered, resolving the four-to-one source conflict above
- The Listings widget does not appear in Manage widgets at all, because it cannot be added or removed
- The panel holds an Add hot sheet action plus three checkboxes, for Contacts, Saved Search, and Tags. Hot Sheets is not a checkbox
- Clicking Add hot sheet adds the widget automatically, with no confirmation message and no save step

**Correction made September 14, 2026.** The first version of this draft listed five widgets in Manage Widgets, including Listings, taken from the old Notion page and corroborated by CRMLS's equivalent. Tara caught it: the Listings widget is not in the panel, because it cannot be toggled. The section lead now reads "These widgets can be turned on and off", the list is four, and the Note explains the absence rather than stating a restriction about a widget the member cannot find in that panel. The screenshot alt text was corrected too.

**Two source conflicts on this one article, and the live Baldwin article won both.** It was right that the Listings widget cannot be reordered, against four sources that mentioned only removal. It was right that the panel holds four widgets, against two sources that said five. Both times the draft had followed the newer Notion page or the numerical majority.

**The scorecard cannot catch this class of error, and it is worth being explicit about that.** Accuracy check 1 asks whether every fact traces to a source; each of these did. Check 2 asks whether unknowns are marked; these were not unknowns, they were sourced and wrong. The scorecard measures retrievability and sourcing discipline, not whether the source told the truth. Only a product check does that. The score is unchanged at 100.0 before and after this correction, which is exactly the blind spot.

## Fin test questions

| Question a member may type | Old answers from one section | New answers from one section |
|---|---|---|
| How do I add a widget to my Dashboard? | Partly. The instruction is prose with no steps and no outcome | Yes. "Choose which widgets display on the Dashboard" |
| Which widgets can I put on my Dashboard? | Partly. The live list is correct but reads as prose with no context on why Listings is absent | Yes. "Choose which widgets display on the Dashboard", which also explains why Listings is not in the panel |
| How do I remove a widget I don't use? | Partly. Same prose passage, no confirmation described | Yes. "Choose which widgets display on the Dashboard" |
| Why can't I remove the Listings widget? | Yes, in an emoji callout | Yes. "Choose which widgets display on the Dashboard", as a **Note:** |
| How do I change the order of my widgets? | Partly. Mixed into a section that also covers filtering | Yes. "Reorder your Dashboard widgets" |
| Will my Dashboard layout stay how I set it? | No | Yes. "Reorder your Dashboard widgets" |
| How do I filter what a widget shows? | Partly. Same mixed section | Yes. "Filter what a Dashboard widget shows" |
| Can I customize my Dashboard on the mobile app? | Yes. "Things to Know" | Yes. "Things to Know" |

## Open items

**Confirm markers in the draft:** none.

**Decisions the team owes**

- **The Arcade walkthrough changed.** The live article embeds `demo.arcade.software/pgyIXO3DO8xMCsDYNahj`; the newer Notion revision embeds `app.arcade.software/share/4DI3IhHDnSC1ad96xd8h`. The draft carries the Notion one because the row reads `Video: Done`, but somebody should confirm the newer recording is the one to publish
- **The Manage widgets screenshot has been captured.** Tara took it on September 14, 2026: the Dashboard with the Manage widgets button called out in the top right and the panel open below, with the Listings widget visible behind. Its placeholder now describes that exact capture and carries matching alt text, so the image only needs dropping into the Notion draft. It cannot be uploaded from a chat paste; it needs the file. **The same capture also fits the Manage widgets placeholder in Dashboard Overview**, so one image covers both articles
- **One screenshot still outstanding:** a widget with its filter control open, for the Filter section
- **Two older screenshots exist on the old Notion page** and were never transferred. The old row reads `Screenshot: Done`, which refers to those rather than anything live. Worth checking whether they are superseded by the new capture
- **The new capture carries a red callout arrow.** Whether annotation of that kind matches the Figma-approved screenshot specs is a question for the visual pass, not a content question
- **The green confirmation's exact wording.** Tara described it as reading Widget added or Widget removed. The draft uses sentence case; worth checking against the screen when the screenshots are captured
- **The old row's MLS update note says:** "We would need to make a decision that we can show the listings from a MLS in the video." A video decision, not a content one, but it is unresolved
- **Seven of the nine outbound and self links use the default help center path** (`support.perchwell.com/en/...`) rather than `/baldwin/en/...`, because that is how the mirror records them. Flag at Intercom transfer

**MLS/AOR changed to Baldwin and CRLMS All, September 14, 2026**

Tara set the Notion row to both MLSs after the draft was written. The body is still Baldwin's. Two things in it are known not to hold for CRMLS:

- **The widget list.** This draft says the panel holds an Add hot sheet action plus checkboxes for Contacts, Saved Search, and Tags, confirmed from a Baldwin screenshot. `crmls/customizing-your-dashboard.md` lists seven available widgets, adding Presentations and Days on Market. Presentations is gone from CRMLS, so that article is stale, but Days on Market is a real CRMLS widget Baldwin does not have
- **The mobile constraint** in Things to Know traces to Baldwin sources only

CRMLS also already has its own article on this subject, `Customizing your Dashboard`, ID 10159813. Publishing this one to both help centers means deciding what happens to that row.

Nothing is wrong with the draft as a Baldwin article. It is only wrong as a CRMLS one, and the property now says it is both.

**Universality**

The old row marks this article `CRMLS?: 100% Applicable` and `NYC?: 100% Applicable`, but CRMLS already has its own separate article on the subject, `Customizing your Dashboard`, ID 10159813, whose widget list runs to seven and includes Presentations and Days on Market. Two things follow:

1. The widget list in this draft is Baldwin's five. A shared body would need that list handled per MLS, exactly as the Dashboard Overview widget question did
2. If the intent is one article for both, the CRMLS row is the one to deprecate, and that is a decision rather than a rewrite

The mobile constraint carries the same caveat as in Dashboard Overview: it traces to Baldwin sources only, and `docs/product-context.md` claims web and mobile parity.
