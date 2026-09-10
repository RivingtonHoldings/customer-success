# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this repo is

The shared Claude Code workspace for the Perchwell Customer Success team. Tara, Kelly, Rafe, Jeff, and Leo use it from the Claude Code desktop app to write and maintain help center content, mine member questions, and keep the Intercom help centers in good shape for Fin. Nobody on the team is an engineer; treat every user as a support writer, not a developer.

Notion and Intercom are provided by claude.ai connectors, not by anything in this repo. Each teammate connects them once in claude.ai under Settings, then Connectors. If a Notion or Intercom tool is missing from a session, the teammate has not connected it yet; say so in plain language and point them at the README. Do not look for an `.mcp.json` and do not create one. The exact tool names live in `docs/connector-tools.md`.

## Perchwell quick reference

- **Product:** Perchwell is the MLS platform members use to search listings, enter and manage listings, run reports, and collaborate with clients. One codebase, web and mobile at full parity.
- **Members:** Real estate agents, brokers, brokerage admins, MLS staff, and invited clients. "Member" is the word for a person using Perchwell through their MLS.
- **In scope for this project:** Baldwin (cut over from Paragon on August 3, 2026) and CRMLS (cutover upcoming, migration source being confirmed).
- **Features members ask about most:** Search and SearchWell (natural language search), Add/Edit (listing entry), Saved Searches and alerts, Hotsheets, Tags, Client collaboration, Reports and CMAs, Print and Export CSV, Dashboard widgets, Contacts and the My MLS roster, Mobile.
- **Support surfaces:** Help centers on support.perchwell.com (one per MLS), Intercom chat and email, and Fin, the Intercom AI agent that answers from help center articles.

Full support-writing reference, glossary, and terminology rules: `docs/product-context.md`.

## Support voice

Two registers. Pick the one that matches the artifact.

### Help center articles

Matter-of-fact and instructional. The reader is a busy real estate professional who wants the answer, not a pitch.

- Second person, imperative. "Click **Actions**," not "You can click Actions."
- One action per numbered step. Never combine a click, a tab, and a scroll in one step.
- Name and bold the exact UI element the reader sees.
- Screenshot placeholders in brackets where an image belongs: `[Screenshot: the Actions menu with Print highlighted]`.
- State defaults, limits, and anything that cannot be undone.
- No marketing adjectives. Describe what the feature does, not how great it is.

### Conversation replies and macros

Friendly and competent. The member may be brand new to Perchwell and not technical, so walk them through one click at a time as if helping someone print a document over the phone.

- Warm opening that answers the question in the first sentence.
- Plain words, short sentences, "you can" is fine here.
- Say where on the screen the element sits ("on the upper right").
- Close with one short invitation to follow up.

### Rules for both registers

- Never use em dashes. Use commas, periods, colons, or semicolons.
- Never use horizontal rules in output files.
- Translate system terms into what the member sees with a "which means" clause. "Fin reads from published articles only, which means a draft article will not change Fin's answers."
- Hedge predictions about member behavior. "Members may ask" beats "members will ask."
- Pair every "don't say X" with "say Y instead."
- Articles never name a legacy platform. Members came from different systems depending on their MLS, and one article serves several, so write "a legacy platform" and keep the legacy feature name the member would recognize: "Members who came from a legacy platform may know the Universal Search Bar as Power Search." Conversation replies and macros are the exception; you know which MLS you are talking to, so name their platform. Never "old system," "retired," or "sunsetted."

## Operational doc conventions

For runbooks, Q&A docs, project status pages, and anything staff-facing:

- Roles and contacts at the top, with title and hyperlinked email on first mention: `[support@perchwell.com](mailto:support@perchwell.com)`, never backticks.
- Scenario labels A, B, C when a question has more than one root cause, each with its own member-facing snippet.
- Audience-named blocks: "Internal note" for staff only, "Email snippet" for member-facing text, "Context and escalation" back to staff. Avoid vague labels like "Short answer."
- Lead with what the doc is, not what it is not.

## The three systems

| System | Role | Who writes there |
|---|---|---|
| This repo | Standards, automations (skills), and a read-only mirror of the Intercom articles | Claude, on the teammate's behalf |
| Notion | Collaborative review layer. Drafts go here for the team to comment on and approve | Claude creates and updates draft pages freely |
| Intercom | Production. What members see and what Fin reads from | Humans publish. Claude pushes drafts only under the rules below |

