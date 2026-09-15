# Starting prompt for an article rewrite

A paste-ready prompt for kicking off `/article-rewrite`, and what to put in it. Written September 15, 2026, from what actually caused rework across the first four migrated articles.

The prompt is short on purpose. `/article-rewrite` reads `docs/standards/content-standards.md`, the golden questions, the Fin-readiness scorecard, and `docs/product-context.md` before it writes a word, so pasting the rules into your prompt adds nothing and starts a second copy of the rulebook drifting. `references/style-rules.md` is the tombstone for the last time that happened.

Your prompt's job is to supply what the skill cannot know.

## Where the edits actually came from

Across Universal Search Bar, Dashboard Overview, Customize Your Dashboard, and Add a Hot Sheet to the Dashboard, the correction commits cluster in five places. Three of them are now automatic. Two still need you.

| What caused the edit | Handled by | You supply |
|---|---|---|
| Wrong button labels, panel contents, modal fields | nothing can catch this | **screenshots** |
| Jargon and stiff phrasing | the plain language gate | nothing |
| Inconsistent names across related articles | the set-consistency pass, if told the set | **which articles it sits with** |
| Bare-noun title kept or changed | nothing | **your call, up front** |
| Invented facts that read plausibly | the sourcing rules | **what you verified yourself** |

Screenshots are the big one. About a third of the corrections traced to a product detail nobody could see from the sources: `Manage Widgets` was capitalized wrongly in eight of the nine places it appeared across both live help centers, the Edit hot sheet modal has five Days boxes where the draft described one field, and `From saved search` sits above `New hot sheet`, which reversed the order of two sections.

## The template

```
/article-rewrite <Notion URL or docs/help-center/... path>

MLS: <Baldwin | CRMLS>
Set: <articles this one sits with, or "standalone">
Title: <keep "<current title>" | propose a task-led one>
Screenshots: <attached, and what each one shows>
I verified in the product: <facts you checked yourself>
I can't verify: <things to mark [confirm:] rather than guess>

Flag anything you'd have to invent before you write it, not after.
Where you chose between two wordings, show me both and why.
```

The last two lines are the only instructions worth adding, because they change the shape of the work rather than repeat a rule already in the standard.

**"Flag anything you'd have to invent before you write it"** stops a false fact at the door. Two reached the first migrated draft because the more confident sentence reads better and nothing marks it as new: "Results populate as you type" became "results appear in a panel below the field", and "statuses like Active, Pending, Closed, and Expired" became "Listings in every status appear".

**"Show me both and why"** surfaces the judgment calls. This is how the good edits happened anyway: you proposed a wording, asked whether it held against the standard, and the better half of each version survived. "Unlike other widgets" became "Unlike the checkboxes" that way, and the Hot Sheet opening got shorter than either draft.

## Filled in

```
/article-rewrite https://app.notion.com/p/1c88b9e014388069925acd9f0fe35189

MLS: Baldwin
Set: sits with Dashboard Overview and Customize Your Dashboard. Keep the
     widget name, the verbs, and the order of the two Hot Sheet types
     consistent across all three.
Title: keep "Add a Hot Sheet to the Dashboard"
Screenshots: both Edit hot sheet modals, one per type, plus the Hot Sheets
     widget as it first opens
I verified in the product: Confirm is the button, not Save; statuses come
     pre-selected; Timeframe has defaults of 1, 7, and 30
I can't verify: whether the 998-day cap is per timeframe or total

Flag anything you'd have to invent before you write it, not after.
Where you chose between two wordings, show me both and why.
```

## One line, when you are moving fast

```
/article-rewrite <url> - Baldwin, sits with <x> and <y>, keep the title, screenshots attached. Flag invented facts before writing.
```

## Mode hints

Append any of these to the prompt:

- **`no notion`** rewrite and score, save the files, skip the Notion page
- **`score only`** score the article as it stands, no rewrite. This is the one for ranking the audit backlog
- **`just do it`** skip the source-difference and title confirmations and go straight to the Notion summary

## What to leave out

Do not paste the voice rules, the plain language do-not list, the 14 golden questions, or "make it sound human". All of them run automatically, and the plain language gate reports pass or fail with every flagged term and its replacement, next to the golden questions and never blended into them.

If an article passes both gates and still reads wrong to you, that is a defect in the rule rather than in the article. Say so, because the four finished articles are the fixture the rules were tested against and a rule that flags one of them is wrong.

## Related

- `notion-ai-prompt.md` in this folder: the same rules as a paste-ready prompt for editing directly in Notion AI, for when you are not in Claude Code
- `docs/standards/content-standards.md`: the rulebook the skill reads
- `workstreams/help-center-overhaul/docs/decisions.md`: why each rule exists
