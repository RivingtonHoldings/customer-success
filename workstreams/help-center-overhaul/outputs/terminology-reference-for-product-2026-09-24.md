# Perchwell terminology: how the help center writes it

This is the working glossary and the naming rules behind the September 2026 help center rewrite, written up for people outside Customer Success. It covers the words we use for features, roles, and concepts in member-facing articles, the words we deliberately avoid, and the places where an article and the product currently say different things.

It is a description of help center practice, not an approved product style guide. Where it disagrees with the product, that is a question, not a correction. The last section lists the ones we would most like resolved.

Owner: Tara Bars, help center project lead, [tara.bars@perchwell.com](mailto:tara.bars@perchwell.com).

Scope: Baldwin and CRMLS help centers. Written September 24, 2026, partway through the rewrite, so the rules are settled but the article set is not.

## How a term gets decided

Four rules do most of the work. They are worth reading before the word lists, because they explain why some entries look inconsistent.

**1. The on-screen label wins for anything the member has to find and click.** A button, filter, menu item, toggle, or navigation target is spelled the way the screen spells it, however awkward it reads in a sentence. "# of Properties" stays over "number of Properties" because that is what the control reads.

**2. A label the member reads but never clicks does not bind.** A status row in a chart, a column heading, or a count is a readout, not a control, and there the word a member would actually type wins over the screen's rendering. This is why articles write "off-market" although the Hot Sheet widget's row reads "Off market."

**3. An on-screen label licenses the control, not the vocabulary.** A word can be on screen and still be the wrong word to build prose from. Articles name the control once, at the moment the member is looking for it, then describe what it does. The Listings widget menu is headed "Scope by," so an article says "Scope by" once and everywhere else says "choose whose listings you see," never "the scope button." An agent looking at a button that reads MLS Listings does not know the word for it is scope.

**4. Write the word a member would type.** Name the real thing, not the category containing it: "listing, agent, or contact," never "record." This is a retrieval rule as much as a readability one. Members search with the words they know, both in the help center and in chat, so a word an agent would not say is also a word our AI agent cannot match them on.

One more that cuts across all four: consistency beats local accuracy. One word used the whole way through lets a member and the AI agent track the same thing, so we do not switch from "modal" to "window" to "pop-up" across three paragraphs even where each would be fine on its own.

## Feature names

These are the names articles use, one line each. Where the internal or help-center name differs from what the member sees on screen, the difference is called out.

- Search: the main listing search page, and the starting point for most workflows.
- SearchWell: natural language search inside Search. The member types a sentence instead of setting filters.
- Universal Search Bar: the search field in the top navigation, which opens a modal. **Name mismatch:** the screen just says Search. Articles name the on-screen label in the first step and tie the two together in the lead sentence.
- Filters: the criteria panel on Search. A saved set of filters becomes a Saved Search.
- Saved Searches: a saved filter set that can send email alerts to the member and to invited clients.
- Hot Sheets: a saved search surfacing new and changed listings matching set criteria, usually on the Dashboard.
- Add/Edit: the listing entry and management form, with real-time compliance checks.
- AI Scribe: generates a fair-housing-compliant listing description inside Add/Edit.
- Listing Management: the member's own listings, status changes, and maintenance.
- Property Details: the page for one listing.
- Building Detail Page: the page for a multi-unit building.
- Tags: folders of listings that can be shared with clients. Deleting a Tag removes the folder, not the listings.
- Client collaboration: shared workspaces, messages, and alerts between an agent and an invited client.
- Contacts: the member's client list, plus the My MLS tab showing the agent roster.
- Reports: generated documents from Search, including the listing report and the Market Conditions Addendum Report (1004MC).
- CMA: Comparative Market Analysis, a report comparing similar properties to estimate value.
- Print: prints the current Search results using the visible columns.
- Export CSV: exports Search results with a saveable column template.
- Dashboard: the landing page with configurable widgets.
- Analytics: market and brokerage statistics.
- Mobile: the Perchwell app, at parity with the web.
- Workspaces: shared views for teams and clients.
- Integrations: third-party tools connected to Perchwell.
- User Settings: profile, notifications, and password.

## Roles

Articles use the role names members see, and state a role only when one gates the workflow.

- Agent: searches, enters listings, runs reports, shares with clients. The default reader.
- Admin / Broker: everything an agent does, plus brokerage-level settings, approval workflows, and roster management.
- MLS staff: administers roles, permissions, compliance, and data distribution.
- Invited client: a buyer or seller an agent invited into Perchwell to view shared listings and collaborate. Limited experience, cannot enter listings.

## Glossary

| Term | How we use it |
|---|---|
| MLS | Multiple Listing Service. Members know it; articles do not define it. |
| MLS ID | The unique identifier for one listing. Always "MLS ID," never "MLS number" or "MLS #." It is the label on the MLS ID filter and on listing cards. |
| Member | A person using Perchwell through their MLS. Preferred over "user" in anything member-facing. |
| Client | An invited buyer or seller. Never used for a member. |
| Cutover | The day the legacy system stops being the system of record and Perchwell takes over. |
| Parallel period | The months before cutover when both systems run at once. |
| System of record | The system where a listing officially lives. |
| Modal | A pop-up window opening over the page. One word for it, used consistently. See the note in the open questions. |
| Timeframe | One word, for a Hot Sheet's date window. The Edit hot sheet modal labels the field Timeframe, so the product's spelling settles it. |
| Collection | A group of articles in the help center. Members see collection names on the help center home page. |

