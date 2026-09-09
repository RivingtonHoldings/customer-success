# QA scorecard: Universal Search Bar

Scored with `docs/standards/fin-readiness-scorecard.md`. First article through the migration path.

## Article and sources

- Title: Universal Search Bar (unchanged). The task-led alternative "Find a Listing, Agent, or Contact with the Universal Search Bar" was proposed and Leo chose to keep the existing title on 2026-09-09
- Old Notion page: https://app.notion.com/p/1c78b9e0143880f3b927daf7d2aca4d5 (Master Article List, last edited 2026-07-17, read only)
- Intercom article 11002620, content ID 11821319, updated 2026-08-10, label `How To: Search`
- Mirror: `docs/help-center/baldwin/universal-search-bar.md` and `docs/help-center/crmls/universal-search-bar.md` (shared into both help centers)
- Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-09-09-universal-search-bar-rewrite.md`
- Notion Draft in the Perchwell Help Center Database [Sep 2026]: https://app.notion.com/p/3d68b9e01438810cb386f3ea550d097c
- Scored by Claude for Leo Jedynak, 2026-09-09

## Source differences (live wins)

| Where | Old Notion page (July 17) | Live article (August 10) | Draft |
|---|---|---|---|
| Listings bullets | Exact address returns a direct match | Bullet dropped | Kept as `[confirm: ...]` |
| Tips | Three bullets | Adds "If you hear Power Search, it refers to the Universal Search Bar" | Merged into one neutral Things to Know bullet |
| Body extras | Click Script toggle, Loom embed, Perchwell banner image | None | Loom kept under the opening; script and banner dropped |
| Headings | H2 with horizontal rules | H1 with horizontal rules | H2 and H3, no rules |
| Images | Two Notion uploads, no alt text | Two Intercom CDN images, no alt text | Live images kept with alt text |

## Golden questions (gate)

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | Old used a decorative emoji, not a pointer |
| 2 visual_content_text | Fail | Pass | Both images had no alt text; both now describe the screen |
| 3 undefined_terms | Pass | Pass | MLS number now glossed as the listing's MLS ID |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Pass | Pass | Old "Tips" is the sanctioned closing heading; new headings all carry the feature name |
| 6 self_contained_sections | Fail | Pass | Old Tips said "this feature" with no name in the section |
| 7 audience_specification | Fail | Pass | Old never said who can use it; new states every role, invited clients pending confirm |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables in either |
| 11 overview_jtbd | Fail | Pass | Old had no opening paragraph; description said "In this article, you will learn" |
| 12 instruction_completeness | Fail | Pass | Old steps stopped at typing; new steps end at the opened record |
| 13 limitations_workarounds | Fail | Pass | Old said "not saved or filtered searches" with no workaround; new lists three limits with the workaround and link for each |
| 14 numerical_clarity | Pass | Pass | No numbers needed |

Gate: old fails 6 of 14. New passes 14 of 14, with four `[confirm: ...]` markers that a reviewer must resolve before transfer (see Open items).

## Dimension scores

| Dimension | Weight | Old | New | Delta |
|---|---|---|---|---|
| Retrieval signals | 30 | 10.0 (2 of 6) | 25.0 (5 of 6) | +15.0 |
| Chunk independence | 25 | 15.0 (3 of 5) | 25.0 (5 of 5) | +10.0 |
| Answer completeness | 25 | 10.7 (3 of 7) | 21.4 (6 of 7) | +10.7 |
| Fin-parsable formatting | 10 | 4.3 (3 of 7) | 10.0 (7 of 7) | +5.7 |
| Accuracy and confidence | 10 | 10.0 (4 of 4) | 10.0 (4 of 4) | 0 |
| **Total** | 100 | **50.0** | **91.4** | **+41.4** |

Old band: Needs rewrite (gate failed on 6 factors). New band: Fin-ready, gate passed.

Failed checks, old: title is a bare noun; no "Use this article to" opening; two of three headings lack the feature name; first sentences do not echo every heading; "this feature" in Tips depends on context; body headings at H1; no audience; no "which means" clause; no workaround for the stated limit; no related links; emoji-led tip with no bold label; no alt text; horizontal rules in the live HTML.

Failed checks, new: retrieval signals 1 (the title stays a bare noun by Leo's choice; the description and opening carry the task words instead) and answer completeness 3 (the article does not say what the Universal Search Bar shows when nothing matches, because neither source does; marked `[confirm: ...]`).

## Fin test questions

Questions members may ask, in their words. "One section" means Fin can answer from a single retrieved section without stitching.

| Question a member may ask | Old article, one section | New article, one section |
|---|---|---|
| How do I look up a listing by MLS number? | Yes | Yes |
| Where is the search bar to find an agent? | Partly (says "top of your screen") | Yes (Search field, upper right of the top navigation) |
| Can I search for a contact by email? | Yes | Yes |
| What happened to Power Search? | Yes | Yes, with a link to New Terminology |
| Can I search several MLS numbers at once in the top search bar? | No | Yes, with the MLS ID filter workaround |
| Does the search bar show closed or expired listings? | Yes | Yes, with what the status badge looks like |
| How do I save the search I typed in the top bar? | No (says it is not for saved searches, no next step) | Yes, links Manage Your Saved Searches |
| Why can't I filter by price in the top search bar? | No | Yes |

## Open items

- [confirm: whether invited clients see the Universal Search Bar, and whether they get agent and contact results] (opening paragraph)
- [confirm: whether Active, Pending, Closed, and Expired is the full status list, and whether off-market or withdrawn listings appear] (What the Universal Search Bar returns)
- [confirm: whether an exact address returns a direct match; the July Notion draft said so and the live article dropped it] (What the Universal Search Bar returns)
- [confirm: whether contact results include only your own contacts or every contact in the brokerage] (What the Universal Search Bar returns)
- [confirm: what the Universal Search Bar shows when nothing matches] (What the Universal Search Bar returns)
- [confirm: where the Universal Search Bar sits in the mobile app] (Things to Know)
- Shared article: the same Intercom article sits in the Baldwin and CRMLS help centers. The new database row is Baldwin, per the old row's `MLS` value. Tara to decide whether CRMLS gets its own row or the shared collection carries the update.
- Manage Your Saved Searches lives in the default help center (`/en/`), not `/baldwin/en/`. Confirm at transfer that the link resolves for Baldwin members.
