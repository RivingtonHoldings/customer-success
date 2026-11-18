# Stage 4 check: `/publish both` preview for TRK-095

Recorded November 18, 2026 on branch `publish-stage4-publish-command`. A preview-only run of the new `/publish` skill by hand: the Notion row and page body, and both live Intercom articles, were read fresh. Nothing was written to Notion or Intercom, no image was hosted, and no repo file besides this one was written. The readiness table was not read again; Baldwin and CRMLS were `Yes` when it was set up on November 16, and the preview says so as such. The Notion version history was not read, so the "who edited" line is shown as it would appear when that cannot be named.

## The preview the skill produces

```
Publish: Universal Search Bar   (Notion row TRK-095, Review Complete)

Ready to publish: Baldwin yes, CRMLS yes (from the readiness table, last read November 16)

Will update in Intercom
  Baldwin  Universal Search Bar   existing article 11002620   (no new article created)
  CRMLS    Universal Search Bar   existing article 18234136   (no new article created)

Nothing to publish for Baldwin
  The Notion text, title, description, both Baldwin screenshots, and the Baldwin video match the live article. Spacing differences were ignored.

What changed since CRMLS was last published
  Text: no change
  Screenshots: 2 cannot be verified (search field in the top navigation; search window after typing 123 Marsh); 0 replaced; 0 unchanged
  Video: 1 added (the CRMLS Universal Search Bar recording; the live CRMLS article has no video)

Left out on purpose
  CRMLS: the 2 Baldwin screenshots and the Baldwin video.

Links: 5 go to CRMLS articles. 0 have no CRMLS article yet.

Needs your attention
  1. The 2 CRMLS screenshots are uploaded files, and this article has no saved record of what was last published, so I cannot tell whether they changed. Choose: re-upload the current Notion images, or stop.
  2. The CRMLS video caption reads "CRMLS: Universal Search Bar", not the standard "CRMLS |" form. It would be kept because the CRMLS video status is Complete, but please confirm it is meant for CRMLS.

Edits since the last publish: the Notion page was last edited November 18 at 15:22 UTC; who edited it could not be read. Intercom has not been edited since the last publish for either MLS.

Next: your choices on items 1 and 2; then I ask you to confirm CRMLS on its own. Baldwin needs nothing.
```

## What this showed

- **Nothing to publish works for Baldwin.** The Notion page was edited on November 18, long after Intercom's last update on November 4, yet the text, title, description, images, and video all match. Without the check, a push would have re-hosted nothing but still counted as a publish. The two Baldwin images are external Intercom links in Notion with paths equal to the live body's, so they are unchanged without any saved record.
- **CRMLS has real differences.** A CRMLS Loom video exists in Notion and not in the live record, and the CRMLS screenshots are uploaded files that cannot be compared. Both land under Needs your attention instead of going out silently.
- **Caption forms.** The `CRMLS: Universal Search Bar` video caption is flagged; the `Baldwin |` one is standard.
- **Links.** All five links in Notion point at Baldwin articles, and each has a CRMLS article (live CRMLS body, November 5 changelog), so the five are rewritten to CRMLS URLs and none is missing. A missing link is untested.
- **Edited in Intercom.** Both live articles were last updated on the same day as the newest changelog line for them (November 4 for Baldwin, November 5 for CRMLS), so there is no warning. Without a media record the check works by day.
- **After the first confirmed push** the media record exists, so the two CRMLS screenshots stop being "cannot be verified" on later runs.

## Not exercised

The readiness read from Notion in this run, the version history names, a refusal (wrong MLS, `Draft` row), `all`, a create, a named exception, and a push. Those need Tara's go-ahead on a real publish.
