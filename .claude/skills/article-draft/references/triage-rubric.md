# Triage Rubric: Release Notes to Help Center Changes

Run this after extracting the feature facts and before drafting anything. The output is a triage table and one of four decisions, presented to the user for confirmation.

## Step 1: Extract feature facts

Fill this table from the release notes. Mark anything the notes do not say as `[confirm: ...]`. Do not fill gaps from memory or by guessing at UI labels.

| Fact | Value |
|---|---|
| Feature name (as the reader will see it) | |
| Product area (Notion `Product Area (Internal)` value) | |
| Entry point (page, menu, button path) | |
| Primary task the reader completes | |
| Steps, in order | |
| Options and their defaults | |
| Limits (counts, dates, roles, plans) | |
| What is saved automatically or cannot be undone | |
| Roles affected (All, Agent, Admin / Broker, Invited client, All - but client) | |
| MLS scope (Baldwin only, All Regions, other) | |
| Related existing features it touches | |
| Media available (Loom, Arcade, screenshots) | |

## Step 2: Find candidate articles

Query the Notion Master Article List using the SQL in `notion-publishing.md`:

1. By `Resource Title LIKE '%<keyword>%'` for two or three keywords from the feature name and the entry point. This is the most reliable query.
2. By `Collection in Intercom` for the collection the feature belongs in.
3. By `Product Area (Internal)` matching the feature's area. Treat this as a supplement: tagging is inconsistent (Tags articles sit under both `Client Collaboration` and `Property Details`), so never rely on it alone.
4. Any row from the queries above whose `Update Status` is `Update Needed`, `Update needed 7/20`, or `Update needed 8/3` (these are already flagged and may absorb this change).

Filter MLS with `"MLS" LIKE '%Baldwin%' OR "MLS" LIKE '%All Regions%'`; many live Baldwin articles are tagged `All Regions` as well. Rows with a `NYC|` or `CRMLS|` title prefix belong to other help centers and are only relevant as phrasing references.

Exclude rows with `HC Status` of `Deprecated ❌` or `Remove from HC` unless the release resurrects that workflow. Fetch the body of every remaining candidate with `HC Status` of `Live ✅`, `Transfer to Intercom`, `Draft`, or `Needs Review`.

If the Notion connector is unavailable, fall back to the local mirror (`docs/help-center/baldwin/README.md` or `docs/help-center/crmls/README.md`, then the article files) and say so in the report. The mirror is refreshed by `/sync-help-center`; check `sync-state.json` in that folder for the last run date.

## Step 3: Decide

Pick exactly one decision.

**A. New article.** Choose when any of these is true:
- The feature adds a new page, report type, object, or entry point that no Live or Draft article covers
- The reader's primary task is not the primary goal of any existing article
- Folding the feature into an existing article would give that article a second primary goal or push it past roughly five major sections
- The feature has its own roles or MLS scope that differ from the closest existing article

**B. Update existing article(s).** Choose when the release changes something inside a workflow that already has an article:
- Step order, button or menu labels, or entry point changed
- A default, limit, or validation rule changed
- A new option or setting appears inside an existing flow
- A statement in the live article is now false (for example "clients cannot be removed from a Tag")
- A screenshot or video shows the old state

**C. Both.** Choose when A applies and one or more existing articles either describe the old behavior, would benefit from a 📖 cross-link to the new article, or list features in an overview or FAQ that should now include the new one. Overview and FAQ articles for the area are the usual candidates.

**D. No help center change.** Choose when:
- The change is internal, admin-only with no reader-visible surface, or a performance or reliability fix
- The behavior is already documented accurately
- The feature is not yet enabled for the MLS in scope (note the expected date in `Upcoming Feature & Dates` instead)

When torn between A and B, prefer B if the existing article stays under one primary goal, and A otherwise. Duplicate articles hurt search more than a slightly longer article does.

## Step 4: Present the triage table

Show this before drafting and wait for confirmation, unless the user already said to draft without checking.

```
Decision: <A | B | C | D> <one-line reason>

| Candidate article | HC Status | Update Status | Why it is affected | Action |
|---|---|---|---|---|
| <title> (<notion url>) | Live ✅ | Updated ✅ | Describes the old default | Update: section "<heading>" |
| <title> | Live ✅ | Update Needed | Overview lists reports; add the new one | Update: add bullet + 📖 link |
| (new) <proposed title> | | | No article covers <task> | New article |

Open items: [confirm: ...]
```

## Step 5: Scope the update

For every article marked Update:
- Change only the sections the release touches. Never reproduce untouched sections; the change sheet lists edits, and includes full text only for sections that are new or rewritten end to end.
- Quote the current text in the change list so a reviewer can find it in Intercom.
- If the article predates the current style rules, do not restyle the whole thing in the same pass. Note "article predates current style; full rewrite recommended separately" in Open items and keep the change list tight.
- Never edit the live Notion page directly. The proposal goes in a sibling Draft page (see `notion-publishing.md`).
