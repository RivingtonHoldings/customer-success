# QA: Find OneHome Features in the Perchwell Client Portal (CRMLS)

Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-11-04-find-onehome-features-in-the-perchwell-client-portal-crmls.md`. New article with no Baldwin counterpart (Baldwin covers CollabLink in What Changed When You Moved to Perchwell). Source: the Matrix doc "External Then vs Now: CRMLS Matrix → Perchwell". Tracker ID: TRK-137 (next free number at Tara's direction, Nov 4, 2026). Notion row name carries a "(CRMLS)" suffix for now. Original article title blank in the master sheet: brand-new article.

## Checks run

- Title, description (132 characters), "Use this article to ..." opening, heading levels, table with intro sentence, "For more information:" list of four links: pass.
- No em dashes, bold, horizontal rules, "you can": pass.
- Legacy product named (OneHome), allowed for Then vs. Now.
- Fin-readiness score and the 14 golden questions: not run. Two confirm markers remain.

## Where the doc rows landed

All 9 OneHome rows are in one table. The "invite up to 100 at once" instruction also appears in Find and Update Contacts Moved from Matrix; both carry the same marker.

## Verified against the CRMLS mirror

- Like, Maybe, and Reject, and Shared properties: match the CRMLS Message Clients and Communicate with Your Agent articles. Removed the earlier marker.
- Clients edit shared saved searches in their client portal: matches the CRMLS Manage Your Saved Searches article.
- A client portal is a workspace for collaborating with the agent: matches the CRMLS Create and Manage Your Contacts draft. This likely answers the "workspace" marker in What Changed (Concierge mode, "the client's workspace"); confirm and clear that marker.

## Open items

| Marker | Question | Notes |
|---|---|---|
| V10 | How does a member invite up to 100 contacts at once? | Doc states 100 with no route |
| V15 | Does Perchwell really send no notice when a client edits a shared saved search? | Surprising behavior; verify before publishing |

## Judgment calls to confirm

- "Like, Maybe, or Reject" replaces the doc's "Like / Maybe / Reject" for readability; same facts.
- Last-visit and visitor activity ("views, likes, dislikes", "logins and shared listings") is the doc's list of what the Tags and Contacts pages show; check against screenshots (V8).
- The Message Clients link points at the CRMLS record (published 12541968). Tags Page Overview and Accept Your Agent's Perchwell Invitation point at Baldwin because their CRMLS records are drafts; repoint before port.

## Fin test questions

1. What replaces OneHome in Perchwell?
2. Can clients view shared listings without an account?
3. Where do I see my client's Favorites in Perchwell?
4. How do clients request a tour in Perchwell?
5. How do I see when a client last logged in?
6. Do my clients get a mobile app?

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

- Removed "in most cases" from the table lead (factor 14); the table lists each feature with its match.
- Defined CSV (comma-separated values) at first use (factor 3).

## Markers resolved, Nov 5, 2026

- Invite row (V10): Tara said one at a time is manual entry and the CSV goes through bulk upload. The row now reads: invite clients from the Contacts page by adding each contact manually, or bulk upload a CSV of up to 100 contacts at a time (100 per the CRMLS Bulk Upload article). Marker removed.
- Shared search edits (V15): Tara confirmed the agent is not notified. Marker removed; the sentence stays.
- No markers remain on this article. Tara wrote TRK-138; the OneHome article is TRK-137.

## Row name, Nov 5, 2026

The "(CRMLS)" suffix was removed from this article's Notion Article Name at Tara's request, so the row now carries the exact article title for the port. The master sheet's title columns were not changed.

## Synced from Notion, Nov 5, 2026

Notion was ahead of the repo. Kelly is the Article Reviewer on all nine rows, Article Due is Nov 12, 2026, Article Status is Ready to Transfer, and Roles is All Except Client, all set by Tara or the team. Article Review Status is still Not Started; the CRMLS port needs Review Finished or Complete. No screenshots on this article.
