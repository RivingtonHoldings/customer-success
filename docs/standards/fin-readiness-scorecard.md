# Fin-readiness scorecard

A per-article score that says how well Fin can retrieve and answer from an article. It sits on top of the content standard (`content-standards.md`) and the golden questions (`golden-questions.md`) in this folder, and it exists so that a rewrite can be judged before and after, and so the audit, the QA pass, and the skills all measure articles with the same yardstick.

Owner: Tara, project lead, [tara.bars@perchwell.com](mailto:tara.bars@perchwell.com). Fin answer-quality owner: Rafe Petkovic, [rafe.petkovic@perchwell.com](mailto:rafe.petkovic@perchwell.com). Written September 9, 2026, after the first migration test (Universal Search Bar). Revised September 10, 2026, when the team reviewed that test and changed the audience, limitations, and redundancy rules. Plain language gate added September 15, 2026; it changes no dimension, no check, and no divisor, so every score recorded against revision 2 stands.

## How the score works

Two layers. The gate decides whether the article is allowed to be called Fin-ready. The score says how far it is from that bar and which part of the article is holding it back.

**Gate: the 14 golden questions.** Each one passes or fails. One failure means the article is not Fin-ready, whatever the score says, because each factor is something Intercom's Content Readiness check scores on its own.

**Second gate: plain language.** Pass or fail, reported next to the golden questions and never blended into them. The 14 are Intercom's and measure retrievability; this one is Perchwell's and measures whether a busy agent can read the article. The two are kept separate the same way Perchwell's Fin-resolved number is reported next to Intercom's rather than merged with it.

It exists because the score cannot see this. All four articles migrated between September 9 and 15 passed 14 of 14 and scored 95.7 to 100.0, and all four still needed a hand pass on their words. The QA record for the first one puts it plainly: "the words were never the problem the scorecard measures ... A member-comprehension defect is invisible to it, and Kelly caught this one by reading as an agent would."

Five checks. Any failure fails the gate.

1. No term from the plain language do-not list in `content-standards.md`, in the sense that list bans, unless a terminology rule in `docs/product-context.md` or an exact on-screen label requires it
2. The article names the real things rather than a category standing in for them
3. The title, description, opening paragraph, and every heading use only words an agent would say out loud. A term that appears on screen still fails this check where the article has adopted it as its own noun rather than naming the control at the point of use
4. No sentence restates the `Steps:` block in the abstract
5. The verb a member would type for the task appears in the section that covers it, not only inside a link's title

Check 3 asks two questions of any term that reads as product vocabulary, not one: is the word on screen, and would a member use it when the control is not in front of them? A word that passes the first and fails the second is the hardest case, because the on-screen test alone waves it through. "Scope" did exactly that on the Listings widget migration, September 16, 2026: the menu is headed Scope by, so the term looked sourced, and the draft went on to call the control "the scope button", which nothing on screen calls it.

Only check 1 is greppable, and it over-flags: "public records" and "return to the Dashboard" are both legitimate and both appear in finished articles. "tiles" inside alt text was a third until September 18, 2026, when the exception was struck; a hit there is now a real hit unless the word is the on-screen label. Checks 2 to 5 are read, the way the navigation-step rule and the possessive-density rule are read. A failure is reported with the terms it flagged and the replacement for each, not as a bare verdict.

**Check set.** The checks below are the September 10, 2026 set, revision 2.

- **Revision 1**, earlier the same day, gave Chunk independence a sixth check and Fin-parsable formatting an eighth, and reworded two Answer completeness checks.
- **Revision 2** followed the Dashboard Overview migration. Retrieval signals gained a seventh check, for list order, and Accuracy and confidence gained a fifth, for member-controlled verbs.

A score recorded against an earlier set is not directly comparable, because both revisions changed dimension divisors. Every scorecard names the set and revision it used, and so does a rescore.

Two QA files predate revision 2. Dashboard Overview has been rescored: the rewrite holds at 96.4, and the original drops from 51.0 to 46.3, out of Needs rewrite and into Not retrievable as written, because the live article fails both new checks. Universal Search Bar is still on revision 1. Its current draft passes both new checks, which lifts it from 95.0 to 95.7; the live-article and September 9 columns in that file have not been rechecked against the new checks and are still revision 1 numbers.

**Score: 0 to 100 across five dimensions.** Each dimension is a list of yes or no checks. The dimension score is the checks passed divided by the checks in the list, multiplied by the weight. The total is the sum of the five. Every check traces to a rule in the content standard or to Intercom's Fin guidance, which means a failed check always has a known fix.

