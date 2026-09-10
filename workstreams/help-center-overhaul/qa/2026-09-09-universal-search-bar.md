# QA scorecard: Universal Search Bar

Scored with `docs/standards/fin-readiness-scorecard.md`. First article through the migration path, and the article whose team review produced the September 10, 2026 revisions to the standard.

Every score below uses the **September 10, 2026 check set**: Chunk independence carries six checks rather than five, and two Answer completeness checks were reworded. Scores recorded before that date are not directly comparable.

## Article and sources

- Title: Universal Search Bar (unchanged). The task-led alternative "Find a Listing, Agent, or Contact with the Universal Search Bar" was proposed and Leo chose to keep the existing title on 2026-09-09
- Old Notion page: https://app.notion.com/p/1c78b9e0143880f3b927daf7d2aca4d5 (Master Article List, last edited 2026-07-17, read only)
- Intercom article 11002620, content ID 11821319, updated 2026-08-10, label `How To: Search`
- Mirror: `docs/help-center/baldwin/universal-search-bar.md` and `docs/help-center/crmls/universal-search-bar.md` (shared into both help centers)
- Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-09-09-universal-search-bar-rewrite.md`
- Notion Draft in the Perchwell Help Center Database [Sep 2026]: https://app.notion.com/p/3d68b9e01438810cb386f3ea550d097c (updated 2026-09-10 with the rewritten body; `Article Status` still `Draft`)
- Scored by Claude for Leo Jedynak, 2026-09-09. Rescored 2026-09-10 after Tara's review, and again the same day after a second review narrowed the article's scope.

## What the review changed

The team read the September 9 draft and returned four points: use MLS ID rather than MLS number, cut role-access language that says nothing, stop leading with what the feature will not do, and keep the structure Fin needs without repeating the same facts. Three of the four traced to the standard rather than to the draft: the standard required an audience statement, made a Limitations section the default, and had no rule against restating facts. The standard, the scorecard, and both skills were revised on September 10 and the draft was rewritten against them.

A second pass the same day narrowed the scope. The first rewrite answered the "where do I go instead" question with three routes to the **Search** page, which turned a lookup article into a Search-page article. Tara cut it to one pointer. The section heading "Open the Universal Search Bar and start a search" was also wrong on the facts: the Universal Search Bar looks a record up and opens it, and no search starts there. It is now "Look up a record with the Universal Search Bar", and it carries the multi-MLS-ID answer, since that is the section a member asking it would land in. Its lead sentence states the every-page behavior as what the member gets rather than what they avoid.

## Source differences (live wins)

| Where | Old Notion page (July 17) | Live article (August 10) | Draft |
|---|---|---|---|
| Listings bullets | Exact address returns a direct match | Bullet dropped | Kept as `[confirm: ...]` |
| Tips | Three bullets | Adds "If you hear Power Search, it refers to the Universal Search Bar" | Merged into one neutral Things to Know bullet |
| Body extras | Click Script toggle, Loom embed, Perchwell banner image | None | Loom kept under the opening; script and banner dropped |
| Headings | H2 with horizontal rules | H1 with horizontal rules | H2 and H3, no rules |
| Images | Two Notion uploads, no alt text | Two Intercom CDN images, no alt text | Live images kept with alt text |
| Identifier | "MLS number" | "MLS ID" at the top, "MLS number" in the body | MLS ID throughout, per the terminology rule added 2026-09-10 |

## Golden questions (gate)

| Factor | Live | Draft | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | Live used a decorative emoji, not a pointer |
| 2 visual_content_text | Fail | Pass | Both images had no alt text; both now describe the screen |
| 3 undefined_terms | Pass | Pass | MLS ID is the settled term and needs no gloss; the September 9 draft's "MLS number (the listing's MLS ID)" parenthetical is gone |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Pass | Pass | Live "Tips" is the sanctioned closing heading; draft headings all carry the feature name |
| 6 self_contained_sections | Fail | Pass | Live Tips said "this feature" with no name in the section |
| 7 audience_specification | Pass | Pass | Read through the house resolution: no role gates this feature, so silence passes. The September 9 draft failed it by claiming every member role has the feature and marking that claim unconfirmed in the same sentence |
| 8 entity_distribution | Pass | Pass | The feature name appears in every section. The September 9 draft repeated the listings/agents/contacts enumeration six times, which the house resolution now names as the wrong reading of this factor |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables in either |
| 11 overview_jtbd | Fail | Pass | Live had no opening paragraph; description said "In this article, you will learn" |
| 12 instruction_completeness | Fail | Pass | Live steps stopped at typing; draft steps end at the opened record |
| 13 limitations_workarounds | Fail | Pass | Live said "not saved or filtered searches" with no route forward. The draft points once at Create a Search with Filters for criteria-based searching and has no Limitations section |
| 14 numerical_clarity | Pass | Pass | No numbers needed |

Gate: the live article fails 4 of 14 under the house resolutions. The draft passes 14 of 14, with five `[confirm: ...]` markers a reviewer must resolve before transfer (see Open items).

## Dimension scores

All three columns on the September 10 check set, so the middle column shows what the review caught.

| Dimension | Weight | Live article | Sept 9 draft | Sept 10 draft |
|---|---|---|---|---|
| Retrieval signals | 30 | 10.0 (2 of 6) | 25.0 (5 of 6) | 25.0 (5 of 6) |
| Chunk independence | 25 | 12.5 (3 of 6) | 20.8 (5 of 6) | 25.0 (6 of 6) |
| Answer completeness | 25 | 14.3 (4 of 7) | 14.3 (4 of 7) | 21.4 (6 of 7) |
| Fin-parsable formatting | 10 | 4.3 (3 of 7) | 10.0 (7 of 7) | 10.0 (7 of 7) |
| Accuracy and confidence | 10 | 10.0 (4 of 4) | 7.5 (3 of 4) | 10.0 (4 of 4) |
| **Total** | 100 | **51.1** | **77.6** | **91.4** |

Bands: live, Needs rewrite. September 9 draft, Ready with fixes. September 10 draft, Fin-ready, gate passed.

Failed checks, live: title is a bare noun; no "Use this article to" opening; two of three headings lack the feature name; first sentences do not echo every heading; "this feature" in Tips depends on context; body headings at H1; the same enumeration appears in two sections; no "which means" clause; the stated limit has no route forward; no related links; emoji-led tip with no bold label; no alt text; horizontal rules in the live HTML.

Failed checks, September 9 draft: chunk independence 6 (the listings/agents/contacts enumeration in three consecutive sections); answer completeness 2 (an unverified claim that every member role has the feature); answer completeness 4 (a Limitations section for three constraints, none of which is a hard cap or irreversible); accuracy 2 (the availability claim was a guess carrying its own confirm marker); plus the two below.

Failed checks, September 10 draft: retrieval signals 1 (the title stays a bare noun by Leo's choice; the description and opening carry the task words instead) and answer completeness 3 (the article does not say what the Universal Search Bar shows when nothing matches, because neither source does; marked `[confirm: ...]`).

## Fin test questions

Questions members may ask, in their words. "One section" means Fin can answer from a single retrieved section without stitching.

| Question a member may ask | Live article, one section | Draft, one section |
|---|---|---|
| How do I look up a listing by MLS ID? | Yes | Yes |
| Where is the search bar to find an agent? | Partly (says "top of your screen") | Yes (Search field, upper right of the top navigation) |
| Can I search for a contact by email? | Yes | Yes |
| What happened to Power Search? | Yes | Yes, with a link to New Terminology |
| Can I search several MLS IDs at once in the top search bar? | No | Yes, from Look up a record, with the MLS ID filter route and a link |
| Does the search bar show closed or expired listings? | Yes | Yes, with what the status badge looks like |
| How do I save the search I typed in the top bar? | No (says it is not for saved searches, no next step) | No, by decision (see coverage note) |
| How do I filter by price? | No | Yes, from When to use, links Create a Search with Filters |

**Coverage note.** Scope was cut on 2026-09-10 to keep the article on the Universal Search Bar, then the multi-MLS-ID answer was put back into the Look up a record section, where a member asking it would land. Saving a search is the one question that left: [Manage Your Saved Searches](http://support.perchwell.com/en/articles/8955646-manage-your-saved-searches) is its proper home, and Fin testing should confirm it retrieves from there rather than from this article.

## Open items

- [confirm: whether Active, Pending, Closed, and Expired is the full status list, and whether off-market or withdrawn listings appear] (What the Universal Search Bar returns)
- [confirm: whether an exact address returns a direct match; the July Notion draft said so and the live article dropped it] (What the Universal Search Bar returns)
- [confirm: whether contact results include only your own contacts or every contact in the brokerage] (What the Universal Search Bar returns)
- [confirm: what the Universal Search Bar shows when nothing matches] (What the Universal Search Bar returns)
- [confirm: where the Universal Search Bar sits in the mobile app] (Things to Know)
- The invited-client question is no longer a blocker for the body, since the draft claims nothing about roles. It still matters for the Notion `Roles` property, currently `All`. Tara or Kelly to confirm whether invited clients see the Universal Search Bar.
- Shared article: the same Intercom article sits in the Baldwin and CRMLS help centers. The new database row is Baldwin, per the old row's `MLS` value. Tara to decide whether CRMLS gets its own row or the shared collection carries the update.
- Every link in the draft now points at `/baldwin/en/`. The default help center link to Manage Your Saved Searches went out with the scope cut, so there is nothing to flag at transfer.
