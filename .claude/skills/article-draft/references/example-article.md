# Example Articles

Two real, live Baldwin articles, chosen by the team on 2026-09-04 as the model for the standard in `docs/standards/content-standards.md`. Use them as the specimen for new drafts.

These are the actual published articles, not idealized versions. The only changes are the ones the standard introduced, and each one is listed under the article so you can see exactly what a live article looks like before and after. Annotations are in `<!-- -->` comments and are not part of the article.

The live sources are mirrored at `docs/help-center/baldwin/how-to-share-a-tag.md` and `docs/help-center/baldwin/create-a-market-conditions-addendum-report-1004mc.md`.

## Specimen 1: flat workflow, no subsections

Use this shape when the article is a set of sibling workflows and none of them needs to be broken down further.

```markdown
# How to Share a Tag

<!-- Article Status: Draft | MLS/AOR: Baldwin | Collection: Tags | Roles: All Except Client | Videos: Yes | Visuals: Yes | Notion: <url> -->

**Description:** Share a Tag with a client using a public link or email, and see what the client sees when they open it.
<!-- 118 characters, names the feature, states the accomplishment -->

Use this article to share a Tag with a client by public link or by email, understand what the client sees when they open it, and send the same Tag again later.
<!-- Jobs-to-be-done opening. Names the outcomes, not the topic. Replaces the old "In this article, you will learn ..." intro, which described the topic instead. -->

https://www.loom.com/embed/c98bdf808cbd42b48b794e8720bb9a34
<!-- Primary video sits directly under the opening paragraph. The written steps below stand on their own without it. -->

## Share a Tag with a public link

Sharing a Tag by public link generates a link you can send however you'd like: by text, email, or on your own website.
<!-- The heading echo. "Sharing a Tag by public link" repeats the heading's terms, so the section identifies itself if Fin retrieves it alone. The live article opens "Generate a link you can send ...", which does not. -->

### Steps:

1. Click **Tags** in the navigation bar
2. Find the Tag and click **Share**
3. Click **Copy Link**
4. Send the link to your client

A success toast confirms the link copied. The client does not need a Perchwell account to open a shared Tag link.
<!-- Instruction completeness: what happens after the last step. The second sentence repeats "shared Tag link" rather than saying "it". -->

## Share a Tag by email

Sharing a Tag by email sends it directly from Perchwell instead of copying a link out.

### Steps:

1. Click **Tags** in the navigation bar
2. Find the Tag and click **Share**
3. Enter the client's email in the **Share via Email** field
4. Click **Send**

The client receives an email with a link to the Tag.

## What your client sees in a shared Tag

Opening a shared Tag link brings the client to a branded page showing the Tag's listings. No login is required.

- They can browse each listing's details by clicking the listing
- They can like or dislike listings. Liked listings are added back to your Tag automatically, and they can undo a reaction at any time

![The shared Tag page a client sees, showing the Tag's listings in a branded grid with like and dislike controls on each listing](https://downloads.intercomcdn.com/i/o/trq7czv5/2588114260/a91df4a4c9a22fe07ae2990e72e5/Screenshot+2026-08-05+at+12_47_25%E2%80%AFPM.png)
<!-- Alt text describes what the screenshot shows. The live article has the same image with none. -->

## Share a Tag again

Re-sharing sends the same Tag's link to a client again, or notifies a client you added after the first share.

### Steps:

1. Click **Tags** in the navigation bar
2. Find the Tag and click **Re-Share**
3. Copy the link, or send it again by email
```

What changed from the live article:

- Added the jobs-to-be-done opening paragraph. The live article has no opening line in the body at all; its intro exists only in the Intercom description field, so Fin's first chunk starts cold at the first heading.
- Added alt text to the screenshot.
- Added heading echoes to the first sentence of each section, and swapped pronouns for the feature name.
- Renamed two headings so they carry the feature: "What your client sees" became "What your client sees in a shared Tag", "Share again" became "Share a Tag again".
- Added the missing "what happens next" line to the email section.
- Removed terminal periods from the step lines.

Heading levels were already correct: title H1, sections H2, `Steps:` H3.

## Specimen 2: nested workflow, with subsections

Use this shape when a section has real subtopics. Note that the levels shift down one from the live article.

