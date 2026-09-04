# Notion Publishing: Master Article List

The CS team's source of truth for help center content is the Master Article List database inside the Master Resource Center in Notion. Every article, live or in progress, is a row. Intercom is downstream: approved Notion pages are transferred to Intercom as unpublished drafts (today by hand, later by the `/article-draft` push stub in `references/intercom-push.md` once the team turns pushes on), and a human publishes them there. Fin reads published articles only.

## IDs

| Thing | Value |
|---|---|
| Master Resource Center page | `https://app.notion.com/p/1c78b9e0143880ee9b21cd479d6e248e` |
| External Resource Center Hub (database) | `https://app.notion.com/p/1c78b9e01438802082c4eb08025fbb0a` |
| Master Article List (data source, use for SQL and create-pages) | `collection://1c78b9e0-1438-80b8-951d-000bc128f119` |
| Data source ID (for `parent.data_source_id`) | `1c78b9e0-1438-80b8-951d-000bc128f119` |
| Workflow Article Template (page template) | `2ca8b9e014388058a52fdb91f3a06609` |
| Navigation Article Template (page template) | `1c78b9e0143880b6a5becf3ec8d28c1b` |
| One Pager Author Style Guide | `https://app.notion.com/p/2ca8b9e014388073aa29fba8407a5684` |
| SEO Guidelines for Help Center Articles | `https://app.notion.com/p/2ca8b9e0143880b28d8edeeb89d597a1` |
| Master Article List SOP | `https://app.notion.com/p/2c98b9e01438803eb60dc494bba29e47` |
| Baldwin public help center | `https://support.perchwell.com/baldwin/en` |

Before the first Notion write in a session, read `notion://docs/enhanced-markdown-spec` with `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-fetch` so the body markdown is valid.

## Schema (properties the skill sets or reads)

| Property | Type | Values the skill uses |
|---|---|---|
| `Resource Title` | title | The article title, Title Case, no gerund |
| `HC Status` | status | `New Article Request`, `Draft`, `Needs Review`, `Peer Review Complete`, `Transfer to Intercom`, `Live ✅`, `Deprecated ❌`, `Remove from HC` |
| `Update Status` | status | `New Article Request`, `Update Needed`, `Draft`, `Needs Review`, `Peer Review Complete`, `Transfer to Intercom`, `Updated ✅`, `Update needed 7/20`, `Update needed 8/3`, `Deprecated ❌`, `Remove from HC` |
| `MLS` | multi_select | `Baldwin`, `CRMLS`, `NYC`, `ICAAR`, `All Regions` |
| `Which HC is it in` | multi_select | same options as MLS plus `None` |
| `Product Area (Internal)` | select | `Search`, `Dashboard`, `Property Details`, `Listing Management`, `Presentation & Reports`, `Reports`, `Client Collaboration`, `Manage People`, `Tagging`, `User Settings`, `Analytics`, `Mobile`, `Integrations`, `Workspaces`, `Security`, `Legacy Platform / Conversion`, `MLS Specific Content`, `General`, `Internal Tools` |
| `Collection in Intercom` | multi_select | `Search`, `Filtering`, `Dashboard`, `Reports`, `Listing Presentations`, `Listing Management`, `Listing Maintenance`, `Tags`, `Client Collaboration`, `Client Experience`, `Invited Client`, `Manage People`, `User Settings`, `Analytics`, `Mobile`, `Workspaces`, `Building Detail Page`, `Getting Started Guide`, `Critical Worklows`, `Then vs. Now`, `FAQ Tips and What's New in Perchwell`, `FAQs & What's Coming`, `What's New in Perchwell`, `Perchie (Snippet)`, `General` |
| `Roles` | multi_select | `All`, `Agent`, `Admin / Broker`, `Invited client`, `All - but client` |
| `Text` | status | `Update Required`, `In progress`, `Needs Review`, `Done`, `Not Required` |
| `Screenshot` | status | `New Screenshots`, `Update Required`, `In progress`, `Needs Review`, `Done`, `Not Required` |
| `Video` | status | `New Video`, `Update Required`, `In progress`, `Needs Review`, `Done`, `Not Required` |
| `Fin AI` | multi_select | `Yes`, `No`, `?` |
| `Links to another articles` | multi_select | `YES`, `NO`, `?` |
| `Video Links` | url | Loom or Arcade share link |
| `Help Center URL (Public)` | url | read only for triage |
| `Intercom Internal URL` | url | read only for triage |
| `Upcoming Feature & Dates` | text | set when decision is D with a future enable date |
| `Comments` | text | short note on provenance, see below |
| `Baldwin?`, `CRMLS?`, `NYC?` | multi_select | `Article for MLS`, `100% Applicable`, `Text Changes`, `0% MLS Specific`, `New screenshots`, `New videos` |

