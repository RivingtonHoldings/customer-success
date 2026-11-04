# CRMLS port map

One row per Notion article the CRMLS mode of `/port-to-intercom` has carried into the CRMLS help center (ID 4767477) as its own Intercom record. The Baldwin record is the one the Notion row's `Intercom URL` points at; the CRMLS record is the one `Intercom URL CRMLS` points at. Started November 4, 2026 with the Client Experience pilot. The skill adds or updates a row at step 9 of the CRMLS mode; a human never edits the IDs by hand.

Columns:

- **Retire list**: the records the CRMLS record replaces. A CRMLS-only legacy record is set to draft after the CRMLS record is published; a shared Baldwin record is removed from the CRMLS collection by a human in Intercom.
- **Gaps**: steps whose CRMLS screenshot does not exist yet, and a video left out because `Video Status CRMLS` is not `Complete`. Cleared when a re-port carries the asset.
- **Flagged links**: cross-links still pointing at `/baldwin/en/` because the target has no CRMLS record yet. Cleared by the link pass once the collection is complete.
- **Retirement**: `pending publish` until a teammate publishes the CRMLS record, then `done` or the step still open.

| Tracker ID | Article | Baldwin ID | CRMLS ID | CRMLS collection | Retire list | Gaps | Flagged links | Retirement |
|---|---|---|---|---|---|---|---|---|
| TRK-015 | Accept Your Agent's Perchwell Invitation | 15521326 | 18231917 | Client Experience (19802003) | 11373210 (legacy, set to draft after publish) | Login-page screenshot under Sign in to Perchwell on a computer (Baldwin only) | 14743530, 11373888, 11373849 | pending publish |
| TRK-016 | Communicate with Your Agent via Messages in Perchwell | 11373888 | 18231941 | Client Experience (19802003) | none (shared record already out of 16867003) | Video (Video Status CRMLS Not Started) | 11373849 | pending publish |
| TRK-017 | Receive Alerts About New Listings | 11373805 | 18231970 | Client Experience (19802003) | none (shared record already out of 16867003) | none | 11373888, 14743530 | pending publish |
| TRK-018 | Share Listings with Your Agent | 11373849 | 18232061 | Client Experience (19802003) | none (shared record already out of 16867003) | Email tab of the Share window; Share window under Messages (Visual Status CRMLS Blocked); video (Not Started) | 11373888 | pending publish |
