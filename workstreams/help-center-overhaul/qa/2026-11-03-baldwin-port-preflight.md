# Baldwin port preflight

A read-only check, run November 3, 2026, of the 71 Baldwin rows in the Perchwell Help Center Database [Sep 2026] that are Ready to Transfer, outside the Search collection. Nothing was written to Notion or Intercom. Create a Listing Performance Report is back in Draft until the feature is live, so it is not included.

## Result

- Every article matches a live, published Intercom article it replaces. None is new.
- None was edited live after October 20, except Manage Listings Page Overview (TRK-049), edited October 20.
- 43 articles reach Baldwin only and can port as they are.
- 28 articles are shared with other help centers. Each needs the same decision made for the Search collection.

## Shared articles

These reach other help centers, so a port changes what those readers see. Every image in them is labeled Baldwin only.

- **Baldwin, CRMLS, and default (15):** TRK-005, 009, 010, 011, 014, 016, 017, 018, 067, 069, 070, 071, 072, 073, 074
- **Baldwin and default (13):** TRK-008, 012, 015, 020, 021, 022, 023, 024, 025, 044, 045, 046, 049

The Search port precedent (October 23): strip the "Baldwin |" labels, keep the Baldwin screenshots, and accept that CRMLS and default readers see them for now.

## Decisions before porting

