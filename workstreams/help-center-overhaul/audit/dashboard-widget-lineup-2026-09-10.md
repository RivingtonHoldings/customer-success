# Dashboard widget lineup across MLSs

Whether one Dashboard Overview article can serve both in-scope MLSs, or whether the widget sections force one article per MLS. Assembled by Claude for Tara, September 10, 2026, from the live mirror in `docs/help-center/` and the old Notion Master Article List. Revised the same day with two facts from Tara: NYC is out of scope, and Listing Presentations has been removed from CRMLS.

This answers the question raised by the September 10 Dashboard Overview migration, recorded in `qa/2026-09-10-dashboard-overview.md` under universality.

## The answer

One body works. Scope is Baldwin and CRMLS only, and the two help centers differ on exactly one widget.

| Widget | Baldwin | CRMLS |
|---|---|---|
| Hot Sheets | Yes | Yes |
| Listings, cannot be removed | Yes | Yes |
| Contacts | Yes | Yes |
| Saved Searches | Yes | Yes |
| Tags | Yes | Yes |
| Days on Market family | No trace | Yes, one or two, unconfirmed |

The five widgets the Dashboard Overview draft already covers are common to both MLSs, so its widget sections are universal as written. The only divergence is the Days on Market family, which is CRMLS-only and already has its own CRMLS articles.

Sources for the enumeration, both live:

- Baldwin: `baldwin/customize-your-dashboard.md` lists Hot Sheets, Contacts, Saved Searches, and Tags under Manage Widgets, and states the Listings widget cannot be removed or reordered. Five total.
- CRMLS: `crmls/customizing-your-dashboard.md` lists Hot Sheets, Listings, Contacts, Saved Searches, Tags, Presentations, and Days on Market, and states the Listing widget cannot be removed. Seven as documented, six now that Presentations is gone.

## Recommendation

**Keep the five core widgets as one shared body, and point at Manage widgets for anything MLS-specific.** This is the same move the integrations section now makes: the product already tells the member what they have, so the article does not duplicate a list that varies. CRMLS's Days on Market widget stays in its own CRMLS articles rather than being conditionally described in a shared body.

The alternative, one row per MLS with duplicated core sections, costs a rewrite per MLS and creates two places to keep in sync, for one widget's worth of difference. A single universal row is not available anyway: `MLS/AOR` is a single select with no "all" option.

Note that a `CRMLS| Perchwell Dashboard Overview` row already exists in the Master Article List at `Draft` status. Whichever route is chosen, that row is the CRMLS starting point and should not be orphaned.

## Two corrections to earlier findings

**CRMLS does have a Tags widget.** An earlier version of this file and of the Dashboard Overview QA file said it does not. That came from `crmls/the-dashboard-page-overview.md`, which omits Tags. But `crmls/customizing-your-dashboard.md`, the article that owns the Manage Widgets enumeration, lists it. For the audit: an overview article's silence is not evidence a feature is absent. Check the article that owns the enumeration.

**The Presentations widget is no longer a divergence.** Tara confirmed on September 10, 2026 that Listing Presentations has been removed from CRMLS. Baldwin never had it: a search across all 123 Baldwin articles returns "presentation" only in report, branding, and analytics contexts, and no Baldwin row for Listing Presentations exists anywhere in the Master Article List. With NYC out of scope, the feature is absent from every in-scope MLS and should not be documented for either.

## Consequence: live CRMLS content documents a removed feature

This is the more urgent finding. Fin answers from published articles, so CRMLS members can currently be told about a feature they do not have. Six live CRMLS articles need attention, in priority order.

| Priority | Article | What is stale |
|---|---|---|
| 1 | `crmls/overview-of-listing-presentations.md` | The entire article. Deprecate it |
| 2 | `crmls/customizing-your-dashboard.md` | "Presentations" as item 6 in the Manage Widgets list |
| 3 | `crmls/the-dashboard-page-overview.md` | A whole "Presentations Widget" section |
| 4 | `crmls/navigating-the-listing-detail-page.md` | The "Add to Listing Presentation" action in the actions list |
| 5 | `crmls/multi-listing-actions-on-the-search-page.md` | A "Listing Presentations" row in the multi-select actions table |
| 6 | `crmls/what-s-new-in-perchwell-crmls.md` | A release note about Listing Presentations cover photos. Historical release content, so the team may prefer to leave it; Fin will still read it as current |

**Not affected, do not change.** Cloud CMA is a separate third-party integration that produces its own listing presentations, and it is unaffected by the removal. That covers `crmls/create-a-cloud-cma-presentation-from-search.md` and the Cloud CMA entry in `crmls/integration-tools-on-the-dashboard.md`. `crmls/create-and-share-full-reports.md` uses "listing presentations" as a lowercase generic activity, not the feature, though rewording it would avoid confusion.

**Also queued in Notion.** Six Master Article List rows cover Listing Presentations, all of them CRMLS or NYC. One, `NYC & CRMLS| Managing Brokerage Slides for Listing Presentation`, sits at `Transfer to Intercom`, which means it is queued to be published for a feature that no longer exists. The others are at `Live`, `Draft`, `Needs Review`, and `New Article Request`. The Master List is read-only for this project, so these are flagged, not touched.

## CRMLS documentation defects found along the way

These belong in the CRMLS audit regardless of the routing decision.

1. **CRMLS disagrees with itself on how many Days on Market widgets exist.** `customizing-your-dashboard.md` lists one item, "Days on Market". Two separate live articles describe two different widgets: `the-days-active-in-the-mls-widget.md` (Days Active in MLS, DAM) and `the-days-active-on-market-widget.md` (Days Active on Market, DOM). This is now the only open question about the CRMLS lineup.
2. **`crmls/the-days-active-on-market-widget.md` names the wrong widget in its own setup section**, reading "The Days Active in MLS widget appears on the Dashboard by default". The two articles also share one screenshot.
3. **`crmls/the-dashboard-page-overview.md` omits the Tags widget** and uses the heading "Listings Widget" twice, once for the widget and once for listing management.
4. **`baldwin/customize-your-dashboard.md` links to article 13903171 as "what is the listings widget on the dashboard"**, but that article's title is `Listings Widget Overview`. Link text should be the article title.

## Questions still open

| Question | Why it matters | Suggested owner |
|---|---|---|
| Does the CRMLS Dashboard have one Days on Market widget or two? CRMLS's own articles disagree | The last unknown in the CRMLS lineup | Kelly Miragliotta |
| Do Baldwin members have a Days on Market widget? Documentation says no, but only product can confirm | Decides whether the shared spine is five widgets or six | Tara, with product |
| Should the six CRMLS articles above be corrected before or after the audit is finalized? | Fin is answering from them today | Tara and Kelly Miragliotta |

Answered on September 10, 2026: NYC is out of scope, so "every MLS" means Baldwin and CRMLS. Listing Presentations is removed from CRMLS and was never a Baldwin feature.
