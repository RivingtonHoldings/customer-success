---
intercom_id: "16414760"
content_id: "19805100"
title: "Create a Market Conditions Addendum Report (1004MC)"
url: "http://support.perchwell.com/baldwin/en/articles/16414760-create-a-market-conditions-addendum-report-1004mc"
help_center: baldwin
help_center_id: 4755399
collection: "Reports"
collection_ids: [17797980]
state: published
mirror_path: "docs/help-center/baldwin/create-a-market-conditions-addendum-report-1004mc.md"
source_notion_url: "https://app.notion.com/p/3bc8b9e01438813688acd503b01d0508"
migrated_from: master-article-list
---

<!-- Article Status: Draft | MLS/AOR: Baldwin | Collection: Reports | Roles: All Except Client | Video Included: No | Visuals Included: Yes | Notion: https://app.notion.com/p/3f78b9e0143881c6b0eae5f69a2f493a | Old title: Creating a Market Conditions Addendum Report (1004MC) -->

# Create a Market Conditions Addendum Report (1004MC)

**Description:** Create a 1004MC Market Conditions Addendum Report from your search results, set its stable range, and email, print, or download it.

Use this article to create a Market Conditions Addendum Report (1004MC) from your search results, set its orientation, Max List Date, and stable range, email, print, or download it, and read the trends it calculates. The 1004MC is the market conditions addendum to an appraisal, Fannie Mae Form 1004MC and Freddie Mac Form 71.

## When to use a Market Conditions Addendum Report

Create a Market Conditions Addendum Report when you need 1004MC market metrics calculated from the exact comparable listings you researched.

- Complete the market conditions section of Fannie Mae Form 1004MC or Freddie Mac Form 71
- Keep the supporting calculations in your appraisal workfile

## Create a 1004MC report from your search results

Create a Market Conditions Addendum Report from the listings you select on the Search page. Search results are the only starting point for this report, and you need at least one selected listing.

### Steps:

1. Click the Results tab
2. Select the comparable listings you want to include
3. Click Actions
4. Select Create a Report
5. Select 1004MC Market Conditions Addendum
6. Click Next

The report window moves to the Customize Report step with your selected listings.

The Market Conditions Addendum Report supports up to 500 listings. If your search finds more than 500, narrow your search filters or your selection first.

## Set up the 1004MC report

Set up the Market Conditions Addendum Report on the Customize Report step of the report window. Selected Listings at the top shows how many listings the report includes.

> Screenshot placeholder: the Customize Report step for a 1004MC Market Conditions Addendum, captured October 12, 2026 by the teammate; save it to `outputs/drafts/images/2026-10-12-1004mc-customize-step.png` | Alt text: The Customize Report step for a 1004MC report, with the selected listing count, Orientation, Max List Date, and stable range fields.

### Choose the 1004MC report orientation

Select a page orientation for the Market Conditions Addendum Report under Orientation:

- Landscape: Lays out the pages horizontally.
- Portrait: Lays out the pages vertically.

### Set the Max List Date for the 1004MC report

The Max List Date anchors every reporting period in the 1004MC report, which means each time window counts back from this date. The field is required and starts at today's date.

Click the calendar icon in the Max List Date field to select the effective date you want for your analysis.

### Set the stable range for the 1004MC report

The stable range decides when a change in the 1004MC report counts as Stable rather than Increasing or Decreasing. Enter a percentage in each field:

- Stable Range High (%): A change above this percentage counts as Increasing. Starts at 5 and must be 0 or greater.
- Stable Range Low (%): A change below this percentage counts as Decreasing. Starts at -5 and must be 0 or less.

A change between the two percentages counts as Stable. Leave a field blank to set it to 0%.

## Email, print, or download the 1004MC report

Click Next on the Customize Report step to open the Generate Report step of the report window. Click Previous to change a setting.

### Email the 1004MC report

Email the Market Conditions Addendum Report to one or more recipients from the Generate Report step.

### Steps:

1. Enter one or more email addresses in the Emails field
2. *(Optional)* Edit the subject in the Email Subject field
3. *(Optional)* Edit the text in the Message field
4. Click Email Report

Each recipient receives the 1004MC report, and Perchwell copies you on the email.

### Print the 1004MC report

Print the Market Conditions Addendum Report from the Generate Report step.

### Steps:

1. Click Print
2. Choose your printer and settings in your browser's print dialog
3. Click Print in the print dialog

Your browser sends the 1004MC report to your printer.

### Download the 1004MC report as a PDF

Click Download on the Generate Report step to save the 1004MC report as a PDF (Portable Document Format) file.

## Read the 1004MC report

The Market Conditions Addendum Report includes Year 1 1004MC tables, your search criteria and a listing summary, and an Explanation of Results.

### Overall trend in the 1004MC report

Each metric in the 1004MC report gets an overall trend of Increasing, Stable, or Decreasing. The trend compares the earliest reported period with the most current one, and your stable range decides when a change counts as Stable.

> **Note:** Where Form 1004MC uses the label Declining, it matches the report's Decreasing value.

### Search criteria and listing summary in the 1004MC report

Every 1004MC report includes your search criteria and a summary of the listings, which documents how you chose your comparable listings.

### Explanation of Results in the 1004MC report

The Explanation of Results documents your report date, your stable range, how trends were calculated, and how missing values were handled. It keeps the calculation logic with your appraisal file, ready to review and validate.

### How the 1004MC report calculates its metrics

The 1004MC report handles missing data, the sale-to-list ratio, and active listing counts in specific ways:

- Missing data does not stop the report. A listing missing a field for one metric is left out of that metric only.
- Median Sale Price as % of List Price is calculated for each sold listing first, then the report shows the median of those percentages. Dividing the median sale price by the median list price gives a different number.
- Active listing counts come from a snapshot date for each period, not from every listing active at any point during the period.
