# Content readiness checklist (14 factors)

Source: Intercom's Content Readiness feature, which scores knowledge base content across 14 factors. Recorded here 2026-09-04 from the team's working copy. The project's success criteria require 100 percent of in-scope articles to pass this checklist before launch.

Apply all 14 factors as a quality checklist when creating a new article, snippet, or internal article; when proposing updates to existing content; and when reviewing content for accuracy or completeness. Flag any factor that would fail before submitting a proposal. If the information needed to fix a factor is not available (for example exact limits for numerical clarity, or which plans or roles are affected for audience specification), ask the user rather than leaving it vague or making it up.

## The factors

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

`/article-draft` and `/article-rewrite` run every factor against the finished draft before saving and list any that fail, with the fix or the question for the user, in their report. The QA pass in `workstreams/help-center-overhaul/qa/` records the result per article.

## Known tension with the current house style

Factor 5 prefers "How to..." or question-form headings. The bundled style rules in `.claude/skills/article-draft/references/style-rules.md` say article titles avoid questions and section headings are task-based sentence case. Until `docs/standards/content-standards.md` settles it, follow this checklist for section headings (question form or "How to...") and keep article titles as the style rules say, and note the choice in the draft's open items.
