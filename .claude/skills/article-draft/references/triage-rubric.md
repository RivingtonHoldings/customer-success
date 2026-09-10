# Triage Rubric: Release Notes to Help Center Changes

Run this after extracting the feature facts and before drafting anything. The output is a triage table and one of four decisions, presented to the user for confirmation.

## Step 1: Extract feature facts

Fill this table from the release notes. Mark anything the notes do not say as `[confirm: ...]`. Do not fill gaps from memory or by guessing at UI labels.

Gathering a fact is not the same as publishing it. `Roles affected` feeds the Notion `Roles` property always, and the article body only when a role gates the workflow. `Limits` feeds the article only where a member will hit the limit, written as the route forward. See `docs/standards/content-standards.md`.

| Fact | Value |
|---|---|
| Feature name (as the reader will see it) | |
| Collection (Notion `Collection` value) | |
| Entry point (page, menu, button path) | |
| Primary task the reader completes | |
| Steps, in order | |
| Options and their defaults | |
| Limits (counts, dates, roles, plans) | |
| What is saved automatically or cannot be undone | |
| Roles affected (All, Agent, Admin/Broker, Invited Client, All Except Client) | |
| MLS scope (Baldwin, CRLMS All, NYC) | |
| Related existing features it touches | |
| Media available (Loom, Arcade, screenshots) | |

## Step 2: Find candidate articles

Query the Perchwell Help Center Database [Sep 2026] using the SQL in `notion-publishing.md`:

1. By `Article Name LIKE '%<keyword>%'` for two or three keywords from the feature name and the entry point. This is the most reliable query.
2. By `Collection` for the collection the feature belongs in.
3. By `MLS/AOR` for the MLS in scope.

Exclude rows whose `Article Status` is `Deprecated` unless the release resurrects that workflow. Fetch the body of every remaining candidate.

The new database only holds what this project has touched, so an empty result does not mean the article does not exist. Check the mirror next, then run the read-only history query against the old Master Article List in `notion-publishing.md`. An article with only an old row still gets a new row in the new database when it needs work; the old row is never updated.

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

| Candidate article | Article Status | Where it lives | Why it is affected | Action |
|---|---|---|---|---|
| <title> (<notion url>) | Live in Intercom | New database | Describes the old default | Update: section "<heading>" |
| <title> | (old row only) | Master Article List | Overview lists reports; add the new one | Update: add bullet and a link, new row in the new database |
| (new) <proposed title> | | | No article covers <task> | New article |

Open items: [confirm: ...]
```

## Step 5: Scope the update

For every article marked Update:
- Change only the sections the release touches. Never reproduce untouched sections; the change sheet lists edits, and includes full text only for sections that are new or rewritten end to end.
- Quote the current text in the change list so a reviewer can find it in Intercom.
- Bring the sections you touch up to `docs/standards/content-standards.md`, but do not restyle the whole article in the same pass. Note "article predates the September 2026 standard; full rewrite recommended separately" in Open items and keep the change list tight.
- Never edit a live Notion page directly, and never write to the old Master Article List. The proposal goes in a Draft page in the new database (see `notion-publishing.md`).