```markdown
# Create a Market Conditions Addendum Report (1004MC)

<!-- Article Status: Draft | MLS/AOR: Baldwin | Collection: Reports | Roles: All Except Client | Videos: No | Visuals: No | Notion: <url> -->

**Description:** Generate a 1004MC Market Conditions Addendum Report from your search results and export it for your appraisal workfile.
<!-- 131 characters -->

Use this article to generate a 1004MC Market Conditions Addendum Report from your comparable listings, set the reporting periods and stable range, and read the results for your appraisal workfile. A 1004MC is the Fannie Mae Form 1004MC / Freddie Mac Form 71 market conditions addendum.
<!-- Opening states the outcomes and defines the abbreviation on first use. -->

## When to use a Market Conditions Addendum Report

Use a Market Conditions Addendum Report when you need 1004MC market metrics calculated from the exact comparable listings you researched.

- Complete the market conditions sections of the Fannie Mae Form 1004MC / Freddie Mac Form 71
- Keep defensible supporting calculations in your appraisal workfile

## Create the report from your search results

Creating a Market Conditions Addendum Report starts from your Search results, so build the comp set you want before you open the report.
<!-- H2, demoted from the live article's H1. The lead sentence is new: the live article jumps straight from the heading to "Steps:". -->

### Steps:

1. Open **Search** and run a search for your comparable listings
2. To use specific listings, select the checkboxes next to them. To use every listing in your results, leave them unselected
3. Click **Actions**, then **Create a Report**
4. Select **Market Conditions Addendum Report**

The report configuration screen opens with your listings loaded.
<!-- The live article moves straight to the 500-listing limit without saying what the last step produces. -->

## Configure the report

Before you generate the report, confirm your listings, report max date, and stable range.

### Choose your listings

- **All listings** (default) includes every listing in your search results
- **Selected listings** appears when you selected specific listings before opening the report

### Set the report max date

The report max date defaults to today and acts as the anchor date for every reporting period, which means each 1004MC time window counts backward from this date.
<!-- "Which means" clause translating a system term into member behavior. -->

- Current: 3 Months
- Prior: 4-6 Months
- Prior: 7-12 Months

Confirm this date matches the effective date you want for your analysis before generating the report.

### Set the stable range

The stable range controls when a market change is classified as **Stable** instead of **Increasing** or **Decreasing**.

- Enter a **High Limit %** and a **Low Limit %** (both default to 0%)
- Changes above the high limit are classified as Increasing
- Changes below the low limit are classified as Decreasing
- Changes within the range are classified as Stable
- Check **Use this overall stable range next time** to save your range for future reports

For example, a stable range of -5% to +5% treats minor market movement as Stable.

### Add optional sections

Check **Include search criteria and listing summary** to document how you built your comp set. This preserves support for the appraisal workfile.

When your settings are confirmed, generate the report.

## Read the 1004MC report

The generated 1004MC report includes Year 1 1004MC tables and an Explanation of Results.

### Overall trend

Each metric in the 1004MC report receives an overall trend of **Increasing**, **Stable**, or **Decreasing**. The trend compares the earliest reported period with the most current reported period, using your stable range to decide when a change counts as Stable.

> **Note:** Where the 1004MC form uses the label **Declining**, use the report's **Decreasing** value.
<!-- Callout leads with a bold label, no emoji. This is the line Fin should carry into an answer about the Declining label. -->

### Explanation of Results

The Explanation of Results is included by default. It documents your report date, your stable range, how trends were calculated, and how missing values were handled, which means you can review, validate, and retain the calculation logic with your appraisal file.

## Limitations of the 1004MC report

- The report supports up to 500 listings. If your search returns more than 500, refine your search filters or reduce your selection before generating the report
- Missing data does not block report generation. If a listing is missing a field required for one metric, it is excluded from that metric only
- Active listing counts come from a snapshot date for each period, not from every listing that was active at any point during the period

## Tips

- The report is calculated from the exact listings in your result set or selection. Adjust your search or selection first if the comp set is not right
- Median Sale Price as % of List Price is calculated per sold listing first, and the report shows the median of those percentages, which means you cannot recreate it by dividing the displayed median sale price by the displayed median list price
```

What changed from the live article:

- Demoted every heading one level: sections from H1 to H2, subsections from H2 to H3, `Steps:` from H2 to H3. The live article competes with its own title at H1.
- Added the jobs-to-be-done opening paragraph and defined 1004MC on first use.
- Renamed headings so each carries the feature: "Report creation" became "Create the report from your search results", "Reading the report" became "Read the 1004MC report".
- Added lead sentences with heading echoes where the live article jumps from heading to list.
- Added the missing "what happens next" line after the creation steps.
- Split the live article's single "Tips" list: the three hard limits moved to a "Limitations of the 1004MC report" section, and only the recommendations stayed under "Tips".
- Moved the Declining label note into a **Note:** callout, since it is a correction Fin should surface.

## Why these two

- Between them they cover both heading shapes: flat sibling sections, and sections with real subtopics.
- Both are task-led, second person, imperative, with bolded UI elements and exact numbers.
- Both state system behavior the member could not discover alone: the client needs no account, liked listings return to the Tag, the 500-listing ceiling, how the median-of-percentages metric is derived.
- Neither uses marketing language, em dashes, or a support footer.
