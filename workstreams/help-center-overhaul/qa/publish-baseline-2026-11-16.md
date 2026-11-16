# Publishing baseline: what the current `/port-to-intercom` would do

Recorded November 16, 2026, before any change to the publishing skills. Read-only: Notion rows and live Intercom articles were read; nothing was written to Notion or Intercom, no scratch drafts were created, and no image was uploaded. The point is to rerun the same four checks after each build stage of the `/publish` proposal and compare. Any difference should be an intended one from the approved proposal.

Method: the Notion row and live Intercom record were read for each article, and the skill's steps 1 to 6 were applied by hand (preconditions, update or create, filtering of MLS-specific media, link resolution, comparison with the live body), with the status precondition recorded as the skill states it. Links were checked against the live bodies and `docs/help-center/crmls-port-map.md`, not by fetching every linked Notion row. Image hosting was not exercised.

Checks run: TRK-081 on Baldwin, TRK-095 on Baldwin, TRK-095 on CRMLS, TRK-127 on CRMLS.

## 1. TRK-081, Filter Your Search by Property Type and Subtype (Baldwin)

- Notion row: MLS Baldwin only, status Live in Intercom, review Complete, Intercom URL filled, last edited Nov 5, 15:43 UTC.
- Live record: article 13922158, published, collection 17797941 (Search / Search, Baldwin), last updated Nov 4, 18:30 UTC.
- Preconditions today: fails. The Baldwin flow requires `Ready to Transfer` and never overwrites a `Live in Intercom` row. A person would have to set the row back first.
- Update or create: update (Intercom URL filled).
- Text, title, description: identical to the live record.
- Media: 3 Baldwin images kept, 3 CRMLS images dropped, Loom video (caption starts `Baldwin |`) kept and already present in the live record.
- Images: the Baldwin screenshots in Notion are uploaded files, not links to the live copies, so today's skill cannot tell whether they match the live images. It would re-host all 3.
- Links: 2 links to Baldwin articles, same as the live record.
- Notion was edited about 21 hours after Intercom was last updated, but the text matches, so the later edit was probably to properties or media.
- Spacing: the live body has no empty spacer paragraphs between blocks, while the converter's spacing rule would add them. Expect whitespace-only differences on any Baldwin re-port.

## 2. TRK-095, Universal Search Bar (Baldwin)

- Notion row: MLS Baldwin and CRMLS, Live in Intercom, review Complete, both URLs filled, last edited Nov 5, 16:16 UTC.
- Live record: article 11002620, published, collection 17797941, last updated Nov 4, 20:15 UTC.
- Preconditions today: fails, for the same status reason as above.
- Update or create: update.
- Text, title, description: identical to the live record.
- Media: 2 Baldwin images kept, 2 CRMLS images dropped, Baldwin Loom video kept and present in the live record.
- Images: the Baldwin images in Notion are Intercom CDN links, and their paths match the images in the live body, so the live copies can be reused.
- Links: 5 links to Baldwin articles, same as the live record.
- Same spacer-paragraph difference as above.

## 3. TRK-095, Universal Search Bar (CRMLS)

- Live record: article 18234136, published, collection 16866865 (Search / Search, CRMLS), last updated Nov 5, 17:56 UTC, which is after the Notion edit.
- Preconditions today: pass. Status Live is accepted, review Complete, MLS contains CRMLS, and the CRMLS Search collection exists.
- Update or create: update (Intercom URL CRMLS filled).
- Text, title, description: identical to the live CRMLS record.
- Media: 2 CRMLS images kept, 2 Baldwin images dropped, the Baldwin-labeled video dropped. The live CRMLS record has no video, which matches.
- Images: the CRMLS images are uploaded files, so they would be re-hosted and cannot be compared with the live ones. This is the "cannot be verified" case in the proposal.
- Links: 5 links resolve to CRMLS articles, matching the live CRMLS record.
- The live record has empty spacer paragraphs after blocks, as the converter produces.

## 4. TRK-127, Create a Quick CMA Report (CRMLS)

- Notion row: MLS CRMLS only, status Draft, review Review Finished, Intercom URL empty, Intercom URL CRMLS filled, Video Status CRMLS Complete, last edited Nov 12, 16:10 UTC.
- Live record: article 18247092, published, collection 16867011 (Reports, CRMLS), last updated Nov 5, 17:51 UTC.
- Preconditions today: fails. The CRMLS flow accepts only `Live in Intercom` or `Ready to Transfer`, and this row is `Draft`. The collection-match check also reads the Baldwin record's collection, and this row has no Baldwin record, so that check has nothing to read.
- Update or create: update.
- Media: 5 CRMLS images kept. The video caption reads `CRMLS: Create a Quick CMA Report`, not `CRMLS |`, so it counts as unlabeled and is kept because Video Status CRMLS is Complete. One image caption has two spaces before the `|`.
- Difference from live: Notion has a Loom video that the live CRMLS record does not contain. A re-port would add it.
- Links: 1 link, to Create a CMA with a Subject Property, resolves to the CRMLS article 18233073, matching the live record.
- Notion was edited a week after the last Intercom update.

## What this baseline shows

1. Baldwin rows that are Live cannot be updated today without moving the status back, and a CRMLS-only row that has been ported stays `Draft`, so it cannot be updated either. This is the gap the proposal's single update rule addresses. The rule needs to say what happens for CRMLS-only rows, which never reach `Live in Intercom` today.
2. For CRMLS-only rows, the collection check has no Baldwin record to read. The proposal's check against the target MLS's collections covers it.
3. Image identity can be confirmed only for images that are Intercom links in Notion. Uploaded images cannot be compared with the live copies, which is the case the proposal's first-publish rule handles.
4. Two caption forms in TRK-127 (`CRMLS:` and `CRMLS  |`) are accepted today as unlabeled. Under the proposal they would be flagged as unrecognized labels.
5. The video missing from the live TRK-127 record is a media addition the new media check should report.