## Words articles avoid

Each is banned in one sense, not as a word, and each has a replacement. A term crossed out with nothing put in its place is not a fix.

| Do not write | Write instead |
|---|---|
| record, entry, entity, object, standing in for the thing | the real noun: listing, agent, contact, Saved Search, Hot Sheet |
| lookup, as a noun | name the task: find a listing, open a contact |
| returns, as in "the search returns three matches" | finds, shows, or "what you find" |
| partial entry, partial match | you do not have to type the whole thing |
| tile | say what the widget displays. Exception: the on-screen labels Tiles View, the Perchwell tile at login, and the collapsible tiles on the Listing Detail Page |
| populates | fills in, appears |
| navigate to | open, click |
| execute, initiate, perform, utilize, leverage | the real verb: run, start, open, click |
| third-party, where it is not accurate | integration |

Also out: marketing framing of any kind. Streamlined, powerful, seamless, ideal for, uncover insights, smarter decision-making. A plainly stated benefit is fine and is not the same thing: "which means you do not have to rerun a search to see it" earns its place because no adjective is doing the work.

Two other house rules that may matter for UI strings: no em dashes anywhere, and the member is the actor in the verb. "Adjust which widgets display," not "change which widgets appear." The system stays the actor only where it genuinely is one, as in "the widget updates automatically."

## Legacy platform mapping

Members arriving from a legacy platform search with their old vocabulary, so articles keep the legacy feature name as a bridge: "Members who came from a legacy platform may know the Universal Search Bar as Power Search."

Articles never name the platform, because one article serves more than one MLS and members came from different systems. Chat replies and macros do name it, since we know who we are talking to. We also never write "old system," "retired," or "sunsetted."

The Baldwin mapping, from the live New Terminology article:

| Legacy term | Perchwell |
|---|---|
| Class | Property Type |
| Property Type | Property Subtype |
| Partial (listing) | Draft |
| Home | Dashboard |
| Maintain Listings | Manage Listings (or Add/Edit) |
| Roster | My MLS (in Contacts), or Manage People (admins) |
| Copy / Clone (listing) | Duplicate |
| Statistical Reporting | Analytics (or Broker Analytics) |
| Market Monitor | Hot Sheet (Dashboard) |
| Spreadsheets | Templates (search results columns) |
| Collaboration Center / CollabLink | Contacts, Messages |
| Listing Carts | Tags |
| Paragon Connect (mobile) | Perchwell app (iOS and Android) |
| Financial Amortizer | Mortgage Calculator (listing detail page) |
| CRS Tax Autofill | Autofill (in Add/Edit) |
| About Me Page | User Settings, then Profile |
| Power Search | Universal Search |
| Assume Identity | Log in as user / Masquerading |

Note that this table is the one place a legacy platform is named, because the whole article exists to translate. Everywhere else the rule above holds.

## Where the help center and the product currently diverge

These are the live ones, and the reason this document is worth a conversation rather than a link. Each is a real string, not a hypothetical.

**Off market.** The Hot Sheet widget labels a status row "Off market." Articles write "off-market," because members type the hyphenated form and nine other uses across the help center agree. We treat the row as a readout rather than a control, so the label does not bind. Worth deciding whether the widget should hyphenate.

**Scope by.** The Listings widget menu is headed "Scope by." The word "scope" is not one an agent uses, so articles name the heading once and otherwise describe the action. The underlying question is whether the heading should say what it does: "Show listings from."

**Tile.** Banned in article prose, but on screen in three unrelated senses: Tiles View on Search, the Perchwell tile at login, and the collapsible tiles on the Listing Detail Page. Three different objects sharing one word.

**Add/Edit versus Manage Listings.** Two names for adjacent things, and our own sources have called Add/Edit "the listing management form" more than once. Members coming from a legacy platform map "Maintain Listings" onto both. This is the mismatch we see cause the most confusion.

**Universal Search Bar.** The feature name nobody sees. The screen says Search, which is also the name of an entirely different page. Articles carry both, which works but costs a sentence every time.

**Timeframe.** One word in the Edit hot sheet modal, two words in four live articles we have not yet touched. We are following the product and correcting the articles as we reach them.

**Modal.** We keep it, knowing it reads as developer vocabulary, because consistency is worth more than any single better word. If UX has a member-facing word it prefers, we would rather switch once, everywhere, than hold the line on ours.

**Member versus user.** Articles say member. The product says "Log in as user," and internal tooling says user throughout. Low stakes, but it is the term we are most strict about in member-facing writing.

**What the assistant is called.** The Baldwin help center refers to the in-product assistant as Perchie, and internally we call it Fin, which is the Intercom product name. We have not confirmed which name is meant to be member-facing in each help center, and it is a question worth settling before it spreads further.

## Where these rules live

The full internal versions, if useful:

- `docs/product-context.md`: feature names, glossary, terminology rules.
- `docs/standards/content-standards.md`: the complete writing standard, including the label rules and the plain language do-not list, with the reasoning and the date each rule was added.
