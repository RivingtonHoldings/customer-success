# Stage 3 check: media record and link exceptions against the baseline

Recorded November 18, 2026 on branch `publish-stage3-media-record-links`. Read-only, like the baseline in `publish-baseline-2026-11-16.md` and the Stage 2 check. The edited skill's steps were applied by hand to the same four checks, using the facts already recorded in the baseline and the Stage 2 check. No Notion row or Intercom article was read again, nothing was written to either, and no image was hosted. No media record exists for any of the four articles yet, so each is a first publish under the new scheme.

## Result per check

| Check | Stage 2 | Stage 3 | Difference intended? |
|---|---|---|---|
| TRK-081, Baldwin | Passes. 3 Baldwin images would be re-hosted because they are uploaded files | Passes. The 3 images are uploaded files with no record to compare against, so each is Cannot be verified and goes under Needs your attention; on confirmation they are re-hosted, as before. The Loom video matches the live body and is kept. The edited-in-Intercom check has no record, so it falls back to the changelog date and does not warn | Yes: the images are now flagged instead of silently re-hosted |
| TRK-095, Baldwin | Passes. Images are Intercom CDN links | Passes. Both images are external links whose paths equal the live body's, so both are Unchanged and keep their Intercom copies. The video is unchanged. 5 links resolve to Baldwin articles | Yes: unchanged state is now reported |
| TRK-095, CRMLS | Passes. 5 links resolve to CRMLS articles | Passes. The 2 CRMLS images are uploaded files, so both are Cannot be verified and listed under Needs your attention. The Baldwin video stays dropped. All 5 links are resolved, so no link decision is needed | Yes: images flagged |
| TRK-127, CRMLS | Refused with the Draft message | Still refused with the same message until the row is set to Ready to Transfer. Once passed, the `CRMLS:` video caption and the `CRMLS  |` image caption are listed under Needs your attention, because the first is not in the `CRMLS |` form (the second only has extra whitespace, which is tolerated, so it is not flagged). The Loom video missing from the live record shows as an Added item. The one link resolves to a CRMLS article | Yes: caption form flagged, video addition reported |

## Other differences to know about

- **Links.** No check has a missing link, so no per-link decision came up. The change is untested on a real missing link; it runs the first time a CRMLS article links to a Baldwin-only article. CRMLS no longer keeps the Baldwin URL by default.
- **Edited in Intercom.** Once a record exists, the check compares the exact `updated_at`, so an edit made on the same day as a push is caught. Until then it uses the newest changelog date, as in Stage 2.
- **Media record.** A confirmed push now writes `docs/help-center/media-record/<Tracker ID>.json`. This folder holds only a format file today, and nothing in it is read for content.
- **Link exceptions.** `docs/help-center/link-exceptions.md` exists and holds no exceptions.
- **Not exercised:** a push, the media record write, the history cross-check through `notion-get-version-changes`, a named exception, and the replaced-screenshot comparison against a real record. They need a real publish, which comes with the `/publish` stage.
- **Not in this stage:** the plain-language preview, the nothing-to-publish check, and the `/publish` command.
