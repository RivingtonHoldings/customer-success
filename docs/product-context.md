# Product context for support writing

Last updated: 2026-09-04. Condensed from the marketing team's product brief for people writing help center articles, macros, and member replies. Personas, objections, and competitive positioning are left out on purpose; support content never sells.

## What Perchwell is

Perchwell is the MLS platform members use every day to search listings, enter and manage their own listings, run reports, and work with clients. It runs on one codebase in the browser and on mobile, which means a feature works the same way on a phone as on a laptop. MLS organizations buy Perchwell and roll it out to their membership; members do not buy it themselves.

Perchwell replaces legacy MLS systems. For Baldwin, that system was Paragon.

## Customer MLSs

| MLS | Status | Notes for support writing |
|---|---|---|
| Baldwin (Baldwin County) | Live. Cut over from Paragon on August 3, 2026 | In scope for the help center overhaul. Members may still think in Paragon terms. |
| CRMLS | Cutover upcoming | In scope for the help center overhaul. Which platform members migrate from is being confirmed. |
| StellarMLS | Customer | Out of scope for this project |
| REcolorado | Customer | Out of scope for this project |

Perchwell also serves brokerages directly (Engel & Volkers, Keller Williams, and NYC brokerages), which is why some Notion articles carry a `NYC|` prefix. Those are not Baldwin or CRMLS content.

## User roles

Use the role names members see. When an article applies to some roles only, say so at the top.

- **Agent:** searches, enters listings, runs reports, and shares with clients. The default reader.
- **Admin / Broker:** everything an agent does, plus brokerage-level settings, approval workflows, and roster management.
- **MLS staff:** administers roles, permissions, compliance, and data distribution. Can masquerade as a member for support.
- **Invited client:** a buyer or seller an agent invited into Perchwell to view shared listings and collaborate. Sees a limited experience and cannot enter listings.
- **All - but client:** the Notion shorthand for every role except invited clients.

## Feature names

One line each, using the name members see in the product. Bold the name in articles when it is a clickable element; leave it plain when it is a concept.

- **Search:** the main listing search page and the starting point for most workflows.
- **SearchWell:** natural language search inside Search. Members type a sentence instead of setting filters.
- **Filters:** the criteria panel on Search; saved sets of filters become Saved Searches.
- **Saved Searches:** a saved filter set that can send email alerts to the member and to invited clients.
- **Hotsheets:** a saved search that surfaces new and changed listings matching specific criteria, usually on the Dashboard.
- **Add/Edit:** the listing entry and management form, with real-time compliance checks.
- **AI Scribe:** generates a fair-housing-compliant listing description inside Add/Edit.
- **Listing Management:** the member's own listings, status changes, and maintenance.
- **Property Details:** the page for one listing.
- **Building Detail Page:** the page for a multi-unit building.
- **Tags:** folders of listings that can be shared with clients. Deleting a Tag removes the folder, not the listings.
- **Client collaboration:** shared workspaces, messages, and alerts between an agent and an invited client.
- **Contacts:** the member's client list, and the My MLS tab that shows the agent roster.
- **Reports:** generated documents from Search, including the listing report and the Market Conditions Addendum Report (1004MC).
- **CMA:** Comparative Market Analysis, a report comparing similar properties to estimate value.
- **Listing Presentations:** branded client-facing presentations built from listings.
- **Print:** prints the current Search results using the visible columns.
- **Export CSV:** exports Search results with a saveable column template.
- **Dashboard:** the landing page with configurable widgets (Hotsheets, Contacts, Saved Searches, Listings).
- **Analytics:** market and brokerage statistics.
- **Mobile:** the Perchwell app, at parity with the web.
- **Workspaces:** shared views for teams and clients.
- **Integrations:** third-party tools connected to Perchwell (showing services, CMA tools, and others).
- **User Settings:** profile, notifications, and password.

## Support surfaces

- **Help center:** one per MLS on support.perchwell.com, organized into collections (Search, Reports, Tags, and so on). Articles are written in Notion, reviewed there, then transferred to Intercom.
- **Fin:** the Intercom AI agent that answers member chats using published help center articles. Fin only reads published articles, which means a draft or unpublished article never changes what Fin says. The Baldwin help center also refers to the assistant as Perchie. [confirm: whether "Perchie" is still the member-facing name for Fin in both help centers]
- **Macros:** saved replies the support team pastes in Intercom. Drafted in this repo, created in Intercom by a human.
- **Labels:** Intercom article labels Fin uses to scope answers to one MLS. Strategy in `docs/standards/fin-labeling.md`.

## Glossary

| Term | Meaning, and how to phrase it for members |
|---|---|
| MLS | Multiple Listing Service. The shared listing database and platform real estate professionals use. Members know the term; do not define it in articles. |
| MLS ID | The unique identifier for one listing. Always write "MLS ID", never "MLS number" or "MLS #". It is the label the member sees on the **MLS ID** filter and on listing cards. Members know the term; do not define it in articles. |
| Member | A person using Perchwell through their MLS. Preferred over "user" in member-facing text. |
| Cutover | The day the legacy system stops being the system of record and Perchwell takes over. For Baldwin, August 3, 2026. |
| Parallel period | The months before cutover when both systems run at once. Baldwin's ran April through July 2026. |
| System of record | The system where a listing officially lives. "Paragon was the system of record, which means new listings still happened in Paragon." |
| RESO | The industry standards body for real estate data. Rarely needed in member content. |
| Masquerading | An MLS staff ability to log in as a member for support. Staff-facing only; do not mention in member articles. |
| Collection | A group of articles in the Intercom help center. Members see collection names on the help center home page. |
| Fin resolved | Perchwell's definition: Fin answered, no teammate sent a message afterward, and the same member did not follow up on the same topic within 48 hours. |
| Human intervention | The share of Fin conversations where a teammate had to step in. Baldwin is around 40 percent; the target is 10 percent or less. |

## Terminology rules

- Use the label the member sees on screen, spelled exactly as the UI spells it. "Add/Edit," not "the listing form."
- A listing's identifier is the **MLS ID**. Never "MLS number," "MLS #," or "listing number," in articles, macros, or replies. Perchwell labels the filter and the listing card **MLS ID**, and one term across every surface is what lets Fin match a member who types either phrasing.
- Say "member" for people using Perchwell and "client" for an invited buyer or seller.
- Name Paragon neutrally when comparing. "In Paragon, printing lived under Reports. In Perchwell, every print starts from **Search**." Never "old system," "retired," or "sunsetted."
- Translate system terms with a "which means" clause instead of assuming the member knows them.
- Hedge predictions about people. "Clients may ask" rather than "clients will ask."
- Do not use internal names, employee names, or Notion property values in member-facing text.
- Never em dashes.
