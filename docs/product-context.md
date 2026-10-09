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

Perchwell also serves brokerages directly (Engel & Volkers, Keller Williams, and NYC brokerages), which is why some Notion articles carry a `NYC|` prefix. Those are not Baldwin or CRMLS content, and NYC is out of scope for the help center overhaul, confirmed September 10, 2026. The new Notion database offers NYC as an `MLS/AOR` option, which is a leftover, not an invitation: "every MLS" in this project means Baldwin and CRMLS.

## User roles

Use the role names members see. When an article applies to some roles only, say so at the top.

- **Agent:** searches, enters listings, runs reports, and shares with clients. The default reader.
- **Admin / Broker:** everything an agent does, plus brokerage-level settings, approval workflows, and roster management.
- **MLS staff:** administers roles, permissions, compliance, and data distribution. Can masquerade as a member for support.
- **Invited client:** a buyer or seller an agent invited into Perchwell to view shared listings and collaborate. Sees a limited experience and cannot enter listings.
- **All - but client:** the Notion shorthand for every role except invited clients.

## Feature names

One line each, using the name members see in the product. Name it exactly and leave it plain; nothing in an article body is bold, per the September 10, 2026 decision and the terminology rules below.

- **Search:** the main listing search page and the starting point for most workflows.
- **SearchWell:** natural language search inside Search. Members type a sentence instead of setting filters.
- **Filters:** the criteria panel on Search; saved sets of filters become Saved Searches.
- **Saved Searches:** a saved filter set that can send email alerts to the member and to invited clients. The button in the upper left of the Search page reads Saved Searches, or the open saved search's name, and opens the My Searches window. Save on a search that has not been saved opens the New Search window, with a required Name this search field; Save with a saved search open opens the Save Search window, with Save New and Update Current. Confirmed by Tara, October 8, 2026.
- **Sharing a saved search:** the member adds clients from the Contacts dropdown in the Edit Search window, which lists existing contacts only, with checkboxes and a Search contacts field, and no option to create a contact. A client must accept their Perchwell invitation to open a shared search; a contact without an account receives alerts only. The client gets an email that they were added, with an Open saved search button. The Allow added contacts to see and edit this search toggle decides access: on, the search appears in the client portal and the client can view results and edit filters and charts; off, the search does not appear in the client portal at all. Changes a client saves update the agent's saved search; there is no separate copy. Tags the agent added to listings stay hidden from clients in the saved search. The member removes a client with the X next to their name in the Contacts field. Turning on Alerts does not email a client by itself: the Recipient dropdown starts at Only me, so the member selects a Recipient option that sends to contacts. The live Manage Your Saved Searches article says client edits go to a copy; that is wrong. Confirmed by Tara, October 8 to 9, 2026.
- **Template Search:** a saved search starred in the My Searches window, so new searches (Start New, or New Search in the My Searches window) start with its filters, sort order, columns, view, and map settings. One at a time; clicking the filled star turns it off. Its columns take priority over a default column template. A search started from it is an ordinary new search, so saving it never changes the Template Search. The star has no hover label. Confirmed by Tara, October 6 to 8, 2026.
- **Hotsheets:** a saved search that surfaces new and changed listings matching specific criteria, usually on the Dashboard.
- **Add/Edit:** the listing entry and management form, with real-time compliance checks.
- **AI Scribe:** generates a fair-housing-compliant listing description inside Add/Edit.
- **Listing Management:** the member's own listings, status changes, and maintenance.
- **Property Details:** the page for one listing.
- **Building Detail Page:** the page for a multi-unit building.
- **Tags:** folders of listings that can be shared with clients. Deleting a Tag removes the folder, not the listings.
- **Client collaboration:** shared workspaces, messages, and alerts between an agent and an invited client.
- **Messages:** conversations with invited clients only. Hovering over the left edge of the Messages page opens the Messages panel (its on-screen heading), with the pencil icon labeled New message at the top; a new message badge sits to the right of the client's name. Sharing listings opens the Share window from three places with different labels: Actions, then Share via Message, in search results (shares every selected listing, even in Preview); Listing Actions, then Share via Message, in Preview (shares only the previewed listing); Actions, then Send as in-app message, on the full Listing Detail Page. All three continue the same way: select a contact, click Share, enter a message of up to 1,000 characters, click Send. An uninvited contact receives the listings by email, and the window offers an Invite this contact to Perchwell checkbox. Client replies to the Messages email appear in the conversation and in the member's email inbox. Clients react with Reject (X), Maybe (question mark), and Like (heart) icons, and the member filters them in Shared properties (lowercase p on screen). Confirmed by Tara, October 8 to 9, 2026.
- **Contacts:** the member's client list, and the My MLS tab that shows the agent roster.
- **Reports:** generated documents from Search, including the listing report and the Market Conditions Addendum Report (1004MC).
- **CMA:** Comparative Market Analysis, a report comparing similar properties to estimate value.
- **Listing Presentations:** branded client-facing presentations built from listings. Removed from CRMLS as of September 2026, and never a Baldwin feature, so do not document it for either in-scope MLS. Cloud CMA, a third-party integration, still produces its own listing presentations and is unaffected by the removal. Six live CRMLS articles still describe the removed feature; they are listed in `workstreams/help-center-overhaul/audit/dashboard-widget-lineup-2026-09-10.md`.
- **Print:** prints the current Search results using the visible columns.
- **Export CSV:** exports Search results with a saveable column template.
- **Dashboard:** the landing page with configurable widgets. Baldwin and CRMLS both have Hotsheets, Contacts, Saved Searches, Tags, and Listings, and the Listings widget cannot be removed or reordered. The lineup is the same five for both MLSs: CRMLS no longer has the Days on Market widget, confirmed by Tara September 23, 2026, so do not document it for either MLS. Four live CRMLS articles still describe it; they are listed in `workstreams/help-center-overhaul/audit/dashboard-widget-lineup-2026-09-10.md`. Days on Market as a listing field is unaffected and still appears in reports, CMAs, and search columns.
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
| Client portal | An invited client's own workspace in Perchwell, where shared saved searches and messages appear. The help center's term, used in Invite Clients to Perchwell; write "client portal", not "the client's portal", and define it on first use in an article. |
| Cutover | The day the legacy system stops being the system of record and Perchwell takes over. For Baldwin, August 3, 2026. |
| Parallel period | The months before cutover when both systems run at once. Baldwin's ran April through July 2026. |
| System of record | The system where a listing officially lives. "The legacy platform was the system of record, which means new listings still happened there." |
| RESO | The industry standards body for real estate data. Rarely needed in member content. |
| Masquerading | An MLS staff ability to log in as a member for support. Staff-facing only; do not mention in member articles. |
| Modal | Developer word for a pop-up window that opens over the page, such as the one the Universal Search Bar opens in the center of the screen. Do not use it in articles. Call it a window named for what it does, "the search window", and keep that name rather than switching to "panel" or "pop-up" partway through. |
| Collection | A group of articles in the Intercom help center. Members see collection names on the help center home page. |
| Fin resolved | Perchwell's definition: Fin answered, no teammate sent a message afterward, and the same member did not follow up on the same topic within 48 hours. |
| Human intervention | The share of Fin conversations where a teammate had to step in. Baldwin is around 40 percent; the target is 10 percent or less. |

