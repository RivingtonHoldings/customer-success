# QA: Listing Field Changes in Perchwell (CRMLS)

Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-11-04-listing-field-changes-in-perchwell-crmls.md`. Mirrors the Baldwin article of the same title (Baldwin record 14459773). Source: the Matrix doc "External Then vs Now: CRMLS Matrix → Perchwell". Tracker ID: TRK-130 (next free number at Tara's direction, added to the master sheet Nov 4, 2026). Notion row name carries a "(CRMLS)" suffix for now. Replaces the blank published CRMLS record 18231908 once ported; do not touch that record until Tara confirms.

## Checks run

- Title, description (128 characters), "Use this article to ..." opening, H1/H2 levels, heading echo in each first sentence: pass.
- No em dashes, bold, horizontal rules, or "you can": pass.
- Fin-readiness score and the 14 golden questions: not run. Two confirm markers remain.

## Differences from the Baldwin article, on purpose

- Baldwin explains where to enter each field in Add/Edit. CRMLS has no listing entry in Perchwell, so the draft covers only how fields and values appear.
- Baldwin's sections (Class and Property Type, Boat slip, Active New Construction, Area, More than 2 pets, Pool Features, Year Built) have no Matrix source and are not carried over.
- The Matrix doc has little field-level content, so this is a four-section article.

## Open items

| Marker | Question | Notes |
|---|---|---|
| V8 | Where does Community appear on a listing, and is it a search filter? | The doc says only "Community, listed under subdivision and complex", and gives no search steps |
| V16 | Is the Perchwell status label Hold or Temp off mkt? | The Matrix doc says Perchwell shows Hold. The CRMLS Filter Your Search by Status and Price Changes draft and the Baldwin status article both say Temp off mkt. A direct conflict; not resolved by majority, so ask Product. The section heading names the CRMLS dashboards' label, which the doc does give |

## Judgment calls to confirm

- "A listing with one of them may be missing" softens the doc's "is missing from a property sub-type filter", per the standard against strengthening a source.
- The article says "property subtype filter" and not the on-screen label, because the CRMLS label is unverified (Baldwin's is Property sub type).
- The doc's other data-quality rows (impossible price, duplicate agent, and similar) stay in the Why Listings and Market Data Can Look Different article, not here.

## Back-links to add

Link to Why Listings and Market Data Can Look Different in Perchwell from the $0 and status sections once that article exists. The CRMLS glossary's Township row links here; its marker can be replaced when this article gets a CRMLS public URL.

## Fin test questions

1. What is Township called in Perchwell?
2. Why is a listing missing when I filter by mixed use?
3. What does a $0 HOA fee mean on a listing in Perchwell?
4. Is Hold the same as Temporarily Off Market?
5. Where did Township go in Perchwell?

## Review results, Nov 4, 2026

Scored by Claude against `docs/standards/fin-readiness-scorecard.md` (check set revision 2, plain language gate), after the draft-quality pass in `.claude/skills/article-rewrite`. Self-scored, so a second reviewer's read is still pending. New article: no old score to compare.

### Golden questions

| Factor | Result | Note |
|---|---|---|
| 1 disambiguation | Pass | No "this screen", "above", or emoji pointers. |
| 2 visual_content_text | Pass | No images; nothing to describe. |
| 3 undefined_terms | Pass | Abbreviations defined at first use after review. |
| 4 structured_enumeration | Pass | Steps and sequences are numbered; sets are bulleted or tabled. |
| 5 query_answer_symmetry | Pass | Headings name what each section answers, per the house reading of factor 5. |
| 6 self_contained_sections | Pass | No dependence on earlier sections; navigation named where a step needs it. |
| 7 audience_specification | Pass | Open to all members; Notion Roles is All. Silence is correct. |
| 8 entity_distribution | Pass | Feature and product names repeat in each section. |
| 9 semantic_chunk_boundaries | Pass | One topic per section. |
| 10 restate_questions | Pass | Every table has an intro sentence. |
| 11 overview_jtbd | Pass | "Use this article to ..." opening. |
| 12 instruction_completeness | Pass | No procedure beyond the outcome sentences. |
| 13 limitations_workarounds | Pass | Gaps are stated once with the route forward, or marked. |
| 14 numerical_clarity | Pass | Exact numbers or a marker for unknowns. |

All 14 pass as drafted, with confirm markers still open. Markers must clear before the row moves to Ready to Transfer.

### Plain language gate

Pass. The "entry" in "listing entry" and "above" in "above your search results" are the product's own sense, not the banned one.

### Dimension scores (new article)

| Dimension | Checks passed | Score |
|---|---|---|
| Retrieval signals | 7 of 7 | 30.0 of 30 |
| Chunk independence | 6 of 6 | 25.0 of 25 |
| Answer completeness | 7 of 7 | 25.0 of 25 |
| Fin-parsable formatting | 8 of 8 | 10.0 of 10 |
| Accuracy and confidence | 5 of 5 | 10.0 of 10 |

Total 100.0 of 100, band Fin-ready. The score does not count open confirm markers against accuracy, so it will not move when they clear.

### Changes the review made

- Defined HOA (homeowners association), MLS (multiple listing service), and CRMLS (California Regional Multiple Listing Service) at first use (factor 3).


## Aligned to Baldwin, Nov 4, 2026

Description reworded to follow the Baldwin article's wording, with Matrix terms swapped in and only enough added to reach 120 characters. Opening and headings were already close to Baldwin's.

## Reviewer input considered, Nov 5, 2026

Reviewer's description kept in shape ("Learn which Matrix listing fields were renamed or are not stored in Perchwell, including Township ...") with one change: "certain property subtypes" became "mixed use subtypes, and more", since "certain" is a vague quantity and the list is not exhaustive (128 characters, passes 120 to 140). It differs from Baldwin's "See which ... such as ... and more" only in "Learn" and "including".

Reviewer's opening kept in substance with three changes: it now opens "Use this article to" (house form); "Perchwell equivalents" became "are called in Perchwell" (the term the sections use, matching the glossary); "identify" became "see". Order still matches the sections: fields and status names, subtypes, then $0 or 0.

Flagged, not changed: the status section heading is long and rests on the Hold or Temp off mkt answer (V16); "Community values appear under subdivision and complex" is the doc's wording and unclear; the article has no links yet (add the data-differences article once it has a public link).

## Reviewer edit applied, Nov 5, 2026

Community replaces Township: Tara's revision applied as written ("The Matrix Township field is called Community in Perchwell. Community values appear under subdivision and complex."). It passes the standards: the first sentence echoes the heading and leads with the legacy name members search for, and the glossary's Township row says the same. Her version drops the confirm marker on where Community appears and whether it is a search filter, so that marker is closed on her say-so. The sentence "appear under subdivision and complex" still comes from the Matrix doc, not a screenshot; the article gives no search route, so nothing is asserted about a Community filter. Remaining marker on this article: Hold or Temp off mkt (V16).

## Marker restored, Nov 5, 2026

At Tara's request the confirm marker on Community replaces Township is back, so she can double check where Community appears on a listing and whether it is a search filter. Her revised wording stays. The marker is open again, which makes two open on this article (this one and Hold or Temp off mkt, V16).

## Reviewer edit considered, Nov 5, 2026: status section

Tara's revision applied with three changes, marker kept. Checked: heading echo passes ("temporarily off-market status" in the first sentence), the marker states only the question (the evidence, that the Matrix doc says Hold while the CRMLS Filter Your Search by Status and Price Changes draft and Baldwin's status article say Temp off mkt, lives here per the standard), and "off-market" follows the mirror's spelling.

Changes: (1) heading hyphenated to "off-market" to match her body text and the mirror; (2) CRMLS defined at first use (golden question 3), which her version dropped; (3) the two sentences were rebuilt so the definition fits under the 25-word limit, and "Both names refer to the same listing status" was folded into "call the same listing status Temporarily Off Market" so the fact is said once. Open again: Hold or Temp off mkt (V16), Community location and filter.

## Reviewer edit considered, Nov 5, 2026: subtypes section

Tara's revision applied with one change. Checked and kept: the heading and body ("may not appear" keeps the doc's hedge; "to find them, search without ..." gives the route forward; the heading uses the words a member would type while the body carries the subtype labels, which is the intended split, so the two spellings stay). Change: her third sentence began "To find these listings" right after "Listings with these subtypes", an echo between back-to-back sentences, so it now reads "To find them, search without applying a property subtype filter." The Mixed Use, Rooms for Rent, and Hotel/Motel spellings come from Tara; the Matrix doc writes "mixed use, rooms for rent, and hotel or motel", so confirm they match the Matrix labels.

## Reviewer edit considered, Nov 5, 2026: $0 or 0 section

Tara's revision applied with four changes. Kept: the HOA definition, the idea of ruling out the misreading ("not as an actual zero", which the standard's surprising-behavior rule supports and the paired-contrast ban does not catch, since it prevents a likely wrong reading), and "not reported". Changes: (1) the MLS (multiple listing service) definition, dropped in her version, restored, because this is the first standalone use of MLS in the article (golden question 3); (2) "did not provide" back to "did not report" so the first sentence echoes the heading and the verb stays one word across the section; (3) "should be interpreted" became "read", the member-in-control verb; (4) her 30-word first sentence was split and the answer moved first, with "On a listing" kept in the second sentence so the section still names a listing when retrieved alone. Test of the 25-word rule: first sentence now 24 words.

## Markers resolved, Nov 5, 2026 (Tara's answer and two screenshots)

- Hold or Temp off mkt (V16): Tara confirmed the off-market status is Hold. Marker removed; the section now says Hold. Check next: the shared Filter Your Search by Status and Price Changes article (TRK-087, live record 11010696) says Temp off mkt, which is Baldwin's status, not CRMLS's; it is logged in open-article-fixes.md. Correction, Nov 5: What Each Listing Status Means (CRMLS), TRK-117, already uses Hold, so my earlier claim that it said Temp off mkt was wrong.
- Community (V8): Tara's Filters screenshot shows a Community section holding two fields, Subdivision name and Subdivision name other, and the filter search for "subdivision" lists both under Community. Her listing screenshot shows Subdivision name other (Arrowhead Woods) in the Land & Lot section. The section now says so and the marker is removed. The doc's "under subdivision and complex" was dropped: the screenshot shows no complex field. Not verified: where the Subdivision name field appears on a listing (the browser find showed two matches for "subdivision"; the second was in the collapsed Location section), and which of the two fields Matrix Township maps to. The article asserts only what the screenshots show.

## Row name, Nov 5, 2026

The "(CRMLS)" suffix was removed from this article's Notion Article Name at Tara's request, so the row now carries the exact article title for the port. The master sheet's title columns were not changed.

## Synced from Notion, Nov 5, 2026

Notion was ahead of the repo. Kelly is the Article Reviewer on all nine rows, Article Due is Nov 12, 2026, Article Status is Ready to Transfer, and Roles is All Except Client, all set by Tara or the team. Article Review Status is still Not Started; the CRMLS port needs Review Finished or Complete. No screenshots on this article.

## Decisions, Nov 5, 2026

- Blank placeholder (record 18231908, Listing Field Changes in Perchwell, published, empty): Tara decided to replace its content in place. The record is published, so the update goes live as soon as it is written. It is a change to a live article, so the port needs the full diff, one confirmation, a changelog line, and a mirror re-sync; no new CRMLS record is created for this article and Intercom URL CRMLS takes this record's URL. Nothing has been written to Intercom.