**Live videos the port would remove.** The Notion draft has only a placeholder where the live article has a working video:
- TRK-018 Share Listings with Your Agent: two Looms
- TRK-019 View Shared Saved Searches: one Arcade
- TRK-070 Quick CMA, TRK-073 Full Report, TRK-074 One Page Report: one Arcade each
- TRK-096 Create and Edit a Tag, TRK-097 Link a Saved Search to a Tag: one Loom each (the QA file says TRK-097's Loom shows the old Tag window)

**Live content Notion does not have.** TRK-049 has a "Share draft listings" section added live on October 20, plus a Tip on photos under 15 MB.

**Links to articles outside Baldwin.**
- TRK-001 and TRK-002 link Analytics Tab Walkthrough to 8955889, which is CRMLS and default only. The Baldwin article is 17453999.
- TRK-001 and TRK-058 link Share and Export Analytics Charts to 8955876, which is CRMLS and default only. No Baldwin copy was found.

**Facts that contradict each other.**
- Push notifications for client messages: TRK-006 says yes, TRK-011 and TRK-055 say no.
- TRK-108 says partials created on July 20 moved; TRK-107 says partials created before July 20.
- TRK-074: capped at 50 listings, then reports over 15 are emailed.
- TRK-068: reports over 500 listings are emailed in one place, and in another you are told to narrow the search.
- TRK-071: "first 15 images", while the photo section holds up to 13.
- Coming Soon Addendum: TRK-031 says it is in the Member Portal; TRK-047 says it will be added soon.
- TRK-054 still lists Auto CMA, which the TRK-066 QA file says is gone.
- TRK-100: the QA file asks whether a public link from Search stays current.

**Other.** Porting TRK-031 should also deprecate Most Common Questions Asked to MLS Staff (14710059), per its QA file.

## Tara's decisions, November 3

- Live videos with only a Notion placeholder are dropped at port. New videos come later, with a re-port.
- TRK-049: the live "Share draft listings" content is now in Notion.
- Analytics links: TRK-001 and TRK-002 now link Analytics Tab Walkthrough at 17453999. The Share and Export Analytics Charts link was cut from TRK-001 and TRK-058. Done in Notion.
- The contradicting facts above: Tara edits them after porting.
- Set Up Saved Searches for Hot Sheets (13903157) has no Notion row and was not in the batch. Add a Hot Sheet to the Dashboard (TRK-020) covers it. Tara archives 13903157 in Intercom once TRK-020 ports in wave 2.
- Shared articles follow the Search rule: strip the "Baldwin |" labels, keep the Baldwin screenshots, and accept that CRMLS and default readers see them for now.

## Small fixes in Notion

- Typos: TRK-067 "will be automatically be sent", TRK-108 "tied to a save search", TRK-013 and TRK-075 a missing period, TRK-112 a stray capital in "Brokerage", TRK-071 a double space.
- TRK-108: "unless you changed it in step 5" points at the wrong step.
- Empty paragraphs that would port as blank gaps: TRK-002, 009, 020, 023, 024, 048, 052, 059, 072, 074, 096, 102.

## Expected at port, no action needed

- Placeholders are omitted and reported. The live article shows no gap.
- Live titles differ from the new Notion titles for many articles. Link text matches once each target ports.
- Open comment threads remain on many pages. Tara edits after porting.

The four group files below hold the per-article tables.

## Port preflight, group A (TRK-001 to TRK-019), Baldwin target

Read-only, run 2026-11-03. All 17 Notion rows are `Ready to Transfer`, MLS Baldwin + CRMLS, `Intercom URL` empty. IDs came from QA files under `workstreams/help-center-overhaul/qa/`. Help centers come from `get_article` parent_ids mapped through `docs/help-center/collections.md` (B = Baldwin, C = CRMLS, D = default). No live article was updated after 2026-10-20; the latest is Client Collaboration FAQ on 2026-10-06.

| TRK | Title | Intercom ID | Live title | State | Help centers (parent_ids) | Live edited after Oct 20 | Notion links / unresolved | Placeholders S/V | Labeled images B/C |
|---|---|---|---|---|---|---|---|---|---|
| 001 | Analytics FAQ | 15200594 | Analytics FAQ | published | B (19642621) | N (07-02) | 1 / 0 (Analytics Page Overview -> 13623210) | 0/0 | 0/0 |
| 002 | Analytics Page Overview | 13623210 | Analytics Tab Overview | published | B (19585615) | N (09-17) | 0 | 1/0 | 6/6 |
| 005 | Bulk Upload Contacts from a CSV File | 10732227 | Bulk Upload Contacts | published | SHARED B+C+D (17797961, 16866993, 12892276) | N (07-02) | 0 | 0/0 | 2/0 |
| 006 | Client Collaboration FAQ | 15201114 | Client Collaboration FAQ | published | B (19642645) | N (10-06) | 0 | 0/0 | 0/0 |
| 007 | Contacts Page Overview | 13975194 | Contacts Page Overview | published | B (17797961) | N (07-28) | 0 | 1/0 (+1 Arcade video embed) | 5/3 |
| 008 | Create and Manage Your Contacts in Perchwell | 14790755 | Create and Manage Your Contacts in Perchwell | published | SHARED B+D (17797961, 579403) | N (07-02) | 0 | 0/0 (+1 Loom embed inside an orange callout) | 5/0 |
| 009 | Export Contacts to a CSV File | 12896093 | Export Your Contact List | published | SHARED B+C+D (17797961, 16866981, 12892276) | N (07-02) | 0 | 0/0 | 2/0 |
| 010 | Invite Clients to Perchwell and Resend Invitations | 11373895 | Invite Clients to Perchwell | published | SHARED B+C+D (17797961, 16866993, 12892276) | N (07-02) | 0 | 0/0 | 3/0 (+1 unlabeled, malformed) |
| 011 | Message Clients in Perchwell | 12541968 | Message Clients in Perchwell | published | SHARED B+C+D (17797961, 16866993, 12892276) | N (07-02) | 0 | 0/0 (+1 Arcade embed) | 4/0 |
| 012 | Set Up Your Clients in Perchwell | 15521779 | Quick Guide: Getting Clients Started in Perchwell | published | SHARED B+D (17797961, 579403) | N (07-02) | 0 | 0/0 | 1/0 |
| 013 | Find and Contact Buyer's Agents with Reverse Prospecting | 16201667 | Reverse Prospecting | published | B (17797961) | N (08-06) | 0 | 0/0 (+1 Loom embed) | 6/0 |
| 014 | Unsubscribe from Saved Search Alert Emails | 13602428 | Unsubscribe from Notifications (For Invited Clients) | published | SHARED B+C+D (17797961, 16867003, 12892229) | N (07-02) | 0 | 0/0 | 2/0 |
| 015 | Accept Your Agent's Perchwell Invitation | 15521326 | Accept Your Agent's Perchwell Invitation | published | SHARED B+D (19361684, 12892229) | N (07-02) | 0 | 0/0 (+1 Arcade embed) | 3/0 |
| 016 | Communicate with Your Agent via Messages in Perchwell | 11373888 | Communicate with Your Agent in Perchwell | published | SHARED B+C+D (19361684, 16867003, 12892229) | N (07-02) | 0 | 0/0 (+1 Loom embed) | 2/0 |
| 017 | Receive Alerts About New Listings | 11373805 | Receive Alerts About New Listings | published | SHARED B+C+D (19361684, 16867003, 12892229) | N (07-02) | 0 | 0/0 | 3/0 |
| 018 | Share Listings with Your Agent | 11373849 | Share Listings with Your Agent | published | SHARED B+C+D (19361684, 16867003, 12892229) | N (08-25) | 0 | 0/1 | 3/0 |
| 019 | View Shared Saved Searches | 14743530 | View Shared Saved Searches | published | B (19361684; 19573826 is "none, 401 everywhere") | N (07-02) | 0 | 0/1 | 3/0 |

None of the 17 contains "[confirm" text, an em dash, "Paragon", a Google Drive link, or bold outside the Description line and callout labels.

## Blockers and flags

### Blockers: the port stops (SHARED with CRMLS, labeled images in the draft)

SKILL.md step 5 stops the port when an article reaches both Baldwin and CRMLS and the draft has labeled images. Eight articles hit this rule. All of them also reach the default help center.

- TRK-005 (10732227)
- TRK-009 (12896093)
- TRK-010 (11373895)
- TRK-011 (12541968)
- TRK-014 (13602428)
- TRK-016 (11373888)
- TRK-017 (11373805)
- TRK-018 (11373849)

Each one needs a decision: split the article per MLS, or pick one image per step. On top of that, most of these drafts have only Baldwin images, so CRMLS and default readers would see Baldwin screenshots.

### Wrong-help-center links (stop under step 5's "not in the target help center" test)

- **TRK-001 and TRK-002:** both link [Analytics Tab Walkthrough] to 8955889. That article sits in CRMLS (16867014) and default (8401610), not Baldwin. The Baldwin article with that title is **17453999**, in collection 19585615.
- **TRK-001:** links [Share and Export Analytics Charts] to 8955876, which is also CRMLS and default only. No Baldwin copy was found.

### SHARED with the default help center only (no CRMLS)

- TRK-008 (14790755)
- TRK-012 (15521779)
- TRK-015 (15521326)

Report these audiences before any diff. All three drafts have only "Baldwin |" images, so default (NYC/brokerage) readers would see Baldwin screenshots. The teammate needs to decide.

### Per-article flags

- **TRK-001:** the one Notion mention resolves to Analytics Page Overview (TRK-002, 13623210). TRK-002 has not ported yet, so its live title is still "Analytics Tab Overview" and the link text will not match it until TRK-002 ports.
- **TRK-002:**
  - The draft has one `Screenshot placeholder (Baldwin)` with empty alt text after "|".
  - There is a trailing empty `<p />`.
  - The first Baldwin caption ends in `<br /><br />`.
  - The 8955889 link uses `http://`.
  - The Notion page has open discussion threads on the Market Activity, Market Analytics and filter lines.
  - Retitle: the live title is "Analytics Tab Overview" and the QA file notes a redirect question.
  - The Notion row shows Visual Status CRMLS "Not Started", but the draft already has 6 CRMLS images. They get dropped for a Baldwin-only port.
- **TRK-005:**
  - The first image's alt text describes "the Create New Contact window ... Bulk upload button", but the step it illustrates says Upload in the upper right opens the Upload Contacts window. The image or alt text may be stale.
  - The live body names Paragon. The Notion draft does not, which is fine.
- **TRK-006:**
  - Every link uses `http://`.
  - The link text "Contacts Page Overview- Mobile" is missing a space.
  - The draft says the mobile app sends push notifications for client messages. TRK-011 says "Push notifications for new messages are not available in the Perchwell mobile app." These contradict each other; confirm before porting either one.
  - The QA file says the live body was edited around Oct 6. That matches updated_at, and the edit came before the review.
- **TRK-007:**
  - The second contact-profile image is captioned "Baldwin |" but comes from the CRMLS screenshot batch (Screenshot_2026-10-29) and its alt text mentions "Shared Buildings". It is probably mislabeled and should be "CRMLS |". As it stands, Baldwin gets two profile images.
  - One `Screenshot placeholder (Baldwin)` is still open.
  - Six links use bare `/en/` paths instead of `/baldwin/en/`: 14790755, 10732227, 11112420, 11373895, 12541968, 12896093.
- **TRK-008:**
  - The Loom video sits inside an orange (placeholder-colored) callout. Confirm whether it is the final video or a placeholder.
  - "See Assign a contact to a group and Edit a contact's details" is plain text, not a link.
- **TRK-009:**
  - The Description line is wrapped in `<p>` and uses "You can".
  - There is a trailing empty `<p />`.
  - The 10732227 link uses a bare `/en/` path.
- **TRK-010:**
  - Notion `Article Review Status` is "Revisions in Progress" while the status is Ready to Transfer. Confirm the review is actually done.
  - One image caption has no MLS label: `\| Alt text: The Upload Contacts window...`.
- **TRK-011:**
  - The draft has an Arcade embed, but Video Status Baldwin is "Not Started".
  - Links use `http://`.
  - "(Optional)" is in italics.
  - The push-notification conflict with TRK-006 is noted above. The live article also says push notifications work.
- **TRK-012:**
  - Retitle from "Quick Guide: Getting Clients Started in Perchwell".
  - The alt text says "Add contact pencil icon", while other drafts call the button Add New. Check it.
- **TRK-013:**
  - Retitle from "Reverse Prospecting".
  - The Loom embed is present, but Video Status Baldwin is "Not Started".
  - A sentence is missing its period: "To reach more than 10 buyer's agents, send another email".
- **TRK-014:**
  - Retitle from "Unsubscribe from Notifications (For Invited Clients)".
  - The link uses `http://`.
  - Notion Collection is "Client Collaboration" and Roles is "Invited Client". The live article sits in Baldwin Client Collaboration (17797961); confirm whether it belongs in Client Experience.
- **TRK-015:**
  - The Arcade embed is present, but Video Status Baldwin is "Not Started".
  - One image is a markdown image hotlinked from downloads.intercomcdn.com, with the caption in its alt.
  - External links go to apps.apple.com, play.google.com and www.perchwell.com/accounts/sign_in. They are expected, but noted.
  - The password alt text says "five green requirement checks" while the list shows four requirements.
  - The draft links "Communicate with Your Agent in Perchwell" (11373888), but that row's Article Name is "...via Messages in Perchwell", so the link text differs.
- **TRK-016:**
  - Retitle from "Communicate with Your Agent in Perchwell".
  - The Loom embed matches the live one.
  - The draft has "You can also sort Listings based on client reactions." It uses "you can" and a capitalized "Listings", and sorting may be an agent-side feature. Check it.
  - The link uses `http://`.
- **TRK-017:** links use `http://`. The Unsubscribe link text uses the draft title, but the live title is still the old one until TRK-014 ports.
- **TRK-018:**
  - The draft has a video placeholder, but the live article has a Loom video (157b29ff...) and a second Loom in a "Create communication templates" section. Porting removes both. Confirm that is intended.
  - The link uses `http://`.
- **TRK-019:**
  - The draft has a video placeholder, but the live article has an Arcade video (0TAXLJjsebpNZr2VUrYT). Porting removes it.
  - The 13903380 link uses `http://`.

## Preflight, group B (read-only, 2026-11-03)

All 19 Notion rows are `Ready to Transfer`. Every one maps to a live, published Intercom article, so none is NEW. Help centers come from `parent_ids`: 10863226 is default Dashboard, 19406083 is default Add/Edit, and every other ID is Baldwin. No article reaches CRMLS. S/V counts placeholders only. Embedded Loom and Arcade videos are real videos and are not counted.

| TRK | Notion title | Intercom ID | Live title | State | Help centers (parent_ids) | Live edited after Oct 20 | Notion links / unresolved | Placeholders S/V | Labeled images B/C |
|---|---|---|---|---|---|---|---|---|---|
| 020 | Add a Hot Sheet to the Dashboard | 13893409 | Add a Hot Sheet to the Dashboard | published | Baldwin 17797865 + default 10863226, SHARED | N (2026-07-20) | 0 / 0 | 0/0 | 1/0 |
| 021 | Customize Your Dashboard | 13623904 | Customize Your Dashboard | published | Baldwin 17797865 + default 10863226, SHARED | N (2026-07-02) | 0 / 0 | 0/0 | 3/0 |
| 022 | Dashboard FAQ | 15216626 | Dashboard FAQ | published | Baldwin 19644346 + default 10863226, SHARED | N (2026-07-20) | 0 / 0 | 0/0 | 1/0 |
| 023 | Dashboard Overview | 13903062 | Dashboard Overview | published | Baldwin 17797865 + default 10863226, SHARED | N (2026-09-29) | 0 / 0 | 0/0 | 8/0 |
| 024 | Access Integrations from the Dashboard or a Listing | 13903183 | Integration Tools on the Dashboard | published | Baldwin 17797865 + default 10863226, SHARED | N (2026-07-02) | 0 / 0 | 0/0 | 3/0 |
| 025 | Find Listings in the Listings Widget | 13903171 | Listings Widget Overview | published | Baldwin 17797865 + default 10863226, SHARED | N (2026-07-02) | 0 / 0 | 0/0 | 3/0 |
| 027 | What Each Listing Status Means | 14709241 (from QA) | Listing Statuses in Perchwell | published | Baldwin 19547885 | N (2026-09-03) | 1 / 0 | 0/0 | 0/0 |
| 028 | Login and Troubleshooting FAQ | 14710265 (from QA) | Login, Access & Troubleshooting Guide and FAQ | published | Baldwin 19547885 | N (2026-07-02) | 0 / 0 | 1/0 | 0/0 |
| 031 | MLS Rules and Compliance FAQ | 14710094 (from QA) | Top Compliance Questions | published | Baldwin 19547885 | N (2026-07-02) | 0 / 0 | 0/0 | 0/0 |
| 030 | All About Property Types and Sub-Types | 14709796 (from QA) | Property Types in Perchwell | published | Baldwin 19547885 | N (2026-07-02) | 0 / 0 | 1/0 | 0/0 |
| 044 | Add and Edit Listings | 13627189 (from QA) | Add and Edit Listings | published | Baldwin 17797908 + default 19406083, SHARED | N (2026-08-04) | 0 / 0 | 0/1 | 5/0 |
| 045 | Write a Listing Description with AI Scribe | 11801815 (from QA) | AI Scribe | published | Baldwin 17797908 + default 19406083, SHARED | N (2026-08-04) | 0 / 0 | 0/0 | 3/0 |
| 046 | Listing Detail Page Overview | 14074994 (from QA) | Listing Detail Page Overview | published | Baldwin 17797908 + default 19406083, SHARED | N (2026-09-10) | 2 / 0 | 0/1 | 8/0 |
| 047 | Listing Maintenance FAQ | 15199904 (from QA) | Listing Maintenance FAQ | published | Baldwin 19642616 | N (2026-10-06) | 0 / 0 | 0/0 | 4/0 |
| 048 | Listing Detail Page FAQ | 15200541 | Listings FAQ | published | Baldwin 19642616 | N (2026-09-01) | 0 / 0 | 0/0 | 1/0 |
| 049 | Manage Listings Page Overview | 13623016 (from QA) | Manage Listings Page Overview | published | Baldwin 17797908 + default 19406083, SHARED | **Y (2026-10-20 12:03 UTC)** | 0 / 0 | 0/1 | 4/0 |
| 050 | Log In as an Agent with Assume Identity | 16053168 (from QA) | Assume Identity | published | Baldwin 18306004 | N (2026-07-30) | 0 / 0 | 0/0 | 9/0 (1 is an intercomcdn image) |
| 051 | Manage People FAQ | 15201140 | Manage People FAQ | published | Baldwin 19642626 | N (2026-07-02) | 0 / 0 | 0/0 | 0/0 |
| 052 | Create and Manage Teams | 14742099 (from QA) | Perchwell Teams | published | Baldwin 18306004 | N (2026-07-02) | 0 / 0 | 0/1 | 3/0 |

Notion links, all resolved, all targets published and in Baldwin:
- TRK-027: "Filter Your Search by Status and Price Changes" (TRK-087, Live in Intercom) resolves to 11010696.
- TRK-046: "Share Listings with Clients from Search" (TRK-093, Live) resolves to 13903326. "Access Integrations from the Dashboard or a Listing" (TRK-024) resolves to 13903183, whose live title is "Integration Tools on the Dashboard" until TRK-024 ports.

Clean on every article: no `[confirm` text, no em dashes, no Paragon in Notion (the live 14709241 and 15199904 still say Paragon, and the drafts remove it), no Google Drive links, and no malformed caption labels. Every caption uses `Baldwin |`. There is no CRMLS-labeled image anywhere.

## Blockers and flags

1. **SHARED with the default help center (10 articles): TRK-020, 021, 022, 023, 024, 025, 044, 045, 046, 049.** Step 4 requires the teammate to decide on each one before the diff. There is no CRMLS overlap, so the step 5 labeled-image stop does not apply. But keeping the `Baldwin |` images, and the `/baldwin/en/` cross-links, shows Baldwin screenshots and Baldwin-path links to default-help-center readers. Notion tags TRK-024, 044, 045, 046 and 049 as Baldwin only. TRK-020 to 023 and 025 are tagged Baldwin and CRMLS, but the live articles are Baldwin plus default, with no CRMLS.
2. **TRK-049 live edited 2026-10-20**, after the October 13 rewrite. The live body has a "Share draft listings" section that Notion lacks: open a draft from Manage Listings, then Actions, then a one page or full report, then download and email it. Its screenshot is dated October 20. Live Tips also mention photos under 15 MB. Merge or confirm the drop before the port. Open fix: Export in the upper right is not in the screenshot.
3. **Placeholders that would ship unfilled:**
   - Screenshot placeholders: TRK-030 (Property type dropdown, bold label, no image) and TRK-028 (orange callout holding the placeholder text plus an unlabeled image).
   - Video placeholders, all with Video Status Not Started: TRK-044, 046, 049, 052.
4. **Article Review Status:** "Review Finished", not "Complete", on TRK-027, 028, 030, 031, 044 to 050, and 052. TRK-051 has no Review Status and no Reviewer. Confirm review is closed.
5. **Open comment threads** are still on TRK-020 (3), 021 (2), 022 (4), 023 (about 9), 024 (1), 025 (2), 044 (3), 046 (3), 047 (6), 048 (4) and 049 (5).
6. **Open article fixes (`docs/open-article-fixes.md`):**
   - TRK-048: the HOA example ($355, $30/mo) does not match the screenshot ($1,050, $88/mo).
   - TRK-049: the Export button question.
   - TRK-052: the screen is titled "Team details", but the article says "Edit Team".
   - TRK-050: one image was rewritten into Notion's other image format. It is a hosted intercomcdn image, and its alt text carries the `Baldwin |` label, which the conversion must strip.
   - TRK-020: the "Visuals Included is No" item looks stale. The row now says Yes and has no placeholder, so remove it from the file.
7. **TRK-031 deprecation:** porting it should also deprecate Most Common Questions Asked to MLS Staff (14710059), which per the QA file was folded into this FAQ. The two drafts also conflict on the Coming Soon Addendum. TRK-031 says it is in the Member Portal under BR Documents, and TRK-047 says it "will be added soon". TRK-031 also says "Member Portal" where TRK-028 says "Baldwin portal".
8. **Link text that changes when siblings port:**
   - 13903171: TRK-044 links it as "Listings Widget Overview" (old title), and TRK-025 renames it.
   - 15200541: TRK-047 links it as "Listings FAQ", which TRK-048 renames.
   - 14709241: TRK-022 and 025 link it as "Listing Statuses in Perchwell", which TRK-027 renames.
   - 16053168: TRK-052 links it as "Assume Identity", which TRK-050 renames.
   - 14742099: TRK-051 links it as "Perchwell Teams", which TRK-052 renames.
   - 13903183 keeps its old title until TRK-024 ports.
   - Several drafts (020, 021, 023, 024, 025) use bare `/en/` links. They need `/baldwin/en/` for Baldwin, or a decision for the shared articles.
9. **Empty `<p />` blocks:** TRK-020 (1, after step 3), 023 (1), and trailing ones on 024, 048 and 052.
10. **Style and content items for a human:**
    - TRK-044: the required-fields screenshot reuses the Autofill alt text, which is a duplicate.
    - TRK-047: "Please reach out" voice and a raw `<p>` block.
    - TRK-049: "You can duplicate any Listing", the agent and office filter bullets have no field names, and "(Optional)" is in italics.
    - TRK-050, 051 and 052 are tagged Baldwin and CRMLS in Notion but are Baldwin-specific ([mls@baldwinrealtors.com](mailto:mls@baldwinrealtors.com), "Baldwin MLS staff"). This is fine for Baldwin, but the MLS tag is wrong.
    - TRK-048 reverses the live "similar listings" answer, and the draft says the page has no such section. This is a product fact; confirm it.
11. **Live content the drafts drop**, all edited before October 20, likely intentional: confirm before the port.
    - TRK-028: the Email Delivery (safe senders) section and "What causes frequent logouts?"
    - TRK-031: "Use GPS in directions" and "within 24 hours of public marketing".
    - TRK-048: "Can I add notes on the listing details page?"

## Port preflight, group C (Mobile and Reports), read-only, 2026-11-03

All 17 Notion rows are `Ready to Transfer` with an empty `Intercom URL`. IDs were taken from the QA files (Sources line) and confirmed against the Baldwin mirror frontmatter. Every live article is `published`, and none was updated after 2026-10-20. Collection 19637741 and 15226711 are "none (401 everywhere)" in collections.md, so they reach no help center.

| TRK | Title (Notion) | Intercom ID | Live title | State | Help centers (parent_ids) | Live edited after Oct 20 | Notion links / unresolved | Placeholders S/V | Labeled images B/C |
|---|---|---|---|---|---|---|---|---|---|
| 053 | Manage Contacts in the Perchwell Mobile App | 14785957 | Contacts Page Overview- Mobile | published (2026-07-29) | Baldwin (19615962) + 19637741 none | N | 0 / 0 | 0/0 | 4/0 |
| 054 | Listing Detail Page in the Perchwell Mobile App | 14784837 | Listing Detail Page Overview | published (2026-07-26) | Baldwin (19615962) + 19637741 none | N | 0 / 0 | 0/0 | 3/0 |
| 055 | Message Clients in the Perchwell Mobile App | 14786130 | Messages Overview | published (2026-07-02) | Baldwin (19615962) + 19637741 none | N | 0 / 0 | 0/0 | 3/0 |
| 056 | Mobile App FAQ | 15201164 | Mobile FAQ | published (2026-07-02) | Baldwin (19642648) + 15226711 none | N | 0 / 0 | 0/0 | 0/0 |
| 057 | Add and Edit Listings in the Perchwell Mobile App | 14785355 | My Listings Overview | published (2026-08-06) | Baldwin (19615962) + 19637741 none | N | 0 / 0 | 0/0 | 4/0 |
| 058 | Search in the Perchwell Mobile App | 14786263 | Search Page Overview | published (2026-07-02) | Baldwin (19615962) + 19637741 none | N | 1 / 0 (TRK-054 page -> 14784837) | 0/0 | 5/0 |
| 059 | Tags in the Perchwell Mobile App | 14786075 | Tags Overview | published (2026-07-02) | Baldwin (19615962) + 19637741 none | N | 2 / 0 (TRK-098 -> 16221617; TRK-096 -> 16221240) | 0/0 | 2/0 |
| 066 | Create a CMA with a Subject Property | 15216797 | Create a CMA with a Subject Property | published (2026-08-12) | Baldwin only (17797980) | N | 0 / 0 | 0/0 (1 Arcade embed) | 3/0 |
| 067 | Create a Listing Report | 8955755 | Create a Listing Report | published (2026-08-12) | SHARED: Baldwin 17797980, CRMLS 16867011, default 579396 | N | 0 / 0 | 3 (Baldwin)/0 | 3/0 |
| 068 | Create a Market Conditions Addendum Report (1004MC) | 16414760 | Create a Market Conditions Addendum Report (1004MC) | published (2026-08-14) | Baldwin only (17797980) | N | 0 / 0 | 0/0 | 2/0 |
| 069 | Create a Media Report | 8955781 | Create a Media Report | published (2026-07-02) | SHARED: Baldwin, CRMLS, default | N | 0 / 0 | 0/0 | 5/0 |
| 070 | Create a Quick CMA Report | 13959293 | Create a Quick CMA Report | published (2026-08-12) | SHARED: Baldwin, CRMLS, default | N | 0 / 0 | 0/1 | 6/0 |
| 071 | Create a Show Sheet | 8955767 | Create a Show Sheet | published (2026-08-12) | SHARED: Baldwin, CRMLS, default | N | 0 / 0 | 0/0 | 5/0 |
| 072 | Create an Itinerary Report | 8955772 | Create an Itinerary Report | published (2026-08-12) | SHARED: Baldwin, CRMLS, default | N | 0 / 0 | 0/0 | 6/0 |
| 073 | Create a Full Report | 12816757 | Create and Share Full Reports | published (2026-09-17) | SHARED: CRMLS 16867011, Baldwin 17797980, default 579396 | N | 0 / 0 | 0/1 | 7/0 |
| 074 | Create a One Page Report | 12816780 | Create One Page Reports | published (2026-08-31) | SHARED: CRMLS, Baldwin, default | N | 0 / 0 | 0/1 | 4/0 |
| 075 | Reports FAQ | 15201097 | Reports FAQ | published (2026-08-31) | Baldwin only (19642643) | N | 0 / 0 | 0/0 | 1/0 |

No "[confirm", em dashes, Paragon, "Alt text" captions missing "|", or stray bold (outside Description and callout labels) turned up in any of the 17 pages.

## Blockers and flags

### Stop under SKILL.md step 5 (shared article with Baldwin-labeled images)
- TRK-067, 069, 070, 071, 072, 073, 074 live in Baldwin, CRMLS, and the default help center, and every image in the draft is captioned `Baldwin |`. Under step 5 the port stops, and the teammate has to choose between splitting the article and picking one image per step. Every cross-link written as `/baldwin/en/` would also be wrong for CRMLS and default readers (070: 15216797; 073: 12816780; 074: 12816757).
- TRK-070 is tagged Baldwin only in Notion, but the live 13959293 reaches CRMLS and default. A port would change the CRMLS and default article too.

### Stop under step 5 (link target not in Baldwin)
- TRK-058: "Share and Export Analytics Charts" links to 8955876, which sits only in CRMLS collection 16867014 (Analytics) and has no Baldwin copy. The teammate decides what to do with it. The Baldwin analytics candidates are 17453999 (Analytics Tab Walkthrough) and 13623210 (Analytics Tab Overview).

### Notion links to resolve (all targets are published and in Baldwin)
- TRK-058: mention of "Listing Detail Page in the Perchwell Mobile App" (TRK-054) resolves to 14784837. That article's live title is still "Listing Detail Page Overview" until TRK-054 ports.
- TRK-059: mention of "Share a Tag with Clients" (TRK-098) resolves to 16221617, live title "How to Share a Tag". Mention of "Create and Edit a Tag" (TRK-096) resolves to 16221240, live title "How to Create a Tag". Both rows are Ready to Transfer, so the link text and the live titles will not match until those two port.

### Links that need the /baldwin/en/ path (bare /en/ in the draft)
- 053: 12541968, 11373895.
- 058: 8955646, 12541968, 8955755.
- 075: 12816757, in the "How do I share a report" answer.
- Several drafts use `http://` rather than `https://`: 054, 055, 056, 058, 073, 074, 075.

### Link text that will not match the live title until the sibling ports
- 054: links "Create One Page Reports" (12816780), which becomes TRK-074.
- 055: links "Tags Overview" (14786075), which becomes TRK-059, and uses "Manage Contacts in the Perchwell Mobile App" as the text for 14785957.
- 075: links "Create a Full Report" (12816757, live "Create and Share Full Reports") and "Create a One Page Report" (12816780, live "Create One Page Reports").

### Placeholders and media
- TRK-067 has 3 orange Baldwin screenshot placeholders:
  - "reuse live image of the Select Report Type step" has no image.
  - One placeholder names a repo path, `outputs/drafts/images/2026-10-12-listing-report-customize-step.png`. That is internal text and must not reach Intercom.
  - "reuse the live image of the Generate Report step" sits right above an actual Generate Report image, so it looks stale.
  - The row's Visual Status Baldwin is still "Not Started".
- TRK-070, 073, 074 each have an orange video placeholder, so each would port with no video. The live articles have Arcade embeds: 13959293, 12816757 (IDl2eNP0YLOorXpgPtaS), and 12816780 (q8cqAyPuAnqnPRjIZdlD). The TRK-070 placeholder says "retired", which is on the banned list, though only in internal text.
- TRK-072 has the Arcade as a bare `app.arcade.software/share/...` link instead of an embed. The live article embeds it.
- TRK-071 keeps the Google Drive "Show Sheet Sample" link, as intended. It is the only Drive link in the group.

### Content issues to raise before porting
- TRK-074 contradicts itself: it says the report is capped at 50 listings, then says a report with more than 15 is emailed.
- TRK-068 says in the intro that a report over 500 listings is emailed automatically. The create section says to narrow the search when there are more than 500.
- TRK-067 states the 500-listing email limit twice, in the Note callout and in the Print section. The Print section also has the typo "will be automatically be sent".
- TRK-071 says a Show Sheet "includes the first 15 images", but the photo section holds up to 13. It also has a double space in "Show Sheet  is".
- TRK-054 still lists Auto CMA in the Actions tab. The TRK-066 QA file records that Auto CMA is gone, per the teammate on Oct 12.
- TRK-075 is missing the final period in "enter the details by hand".
- TRK-070's Notion row has no Article Review Status and no Article Reviewer, even though it is Ready to Transfer.
- TRK-055 says the app sends no push notifications. The live article says it does. That reads as a deliberate correction; noting it for the diff.

### Markup cleanup
- Empty `<p />` blocks: 059 (1), 072 (1), 074 (1).
- Stray `<br />`: 058, 067, 068, 072, 073.
- Bare `<p>` wrappers with trailing spaces: 066, 070.
- 070 has a caption written `Baldwin  |`, with a double space.
- `<i>(Optional)</i>` italics appear in 066, 070, 071, and 073.

### Unresolved comment anchors
Comment anchors are still in place in 054 (3), 057 (2), 059 (1), 066 (3), 067 (3), 072 (2), 073 (3), 074 (3), and 075 (1). Their resolved state was not checked.

### open-article-fixes.md
It has entries for 067, 068, 069, 072, and 073.
- Already fixed in Notion, so they can come off the list:
  - 068: the Customize Report image is now present.
  - 073: the Page 1 and Page 2 captions are present.
  - 072: a first-page image is present.
- Still open:
  - 067: the "% Change +9893.57%" row in the sample.
  - 069: the "photos and floor plans" wording.
  - 072: the default-on Agent name and phone mismatch in the sample.

## Preflight, group D (TRK-096 to TRK-114), read-only

All 18 Notion rows are `Ready to Transfer` / `Review Finished`. No Notion row has an Intercom URL except TRK-100. Every match below was found in the QA file or the Baldwin mirror, then confirmed with `get_article` or `search_articles` (help center 4755399). Every live article is `published`. Every one sits only in Baldwin collections, so none is SHARED. None was updated after 2026-10-20.

| TRK | Notion title | Intercom ID (collection) | Live title | State | Help centers | Live edited after Oct 20 | Notion links / unresolved | Placeholders S/V | Labeled images B/C |
|---|---|---|---|---|---|---|---|---|---|
| 096 | Create and Edit a Tag | 16221240 (17797953 Tags) | How to Create a Tag | published, 2026-08-19 | Baldwin | N | 0 / 0 | 0 / 1 | 7 / 0 |
| 097 | Link a Saved Search to a Tag | 16221382 (17797953) | How to Link a Saved Search to a Tag | published, 2026-08-06 | Baldwin | N | 0 / 0 | 0 / 1 | 4 / 0 |
| 098 | Share a Tag with Clients | 16221617 (17797953) | How to Share a Tag | published, 2026-08-06 | Baldwin | N | 0 / 0 | 0 / 0 (Loom embed) | 5 / 0 |
| 099 | Add Listings to a Tag | 16221347 (17797953) | How to Tag Individual Listings | published, 2026-08-06 | Baldwin | N | 0 / 0 | 0 / 0 (Loom embed) | 3 / 0 |
| 100 | Tags FAQ | 15216706 (19644367 Tags / FAQs) | Tags FAQ | published, 2026-08-05 | Baldwin | N | 0 / 0 | 0 / 0 | 0 / 0 |
| 101 | Tags Page Overview | 14465546 (17797953) | Tags Page Overview | published, 2026-08-06 | Baldwin | N | 0 / 0 | 0 / 0 (Loom embed) | 2 / 0 |
| 102 | Sample Emails to Tell Clients About Perchwell | 15521036 (19197859 Then vs. Now) | Agent-to-Client Transition Email Templates | published, 2026-07-02 | Baldwin | N | 0 / 0 | 0 / 0 | 0 / 0 |
| 103 | Listing Field Changes in Perchwell | 14459773 (19197859) | Field & Data Representation Upgrade | published, 2026-07-02 | Baldwin | N | 0 / 0 | 0 / 0 | 0 / 0 |
| 104 | What Changed When You Moved to Perchwell | 14459729 (19197859) | Key Workflow Changes | published, 2026-07-22 | Baldwin | N | 0 / 0 | 0 / 0 | 0 / 0 |
| 105 | Find Familiar Features by Their Perchwell Names | 14459704 (19197859) | New Terminology | published, 2026-07-02 | Baldwin | N | 0 / 0 | 0 / 0 | 0 / 0 |
| 106 | Find and Update Contacts Moved from Paragon | 14726035 (19197859) | Your Data: Contacts from Paragon | published, 2026-07-02 | Baldwin | N | 0 / 0 | 0 / 0 | 1 / 0 |
| 107 | Find Your Partial Listings in Perchwell | 14727432 (19197859) | Your Data: Listings & Partials | published, 2026-08-04 | Baldwin | N | 0 / 0 | 0 / 0 | 1 / 0 |
| 108 | Review Your Data Moved from Paragon | 14725404 (19197859) | Your Data: Perchwell Best Practices | published, 2026-08-04 | Baldwin | N | 2 / 0 (TRK-106 to 14726035, TRK-107 to 14727432) | 0 / 0 | 1 / 0 |
| 109 | Review Saved Searches Moved from Paragon | 14725825 (19197859) | Your Data: Saved Searches from Paragon | published, 2026-07-30 | Baldwin | N | 0 / 0 | 0 / 0 | 2 / 0 |
| 110 | Update Your Brokerage Logo and Colors | 14057465 (19361693 User Settings) | Add Branding to a Brokerage | published, 2026-07-02 | Baldwin | N | 0 / 0 | 0 / 0 | 4 / 0 (2 are reused intercomcdn images) |
| 112 | Create Brokerage Email Templates | 15653156 (19361693) | Create Communication Templates for your Brokerage | published, 2026-07-02 | Baldwin | N | 0 / 0 | 0 / 0 | 2 / 0 (1 reused intercomcdn image) |
| 113 | Log In to the Perchwell Mobile App | 15280170 (19648857 User Settings / Log In to Perchwell) | How to Log in to the Perchwell Mobile App | published, 2026-07-02 | Baldwin | N | 0 / 0 | 0 / 0 | 1 / 0 |
| 114 | User Settings FAQ | 16180793 (19361693) | User Settings FAQs | published, 2026-08-06 | Baldwin | N | 0 / 0 | 0 / 0 | 3 / 0 |

Checked on every page and found nothing: `[confirm` text, em dashes, bold other than `Description:` and `Important:`, Paragon outside Then vs. Now, Google Drive links, and malformed captions. Every caption reads `Baldwin \| Alt text:`.

## Blockers and flags

**Stops under SKILL.md:** none. No article is SHARED, so the labeled-image rule does not stop any port. Every link target is a published Baldwin article. The two Notion mentions in TRK-108 resolve to published Baldwin articles.

**Flags for the teammate:**

1. **TRK-096 to 101, 110, 112: CRMLS audience.** Notion tags these Baldwin and CRMLS, but each live article sits only in Baldwin. A port reaches Baldwin only. CRMLS has separate articles, for example "Saving Listings with Tags" (QA note on TRK-099), and needs its own decision.
2. **TRK-096: video mismatch.** The page has a video placeholder, but Video Included is No and Video Status Baldwin is Not Started. This is an open item in `docs/open-article-fixes.md`. The live article has a Loom (0cc1fcba…), and the port drops it. The page also has 2 empty `<p />` blocks.
3. **TRK-097: video.** The page has a video placeholder, and the live Loom (ac5b7a3c…) is dropped. The QA file says that Loom shows the old Tag window.
4. **TRK-098, 099, 101: old Looms.** These keep the same Loom embeds as the live articles. Video Status is Not Started, and the Looms likely show the old UI.
5. **TRK-100: open QA item.** The QA file says to confirm the claim that a public link from Search keeps its listings current ("stay current on both") before transfer. The live article says a public link "does not update automatically." The link text "Share Multiple Listings in Perchwell" differs from the live title of 13903326, now "Share Listings with Clients from Search".
6. **TRK-102:** 1 empty `<p />`.
7. **TRK-105: bare `/en/` links.** Six links omit `/baldwin/`: 11962073, 13623016, 13903062, 13893409, 14786130 and 14786075. The step 5 rewrite needs to add it. Several links use old titles of siblings in this batch: Key Workflow Changes, Your Data: Listings & Partials, User Settings FAQs, and How to Log in to the Perchwell Mobile App. "Under Construction" differs from TRK-103, which writes "Under construction".
8. **TRK-107:** one bare `/en/` link (13623016).
9. **TRK-108: content defects.**
   - The partials bullet says "created on July 20th, 2026". TRK-107 says "before July 20, 2026", and that sentence carries an open comment anchor.
   - There is a typo: "tied to a save search".
   - "Recipient is set to Only me unless you changed it in step 5" points at the wrong step, because step 5 is Click Update.
   - The link texts still use old titles: Agent-to-Client Transition Email Templates, How to Create a Tag, and Your Data: Saved Searches from Paragon.
10. **TRK-109:** the link text "Field & Data Representation Upgrade" is TRK-103's old title. "Under Construction" capitalization differs from TRK-103. The QA file says the live article's images show contact names; the draft replaces them.
11. **TRK-110:** the Description says "brokerage admin" and the body says "broker admin".
12. **TRK-112:** the QA file says the title change needs teammate confirmation. Step 3 says "Email copy templates", but the body calls the page "Communication Templates". The last heading has a stray capital: "Find Brokerage email templates".
13. **Link text on old titles (TRK-096 to 101, 103).** Tags siblings link with live titles such as How to Create a Tag and How to Tag Individual Listings, the agreed set convention. They match only after the siblings port. TRK-103 uses new titles for 14709796, 14710094 and 14744497 ahead of their ports.
14. **External links:** Loom embeds (TRK-098, 099, 101) and Baldwin MLS mailto/phone (TRK-113, 114). These are MLS staff contacts, not member data.
15. **Open comment anchors** are still on TRK-096, 097, 099, 100, 101, 104, 108, 110 and 112. Check them before porting.
