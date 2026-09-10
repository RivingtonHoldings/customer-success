# Golden questions: the 14 content readiness factors

The team calls these the golden questions. Source: Intercom's Content Readiness feature, which scores knowledge base content across 14 factors. Recorded here 2026-09-04 from the team's working copy. The project's success criteria require 100 percent of in-scope articles to pass this checklist before launch.

Apply all 14 factors as a quality checklist when creating a new article, snippet, or internal article; when proposing updates to existing content; and when reviewing content for accuracy or completeness. Flag any factor that would fail before submitting a proposal. If the information needed to fix a factor is not available (for example exact limits for numerical clarity, or which plans or roles are affected for audience specification), ask the user rather than leaving it vague or making it up.

## The 14 golden questions

1. **disambiguation**: Avoid vague references like "this screen" or "the field shown above." Every reference must be self-descriptive. Do not use emoji (👇 ☝️) to point at visual content.
2. **visual_content_text**: Every image must have descriptive alt text explaining what the screenshot or diagram shows. A trailing colon followed by an image with no alt text is not acceptable; describe the visual in text too.
3. **undefined_terms**: Define abbreviations and product-specific terms on first use. Examples: CSV (comma-separated values), GDPR (General Data Protection Regulation), 2FA (two-factor authentication), Elasticsearch, UserMessage. Do not assume the reader knows internal terminology.
4. **structured_enumeration**: Multi-step processes must use numbered lists. Lists of items must use bullet points. Never describe steps or enumerations in flowing prose. If a sentence says "the following:" it must be followed by an actual list.
5. **query_answer_symmetry**: Headings should mirror how a customer would phrase a question. Avoid bare noun phrases ("Invite reminder emails") or bare imperatives ("Add a teammate"). Prefer "How to..." or question-form headings.
6. **self_contained_sections**: Every section must make sense if retrieved independently by Fin, without surrounding context. Avoid "as described above," "the field shown above," "Then..." as an opener, or references to prior steps without restating them.
7. **audience_specification**: State who the content is for and what permissions or plan access is required. Do not assume the reader knows their own role or access level.
8. **entity_distribution**: Repeat key entities (product names, feature names, the article's core topic) throughout the article, not just in the opening. Sections retrieved in isolation should still be identifiable as belonging to the right topic.
9. **semantic_chunk_boundaries**: Each section should cover one focused topic. Avoid mixing unrelated information in the same block. Long sections should be broken up with meaningful subheadings.
10. **restate_questions**: Tables and standalone blocks must include enough context to be understood without the heading hierarchy. Add an intro sentence before tables that states what the table covers and where it applies.
11. **overview_jtbd**: The opening paragraph must state the job or jobs the reader will accomplish, not just the topic. "This article covers X" is weaker than "Use this article to do Y, troubleshoot Z, or understand W."
12. **instruction_completeness**: Step-by-step instructions must be complete end to end. Include what happens after the final step (confirmation dialogs, what to expect, next actions). Do not stop at "click Remove" without describing what follows.
13. **limitations_workarounds**: If a feature has known limitations, gaps, or workarounds, document them explicitly. Do not just say "some things aren't supported"; say which ones and what to do instead.
14. **numerical_clarity**: All numbers, thresholds, limits, durations, and quantities must be stated precisely. Avoid "some," "a few," "shortly," or vague ranges. Use exact values where known; ask the user if unknown.

## How the skills use this

`/article-draft` and `/article-rewrite` run every golden question against the finished draft before saving and list any that fail, with the fix or the question for the user, in their report. The 14 factors are also the gate of the Fin-readiness scorecard (`fin-readiness-scorecard.md` in this folder), which adds a 0 to 100 score on top; `/article-rewrite` scores an article before and after a rewrite. The QA pass in `workstreams/help-center-overhaul/qa/` records both per article. Golden questions are a checklist for articles, not a set of member questions; real member questions, if the team wants them later, would be a separate artifact.

## How the house standard resolves factor 5

Factor 5 prefers "How to..." or question-form headings, and the older house style banned questions outright. `content-standards.md`, approved September 4, 2026, settles it:

- Section headings must name what the section answers and carry the feature name. "Set the report max date" and "Refunds for cancelled subscriptions" pass; "Settings" and "Refunds" do not. Intercom's own wording is that a heading should name what the section answers, which a specific task-led heading does as well as a question does.
- FAQ articles use one question-form heading per question. Intercom recommends a header per question for FAQ content.
- Question-form headings are allowed in any article type when they match how members ask.
- Article titles follow the approved Notion naming standard, which permits questions, "How to," and -ing constructions when they read more naturally, and prefers concise action-led titles otherwise.

A draft no longer needs to note this choice in its open items.

## How the house standard resolves factor 7

Factor 7 asks the writer to state who the content is for and not to assume the reader knows their own role. Read literally, it produces a line on every article saying the feature is available to everyone, which is what the first migration test produced. `content-standards.md`, revised September 10, 2026, settles it:

- A role is stated only where a role gates the workflow, or where the feature behaves differently depending on who is looking at it. Silence means every member.
- The factor's real target is the reader who tries a workflow and fails because they lack access. An unrestricted feature has no such reader.
- An unverified availability claim paired with a `[confirm: ...]` marker fails this factor rather than passing it. The claim is the part Fin quotes, and it is the part that is unverified.
- The Notion `Roles` property records the audience for every article whether or not the body says anything, so the information is not lost.

## How the house standard resolves factor 8

Factor 8 asks for key entities to be repeated throughout the article so a section retrieved alone is still identifiable. It says entities, not facts, and the first migration test read it as license to state the same three capabilities in six places.

- What repeats is the feature name, the heading's key terms in the sentence below it, and anything a step depends on.
- What does not repeat is the fact itself. Each fact has one canonical home; a later section names that section or links the article instead of restating it.
- `content-standards.md`, under Say each fact once, holds the full split.

## How the house standard resolves factor 13

Factor 13 requires that a limitation, when it is documented, be specific: which thing is not supported and what to do instead, rather than "some things aren't supported." It does not require a Limitations section, and it does not ask the writer to go looking for gaps.

- The house standard writes constraints as the route forward, in the section where the member meets them, and reserves a dedicated section for a hard cap with an exact number or something irreversible.
- A constraint stated as an alternative path passes this factor. "To look up several listings at once, use the **MLS ID** filter on the **Search** page" names the gap and the workaround in one sentence.
- An article with no constraint worth stating passes the factor by saying nothing. It does not need to declare that the feature has no limitations.
- `content-standards.md`, under Constraints, and where to go instead, holds the full rule.
