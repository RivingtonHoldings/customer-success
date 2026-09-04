# Notion Publishing: Perchwell Help Center Database [Sep 2026]

The CS team created a new Notion database for the September 2026 help center project, to simplify the work and make the state of each article obvious. It is the system of record for this project.

**The rule for the rest of the project:** articles this project drafts or updates are added to the new database. The old Master Article List is read-only. Query it for history and triage, never write to it, and do not mirror a change into it.

Intercom is downstream of both: approved Notion pages are transferred to Intercom as unpublished drafts by hand, and a human publishes them there. Fin reads published articles only.

## IDs

| Thing | Value |
|---|---|
| Perchwell Help Center Database [Sep 2026] | `https://app.notion.com/p/3d18b9e0143880558dc9d9574f5abab8` |
| Data source (use for SQL and create-pages) | `collection://3d18b9e0-1438-80cc-ab0f-000bf0fc1389` |
| Data source ID (for `parent.data_source_id`) | `3d18b9e0-1438-80cc-ab0f-000bf0fc1389` |
| Template Article (the standard as a fill-in page) | `https://app.notion.com/p/3d18b9e0143880189917f12bdc34c500` |
| Notion project page (system of record for the project) | `https://app.notion.com/p/3c88b9e0143880ec8fbee25ec0b38975` |
| Article & Collection Naming Standards | `https://app.notion.com/p/3ce8b9e0143881b790c6c7c29eb11009` |
| Perchwell Product Style Guide | `https://app.notion.com/p/2a48b9e014388092a38cd7d1f4b4cb60` |
| Baldwin public help center | `https://support.perchwell.com/baldwin/en` |
| Master Article List (old, read-only) | `collection://1c78b9e0-1438-80b8-951d-000bc128f119` |

Before the first Notion write in a session, read `notion://docs/enhanced-markdown-spec` with the Notion connector's fetch tool so the body markdown is valid. Tool names are in `docs/connector-tools.md`; the server ID differs per teammate, so match on the tool name, not the full prefix.

## Schema

Seven properties. `Last updated` is system-managed; do not set it.

| Property | Type | Values |
|---|---|---|
| `Article Name` | title | The article title, matching the title in the body exactly |
| `Article Status` | status | `New Article Request`, `Draft`, `Ready to Transfer`, `Live in Intercom`, `Deprecated` |
| `MLS/AOR` | select | `Baldwin`, `CRLMS All`, `NYC` |
| `Collection` | select | `Getting Started Guide`, `Then vs. Now`, `Dashboard`, `Search`, `Tags`, `Client Collaboration`, `Manage People`, `Manage Listings`, `Reports`, `Analytics`, `User Settings`, `Client Experience`, `FAQs`, `Mobile`, `What's New`, `Integrations` |
| `Roles` | select | `All`, `Agent`, `Admin/Broker`, `Invited Client`, `All Except Client` |
| `Videos` | select | `Yes`, `No` |
| `Visuals` | select | `Yes`, `No` |
| `Last updated` | last_edited_time | Read only |

Every property except `Article Name` is a single select, so an article belongs to exactly one collection, one MLS, and one role group. An article that needs two collections needs splitting, or a decision from the user about which one wins.

Two open items for the team, flagged rather than worked around:

- The new database has no equivalent of the old `Fin AI`, `Text`, `Screenshot`, or `Video` workflow-status fields. `Videos` and `Visuals` record whether the article has them, not whether they are done. `docs/standards/fin-labeling.md` derives Fin labels from Notion fields, so it now derives them from `MLS/AOR` and `Collection`.
- The `MLS/AOR` option reads `CRLMS All`. If that is meant to be CRMLS, the option needs renaming in Notion; use the string exactly as it appears until then, since a select write with an unknown option fails.

## Triage queries

Query the new database first with the Notion connector's query-data-sources tool. The table name in SQL is the data source URL in double quotes.

By collection:

```sql
SELECT "Article Name", "Article Status", "MLS/AOR", "Collection", "Roles", url, "Last updated"
FROM "collection://3d18b9e0-1438-80cc-ab0f-000bf0fc1389"
WHERE "Collection" = ?
  AND "Article Status" != 'Deprecated'
ORDER BY "Last updated" DESC
```

By title keyword (run once per keyword, binding `%keyword%`):

```sql
SELECT "Article Name", "Article Status", "MLS/AOR", "Collection", url
FROM "collection://3d18b9e0-1438-80cc-ab0f-000bf0fc1389"
WHERE "Article Name" LIKE ?
ORDER BY "Last updated" DESC
```

By MLS:

```sql
SELECT "Article Name", "Article Status", "Collection", url
FROM "collection://3d18b9e0-1438-80cc-ab0f-000bf0fc1389"
WHERE "MLS/AOR" = ?
ORDER BY "Last updated" DESC
```

