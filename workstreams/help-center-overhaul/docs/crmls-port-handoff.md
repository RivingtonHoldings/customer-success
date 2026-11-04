# CRMLS port: where it stands and how to pick it up

Status page for the CRMLS help center port, the project that replaces every article in the CRMLS help center (ID 4767477) with a record built from the Notion row, carrying the CRMLS screenshots and videos. Paused by Leo on November 4, 2026 with four of the five Client Experience pilot articles created as drafts. Anyone on the team can resume from this page.

## Roles and contacts

- Leo Jedynak, decision owner for the port and the pilot: [leo.jedynak@perchwell.com](mailto:leo.jedynak@perchwell.com)
- Tara, publishes Intercom drafts and sets Fin labels
- Visual owner for the pilot rows (Notion `Visual Owner`): the missing CRMLS screenshots listed below are theirs
- Video owner for the pilot rows (Notion `Video Owner`): the CRMLS recordings are theirs

## What is true right now

- The CRMLS mode of `/port-to-intercom` exists and has been used. Say "port to CRMLS" with a Notion page URL. The rules are in `.claude/skills/port-to-intercom/SKILL.md` under CRMLS mode, and the policy in `.claude/skills/article-draft/references/intercom-push.md`.
- The Notion database has a new `Intercom URL CRMLS` property. One row drives two Intercom records: `Intercom URL` is the Baldwin record, `Intercom URL CRMLS` is the CRMLS record. Four rows are filled (TRK-015 to TRK-018).
- `docs/help-center/crmls-port-map.md` lists each pair of records, what the CRMLS record replaces, what is still missing from it, and which links still point at Baldwin.
- `docs/help-center/collections.md` was regenerated on November 4 after a teammate restructured the CRMLS collections to Baldwin's names. CRMLS now has Client Experience (19802003), Getting Started Guide (19802001), Then vs. Now (19802002), Manage People (19802005), User Settings (19802006), FAQs & Cheat Sheets (19802007), Mobile (19802008), and Perchwell Training Sessions (19802009), alongside the legacy collections. Listing Maintenance does not exist yet; CRMLS still has "Listings" (16866957).
- Both mirrors were re-synced on November 4 with a clean second run. The CRMLS mirror shows the new drafts under Client Experience.

## The four CRMLS drafts that exist