Read-only, do not set: `Author`, `Last Updated`, `Text Owner`, `Screenshot Owner`, `Video Owner`, `Final Review & Upload`.

## Triage queries

Use `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-query-data-sources` with `data_source_urls: ["collection://1c78b9e0-1438-80b8-951d-000bc128f119"]`. Table name in SQL is the data source URL in double quotes.

By product area:

```sql
SELECT "Resource Title", "HC Status", "Update Status", "MLS", "Collection in Intercom",
       "Help Center URL (Public)", url, "Last Updated"
FROM "collection://1c78b9e0-1438-80b8-951d-000bc128f119"
WHERE "Product Area (Internal)" = ?
  AND "HC Status" NOT IN ('Deprecated ❌', 'Remove from HC')
ORDER BY "Last Updated" DESC
```

By title keyword (run once per keyword):

```sql
SELECT "Resource Title", "HC Status", "Update Status", "MLS", "Product Area (Internal)", url
FROM "collection://1c78b9e0-1438-80b8-951d-000bc128f119"
WHERE "Resource Title" LIKE ?
ORDER BY "Last Updated" DESC
```

Bind `%keyword%`.

By Intercom collection:

```sql
SELECT "Resource Title", "HC Status", "Update Status", url
FROM "collection://1c78b9e0-1438-80b8-951d-000bc128f119"
WHERE "Collection in Intercom" LIKE ?
  AND ("MLS" LIKE '%Baldwin%' OR "MLS" LIKE '%All Regions%')
ORDER BY "Last Updated" DESC
```

Bind `%Reports%` style patterns; multi-selects are stored as JSON arrays, so `LIKE` is the practical match. Verified working on 2026-08-27.

Already flagged for update in the same area:

```sql
SELECT "Resource Title", "Update Status", url
FROM "collection://1c78b9e0-1438-80b8-951d-000bc128f119"
WHERE "Product Area (Internal)" = ?
  AND "Update Status" IN ('Update Needed', 'Update needed 7/20', 'Update needed 8/3')
```

Then fetch each candidate's body with `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-fetch` using its `url`.

## Creating a new article page

Confirm once with the user before writing, in the marketing-weekly-planning style: a compact summary of the page and its properties, then wait for "go."

```
Creating 1 Draft in the Master Article List:
- Create a Market Conditions Addendum Report (1004MC)
  HC Status: Draft | Update Status: Draft | MLS: Baldwin | Product Area: Presentation & Reports
  Collection: Reports | Roles: All - but client | Text: In progress | Screenshot: New Screenshots | Video: New Video
Go?
```

Call shape:

```json
{
  "parent": { "type": "data_source_id", "data_source_id": "1c78b9e0-1438-80b8-951d-000bc128f119" },
  "pages": [{
    "properties": {
      "Resource Title": "<title>",
      "HC Status": "Draft",
      "Update Status": "Draft",
      "MLS": ["Baldwin"],
      "Which HC is it in": ["Baldwin"],
      "Product Area (Internal)": "<area>",
      "Collection in Intercom": ["<collection>"],
      "Roles": ["<role>"],
      "Text": "In progress",
      "Screenshot": "New Screenshots",
      "Video": "New Video",
      "Fin AI": ["?"],
      "Links to another articles": ["YES"],
      "Comments": "Drafted from release notes via /article-draft on YYYY-MM-DD. Repo copy: workstreams/help-center-overhaul/outputs/drafts/<file>.md"
    },
    "content": "<Notion markdown body>"
  }]
}
```

