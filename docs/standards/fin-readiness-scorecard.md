# Fin-readiness scorecard

A per-article score that says how well Fin can retrieve and answer from an article. It sits on top of the content standard (`content-standards.md`) and the golden questions (`golden-questions.md`) in this folder, and it exists so that a rewrite can be judged before and after, and so the audit, the QA pass, and the skills all measure articles with the same yardstick.

Owner: Tara, project lead, [tara.bars@perchwell.com](mailto:tara.bars@perchwell.com). Fin answer-quality owner: Rafe Petkovic, [rafe.petkovic@perchwell.com](mailto:rafe.petkovic@perchwell.com). Written September 9, 2026, after the first migration test (Universal Search Bar). Revised September 10, 2026, when the team reviewed that test and changed the audience, limitations, and redundancy rules.

## How the score works

Two layers. The gate decides whether the article is allowed to be called Fin-ready. The score says how far it is from that bar and which part of the article is holding it back.

**Gate: the 14 golden questions.** Each one passes or fails. One failure means the article is not Fin-ready, whatever the score says, because each factor is something Intercom's Content Readiness check scores on its own.

**Check set.** The checks below are the September 10, 2026 set. Chunk independence gained a sixth check that day, Fin-parsable formatting gained an eighth, and two Answer completeness checks were reworded, so a score recorded before that date is not directly comparable to one recorded after. A rescored article says which set it used.

**Score: 0 to 100 across five dimensions.** Each dimension is a list of yes or no checks. The dimension score is the checks passed divided by the checks in the list, multiplied by the weight. The total is the sum of the five. Every check traces to a rule in the content standard or to Intercom's Fin guidance, which means a failed check always has a known fix.

| Dimension | Weight | What it measures |
|---|---|---|
| Retrieval signals | 30 | Whether the title, description, opening, and headings carry the words a member types, so Fin finds the right section |
| Chunk independence | 25 | Whether each section still makes sense and identifies its topic when Fin retrieves it alone |
| Answer completeness | 25 | Whether a retrieved section contains a whole answer: what to do, what happens next, who it applies to, what the limits are |
| Fin-parsable formatting | 10 | Whether the HTML Fin reads has clean headings, lists, labels, and alt text |
| Accuracy and confidence | 10 | Whether every fact is sourced and every unknown is marked instead of guessed |

### Retrieval signals (30 points, 6 checks)

1. The title is task-focused and names the outcome, per the naming standard
2. The description is 120 to 140 characters and names the feature
3. The opening paragraph is "Use this article to ..." and names the feature and the outcomes
4. Every H2 and H3 names what the section answers and carries the feature name where it fits
5. The first sentence under every heading echoes the heading's key terms
6. No heading appears twice in the article

### Chunk independence (25 points, 6 checks)

1. No section depends on "above", "then", or the section before it
2. The feature name is repeated in every section; sections do not fall back to "it"
3. Each section covers one topic; long sections are split with H3 subheadings
4. Paragraphs run two to four sentences
5. Heading levels are H1 title only, H2 sections, H3 subsections and `Steps:`
6. No fact or enumeration is stated in more than one section; the feature name repeats, its capabilities do not

### Answer completeness (25 points, 7 checks)

1. Every `Steps:` block ends with what happens after the last step
2. A role is stated where one gates the workflow or changes the behavior, and the article makes no unverified claim that every member has the feature
3. Defaults and system behavior are stated, with a "which means" clause for system terms
4. Any constraint a member will hit is stated where they meet it, framed as the route forward; no Limitations section unless a hard cap or an irreversible action earns one
5. Every number, threshold, and duration is exact; nothing is "some" or "a few"
6. Abbreviations and product terms are defined on first use
7. Related workflows are linked with descriptive text instead of re-explained

### Fin-parsable formatting (10 points, 8 checks)

1. Steps are a numbered list, one action each, no terminal periods, UI elements named exactly
2. Callouts lead with a bold **Note:**, **Important:**, or **Tip:** label, and none are stacked
3. No other bold in the body
4. No emoji anywhere, including as pointers at images
5. Every image has descriptive alt text; placeholders carry the alt text they will use
6. Every table has an intro sentence above it
7. No horizontal rules, HTML, toggles, or columns
8. No em dashes

### Accuracy and confidence (10 points, 4 checks)

1. Every fact traces to release notes, the live article, or a Notion page
2. Anything unconfirmed is marked `[confirm: ...]`, never guessed, and no hedged source has been strengthened into a definite or universal claim
3. No marketing adjectives from the do-not list in the content standard
4. Paragon and other legacy systems are named neutrally

## Bands

| Score | Band | What it means |
|---|---|---|
| 90 to 100 | Fin-ready | Passes the gate and needs at most cosmetic fixes. Ready to move to `Ready to Transfer` |
| 75 to 89 | Ready with fixes | Close. The scorecard lists the failed checks and the fix for each; apply them before transfer |
| 50 to 74 | Needs rewrite | Fin may find the article but will answer from incomplete or cold sections. Rewrite against the standard |
| 0 to 49 | Not retrievable as written | The article will not surface reliably or will surface the wrong section. Rewrite from the template |

An article in the Fin-ready band that fails a golden question is reported as "Fin-ready score, gate failed on <factor>" and is not moved forward until the factor passes.

## Fin test questions

Every scorecard carries five to eight questions members may ask that the article should answer, written the way a member would type them into chat. For each question, record whether the old article answers it from a single section and whether the new article does. This is the part of the scorecard the team can paste into Fin's test mode after the article is transferred, which means the scorecard predicts Fin's behavior and the test run checks the prediction.

Write the questions from the article's outcomes and from the Search FAQ and conversation themes already in the repo, never from member conversations quoted verbatim.

## The QA file

One file per scored article at `workstreams/help-center-overhaul/qa/YYYY-MM-DD-<slug>.md`. It holds:

1. Article name, the old title if it changed, and the sources: old Notion URL, Intercom article ID and content ID, mirror path(s)
2. Who scored it and when
3. The golden questions table: factor, old result, new result, note
4. The dimension table: dimension, old score, new score, delta
5. Total score and band for old and new
6. The Fin test questions table
7. Open items: every `[confirm: ...]` marker and every decision the team still owes

No member names, emails, phone numbers, or addresses ever appear in a QA file. The scorecard is about the article, not the conversations.

## How the skills use this

- `/article-rewrite` scores the original before rewriting and the rewrite after, reports both with the delta, and saves the QA file. A migrated article is not created in Notion until the scorecard has run.
- `/article-draft` scores a new draft once, after the golden questions, and reports the band with the failed checks.
- The audit (`workstreams/help-center-overhaul/audit/`) may use the old score alone to rank the backlog: lowest band first, then lowest score within the band.
