# Starting prompt for an article rewrite

A paste-ready prompt for kicking off `/article-rewrite`, and what to put in it. Written September 15, 2026, from what actually caused rework across the first four migrated articles. Revised September 22, 2026 after Integration Tools on the Dashboard, which removed two fields and added three.

The prompt is short on purpose. `/article-rewrite` reads `docs/standards/content-standards.md`, the golden questions, the Fin-readiness scorecard, and `docs/product-context.md` before it writes a word, so pasting the rules into your prompt adds nothing and starts a second copy of the rulebook drifting. `references/style-rules.md` is the tombstone for the last time that happened.

Your prompt's job is to supply what the skill cannot know.

## Where the edits actually came from

Across Universal Search Bar, Dashboard Overview, Customize Your Dashboard, and Add a Hot Sheet to the Dashboard, the correction commits cluster in five places. Three of them are now automatic. Two still need you.

| What caused the edit | Handled by | You supply |
|---|---|---|
| Wrong button labels, panel contents, modal fields | nothing can catch this | **screenshots** |
| Jargon and stiff phrasing | the plain language gate | nothing |
| Inconsistent names across related articles | the set-consistency pass | nothing; the skill runs the check |
| Bare-noun title kept or changed | nothing | **your call, and candidates to choose between** |
| Invented facts that read plausibly | the sourcing rules, plus the flag-first line | **answers, when the skill asks** |
| An article quietly growing a second surface | the hand-off table, for an Overview | **a yes or no on the proposed split** |
| A question spent on something you already knew was broken | nothing | **what is already known wrong** |

**Two of these changed on September 24, 2026, after Search Page Overview.** `Hands off:` is now optional on an Overview, because the skill computes the hand-off table itself and comes back with a proposal to approve rather than a question to answer; fill it in only when you already know the answer and want to skip the proposal. And `Screenshots:` is now "what changed", not "everything the article needs", because the skill reads the article's existing images first. Asking for shots the live article already carries cost a round on that migration, and the old images answered eight of fourteen open questions once they were read.

Screenshots are the big one. About a third of the corrections traced to a product detail nobody could see from the sources: `Manage Widgets` was capitalized wrongly in eight of the nine places it appeared across both live help centers, the Edit hot sheet modal has five Days boxes where the draft described one field, and `From saved search` sits above `New hot sheet`, which reversed the order of two sections.

**Integration Tools on the Dashboard, September 22, is the strongest case for screenshots so far, because nothing disagreed.** The old Notion page and the live article both listed SentriLock on the Dashboard Integrations panel and both omitted CRS Login. One screenshot showed SentriLock absent and CRS Login present, and also settled that `InfoSparks` is the right capitalization and that integrations open in a new tab rather than a new window. Two documents written from the same screen had gone stale together, which is the case `content-standards.md` covers under "Agreement between sources is not verification".

## Two fields that were removed, and why

**`I verified in the product:` and `I can't verify:` are gone.** On Integration Tools both were left blank and nothing was lost, because "flag anything you'd have to invent" produced seven specific questions and the teammate answered all seven in one message. That is the better order: the skill knows where its gaps are and the teammate does not, so asking the teammate to predict them in advance asks the wrong person. What replaced them is one clause promising an answer, which tells the skill to wait rather than write `[confirm:]` markers it will have to resolve later.

**`Set:` stopped being a declaration.** It read `standalone` on Integration Tools, and CRMLS turned out to hold a twin article with the identical title, 13921493. A grep of the mirror found it in seconds. The set is discoverable, so asking for it as a statement invites a confident wrong answer; it is now a hint, and the skill runs the collision and set checks either way.

## The template

```
/article-rewrite <Notion URL or docs/help-center/... path>

MLS: <Baldwin | CRMLS>
Covers: <the surface this article is for>
Hands off: <what belongs in another article, and which one. Optional on an
    Overview; the skill proposes a hand-off table for you to approve>
Title: <keep "<current title>" | propose 2 or 3 with the tradeoff for each>
Screenshots: <what has changed since the article's current images, attached.
    Cropped to exclude addresses, agent names, and license numbers>
Set: <articles it sits with, if you know. The skill checks for others>
Already known wrong: <anything live that is stale, and whether it is
    being fixed>

Flag anything you'd have to invent before you write it, not after, and ask
the product questions in one batch. I'll answer before you draft.
Where you chose between two wordings, show me both and why.
```