All four sit in Client Experience (19802003), state draft, author 8314814 (the connector's admin). None is published. Nothing in Baldwin was changed.

| Tracker | Article | Baldwin record | CRMLS record | What is missing in the CRMLS record |
|---|---|---|---|---|
| TRK-015 | Accept Your Agent's Perchwell Invitation | 15521326 | 18231917 | Login-page screenshot under Sign in to Perchwell on a computer (only a Baldwin one exists) |
| TRK-016 | Communicate with Your Agent via Messages in Perchwell | 11373888 | 18231941 | Video (Video Status CRMLS is Not Started) |
| TRK-017 | Receive Alerts About New Listings | 11373805 | 18231970 | Nothing |
| TRK-018 | Share Listings with Your Agent | 11373849 | 18232061 | Two screenshots (Email tab of the Share window; Share window under Messages) and the video. Visual Status CRMLS is Blocked |

Every cross-link in these four still points at `/baldwin/en/` except the Unsubscribe link in TRK-017, which points into CRMLS because that shared record still sits in a CRMLS collection. The link pass (below) fixes the rest once all five records exist.

## The one article not yet ported

TRK-019, View Shared Saved Searches (Baldwin 14743530). Its CRMLS body was converted and reviewed in the dry run but never written to Intercom, because Leo paused before confirming. To create it, run "port to CRMLS" on its Notion page (`https://app.notion.com/p/3f98b9e01438810085e3f0a19dc5ff5f`). Expected result: 3 CRMLS screenshots, no video (Not Started), two links kept on Baldwin. It replaces legacy CRMLS record 11373447.

## Things a teammate created today that need a decision

The collection restructure created seven **published** CRMLS records with empty bodies, one per new collection, author 10644865, created 17:38 to 17:45 UTC on November 4. They make the new collections visible on the public site, and they also give CRMLS members and Fin blank articles to open:

| Record | Title | Collection |
|---|---|---|
| 18231637 | Share Listings With Your Agent | Client Experience (19802003) |
| 18231652 | Masquerade an Agent's Account | Manage People (19802005) |
| 18231676 | Update Your Brokerage Logo and Colors | User Settings (19802006) |
| 18231693 | Common Perchwell FAQs | FAQs & Cheat Sheets (19802007) |
| 18231715 | Search in the Perchwell Mobile App | Mobile (19802008) |
| 18231729 | Perchwell Quick Start Training & Workshop | Perchwell Training Sessions (19802009) |
| 18231908 | Listing Field Changes in Perchwell | Then vs. Now (19802002) |

18231637 duplicates the subject of the port's draft 18232061 in the same collection. Recommended: unpublish each placeholder as soon as a real CRMLS record is published in its collection, and unpublish 18231637 when 18232061 goes live. Confirm with whoever created them before touching them; the port did not create them and the map does not list them.

Also created today and still to delete by hand in Intercom: scratch draft 18231816, "Scratch: CRMLS Client Experience image shelf 2026-11-04 (delete me)", with no collection. It only exists to have re-hosted the 11 CRMLS screenshots.

## How to resume, in order

1. Run `/setup-check` and `/sync-help-center`. A clean second run means the mirror can be trusted.
2. Port TRK-019 with "port to CRMLS" (see above). One confirmation, one changelog line, one map row, fill `Intercom URL CRMLS`.
3. Run the **link pass**: "port to CRMLS" once more over each of the five Client Experience rows. Each is an update of the existing CRMLS record, and the only change should be `/baldwin/en/` links turning into `/crmls/en/` links to the five new records. The link to Create a Search with Filters (13903380) stays on Baldwin until the Search collection ports. Confirm each article.
4. Ask Tara to publish the five drafts in Intercom and set Fin labels (`MLS: CRMLS`).
5. **Retire** what they replace, with one confirmation each: set legacy records 11373210 (Accept Your Agent's Perchwell Invitation) and 11373447 (View Shared Saved Searches) to draft with `update_article` carrying `id` and `state` only. Leave 11403062 (Engaging with Multiple Agents, already a draft) for a human to delete. Unsubscribe from Saved Search Alert Emails (13602428) is a Client Collaboration row, not part of this pilot.
6. Decide the fate of the seven empty placeholders above, then re-probe `collections.md` and re-sync.
7. Next collection. The CRMLS-scoped Notion rows, grouped by the Baldwin collection their live article sits in, are listed in the plan file section "CRMLS collections" and in `decisions.md` (2026-11-04). Client Collaboration (9 live rows plus its FAQ) is the natural next wave; CRMLS still has the legacy Agents and Invited Clients sub-collections under it.

## Open items for the visual and video owners

- TRK-015: a CRMLS login-page screenshot (Sign in to Perchwell on a computer). The Notion page has only the Baldwin one.
- TRK-018: CRMLS screenshots of the Email tab of the Share window and of the Share window under Messages. `Visual Status CRMLS` is Blocked.
- TRK-016, TRK-018, TRK-019: CRMLS videos. `Video Status CRMLS` is Not Started on all three. When a recording lands, set the row's `Video Status CRMLS` to Complete (or label the video `CRMLS |` in its Notion caption) and re-run the CRMLS port as an update.
- When any of these land, the CRMLS mode re-port carries them; the Baldwin record is not touched.

## Where the rules and records live

- Skill: `.claude/skills/port-to-intercom/SKILL.md` (CRMLS mode, Link pass, Retirement) and `references/intercom-html.md` (video label rows, Arcade links).
- Policy: `.claude/skills/article-draft/references/intercom-push.md`; schema: `.claude/skills/article-draft/references/notion-publishing.md`.
- Decision: `workstreams/help-center-overhaul/docs/decisions.md`, entry 2026-11-04.
- Records: `docs/help-center/changelog.md` (four CRMLS lines dated 2026-11-04), `docs/help-center/crmls-port-map.md`, `docs/help-center/collections.md`.
- The converter used for the pilot lived in the session scratchpad and is not in the repo; the skill text is the source of truth and the next port rebuilds the body from it.
