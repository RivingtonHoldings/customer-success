# Help center overhaul

Workstream rules and goals for the MLS Help Center Standardization and Scalability project. Facts, status, and contacts live in `docs/`; this file is instructions.

## Project facts

- **Name:** MLS Help Center Standardization and Scalability
- **Timeline:** September 1 to October 2, 2026 (five weeks)
- **Lead:** Tara
- **Scope:** Baldwin and CRMLS help centers
- **Goal:** 10 percent or less human intervention on Fin across MLS help centers, with CRMLS meeting it at cutover. Baldwin is around 40 percent today (August 25 cutover-conversation sampling).
- **System of record:** the Notion project page, ID `3c88b9e0143880ec8fbee25ec0b38975` (https://app.notion.com/p/3c88b9e0143880ec8fbee25ec0b38975). When this repo and Notion disagree, Notion wins and the repo gets updated.
- **Fin-resolved, Perchwell definition:** Fin answered, no teammate sent a message on that conversation afterward, and no follow-up from the same member on the same topic within 48 hours. Report it weekly alongside Intercom's own resolution number, kept separate, never blended.

## Milestones

| Date | Milestone |
|---|---|
| September 4, 2026 | Help center standards and Fin labeling strategy finalized |
| September 11, 2026 | Content audit finalized and prioritized; backlog set |
| September 18, 2026 | Required article updates and new content completed |
| September 25, 2026 | Required visual and video updates completed |
| October 2, 2026 | Fin answer quality and content QA validated; maintenance process documented |

## What lives where

- `docs/` - `project-status.md` (contacts, current status, open questions) and `decisions.md` (what was decided and why). Update these, do not append to them.
- `audit/` - The article-by-article audit of Baldwin and CRMLS content: recommendation, rationale, and priority per article. Kelly owns the Baldwin audit.
- `golden-questions/` - The golden question set mined from real member conversations, used to test Fin. Built by `/golden-questions`.
- `qa/` - The 14-factor content-readiness checklist results and Fin answer-quality test runs.
- `fin-reports/` - Weekly Fin resolution reports using the Perchwell definition.
- `outputs/` - Finished deliverables, including article drafts under `outputs/drafts/`. Do not read this folder unless asked.
- `confidential/` - Raw conversation excerpts and anything with a member name, email, phone, or address. Git-ignored.

## Working rules

- Read `docs/standards/` before drafting or rewriting any article. If a standards file is still a placeholder, say so and fall back to the skill's bundled rules.
- Every article recommendation in the audit needs a rationale and a priority, not just a verdict.
- Golden questions and QA results must be free of member identifiers before they leave `confidential/`.
- Fin numbers always state which definition they use.
- This workstream can be archived after October 2, 2026. Evergreen content (macros, standards) belongs in `workstreams/support-ops/` or `docs/standards/`, not here.