`Covers` and `Hands off` can be dropped when the article covers one surface and obviously stays there. Everything else earns its line.

The last two instructions are the only ones worth adding, because they change the shape of the work rather than repeat a rule already in the standard.

**"Flag anything you'd have to invent before you write it"** stops a false fact at the door. Two reached the first migrated draft because the more confident sentence reads better and nothing marks it as new: "Results populate as you type" became "results appear in a panel below the field", and "statuses like Active, Pending, Closed, and Expired" became "Listings in every status appear".

**"Show me both and why"** surfaces the judgment calls. This is how the good edits happened anyway: you proposed a wording, asked whether it held against the standard, and the better half of each version survived. "Unlike other widgets" became "Unlike the checkboxes" that way, and the Hot Sheet opening got shorter than either draft.

**"Ask the product questions in one batch. I'll answer before you draft"** is what turns a flagged unknown into a fact instead of a `[confirm:]` marker. Markers are a fallback for when nobody can answer; they still have to be resolved before transfer, so a marker written on Monday is a question asked twice. On Integration Tools the batch came back with seven answers and two scope decisions, and the draft was written once.

**Covering two surfaces is the failure this catches.** On Integration Tools the skill added a full listing-detail procedure in answer to one of its own questions, which quietly made a Dashboard-only title inaccurate, and nobody noticed for three exchanges. Naming the boundary up front is cheaper than discovering it during the title discussion. The fix, once seen, was to cut the second surface down to a pointer and keep the narrow title.

## Filled in

```
/article-rewrite https://app.notion.com/p/30a8b9e01438800c8c14d12b92c67987

MLS: Baldwin
Covers: the Integrations panel on the Dashboard
Hands off: integrations on a listing, to Listing Detail Page Overview.
     Name where they are and link out; do not repeat the steps
Title: keep "Integration Tools on the Dashboard", or propose 2 or 3
     task-led ones with the tradeoff for each
Screenshots: the Integrations panel revealed and collapsed, and the
     Actions menu on a listing with Integrations open. The listing one
     is cropped to exclude the address and the listing agent
Set: I think standalone, but check
Already known wrong: SentriLock is off the Baldwin panel and the team is
     looking into why. Write it as though it belongs there

Flag anything you'd have to invent before you write it, not after, and ask
the product questions in one batch. I'll answer before you draft.
Where you chose between two wordings, show me both and why.
```

That prompt is the September 22 one rewritten with hindsight. What the real prompt lacked cost four rounds on the title, one round rediscovering that SentriLock was broken, and a listing-detail section that had to be cut back down after it was written.

## One line, when you are moving fast

```
/article-rewrite <url> - Baldwin, keep the title, screenshots attached. Flag invented facts before writing and batch the questions.
```

## After the draft exists: "consider this"

The prompt above starts a rewrite. Once a draft is on the page, the fastest mode is not to ask for another pass but to paste your own wording and ask for a ruling:

```
Consider "<your sentence>"
Is that too repetitive or does it break any rules?
```

This worked better on September 22 than either side drafting alone. Of five rewrites pasted this way, three were straight improvements and went in unchanged, one needed a word restored, and one was declined with the rule named. The reason it works is that it splits the job along the line where each side is actually stronger: you know how it should read to an agent, and the skill knows which of the forty-odd rules the sentence is about to trip.

Two things make the ruling useful rather than agreeable:

- **Ask for the rule, not a verdict.** "Does it break any rules" gets a named rule and a score consequence. "Is this better" gets an opinion.
- **Expect a counter-proposal when the answer is no.** A declined sentence should come back with the smallest version that keeps your intent. "ShowingTime also appears directly on your listings in the Listings widget for listing-specific showing management" was declined for repeating a procedure that already had a home; what shipped was "ShowingTime also opens from the Listings widget, on listings that belong to you."

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
