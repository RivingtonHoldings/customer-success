# QA: Add Charts to the Analytics View on Search (CRMLS)

- Article name: Add Charts to the Analytics View on Search (CRMLS), TRK-004 (assigned by Tara, November 18, 2026)
- Source: the Baldwin draft (TRK-003, see `2026-11-17-add-charts-to-the-analytics-view-on-search.md`), changed for CRMLS using Tara's seven Charts window screenshots of November 18, 2026 (context only, not article images). There is no live CRMLS article to migrate.
- Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-11-18-add-charts-to-the-analytics-view-on-search-crmls-rewrite.md`
- Notion page: https://app.notion.com/p/41c8b9e01438812fb535e8042444141f
- Reason for a separate row: CRMLS differs from Baldwin in seven places (category count in the description and two leads, plus the Distribution, Location, Trends, and Median items), which is over the few-places threshold for keeping one row.
- Scored by Claude for Tara, November 18, 2026, against scorecard revision 2. No old version exists, so there is no before score.

## CRMLS differences from the Baldwin draft

| Item | Baldwin | CRMLS |
|---|---|---|
| Categories | 4 | 5, adding Trends |
| Distribution | DOM by Price Segment | DAM by Price Segment |
| Location, Median | Days on Market | Days Active in MLS |
| Trends | none | Market Inventory, labeled Monthly |

## Golden questions

13 of 14 pass. Factor 3 (undefined_terms) fails: "DAM by Price Segment" appears as the chart's on-screen name and the article cannot define DAM until Tara confirms what it stands for. The marker `[confirm: what DAM stands for]` stays in the Notion draft. Scored as Fin-ready with the gate failed on factor 3, per the scorecard.

## Plain language gate

Pass. All chart names are on-screen labels of options the member selects.

## Dimensions

Same as the Baldwin draft (100.0) with one deduction: Answer completeness check 6 (abbreviations defined on first use) fails on DAM, 25.0 becomes 21.4, for a total of 96.4.

## Fin test questions

| Question | Answers from one section |
|---|---|
| How do I open Analytics on the Search page? | Yes |
| How do I add a chart to my search results? | Yes |
| What is in the Trends category? | Yes |
| What is the Market Inventory chart? | Partly, the article names it but does not define it |
| Is there a Days Active in MLS chart? | Yes |
| How many charts can I add to Analytics? | Yes |

## Open items

1. **DAM.** Confirm what DAM stands for in "DAM by Price Segment" and define it on first use.
2. **Market Inventory and Monthly.** The Trends item says only what the screen shows. Confirm what the chart shows and whether "Monthly" is a setting or a fixed label.
3. **Video.** The CRMLS row has no video; Video Status CRMLS is Not Needed, which is an assumption. Change it if a CRMLS recording is wanted.
4. **Analytics FAQ link.** The CRMLS article links to Analytics FAQ, which has no CRMLS record yet (Intercom URL CRMLS is empty). Port that record first.
5. **Search Analytics.** The empty CRMLS Analytics view is headed "Search Analytics" on screen. The set uses "Analytics view" (this article, Analytics FAQ) and "Search Analytics" (Search Page Overview). Pick one.
6. **Purpose lines and the 8-chart limit** carry over from the Baldwin draft's open items; neither is confirmed for CRMLS.