Set `Screenshot` and `Video` to `Not Required` only if the user says the article needs none. If a Loom or Arcade link exists, set `Video Links` and `Video: Needs Review`.

Do not pass `template_id` together with `content`; the skill writes the full body itself.

## Publishing an update change sheet

Never overwrite a `Live ✅` page. The change sheet is one page for the whole release.

If the user names a target page (a launch task, the release note, a CS task), write the sheet there with `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-update-page` (`insert_content` at end, or `replace_content` if the user says the page is empty or theirs to overwrite). Otherwise create one sibling row in the Master Article List:

- `Resource Title`: `Help center changes: <feature> (YYYY-MM-DD)`
- `HC Status`: `Draft`, `Update Status`: `Update Needed`
- `MLS`, `Which HC is it in`: from the release note's target MLS
- `Comments`: `Change sheet for <n> articles, triggered by <release note url>. Repo copy: workstreams/help-center-overhaul/outputs/drafts/<file>-changes.md`
- `content`: the change sheet body

Notion shape for the sheet: a one-line intro, `##` heading per article with the Notion page mentioned via `<mention-page>`, plain bullets for edits using `→`, a `###` heading plus final-form text only for new or rewritten sections, and one `## Open items` list. No callouts, toggles, or tables in the sheet; keep callouts for the paste-ready sections themselves where the live article style calls for them.

After publishing, offer to set each source row's `Update Status` to `Update Needed` with `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-update-page`. Only do it when the user says yes.

## Markdown to Notion mapping

The repo file is plain markdown. Convert when building `content`:

| Repo markdown | Notion markdown |
|---|---|
| `# Title` line at the top | Omit. The title lives in `Resource Title`. |
| `<!-- Status: ... -->` metadata comment | Omit. |
| `**Description:** text` | Keep as the first paragraph, `**Description:** text` |
| `## In this article:` | `## In this article:` (unchanged) |
| `# Section` / `### Subsection` / `### Steps:` | Unchanged |
| `> 💡 **Tip**: text` | `<callout icon="💡" color="gray_bg">` then a tab-indented line `**Tip**: text`, then `</callout>` |
| `> ⚠️ **Note**: text` | `<callout icon="⚠️" color="yellow_bg">` ... `</callout>` |
| `> 📖 phrasing [Title](url)` | `<callout icon="📖" color="gray_bg">` with the link. If the target is a Notion page, use `<mention-page url="<notion url>"/>` instead of a markdown link |
| `> 📹 phrasing [Loom](url)` | `<callout icon="📹" color="gray_bg">` with the link |
| `> ⚒️ **Paragon vs. Perchwell**: text` | `<callout icon="⚒️" color="orange_bg">` ... `</callout>` |
| A bare Loom or Arcade URL under the intro | `<video src="<url>"></video>` |
| `> 📹 Video placeholder: ...` / `> 🖼️ Screenshot placeholder: ...` | `<callout icon="🖼️" color="orange_bg">` with the placeholder text, so owners can spot it |
| Markdown table | `<table header-row="true">` with `<tr>` and `<td>` rows; cells hold plain rich text |
| Support footer blockquote | `<callout color="green_bg">` with three tab-indented lines: `**Connect with our Support Team:**`, `✉️ **Email:** [support@perchwell.com](mailto:support@perchwell.com)`, `💬 **Chat:** Click the chat icon at the bottom of the page to reach our support team.` |
| Blank lines | Drop them. Notion spaces blocks itself; use `<empty-block/>` only if a visual gap is essential |
| Em dashes | Must not exist. Fix before converting |

Escape `*`, `[`, `]`, `<`, `>`, `|`, `{`, `}` when they appear as literal text outside markdown syntax (for example a literal `%` needs no escape, but `1004MC / Form 71 [MC]` would need `\[MC\]`).

## After publishing

Report the new page URL(s). Remind the user that, per the SOP, the remaining steps are manual and owned by CS: peer review, `Transfer to Intercom`, setting `Help Center URL (Public)`, toggling Fin AI on, and assigning the MLS audience in Intercom.