| Dimension | Weight | What it measures |
|---|---|---|
| Retrieval signals | 30 | Whether the title, description, opening, and headings carry the words a member types, so Fin finds the right section, and whether the article's shape matches what the opening promised |
| Chunk independence | 25 | Whether each section still makes sense and identifies its topic when Fin retrieves it alone |
| Answer completeness | 25 | Whether a retrieved section contains a whole answer: what to do, what happens next, who it applies to, what the limits are |
| Fin-parsable formatting | 10 | Whether the HTML Fin reads has clean headings, lists, labels, and alt text |
| Accuracy and confidence | 10 | Whether every fact is sourced, every unknown is marked instead of guessed, and the voice stays inside the standard's do-not lists |

### Retrieval signals (30 points, 7 checks)

1. The title is task-focused and names the outcome, per the naming standard, and does not repeat another article's name, a Perchwell page name, or a collection name
2. The description is 120 to 140 characters and names the feature
3. The opening paragraph is "Use this article to ..." and names the feature and the outcomes
4. Every H2 and H3 names what the section answers and carries the feature name where it fits
5. The first sentence under every heading echoes the heading's key terms
6. No section heading appears twice in the article; the `Steps:` H3 is exempt, since the standard requires it once under each procedure
7. The sections follow the order of any list in the opening paragraph or a lead sentence, and every item in that list has a section behind it

### Chunk independence (25 points, 6 checks)

1. No section depends on "above", "then", or the section before it
2. The feature name is repeated in every section; sections do not fall back to "it"
3. Each section covers one topic; long sections are split with H3 subheadings
4. Paragraphs run two to four sentences
5. Heading levels are H1 title only, H2 sections, H3 subsections and `Steps:`
6. No fact or enumeration is stated in more than one section; the feature name repeats, its capabilities do not. Parallel procedures are the exception: each `Steps:` block carries every step it needs, because Fin has to be able to answer from either one alone

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

### Accuracy and confidence (10 points, 5 checks)

1. Every fact traces to release notes, the live article, or a Notion page
2. Anything unconfirmed is marked `[confirm: ...]`, never guessed; no hedged source has been strengthened into a definite or universal claim; and no marker sits on a detail while the claim around it goes unmarked
3. No marketing adjectives from the do-not list in the content standard
4. No legacy platform is named; the comparison says "a legacy platform" and keeps the legacy feature name
5. Verbs name what the member does rather than what the screen does back, and no "you can", "allows you to", or verb "use" outside the accepted exceptions

## Bands

| Score | Band | What it means |
|---|---|---|
| 90 to 100 | Fin-ready | Passes the gate and needs at most cosmetic fixes. Ready to move to `Ready to Transfer` |
| 75 to 89 | Ready with fixes | Close. The scorecard lists the failed checks and the fix for each; apply them before transfer |
| 50 to 74 | Needs rewrite | Fin may find the article but will answer from incomplete or cold sections. Rewrite against the standard |
| 0 to 49 | Not retrievable as written | The article will not surface reliably or will surface the wrong section. Rewrite from the template |

An article in the Fin-ready band that fails a golden question is reported as "Fin-ready score, gate failed on <factor>" and is not moved forward until the factor passes. An article that fails the plain language gate is reported the same way, as "Fin-ready score, plain language gate failed on <terms>". `Ready to Transfer` needs all three: the Fin-ready band, the golden questions, and plain language.

## Fin test questions

Every scorecard carries five to eight questions members may ask that the article should answer, written the way a member would type them into chat. For each question, record whether the old article answers it from a single section and whether the new article does. This is the part of the scorecard the team can paste into Fin's test mode after the article is transferred, which means the scorecard predicts Fin's behavior and the test run checks the prediction.

Write the questions from the article's outcomes and from the Search FAQ and conversation themes already in the repo, never from member conversations quoted verbatim.

## The QA file

One file per scored article at `workstreams/help-center-overhaul/qa/YYYY-MM-DD-<slug>.md`. It holds:

1. Article name, the old title if it changed, and the sources: old Notion URL, Intercom article ID and content ID, mirror path(s)
2. Who scored it and when
3. The golden questions table: factor, old result, new result, note
4. The plain language gate: pass or fail, and for a failure every term flagged with its replacement
5. The dimension table: dimension, old score, new score, delta
6. Total score and band for old and new
7. The Fin test questions table
8. Open items: every `[confirm: ...]` marker and every decision the team still owes

No member names, emails, phone numbers, or addresses ever appear in a QA file. The scorecard is about the article, not the conversations.

## How the skills use this

- `/article-rewrite` scores the original before rewriting and the rewrite after, runs both gates on the rewrite, reports everything with the delta, and saves the QA file. A migrated article is not created in Notion until the scorecard has run.
- `/article-draft` scores a new draft once, after the golden questions, and reports the band with the failed checks.
- The audit (`workstreams/help-center-overhaul/audit/`) may use the old score alone to rank the backlog: lowest band first, then lowest score within the band.