The new database only holds what this project has touched, so an article that exists in the live help center may have no row yet. When a keyword search comes back empty, check the mirror in `docs/help-center/`, then the old Master Article List for the article's history:

```sql
SELECT "Resource Title", "HC Status", "Update Status", "MLS", "Help Center URL (Public)", url
FROM "collection://1c78b9e0-1438-80b8-951d-000bc128f119"
WHERE "Resource Title" LIKE ?
ORDER BY "Last Updated" DESC
```

That query is for reading only. When an article with an old row needs work, create a new row in the new database and carry the facts across. Leave the old row alone.

## Creating a page

Confirm once with the user before writing: a compact summary of the page and its properties, then wait for "go."

```
Creating 1 Draft in the Perchwell Help Center Database [Sep 2026]:
- Create a Market Conditions Addendum Report (1004MC)
  Article Status: Draft | MLS/AOR: Baldwin | Collection: Reports
  Roles: All Except Client | Videos: No | Visuals: Yes
Go?
```

Call shape:

```json
{
  "parent": { "type": "data_source_id", "data_source_id": "3d18b9e0-1438-80cc-ab0f-000bf0fc1389" },
  "pages": [{
    "properties": {
      "Article Name": "<title>",
      "Article Status": "Draft",
      "MLS/AOR": "Baldwin",
      "Collection": "<collection>",
      "Roles": "<role>",
      "Videos": "<Yes or No>",
      "Visuals": "<Yes or No>"
    },
    "content": "<Notion markdown body>"
  }]
}
```

`Videos` and `Visuals` record whether the finished article will carry them, so a draft with screenshot placeholders is `Visuals: Yes`. Do not pass `template_id` together with `content`; the skill writes the full body itself.

## Publishing an update change sheet

Never overwrite a page whose `Article Status` is `Live in Intercom`. The change sheet is one page for the whole release.

If the user names a target page, write the sheet there with the Notion update-page tool (`insert_content` at the end, or `replace_content` if the user says the page is empty or theirs to overwrite). Otherwise create one sibling row in the new database:

- `Article Name`: `Help center changes: <feature> (YYYY-MM-DD)`
- `Article Status`: `Draft`
- `MLS/AOR` and `Collection`: from the release note's target
- `content`: the change sheet body

Notion shape for the sheet: a one-line intro, an `##` heading per article with the Notion page mentioned via `<mention-page>`, plain bullets for edits using `->`, an `###` heading plus final-form text only for new or rewritten sections, and one `## Open items` list. No callouts or tables in the sheet.

After publishing, offer to set the affected rows' `Article Status`. Only do it when the user says yes.

## Markdown to Notion mapping

The repo file is plain markdown. Convert when building `content`:

| Repo markdown | Notion markdown |
|---|---|
| `# Title` line at the top | Omit. The title lives in `Article Name` |
| `<!-- Article Status: ... -->` metadata comment | Omit |
| `**Description:** text` | Keep as the first paragraph, `**Description:** text` |
| Opening `Use this article to ...` paragraph | Keep as an ordinary paragraph, no heading above it |
| `## Section` / `### Subsection` / `### Steps:` | Unchanged |
| `> **Note:** text` | `<callout color="gray_bg">` then a tab-indented line `**Note:** text`, then `</callout>` |
| `> **Important:** text` | `<callout color="yellow_bg">` with the same shape |
| `> **Tip:** text` | `<callout color="gray_bg">` with the same shape |
| A link to a related article | An ordinary sentence with a markdown link, or `<mention-page url="<notion url>"/>` when the target is a Notion page |
| A bare Loom or Arcade URL under the opening paragraph | `<video src="<url>"></video>` |
| `> Video placeholder: ...` / `> Screenshot placeholder: ... | Alt text: ...` | `<callout color="orange_bg">` with the placeholder text, so owners can spot it |
| Markdown image with alt text | Keep the alt text; it is required |
| Markdown table | `<table header-row="true">` with `<tr>` and `<td>` rows; cells hold plain rich text |
| Blank lines | Drop them. Notion spaces blocks itself; use `<empty-block/>` only if a visual gap is essential |
| Em dashes | Must not exist. Fix before converting |

There is no support footer and no `In this article:` heading to convert. Both were retired on September 4, 2026.

Escape `*`, `[`, `]`, `<`, `>`, `|`, `{`, `}` when they appear as literal text outside markdown syntax (for example `1004MC / Form 71 [MC]` needs `\[MC\]`).

## After publishing

Report the new page URL(s). Remind the user that the remaining steps are manual and owned by CS: peer review, moving the row to `Ready to Transfer`, transferring to Intercom, setting the Fin labels, assigning the MLS audience, and publishing.