## Write rules, as a ladder

Each rung requires more than the one before it.

1. **Notion draft pages:** created and updated freely. No confirmation needed beyond the normal "here is what I am about to create" summary.
2. **New Intercom articles:** pushed only after the Notion draft is approved, and always in `draft` state. Publishing is a human action inside Intercom. Claude never sets an article to published.
3. **Updates to live Intercom articles:** require all four of these, every time:
   - a full before-and-after diff shown in the conversation,
   - explicit confirmation per article. "Yes to all" is not accepted; ask again for each one,
   - an entry in `docs/help-center/changelog.md`,
   - a mirror re-sync with `/sync-help-center` afterward.
4. **Never:** Claude does not write conversations, contacts, companies, or macros in Intercom. Macros are drafted in the repo and a human creates them in Intercom.

Until the team turns pushes on, target September 11, 2026, this repo is read-only toward Intercom. Rungs 2 and 3 are documented so the skills are ready, not so they run today. The Intercom article write tools are on the ask list in `.claude/settings.json` so they always prompt.

## Privacy

Member names, emails, phone numbers, and addresses never appear in committed files. Raw conversation excerpts, exports, and anything quoting a member verbatim go in a `confidential/` folder, which is git-ignored. Before saving any file outside `confidential/`, strip identifiers and replace them with neutral placeholders like "the member" or "[email]". When in doubt, put it in `confidential/`.

## Git

Teammates never run git. Claude does it for them:

- At session start, offer to pull the latest from main (`/setup-check` does this).
- At session end, offer to commit and push, with a one-line message describing the work.
- Before committing, check `git status` for anything under a `confidential/` folder or anything containing a member name or email, and leave it out.

## Knowledge management

This repo is the team's second brain for help center work. Keep it useful for someone picking the work up cold.

- **Ask before writing to team docs.** At the end of a conversation, summarize what seems worth capturing and let the user decide.
- **Keep docs current, not cumulative.** Update the existing file. Remove stale information instead of stacking new paragraphs on old ones.
- **Separate instructions from facts.** `CLAUDE.md` files hold goals, rules, and tone. `docs/` folders hold facts, status, contacts, and decisions.
- **Never read an `outputs/` folder unless asked.** Outputs are deliverables, not context.
- **Where things go:** cross-team rules in this file; project rules in the workstream `CLAUDE.md`; facts in the workstream `docs/`; reusable procedures in `.claude/skills/`; personal Claude memory stays outside the repo.

## Repository structure

- `README.md` - Ten-minute setup guide for a teammate who has never used a terminal.
- `docs/product-context.md` - Support-writing reference: what Perchwell is, features, glossary, terminology rules.
- `docs/connector-tools.md` - Exact Notion and Intercom tool names from the claude.ai connectors. `settings.json` references these.
- `docs/standards/` - Content standards, Fin labeling strategy, the golden questions (Intercom's 14 content readiness factors every article must pass), and the Fin-readiness scorecard that scores an article 0 to 100 on top of them. The skills read these before drafting.
- `docs/help-center/baldwin/` and `docs/help-center/crmls/` - Read-only mirror of the live Intercom help centers, one markdown file per article, refreshed by `/sync-help-center`.
- `docs/help-center/changelog.md` - One line per change to a live article.
- `docs/build-log.md` - How this repo was built and every judgment call made along the way.
- `workstreams/help-center-overhaul/` - The September 2026 standardization project. Has its own `CLAUDE.md`, plus `docs/`, `audit/`, `qa/` (one scorecard per article), `fin-reports/`, `outputs/`, and `confidential/`. Archive after October 2, 2026.
- `workstreams/support-ops/` - Evergreen support content that outlives any project: macro drafts and their index.
- `.claude/skills/` - Shared skills: setup-check, sync-help-center, article-draft, article-rewrite (also migrates an old Master Article List page into the new Notion database and scores it), intercom-macros, humanizer, skill-creator, learn-and-update-repo.
- `.claude/commands/` - One slash command per skill.
- `.claude/settings.json` - Shared permissions: connector reads and Notion page writes are allowed, Intercom article writes always prompt, conversation writes are denied.

**Working in a workstream:** open the repo root in the Claude Code desktop app. Claude reads this file plus the workstream `CLAUDE.md` when it works inside that folder.