## Terminology rules

When a term is settled, list every Notion draft and repo copy in the set that uses the old term, update them together, and record the rollout on the term's line below.

- Use the label the member sees on screen, spelled exactly as the UI spells it, and do not bold it. "Add/Edit," not "the listing form."
- A pop-up window that opens over the page is a window, named for what it does: "the search window". One name for it, used consistently, so a member and Fin both track the same thing. Never "modal"; agents do not say it.
- A Hot Sheet's date window is a timeframe, one word. The Edit hot sheet modal labels the field `Timeframe`, and the Dashboard FAQ asks "What is the maximum timeframe for a hot sheet?", so one word is both the product's spelling and the majority of the live help centers. Two words appears in four live articles and is the form to correct when those are next touched.
- The control above the search results that reads "Columns:" followed by the applied template's name is the Columns menu, across every Search article. Settled by Tara, October 8, 2026. Customize Your Search Results View and Search Page Overview were updated to match on October 8, 2026.
- A listing's identifier is the MLS ID. Never "MLS number," "MLS #," or "listing number," in articles, macros, or replies. Perchwell labels the filter and the listing card **MLS ID**, and one term across every surface is what lets Fin match a member who types either phrasing.
- Say "member" for people using Perchwell and "client" for an invited buyer or seller.
- Articles say "a legacy platform", never the platform's name, because one article serves more than one MLS and members came from different systems. Keep the legacy feature name, which is what a member actually searches for: "In a legacy platform this was called Power Search." Conversation replies and macros may name the platform, since you know which MLS the member belongs to. Never "old system," "retired," or "sunsetted."
- Translate system terms with a "which means" clause instead of assuming the member knows them.
- Hedge predictions about people. "Clients may ask" rather than "clients will ask."
- Do not use internal names, employee names, or Notion property values in member-facing text.
- Never em dashes.
