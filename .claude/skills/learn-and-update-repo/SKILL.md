---
name: learn-and-update-repo
description: "After completing any task, use this skill to review the session, extract learnings from the user's refinements, and update the skills and workstream knowledge so future outputs are better. Use this whenever the user says 'learn from this,' 'update the repo,' 'capture what we learned,' 'improve the skills,' or 'let's do a retro.' Also use when the user finishes a substantial task and wants to make sure the learnings are preserved for next time."
---

# Learn and Update Repo

You just finished a task with the user. They refined your output through feedback, and now they want to capture what was learned so the system gets smarter. Your job is to review the conversation, extract the learnings, and propose updates to the right files.

## Why This Matters

Every refinement the user makes is a signal. If you wrote a help center step that combined two clicks and they split it, or a macro opening that buried the answer and they moved it to the first line, that is not a one-time fix. It is a pattern that should be encoded into the skill that produced it, so the next session starts closer to the final output. The goal is that over many sessions, first drafts become final drafts.

## Step 1: Review the Session

Read through the full conversation and identify:

- **What was the task?** (an article draft, a rewrite, a macro set, a golden question run, a QA pass)
- **Which skills were involved?** (`/article-draft`, `/article-rewrite`, `/intercom-macros`, `/golden-questions`, `/sync-help-center`, and so on)
- **Which workstream does this belong to?** (`workstreams/help-center-overhaul/` or `workstreams/support-ops/`)
- **What refinements did the user make?** Look for:
  - Direct corrections ("don't do X", "change this to Y")
  - Rejected approaches (structures they replaced, phrasing they cut)
  - Preferences expressed ("this one is right", "keep it like this")
  - New information introduced (facts, product details, decisions that improved the output)

## Step 2: Extract Learnings

For each refinement, write it down as:
- **What happened:** The initial approach or output
- **What should have happened:** The user's preferred approach
- **Why:** The reasoning (stated or inferred)
- **Is this generalizable?** Would this apply to future tasks of this type, or was it specific to this one output?

Only keep generalizable learnings. Discard one-off corrections that will not recur.

## Step 3: Present and Ask

Show the user a summary of the learnings you extracted, organized by where they would be applied. Then ask which categories they want to update.

The four layers, from most general to most specific:

**Support voice and shared rules (root `CLAUDE.md`):**
Rules that apply to everything the team writes. Examples: "never use em dashes," "one action per step," "translate system terms with a which-means clause," "hedge predictions about members."

**Standards (`docs/standards/`):**
Team-approved content standards, Fin labeling rules, and the QA checklist. These are owned by Tara with Rafe and Kelly as approvers, so propose the edit and flag that it needs their sign-off rather than applying it silently.

**Skills (`.claude/skills/`):**
Craft-level improvements that apply to anyone using the skill. Examples: "put the answer in the first sentence of a macro," "quote current text exactly in change sheets," "check the mirror before searching Intercom." Keep these product-agnostic where possible so the skill stays reusable for the next MLS.

**Workstream knowledge (`workstreams/*/docs/`):**
Facts, decisions, contacts, and context specific to a project. Examples: "CRMLS members are migrating from [platform]," "the Fin pass-rate target is X." Follow the knowledge management rules in the root `CLAUDE.md`: ask before writing, update existing files rather than creating new ones, separate instructions from facts.

Ask the user which categories they want to update. They may want all four, or just one or two.

## Step 4: Propose Specific Edits

For each selected category:

1. **Read the target file** before proposing changes
2. **Check for existing coverage.** If a learning is already captured (even partially), propose updating the existing content rather than adding a duplicate.
3. **Show the user exactly what you would change:**
   - Which file
   - Where in the file (which section)
   - The specific addition or edit
   - Why this change will improve future output
4. **Wait for approval** before making any changes

Keep additions concise. A learning that takes a paragraph to explain in conversation should become 1 to 3 lines in a skill file. The goal is actionable guidance, not documentation of the conversation.

## Step 5: Apply Changes

Once approved, make the edits. Then:
- Read each modified file to confirm the additions integrate cleanly
- Check that no em dashes were introduced
- Check that no horizontal rules (---) were added in output-facing content
- Check that no member name, email, phone number, or address was introduced
- Summarize what was updated

## What NOT to Capture

- Task-specific details (the actual article or macro that was written)
- Anything already in the output files (`workstreams/*/outputs/`)
- One-off corrections that will not recur
- Information that can be derived from the code or git history
- Learnings that duplicate what is already in the target file
- Anything from a `confidential/` folder

## When There's Nothing to Learn

Sometimes a session goes smoothly and the first output is close to final. If you review the conversation and find no generalizable refinements, say so. Do not force updates for the sake of updating.
