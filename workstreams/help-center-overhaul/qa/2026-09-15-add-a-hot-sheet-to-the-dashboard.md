# QA: Add a Hot Sheet to the Dashboard

## Article and sources

- **Article name:** Add a Hot Sheet to the Dashboard
- **Old title:** unchanged. Already task-led and matches the naming standard
- **Article type:** Workflow
- **Old Notion page:** https://app.notion.com/p/1c88b9e014388069925acd9f0fe35189 (Master Article List, read only)
- **Intercom article ID:** 13893409 | **Content ID:** 16137563
- **Mirror path:** `docs/help-center/baldwin/add-a-hot-sheet-to-the-dashboard.md`
- **Shared across help centers:** no. Article 13893409 appears in `baldwin/` only. CRMLS has its own, `Adding a Hot Sheet to the Dashboard`
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-09-15-add-a-hot-sheet-to-the-dashboard-rewrite.md`
- **Notion draft:** https://app.notion.com/p/3dc8b9e01438815891e6ccd033eccf97

Scored by Claude for Tara, September 15, 2026, using the **September 10, 2026 check set, revision 2**.

**Source precedence, and a first.** The live article was updated 2026-07-20 at 22:43; the old Notion page was last edited the same day at 20:12. **The live article is the newer source by two and a half hours**, so for the first time in this run the standard's rule and the dates agree. On the two Dashboard articles they pulled against each other and the rule was right; here nothing had to be broken. The mirror was synced the previous day, and this article was not among the four that changed, so the baseline is current.

The row is flagged `Text: Update Required`, `Screenshot: Update Required`, and `Video: Update Required`, so CS already considered the whole article due for work.

## Source differences and how each was resolved

| Fact | Live article | Old Notion page | Resolution |
|---|---|---|---|
| Hot Sheet types | "property type, timeframe, and status"; Saved Search tracks "new listings, price changes, and status updates" | drops timeframe; Saved Search is just "listing activity" | **Live.** Newer and more specific on both counts |
| When to use | 3 situations | 5, adding "across the overall MLS" and "for a specific city or property type" | **Merged.** The two extra situations are additive, not contradictory |
| New Hot Sheet scope | "by property type" | "by property type **or location**" | **Live**, confirmed by Tara. Baldwin cannot filter by location; only CRMLS can |
| Widget setup | 4 steps | 5, the last naming the two types | **Live.** Notion's fifth step duplicates the two sections that follow. Kept as a one-line bridge after the steps instead |
| New Hot Sheet video | `demo.arcade…hEIjX3Ev` | `app.arcade…SINhoyOb` | **Notion**, per the migration rule that the old page supplies the video link. Two different recordings; see Open items |
| Saved Search video | `demo.arcade…1EP0inuZ` | `app.arcade…1EP0inuZ` | Same recording, different host. Used the `app.arcade.software/share/` form, matching the row's `Video Links` |
| What a Hot Sheet does once built | absent | "click into the bars to see the listings" | **Notion**, corroborated by `baldwin/hot-sheets.md` and `crmls/the-dashboard-page-overview.md` |
| Time frame cap | "2+ years" in Tips | absent | **Neither.** Replaced with the exact figure, 998 days, from `baldwin/dashboard-faq.md` |

## Corrections from a product screenshot, September 15, 2026

Tara sent a screenshot of the Dashboard with the Manage widgets panel open, a new Hot Sheet widget mid-setup, and two finished Hot Sheets. It corrected four things and added one fact no source had.

**Both button labels are lowercase.** The chooser reads **New hot sheet** and **From saved search**, not the title-cased forms every written source uses. This is the third label the live articles capitalize and the product does not, after Manage widgets and Add hot sheet.

**"Quick hot sheet" is Baldwin vocabulary, not CRMLS-only.** The two finished widgets are subtitled **Quick hot sheet** and **Saved search hot sheet**. The draft had dropped that term on the reasoning that it came from CRMLS's article, which was wrong: there are two naming layers, the buttons a member clicks and the label the resulting widget carries. The old Notion page's "New Hot Sheet (Quick Hot Sheet)" formulation was right about this and the first draft discarded it. Sections are now named for the type, so a member looking at a widget labeled Quick hot sheet finds the phrase, and the steps name the button.

**The time frame is a typed field, and the tabs are member-set.** The screenshot shows different tab sets on the two widgets, 1/7/30/45/60 on one and 1/3/7 on the other, which looked like fixed presets that varied by type. Tara confirmed the opposite: the time frame is a text field accepting up to 998 days, and every tab on a Hot Sheet is a time frame the member configured. So the Dashboard FAQ's 998-day figure is correct, the step now says to type it, and the tabs are described in Things to Know as what they are.

**The product has a better definition than the draft did.** The setup card reads "Hot sheets show market events for a saved search or custom market segment." The draft said "monitors listing changes". The opening now uses the product's wording, and "market events" is what the widget rows actually are: Coming soon, Listed, Price incr., Price drop, Pending, Closed, Expired, Off market.

The screenshot also confirms the payoff added during the rewrite. Each Hot Sheet row is a counted, clickable bar, so "click one of its bars to open the listings behind it" is now visible rather than inferred from three text sources.

**Location filtering was left out, and Tara confirmed that was right.** The Notion page says a New Hot Sheet filters "by property type or location", and CRMLS's article says "by property type or location, **depending on the MLS**". The live Baldwin article says property type only, and its steps have no location step. Tara confirmed on September 15 that **Baldwin cannot filter a quick hot sheet by location; only CRMLS can.**

This is the one case in the four migrations where a decision to leave something out was later confirmed correct. The three factual errors before it all came from inferring a capability in. The signal that worked here was the hedge in the corroborating source itself: "depending on the MLS" is a source telling you it does not know about your MLS, and it was worth more than the two sources that stated the capability flatly. A location step is needed if this article is ever adapted for CRMLS.

**Button labels corrected from the product.** The live article says "Manage Widgets" and "Add Hot Sheet"; Tara's screenshot of the panel on September 14 shows **"Manage widgets"** and **"Add hot sheet"**. The draft uses the on-screen forms.

Dropped per the migration rules: the `In this article:` heading, the Click Script toggle, the trailing Perchwell banner image, horizontal rules, and the emoji-led callout.

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1. disambiguation | Pass | Pass | Neither uses emoji as a pointer in the live body |
| 2. visual_content_text | Pass | Pass | No images in either. Two walkthrough videos, one per setup flow |
| 3. undefined_terms | Pass | Pass | Both define a Hot Sheet on first use |
| 4. structured_enumeration | Pass | Pass | Both use numbered steps and bullets |
| 5. query_answer_symmetry | Fail | Pass | Live headings "Hot Sheet types", "Hot Sheet widget setup", "New Hot Sheet setup" are bare noun phrases. New headings are task-led |
| 6. self_contained_sections | Pass | Pass | Neither points backward. Both name the Hot Sheet widget as the surface each flow starts from |
| 7. audience_specification | Pass | Pass | No role gates this workflow, so silence passes |
| 8. entity_distribution | Pass | Pass | Hot Sheet appears in every section of both |
| 9. semantic_chunk_boundaries | Pass | Pass | One topic per section in both |
| 10. restate_questions | Pass | Pass | No tables. The situations list carries a lead sentence |
| 11. overview_jtbd | Fail | Pass | Live body has no opening paragraph; its description opens "In this article, you will learn how to" |
| 12. instruction_completeness | Fail | Pass | Live sets out three procedures and none says what it produces. Both setup flows stop at the save click. All three new Steps blocks end with an outcome |
| 13. limitations_workarounds | Pass | Pass | Both state the time frame cap and the mobile constraint |
| 14. numerical_clarity | Fail | Pass | "2+ years" is the only quantity in the live article and it is vague. Now 998 days |

**Old gate:** failed on 4 factors (5, 11, 12, 14).
**New gate:** all 14 pass, with no open confirm markers.

## Dimension scores

Revision 2 of the September 10, 2026 check set.

| Dimension | Weight | Old | New | Delta |
|---|---|---|---|---|
| Retrieval signals | 30 | 17.1 (4/7) | 30.0 (7/7) | +12.9 |
| Chunk independence | 25 | 16.7 (4/6) | 25.0 (6/6) | +8.3 |
| Answer completeness | 25 | 10.7 (3/7) | 25.0 (7/7) | +14.3 |
| Fin-parsable formatting | 10 | 7.5 (6/8) | 10.0 (8/8) | +2.5 |
| Accuracy and confidence | 10 | 8.0 (4/5) | 10.0 (5/5) | +2.0 |
| **Total** | **100** | **60.0** | **100.0** | **+40.0** |

| | Old | New |
|---|---|---|
| Score | 60.0 | 100.0 |
| Band | Needs rewrite | Fin-ready |
| Gate | Failed, 4 factors | Passed |

### Checks the old article failed

- **Retrieval signals:** description runs 163 characters, over Intercom's 140 cap; no opening paragraph; three headings are bare noun phrases; two sections jump from heading straight to `Steps:` with no lead sentence
- **Chunk independence:** every section is an H1, competing with the title; the "Hot Sheet types" section enumerates the two types and each setup section then describes its type again, so one of the two is doing no work
- **Answer completeness:** none of the three procedures says what it produces; no "which means" clause; the article links to nothing at all, despite the whole Saved Search flow depending on a Saved Search the member has to build first
- **Fin-parsable formatting:** bold on every UI element; "The new Hot Sheet widget appears on your Dashboard" is an outcome written as a numbered step
- **Accuracy and confidence:** "Hot Sheets let you monitor listing changes" is the "allows you to" construction in another form

## Facts confirmed in the product by Tara, September 15, 2026

- Both setup flows end with the same control, **Confirm**. The live article's "Save your Hot Sheet" was loose wording for it
- After Confirm, the Hot Sheet fills in on the Dashboard with matching activity, in place
- The time frame is a text field accepting up to 998 days. The tabs across the top of a finished Hot Sheet are time frames the member configured, not a fixed set, and they differ between Hot Sheets for that reason
- Baldwin cannot filter a quick hot sheet by location. Only CRMLS can, which is why the draft has no location step

## What the rewrite added that no version had

- **The outcome of the whole workflow.** Neither source said what a member does with a Hot Sheet once built. Clicking a bar to open the listings behind it now sits in "When to use a Hot Sheet", sourced from the Notion page and corroborated twice
- **Why a Hot Sheet beats a search.** It updates automatically from current MLS data, which is the reason to build one and appeared in neither version of this article
- **Links.** The live article linked to nothing. The draft links Manage Your Saved Searches from the flow that depends on one, plus Dashboard FAQ and Customize Your Dashboard

## Fin test questions

| Question a member may type | Old answers from one section | New answers from one section |
|---|---|---|
| How do I add a Hot Sheet to my Dashboard? | Partly. The steps are there but nothing says what the result is | Yes. "Add a Hot Sheet widget to the Dashboard" |
| What is the difference between the two Hot Sheet types? | Partly. Split across "Hot Sheet types" and two setup sections | Yes. Each setup section's lead states its type |
| How do I make a Hot Sheet from a saved search? | Partly. Steps stop at the save click | Yes. "Set up a Hot Sheet from a Saved Search" |
| How far back can a Hot Sheet go? | No. "2+ years" is vague and sits in Tips | Yes. "Things to Know", 998 days |
| What do I do with a Hot Sheet once I have made one? | No | Yes. "When to use a Hot Sheet" |
| Does a Hot Sheet update on its own? | No | Yes. "When to use a Hot Sheet" |
| Why should I use a Hot Sheet instead of just searching? | Partly | Yes. "When to use a Hot Sheet" |
| Can I set up Hot Sheets on my phone? | No | Yes. "Things to Know" |

## Open items

**Confirm markers in the draft:** none.

**Decisions the team owes**

- **Two different Arcade recordings for the New Hot Sheet flow.** The live article embeds `demo.arcade.software/hEIjX3EvfRviX1ElurDi`; the Notion page and the row's `Video Links` give `app.arcade.software/share/SINhoyObS2qHu9aF1HE0`. The draft carries the Notion one per the migration rule, but `Video: Update Required` on the row suggests both may be stale. Someone should confirm which recording ships, for both flows
- **Widget naming is inconsistent across the migrated set.** This article and the live one say "Hot Sheet widget", singular. The Dashboard Overview draft says "Hot Sheets widget", plural, in a heading. One term across the set is what lets Fin match either phrasing; worth settling before transfer. The September 15 screenshot does not settle it, since it shows the two finished widgets labeled by type rather than a generic widget name
- **`Screenshot: Update Required`, but the article has no images.** The draft carries none either, since both setup flows have a walkthrough video. Worth confirming that a video is considered sufficient for this article rather than a missing screenshot
- **Seven of the eight outbound and self links use the default help center path** (`support.perchwell.com/en/...`) rather than `/baldwin/en/...`, because that is how the mirror records them. Flag at Intercom transfer

**Universality**

The old row marks this article `CRMLS?: 100% Applicable` and `NYC?: 100% Applicable`, but CRMLS has its own version, `Adding a Hot Sheet to the Dashboard`, which differs in two ways that matter: it names the types "Quick Hot Sheets" and "Saved Search Hot Sheets", and it caps a Dashboard at **5 Hot Sheets** where Baldwin's FAQ says there is no limit. This draft is Baldwin's. Per Tara on September 14, no CRMLS articles are being edited yet.
