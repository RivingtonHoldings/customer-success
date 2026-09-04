---
intercom_id: "16414760"
content_id: "19805100"
title: "Create a Market Conditions Addendum Report (1004MC)"
description: "In this article, you will learn how to generate a 1004MC Market Conditions Addendum Report from your search results and export it to PDF for your appraisal workfile."
url: "http://support.perchwell.com/baldwin/en/articles/16414760-create-a-market-conditions-addendum-report-1004mc"
help_center: baldwin
help_center_id: 4755399
collection: "Reports"
collection_ids: [17797980]
collections: ["Reports"]
state: published
author_id: 8314814
created_at: 2026-08-14T14:39:21Z
updated_at: 2026-08-14T14:46:01Z
labels: []
body_source: public-help-center
synced_at: 2026-09-04T16:50:44Z
---

# Create a Market Conditions Addendum Report (1004MC)

# When to use a Market Conditions Addendum Report

Use this report when you need 1004MC market metrics calculated from the exact comparable listings you researched.
- Complete the market conditions sections of the Fannie Mae Form 1004MC / Freddie Mac Form 71
- Keep defensible supporting calculations in your appraisal workfile

# Report creation

## Steps:
1. Open **Search** and run a search for your comparable listings
2. To use specific listings, select the checkboxes next to them. To use every listing in your results, leave them unselected.
3. Click **Actions**, then **Create a Report**
4. Select **Market Conditions Addendum Report**

The report supports up to 500 listings. If your search returns more than 500, refine your search filters or reduce your selection before generating the report.

# Report configuration

Before you generate the report, confirm your listings, report date, and stable range.

## Choose your listings
- **All listings** (default) includes every listing in your search results
- **Selected listings** appears when you selected specific listings before opening the report

## Set the report max date

The report max date defaults to today and acts as the anchor date for every reporting period, which means each 1004MC time window counts backward from this date.
- Current: 3 Months
- Prior: 4-6 Months
- Prior: 7-12 Months

Confirm this date matches the effective date you want for your analysis before generating the report.

## Set the stable range

The stable range controls when a market change is classified as **Stable** instead of **Increasing** or **Decreasing**.
- Enter a **High Limit %** and a **Low Limit %** (both default to 0%)
- Changes above the high limit are classified as Increasing
- Changes below the low limit are classified as Decreasing
- Changes within the range are classified as Stable
- Check **Use this overall stable range next time** to save your range for future reports

For example, a stable range of -5% to +5% treats minor market movement as Stable.

## Add optional sections
- Check **Include search criteria and listing summary** to document how you built your comp set. This can help you preserve support for the appraisal workfile.

When your settings are confirmed, generate the report.

# Reading the report

The generated report includes Year 1 1004MC tables and an Explanation of Results.

## Overall trend

Each metric receives an overall trend of **Increasing**, **Stable**, or **Decreasing**. The trend compares the earliest reported period with the most current reported period, using your stable range to decide when a change counts as Stable.

Where the 1004MC form uses the label **Declining**, use the report's **Decreasing** value.

## Explanation of Results

The report includes an Explanation of Results by default. It documents your report date, your stable range, how trends were calculated, and how missing values were handled, which means you can review, validate, and retain the calculation logic with your appraisal file.

# Tips
- The report is calculated from the exact listings in your result set or selection. Adjust your search or selection first if the comp set is not right.
- Missing data does not block report generation. If a listing is missing a field required for one metric, it is excluded from that metric only.
- Median Sale Price as % of List Price is calculated per sold listing first, and the report shows the median of those percentages. This means you cannot recreate it by dividing the displayed median sale price by the displayed median list price.
- Active listing counts come from a snapshot date for each period, not from every listing that was active at any point during the period.
