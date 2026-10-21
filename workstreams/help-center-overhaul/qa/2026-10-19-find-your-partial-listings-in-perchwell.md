# QA: Find Your Partial Listings in Perchwell

- Old title: Your Data: Listings & Partials
- Sources: old Notion page https://app.notion.com/p/34a8b9e0143880c9bbf9e3ef6c040483; Intercom article 14727432, content 17294871; mirror `docs/help-center/baldwin/your-data-listings-partials.md` (matches the live stored body, checked with `get_article` October 19, 2026); Draft Listings (a.k.a. PartialProperty) PRD; Manage Listings Page Overview draft (Notion) for the Publication status filter and pencil icon
- Product answers: Kevin, October 19, 2026 (which partials moved, re-creating a missing one, imported drafts look the same, broker visibility, published listings)
- Scored by Claude for Kevin, October 19, 2026. Scorecard check set revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Pass | Pass | Old had no images; new reuses the Publication status screenshot with alt text |
| 3 undefined_terms | Fail | Pass | "System of record" was undefined; draft listing now defined with a which-means clause |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | No headings before; each section now names what it answers |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | Agents and brokerage admins stated where visibility differs |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Fail | Pass | One block mixed what moved and what to do; now three sections |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | "Use this article to" opening |
| 12 instruction_completeness | Fail | Pass | Old never said where the drafts are; new has steps and an outcome |
| 13 limitations_workarounds | Fail | Pass | Partials after July 20 now get a route: re-create or update in the Add/Edit form |
| 14 numerical_clarity | Pass | Pass | |

## Plain language gate

Pass. Greps for the do-not list, "you can", "use", em dashes, bold, "appear", and "display" returned only "does not appear in search results", where the system is the actor. "Partial" is the legacy term members search for; it is kept and tied to "draft listing" in the first section.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 8.6 (2/7) | 30.0 (7/7) | +21.4 |
| Chunk independence (25) | 20.8 (5/6) | 25.0 (6/6) | +4.2 |
| Answer completeness (25) | 10.7 (3/7) | 25.0 (7/7) | +14.3 |
| Fin-parsable formatting (10) | 8.75 (7/8) | 10.0 (8/8) | +1.25 |
| Accuracy and confidence (10) | 8.0 (4/5) | 10.0 (5/5) | +2.0 |
| Total | 56.9 | 100.0 | +43.1 |

Old band: Needs rewrite. New band: Fin-ready, gate passed, one confirm marker open.

Old failures: "Your Data:" bare-noun title; 101-character "In this article" description; no jobs opening; no headings; one-sentence paragraphs; "system of record" undefined; no route for partials that did not move; no links; em dashes; Paragon named twice.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| Where are my partials in Perchwell? | Partly, says they are drafts but not where | Yes |
| How do I find my draft listings? | No | Yes |
| Did all my partial listings come over? | Yes | Yes |
| I changed a partial after July 20 and the change is missing. What do I do? | No | Yes |
| How do I re-create a partial that is not in Perchwell? | No | Yes |
| Can my broker see my draft listings? | No | Yes |
| What is a partial called in Perchwell? | Yes | Yes |

## Source differences

- Which partials moved: the live article and old Notion page say all; Your Data: Perchwell Best Practices says a 1/1/2023 cutoff; the PRD says created within the last year. Kevin: every partial created before July 20, 2026. The draft follows Kevin. The Best Practices table's 1/1/2023 cutoff now contradicts this article; fix it when that article is migrated.
- Published listings: the old Notion page described the parallel-period sync, which no longer applies after cutover. The live article dropped it. Kevin confirmed published listings are in Perchwell; the draft says so in one sentence.
- "Does not appear in search results" for drafts comes from the PRD ("Drafts only show in Manage Listings (not search)"), not from the teammate.

## Open items

- [confirm: whether a draft whose status is outside the Status filter defaults, such as Closed, shows without selecting that status]. The Manage Listings Status filter defaults to Coming soon, Active, Active under contract, and Pending (screenshot, August 10, 2026), and the PRD says drafts can carry Active, Coming Soon, or Closed. If Closed drafts are hidden, the steps need "select All under Status", and the Manage Listings Page Overview draft's "Find your draft listings" section needs the same fix.
- The Manage Listings Page Overview link points to the default help center (`/en/`); flag at port.
- Set consistency: Find Familiar Features by Their Perchwell Names links this article as "Your Data: Listings & Partials". Update its link title to Find Your Partial Listings in Perchwell once this article is ported.
- Old row note: "Can use for MLSs coming from Paragon. Will need to do one for each MLS tech provider." The July 20 date is Baldwin's; a CRMLS version needs its own facts.
