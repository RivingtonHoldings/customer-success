# Dashboard widget lineup across MLSs

Whether one Dashboard Overview article can serve every MLS, or whether the widget sections force one article per MLS. Assembled by Claude for Tara, September 10, 2026, from the live mirror in `docs/help-center/` and the old Notion Master Article List.

This answers the question raised by the September 10 Dashboard Overview migration, recorded in `qa/2026-09-10-dashboard-overview.md` under universality.

## The answer in one line

The five widgets Baldwin documents are all present in CRMLS too, so the core of the article is universal. CRMLS and NYC carry two or three widgets Baldwin has no trace of, so the widget section is the only part that has to vary.

## Correction to the earlier finding

The Dashboard Overview QA file said CRMLS has no Tags widget. **That was wrong**, and it is corrected there now. It came from reading `crmls/the-dashboard-page-overview.md`, which does not mention a Tags widget. But `crmls/customizing-your-dashboard.md`, which is the article that enumerates the Manage Widgets list, lists Tags as an available widget. CRMLS members have the Tags widget; their Dashboard overview article just omits it.

The lesson for the audit: an overview article's silence is not evidence a feature is absent. Check the article that owns the enumeration.

## Documented lineup

| Widget | Baldwin | CRMLS | NYC |
|---|---|---|---|
| Hot Sheets | Yes | Yes | Not established |
| Listings | Yes, cannot be removed | Yes, cannot be removed | Not established |
| Contacts | Yes | Yes | Not established |
| Saved Searches | Yes | Yes | Not established |
| Tags | Yes | Yes | Not established |
| Presentations | **No trace** | Yes | Yes |
| Days on Market family | **No trace** | Yes | Yes |

Sources for the enumeration, both live:

- Baldwin: `baldwin/customize-your-dashboard.md` lists Hot Sheets, Contacts, Saved Searches, and Tags under Manage Widgets, and states the Listings widget cannot be removed or reordered. Five total.
- CRMLS: `crmls/customizing-your-dashboard.md` lists Hot Sheets, Listings, Contacts, Saved Searches, Tags, Presentations, and Days on Market, and states the Listing widget cannot be removed. Seven total.

## Why Presentations and Days on Market look genuinely absent from Baldwin

Not merely undocumented. Three independent signals point the same way.

**Presentations.** A search for "presentation" across all 123 Baldwin articles returns only report, branding, and analytics contexts, never a widget or a Listing Presentations feature. CRMLS has a dedicated `overview-of-listing-presentations.md`. In the Notion Master Article List, every Listing Presentations row carries `MLS` of `["NYC","CRMLS"]` or `["CRMLS"]`, across five separate rows. **No Baldwin row for Listing Presentations exists.**

**Days on Market family.** A search across Baldwin returns the metric only in report, listing-detail, and FAQ contexts, never as a Dashboard widget. Baldwin's one Notion row, "Days on Market & Days Under Contract", sits in the `FAQs & What's Coming` collection and is about the metric, not a widget. The widget rows are `CRMLS | Watching the Days on Market`, `CRMLS| The Days Active in the MLS Widget`, and NYC's `Days on Market Chart`, all in the `Dashboard` collection.

**Confidence.** High that these are CRMLS and NYC features Baldwin does not have. Not certain, because absence of documentation is not absence of a feature, and only a product answer closes it. That question is listed below.

## CRMLS documentation defects found along the way

These belong in the CRMLS audit regardless of what is decided about universality.

1. **CRMLS disagrees with itself on how many DOM widgets exist.** `customizing-your-dashboard.md` lists one item, "Days on Market". But two separate live articles describe two different widgets: `the-days-active-in-the-mls-widget.md` (Days Active in MLS, DAM) and `the-days-active-on-market-widget.md` (Days Active on Market, DOM). The CRMLS lineup is either seven widgets or eight, and the help center does not say which.
2. **`crmls/the-days-active-on-market-widget.md` has a copy-paste error.** Its setup section reads "The Days Active in MLS widget appears on the Dashboard by default", naming the other widget. Both articles also share one screenshot.
3. **`crmls/the-dashboard-page-overview.md` omits the Tags widget** and uses the heading "Listings Widget" twice, once for the widget and once for listing management.
4. **`baldwin/customize-your-dashboard.md` links to article 13903171 as "what is the listings widget on the dashboard"**, but that article's actual title is `Listings Widget Overview`. Link text should be the article title.

## What this means for the article

The five core widgets are common ground, and every other Baldwin-specific thing in the Dashboard Overview draft is a link or a claim, not a widget. So the widget sections do not force separate articles by themselves. Three routes, in order of how much they ask of the team:

**Route A, one body with a variable widget section.** Keep the five core widget sections as the universal spine. Replace any MLS-only widget with a sentence pointing at Manage Widgets as the source of truth, the same move the integrations section now makes: "Click Manage widgets to see the widgets your MLS includes." The CRMLS and NYC extras then live in their own articles, which already exist for CRMLS. Cheapest, and consistent with the integrations precedent.

**Route B, one row per MLS sharing a spine.** Each MLS gets a row whose five core sections are identical text, plus the widget sections that MLS actually has. Matches the current single-select `MLS/AOR` schema with no change. Costs a rewrite per MLS and creates three places to keep in sync.

**Route C, one universal row.** Requires a schema change, because `MLS/AOR` is a single select with no "all" option, and requires the MLS-only widgets to be documented as conditional in one body.

Route A is the recommendation, on the same reasoning the integrations section was genericized: the product already tells the member what they have, and the article does not need to duplicate a list that varies.

Note that a `CRMLS| Perchwell Dashboard Overview` row already exists in the Master Article List at `Draft` status, and `NYC | Perchwell Dashboard Overview` at `Needs Review`. Whichever route is chosen, those two rows are the existing starting points and should not be orphaned.

## Questions this raises

| Question | Why it matters | Suggested owner |
|---|---|---|
| Do Baldwin members have a Presentations widget or a Days on Market widget on the Dashboard? Documentation says no, across three signals, but only product can confirm | Decides whether the widget spine is five or seven, and therefore whether Route A works | Tara, with product |
| Does the CRMLS Dashboard have one Days on Market widget or two (Days Active in MLS and Days Active on Market)? | CRMLS's own articles disagree, so the CRMLS lineup is unknown today | Kelly Miragliotta |
| Is NYC in scope for "universal"? It is an `MLS/AOR` option and has its own Dashboard Overview row, but `docs/product-context.md` puts NYC outside this project | Changes universal from two help centers to three | Tara |
| Which route, A, B, or C? | Blocks the CRMLS Dashboard Overview and any further overview migration | Tara |
