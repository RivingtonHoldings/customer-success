---
name: intercom-macros
description: Turn new feature context, usually release notes, into paste-ready Intercom macros (canned responses) the CS team saves to answer member questions. Use this skill whenever the user mentions "macro," "macros," "canned response," "saved reply," "canned reply," "support responses for," "CS responses," "what should support say," "help CS answer questions about," or pastes release notes and asks how support should handle the questions a feature will generate, even if they never say the word Intercom. It anticipates the questions members are likely to ask, drafts one macro per question, cross-links help center articles from the local mirror, and saves drafts to workstreams/support-ops/macros/. Intercom is never written to.
---

# Intercom Macros

A macro is a canned response saved in the Intercom macro database. When a member asks a common question, a CS rep finds the macro by title and pastes it instead of composing an answer from scratch. This skill turns feature context, usually release notes, into a set of paste-ready macro drafts. CS adds the screenshots, creates the macros in Intercom, and owns them from there.

Two readers shape every macro. The **CS rep** finds it by searching titles, so the title must read the way members actually ask the question. The **member** may be brand new and non-technical, so the body walks them through the workflow one click at a time, as if helping a tech-illiterate person print a document over the phone. A step that feels too obvious to write down is almost always worth writing down.

## Inputs

- **Feature context** (required): release notes as pasted text, a repo path, or a Notion link. Read the whole thing before extracting.
- **MLS scope** (optional, default Baldwin): which customer's members will ask. Determines the title prefix and any transition voice.
- **Known questions** (optional): if CS has already reported what members are asking, those questions come first and anchor the set.
- **Mode hints** (optional): "just draft it" skips the question-list confirmation; "questions only" stops after the anticipated-question list.

If the release notes leave out a UI label, a default, a limit, or a step, do not invent it. Write `[confirm: <what is missing>]` inline and list every marker under Open items. A macro with two confirm markers is more useful than a fluent one that walks a member to a button that does not exist.

## Workflow

1. **Read context.** Read `references/macro-format.md` in full. Read the conversation register in the root `CLAUDE.md`. If the feature touches the Paragon transition, read the terminology rules in `docs/product-context.md`.
2. **Extract the feature facts.** From the release notes only: entry point, exact UI labels, step order, defaults, limits, side effects (emails sent, data changed, anything automatic), and who can see the feature. Every blank becomes a `[confirm: ...]` marker.
3. **Anticipate the questions.** List the distinct questions members are likely to ask, phrased the way a member would type them into chat. Sweep these categories; most features produce 2 to 5 questions, not one per category:
   - **How do I ...?** The core workflow, and any secondary workflow with its own entry point.
   - **Where is / where did ... go?** Anything moved, renamed, or replaced, especially for members coming from Paragon.
   - **Why did ... happen?** Side effects members notice before they notice the feature: an email their client received, a changed default, a new item in their UI.
   - **Can I still / how do I undo ...?** Old behavior members may want back, settings they can change, actions they can reverse.
   - **What happens to my ...?** Existing data, saved settings, things migrated or defaulted on their behalf.
   Present the question list with a one-line rationale each and wait for confirmation, unless the user said to just draft it. Questions CS already reported are included verbatim.
4. **Check for existing macros.** Read `workstreams/support-ops/macros/README.md`. If a macro already covers one of the questions, propose an update to that file instead of a duplicate.
5. **Find the related article.** Scan the local mirror index for the MLS in scope, `docs/help-center/baldwin/README.md` or `docs/help-center/crmls/README.md`, for a live article covering the workflow. The article file's frontmatter carries the public URL. If the mirror has nothing (or looks stale per `sync-state.json`), fall back to the read-only Intercom search tool `mcp__eff8e27b-83eb-43ee-befe-90e26bf3b57b__search_articles`; if that is unavailable or finds nothing, use the placeholder `[link: <article title>]` for CS to resolve. Never write to Intercom.
6. **Draft one macro per question**, following the format and worked examples in `references/macro-format.md`.
7. **Self-review.** Run the checklist at the end of `references/macro-format.md`. Also grep the draft for em dashes and horizontal rules; both are banned.
8. **Save and index.** See Saving the output.
9. **Report.** State the macro titles, the saved path, the open `[confirm: ...]` items, and the manual CS steps that remain: capture each screenshot placeholder with highlight boxes or arrows, create each macro in Intercom (New macro, paste, set **Available for** Everyone and **Available when** Starting conversations, Replying, Adding notes, Save), and personalize the closing line if they like.

## Rules

**Titles.** The title is the search key. Phrase it the way members ask: questions are welcome ("How do I hide the map?"), unlike help center article titles. Prefix with an ALL-CAPS keyword so related macros cluster in the list: the MLS name when the answer is MLS-specific (`BALDWIN- `), then or instead a short topic keyword (`CSV- `, `ALERTS- `). Example: `CSV- How can I create a CSV template?`

**Voice.** A friendly, competent support rep in chat, not documentation. "You can" is fine here; this is conversation, not a help article. Second person, plain words, short sentences. Name and bold the exact UI element the member sees. Paste direct URLs when the destination has one. State defaults, limits, and anything irreversible. Translate system terms with a "which means" clause. Hedge predictions about people ("clients may ask"). No em dashes, no horizontal rules, no marketing adjectives, no internal jargon. End with one short, warm closing line inviting follow-up.

**Steps.** Numbered, one action per step, starting from a page the member can always find (usually **Search** or a direct URL). Never skip a click, a tab, or a scroll. Include where on the screen the element sits ("on the upper right-hand side") because the member cannot see your screen.

**Screenshots.** Do not create images; CS owns them. After each step that directs the member somewhere on screen, add a placeholder on its own line telling CS exactly what to capture and what to highlight: `[Screenshot: <screen or menu state>. Highlight: <the element to box or arrow>.]`

**Accuracy.** Every fact traces to the release notes or a live article. Unknowns are `[confirm: ...]`, never guesses.

## Saving the output

- One file per feature release: `workstreams/support-ops/macros/YYYY-MM-DD-<feature-slug>-macros.md`, all macros inside, using the file template in `references/macro-format.md`.
- Append one line to the index in `workstreams/support-ops/macros/README.md` (create the file with a one-line header if it does not exist yet).
- Re-running on the same feature the same day overwrites the file and its index line. A later day creates a new dated file and the report links the previous one.

## Handoffs

- The feature also needs documentation: `/article-draft` drafts the article; a macro then links it.
- A macro reads stilted: run `/humanizer` on the saved file, then re-check the format checklist.
