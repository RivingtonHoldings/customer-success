# Connector tools

These tools come from claude.ai connectors, not from any file in this repo. Each teammate connects Notion and Intercom once in claude.ai under Settings, then Connectors, and the tools appear in every Claude Code session on that account. There is no `.mcp.json` in this repo and there should not be one.

`.claude/settings.json` references these exact names in its permissions lists. If a name here changes, settings.json must change with it.

The tool name has three parts: `mcp__`, the connector's server ID, and the tool's own name. The server IDs below were captured from Leo's session on 2026-09-04. They are expected to be the same for every teammate on the Perchwell claude.ai organization, which means settings.json should work for everyone without edits. If a teammate's `/setup-check` reports the tools as missing while their connector is connected, compare their tool names against this file first.

Inventory date: 2026-09-04.

## Notion

Server ID: `c9a24086-67bc-4593-858e-3f11e07b6f9d`
Prefix: `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__`

### Reads

| Tool name | What it does |
|---|---|
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-ai-search` | Semantic search across the workspace |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-search` | Keyword search across pages, databases, and users |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-fetch` | Read a page, database, data source, or view by URL or ID |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-query-data-sources` | Query one database's rows |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-query-multiple-data-sources` | Query across several databases (full Notion MCP only) |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-query-meeting-notes` | Query AI meeting notes |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-get-comments` | Read comments on a page |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-get-users` | List workspace users |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-get-teams` | List teamspaces |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-list-recent-pages` | Recently viewed pages |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-list-favorite-pages` | Favorited pages |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-list-private-pages` | Private pages |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-list-shared-pages` | Pages shared with the user |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-download-attachment` | Download a file attached to a page |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-get-async-task` | Poll a background create or update task |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-search-skills` | Find Notion skills |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-search-agents` | Find Notion custom agents |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-search-sessions` | Find Notion agent sessions |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-query-sessions` | Query Notion agent sessions |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-get-session-status` | Status of a Notion agent session |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-list-session-events` | Events in a Notion agent session |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-read-session-event` | One event in a Notion agent session |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-wait-session` | Wait for a Notion agent session to finish |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-check-mcp-next-steps` | Informational card about MCP setup |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-show-advanced-analysis-next-steps` | Informational card about full Notion MCP |

### Writes

| Tool name | What it does | Allowed here? |
|---|---|---|
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-create-pages` | Create pages (used for review drafts) | Yes, on the allow list |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-update-page` | Update a page's content or properties | Yes, on the allow list |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-create-comment` | Comment on a page | Prompts |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-create-database` | Create a database | Prompts |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-update-data-source` | Change a database's schema | Prompts |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-create-view` | Create a database view | Prompts |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-update-view` | Change a database view | Prompts |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-create-folder` | Create a folder | Prompts |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-update-folder` | Change a folder | Prompts |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-create-file-upload` | Start a file upload | Prompts |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-create-attachment` | Attach a file to a page | Prompts |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-duplicate-page` | Duplicate a page | Prompts |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-move-pages` | Move pages | Prompts |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-convert-page-to-skill` | Turn a page into a Notion skill | Prompts |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-spawn-session` | Start a Notion agent session | Prompts |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-send-message-to-session` | Message a Notion agent session | Prompts |
| `mcp__c9a24086-67bc-4593-858e-3f11e07b6f9d__notion-stop-session` | Stop a Notion agent session | Prompts |

## Intercom

Server ID: `eff8e27b-83eb-43ee-befe-90e26bf3b57b`
Prefix: `mcp__eff8e27b-83eb-43ee-befe-90e26bf3b57b__`

### Reads

| Tool name | What it does |
|---|---|
| `mcp__eff8e27b-83eb-43ee-befe-90e26bf3b57b__list_articles` | Page through every help center article (metadata only) |
| `mcp__eff8e27b-83eb-43ee-befe-90e26bf3b57b__search_articles` | Search articles by phrase, state, or help center ID |
| `mcp__eff8e27b-83eb-43ee-befe-90e26bf3b57b__get_article` | Read one article including its body |
| `mcp__eff8e27b-83eb-43ee-befe-90e26bf3b57b__search_conversations` | Filter conversations by date, Fin participation, tags, and more |
| `mcp__eff8e27b-83eb-43ee-befe-90e26bf3b57b__get_conversation` | Read one conversation's full thread |
| `mcp__eff8e27b-83eb-43ee-befe-90e26bf3b57b__search` | Query-language search over conversations or contacts |
| `mcp__eff8e27b-83eb-43ee-befe-90e26bf3b57b__fetch` | Read a conversation, contact, or company by prefixed ID or URL |
| `mcp__eff8e27b-83eb-43ee-befe-90e26bf3b57b__search_contacts` | Find contacts |
| `mcp__eff8e27b-83eb-43ee-befe-90e26bf3b57b__get_contact` | Read one contact |
| `mcp__eff8e27b-83eb-43ee-befe-90e26bf3b57b__list_companies` | List or look up companies |
| `mcp__eff8e27b-83eb-43ee-befe-90e26bf3b57b__get_company` | Read one company |

### Writes

| Tool name | What it does | Allowed here? |
|---|---|---|
| `mcp__eff8e27b-83eb-43ee-befe-90e26bf3b57b__create_article` | Create a help center article | On the ask list, always prompts |
| `mcp__eff8e27b-83eb-43ee-befe-90e26bf3b57b__update_article` | Update a help center article | On the ask list, always prompts |
| `mcp__eff8e27b-83eb-43ee-befe-90e26bf3b57b__add_internal_note` | Add a teammate-only note to a conversation | On the deny list, Claude never writes conversations |
| `mcp__eff8e27b-83eb-43ee-befe-90e26bf3b57b__submit_mcp_feedback` | Send feedback to Intercom's MCP team (leaves the workspace) | On the deny list |

Intercom has no macro, contact, or company write tools on this connector, so those rules in CLAUDE.md are enforced by the connector itself as well as by policy.
