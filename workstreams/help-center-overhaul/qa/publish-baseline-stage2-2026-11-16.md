# Stage 2 check: the edited `/port-to-intercom` against the baseline

Recorded November 16, 2026 on branch `publish-stage2-port-generalization`. Read-only, like the baseline in `publish-baseline-2026-11-16.md`: the edited skill's steps were applied by hand to the same four checks, using the Notion rows and live Intercom articles already read for the baseline, plus the readiness table on the Production Tracker and the changelog. Nothing was written to Notion or Intercom, and no image was hosted.

## Result per check

| Check | Baseline (before) | Stage 2 (after) | Difference intended? |
|---|---|---|---|
| TRK-081, Baldwin | Fails: row is Live, Baldwin required Ready to Transfer | Passes every precondition. Update of 13922158. Title matches. Collection 17797941 is Baldwin's. Readiness Baldwin Yes. Last changelog line 2026-11-04, live article updated the same day, so no edited-in-Intercom warning | Yes, this is the update rule |
| TRK-095, Baldwin | Fails, same reason | Passes. Update of 11002620. Same checks as above; newest Baldwin line 2026-11-04, live updated the same day | Yes |
| TRK-095, CRMLS | Passes | Passes. Update of 18234136. Collection 16866865 is CRMLS's. Newest line 2026-11-05, live updated the same day | No change |
| TRK-127, CRMLS | Fails with a bare precondition failure, and the collection check has no Baldwin record to read | Refused with the plain message: "This row is Draft, but its CRMLS article is already published. Set the row to Ready to Transfer to publish edits." The title check now strips the ` (CRMLS)` suffix and matches the live title, and the collection check reads the live article's own collection (16867011, CRMLS's), so it works without a Baldwin record | Yes: plain message and suffix handling |

Everything else is unchanged from the baseline: the same text, the same images kept and dropped for each MLS, the same video handling, the same link results, and the same re-hosting of uploaded images.

## Other differences to know about

- **Target is now required.** The old skill defaulted to Baldwin when no MLS was named. It now asks. This follows from treating every MLS as a peer.
- **Retire list only on a create.** The search for legacy records in the target help center now runs when a record is created, not on every port. CRMLS updates previously ran it too.
- **Status after a push.** A push from a `Ready to Transfer` row sets `Live in Intercom`, for any MLS. A CRMLS port from a `Ready to Transfer` row used to leave the status alone. A push from a `Live in Intercom` row never changes it.
- **Edited-in-Intercom check is new.** It uses the newest changelog date, not the exact timestamp the later media record will store, so an edit made on the same day as the last publish is not flagged.
- **TRK-127 after a status fix:** once Tara sets the row to `Ready to Transfer`, it passes, and the push then sets it to `Live in Intercom`.
- **Link rule:** unchanged from today. For CRMLS the keep-and-flag fallback remains; for any other MLS the stop-on-link rule applies. The per-link decision workflow replaces both in the next stage.
- **Not exercised:** image hosting, the Notion and Intercom writes, and the mirror re-sync. Those need a real publish, which is a later step.
