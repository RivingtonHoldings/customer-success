# Baldwin batch port report

The record of the November 3, 2026 batch port. It moved the Baldwin rows of the Perchwell Help Center Database [Sep 2026] (all collections except Search) from Notion into the live Intercom articles they replace. It ran under the one-time exception in `docs/decisions.md` (2026-11-03): no per-article diff or confirmation in chat. Tara approved each Intercom write through its permission prompt and reviews the articles in Intercom afterward. Per-article detail is in `docs/help-center/changelog.md`. A copy of every live body from before the port is in `qa/port-backups/2026-11/`, named by Intercom ID, so any article can be restored.

## Wave 1: Baldwin-only articles

**Result:**
- 41 of 43 articles are live and match their Notion draft. Every one stayed published in the same collections.
- Every image is on Intercom's CDN, and no Notion URL went out.
- Each Notion row is set to Live in Intercom, with its Intercom URL filled in.
- After the mirror re-sync, the second run reported zero changes. All 41 rebuilt files carry their new title and opening sentence.

### Not ported: Intercom kept the old text

The update returned success, but the stored article kept its old body, description, and author; only the edit time moved. This happened twice for Tags FAQ and once for User Settings FAQ. A likely cause is an unsaved draft version open in the Intercom editor. Check each article in Intercom, then re-port it once through `/port-to-intercom`. Both Notion rows are still Ready to Transfer.

- TRK-100 [Tags FAQ](https://support.perchwell.com/baldwin/en/articles/15216706-tags-faq) (15216706)
- TRK-114 [User Settings FAQs](https://support.perchwell.com/baldwin/en/articles/16180793-user-settings-faqs) (16180793)

### Ported articles

"Title before" is the live title the article replaced. Images counts the screenshots now on the article. Omitted placeholders are Notion screenshot or video placeholders with no file yet; they leave no gap on the live page.

| TRK | Article | ID | Title before | Images | Omitted placeholders | Live video dropped |
|---|---|---|---|---|---|---|
| 001 | [Analytics FAQ](https://support.perchwell.com/baldwin/en/articles/15200594-analytics-faq) | 15200594 | same | 0 | 0 | none |
| 002 | [Analytics Page Overview](https://support.perchwell.com/baldwin/en/articles/13623210-analytics-page-overview) | 13623210 | Analytics Tab Overview | 6 | 1 | none |
| 006 | [Client Collaboration FAQ](https://support.perchwell.com/baldwin/en/articles/15201114-client-collaboration-faq) | 15201114 | same | 0 | 0 | none |
| 007 | [Contacts Page Overview](https://support.perchwell.com/baldwin/en/articles/13975194-contacts-page-overview) | 13975194 | same | 6 | 0 | none |
| 013 | [Find and Contact Buyer's Agents with Reverse Prospecting](https://support.perchwell.com/baldwin/en/articles/16201667-find-and-contact-buyer-s-agents-with-reverse-prospecting) | 16201667 | Reverse Prospecting | 5 | 0 | none |
| 019 | [View Shared Saved Searches](https://support.perchwell.com/baldwin/en/articles/14743530-view-shared-saved-searches) | 14743530 | same | 3 | 1 | arcade 0TAXLJjsebpNZr2VUrYT |
| 027 | [What Each Listing Status Means](https://support.perchwell.com/baldwin/en/articles/14709241-what-each-listing-status-means) | 14709241 | Listing Statuses in Perchwell | 0 | 0 | none |
| 028 | [Login and Troubleshooting FAQ](https://support.perchwell.com/baldwin/en/articles/14710265-login-and-troubleshooting-faq) | 14710265 | Login, Access & Troubleshooting Guide and FAQ | 1 | 0 | none |
| 031 | [MLS Rules and Compliance FAQ](https://support.perchwell.com/baldwin/en/articles/14710094-mls-rules-and-compliance-faq) | 14710094 | Top Compliance Questions | 0 | 0 | none |
| 030 | [All About Property Types and Sub-Types](https://support.perchwell.com/baldwin/en/articles/14709796-all-about-property-types-and-sub-types) | 14709796 | Property Types in Perchwell | 1 | 0 | none |
| 047 | [Listing Maintenance FAQ](https://support.perchwell.com/baldwin/en/articles/15199904-listing-maintenance-faq) | 15199904 | same | 4 | 0 | none |
| 048 | [Listing Detail Page FAQ](https://support.perchwell.com/baldwin/en/articles/15200541-listing-detail-page-faq) | 15200541 | Listings FAQ | 1 | 0 | none |
| 050 | [Log In as an Agent with Assume Identity](https://support.perchwell.com/baldwin/en/articles/16053168-log-in-as-an-agent-with-assume-identity) | 16053168 | Assume Identity | 8 | 0 | none |
| 051 | [Manage People FAQ](https://support.perchwell.com/baldwin/en/articles/15201140-manage-people-faq) | 15201140 | same | 0 | 0 | none |
| 052 | [Create and Manage Teams](https://support.perchwell.com/baldwin/en/articles/14742099-create-and-manage-teams) | 14742099 | Perchwell Teams | 3 | 1 | none |
| 053 | [Manage Contacts in the Perchwell Mobile App](https://support.perchwell.com/baldwin/en/articles/14785957-manage-contacts-in-the-perchwell-mobile-app) | 14785957 | Contacts Page Overview- Mobile | 2 | 0 | none |
| 054 | [Listing Detail Page in the Perchwell Mobile App](https://support.perchwell.com/baldwin/en/articles/14784837-listing-detail-page-in-the-perchwell-mobile-app) | 14784837 | Listing Detail Page Overview | 3 | 0 | none |
| 055 | [Message Clients in the Perchwell Mobile App](https://support.perchwell.com/baldwin/en/articles/14786130-message-clients-in-the-perchwell-mobile-app) | 14786130 | Messages Overview | 3 | 0 | none |
| 056 | [Mobile App FAQ](https://support.perchwell.com/baldwin/en/articles/15201164-mobile-app-faq) | 15201164 | Mobile FAQ | 0 | 0 | none |
| 057 | [Add and Edit Listings in the Perchwell Mobile App](https://support.perchwell.com/baldwin/en/articles/14785355-add-and-edit-listings-in-the-perchwell-mobile-app) | 14785355 | My Listings Overview | 4 | 0 | none |
| 058 | [Search in the Perchwell Mobile App](https://support.perchwell.com/baldwin/en/articles/14786263-search-in-the-perchwell-mobile-app) | 14786263 | Search Page Overview | 5 | 0 | none |
| 059 | [Tags in the Perchwell Mobile App](https://support.perchwell.com/baldwin/en/articles/14786075-tags-in-the-perchwell-mobile-app) | 14786075 | Tags Overview | 2 | 0 | none |
| 066 | [Create a CMA with a Subject Property](https://support.perchwell.com/baldwin/en/articles/15216797-create-a-cma-with-a-subject-property) | 15216797 | same | 3 | 0 | none |
| 068 | [Create a Market Conditions Addendum Report (1004MC)](https://support.perchwell.com/baldwin/en/articles/16414760-create-a-market-conditions-addendum-report-1004mc) | 16414760 | same | 2 | 0 | none |
| 075 | [Reports FAQ](https://support.perchwell.com/baldwin/en/articles/15201097-reports-faq) | 15201097 | same | 1 | 0 | none |
| 096 | [Create and Edit a Tag](https://support.perchwell.com/baldwin/en/articles/16221240-create-and-edit-a-tag) | 16221240 | How to Create a Tag | 8 | 1 | loom 0cc1fcba5b3b480f8d57e5b6eca525bf |
| 097 | [Link a Saved Search to a Tag](https://support.perchwell.com/baldwin/en/articles/16221382-link-a-saved-search-to-a-tag) | 16221382 | How to Link a Saved Search to a Tag | 3 | 1 | loom ac5b7a3c722f4cd88ef0e26bbf758bb8 |
| 098 | [Share a Tag with Clients](https://support.perchwell.com/baldwin/en/articles/16221617-share-a-tag-with-clients) | 16221617 | How to Share a Tag | 4 | 0 | none |
| 099 | [Add Listings to a Tag](https://support.perchwell.com/baldwin/en/articles/16221347-add-listings-to-a-tag) | 16221347 | How to Tag Individual Listings | 3 | 0 | none |
| 101 | [Tags Page Overview](https://support.perchwell.com/baldwin/en/articles/14465546-tags-page-overview) | 14465546 | same | 2 | 0 | none |
| 102 | [Sample Emails to Tell Clients About Perchwell](https://support.perchwell.com/baldwin/en/articles/15521036-sample-emails-to-tell-clients-about-perchwell) | 15521036 | Agent-to-Client Transition Email Templates | 0 | 0 | none |
| 103 | [Listing Field Changes in Perchwell](https://support.perchwell.com/baldwin/en/articles/14459773-listing-field-changes-in-perchwell) | 14459773 | Field & Data Representation Upgrade | 0 | 0 | none |
| 104 | [What Changed When You Moved to Perchwell](https://support.perchwell.com/baldwin/en/articles/14459729-what-changed-when-you-moved-to-perchwell) | 14459729 | Key Workflow Changes | 0 | 0 | none |
| 105 | [Find Familiar Features by Their Perchwell Names](https://support.perchwell.com/baldwin/en/articles/14459704-find-familiar-features-by-their-perchwell-names) | 14459704 | New Terminology | 0 | 0 | none |
| 106 | [Find and Update Contacts Moved from Paragon](https://support.perchwell.com/baldwin/en/articles/14726035-find-and-update-contacts-moved-from-paragon) | 14726035 | Your Data: Contacts from Paragon | 1 | 0 | none |
| 107 | [Find Your Partial Listings in Perchwell](https://support.perchwell.com/baldwin/en/articles/14727432-find-your-partial-listings-in-perchwell) | 14727432 | Your Data: Listings & Partials | 1 | 0 | none |
| 108 | [Review Your Data Moved from Paragon](https://support.perchwell.com/baldwin/en/articles/14725404-review-your-data-moved-from-paragon) | 14725404 | Your Data: Perchwell Best Practices | 1 | 0 | none |
| 109 | [Review Saved Searches Moved from Paragon](https://support.perchwell.com/baldwin/en/articles/14725825-review-saved-searches-moved-from-paragon) | 14725825 | Your Data: Saved Searches from Paragon | 2 | 0 | none |
| 110 | [Update Your Brokerage Logo and Colors](https://support.perchwell.com/baldwin/en/articles/14057465-update-your-brokerage-logo-and-colors) | 14057465 | Add Branding to a Brokerage | 2 | 0 | none |
| 112 | [Create Brokerage Email Templates](https://support.perchwell.com/baldwin/en/articles/15653156-create-brokerage-email-templates) | 15653156 | Create Communication Templates for your Brokerage | 1 | 0 | none |
| 113 | [Log In to the Perchwell Mobile App](https://support.perchwell.com/baldwin/en/articles/15280170-log-in-to-the-perchwell-mobile-app) | 15280170 | How to Log in to the Perchwell Mobile App | 1 | 0 | none |

### Check in Intercom

These went live as Notion had them. Each one is worth a look.

- **Bylines.** Every ported article now shows Tara (5472692) as the author. Intercom stamps the acting admin on any API update.
- **Link text from before the renames.** Some links still use a sibling's old title as link text, such as "How to Create a Tag" in the Tags set, "Key Workflow Changes" in Find Familiar Features by Their Perchwell Names, and "Perchwell Teams" and "Assume Identity" in Manage People FAQ. Every link still opens the right article, because Intercom finds articles by ID. Update the text in Notion and re-port when convenient.
- **Headings.** Intercom stores each H2 as H1 and each H3 as H2. This is expected and renders the same as every other article.
- **Table headers.** In Find Familiar Features by Their Perchwell Names (TRK-105) and Review Saved Searches Moved from Paragon (TRK-109), Intercom dropped the gray shading on table header rows. The header text is still there.
- **Contacts Page Overview (TRK-007).** The second contact profile screenshot is labeled Baldwin, but it shows a Shared Buildings tab and came from the CRMLS batch. The article now shows two profile screenshots in a row.
- **Videos dropped by decision.** Create and Edit a Tag (Loom 0cc1fcba), Link a Saved Search to a Tag (Loom ac5b7a3c), and View Shared Saved Searches (one Arcade) have no video until the new ones are ready.
- **Content flags carried through from the preflight.** These are Tara's edits, to make later:
  - Coming Soon in MLS Rules and Compliance FAQ vs Listing Maintenance FAQ
  - the July 20 partials date in Review Your Data Moved from Paragon vs Find Your Partial Listings
  - "unless you changed it in step 5" and "tied to a save search" in Review Your Data Moved from Paragon
  - push notifications in Client Collaboration FAQ vs Message Clients in the Mobile App
  - Auto CMA in Listing Detail Page in the Mobile App
- **Open Notion comment threads** remain on several pages. The text they anchor went live as written.

### Cleanup for Tara in Intercom

- Delete scratch draft **18180010** ("Scratch: Baldwin batch port images wave 1 batch 1"). It only held images for re-hosting.
- Archive **14710059** Most Common Questions Asked to MLS Staff, now replaced by MLS Rules and Compliance FAQ (TRK-031).
- Archive **13903157** Set Up Saved Searches for Hot Sheets. Add a Hot Sheet to the Dashboard (TRK-020) is now live and covers it; the old article has no Notion row.
- Remove the internal-note lines from Notion, then re-port: "Video is applicable to all customers" is live in Create and Manage Your Contacts in Perchwell (TRK-008), and "This video can be used for all customers" is new in the TRK-053 Notion page.

### Mirror

The re-sync updated 43 Baldwin files: the 41 ports, plus Tags FAQ and User Settings FAQs, whose edit times moved. It also deleted 45 stale Baldwin files and 5 CRMLS files, using the sync fix made today. Those were the 19 leftovers from earlier renames plus the old file of each article renamed in this batch.

## Wave 2: shared articles

**Result:**
- All 28 articles are live and match their Notion draft, all still published in the same collections.
- Every image is on Intercom's CDN, and each Notion row is set to Live in Intercom.
- The mirror re-sync updated 26 Baldwin and 15 CRMLS files and deleted 11 and 7 stale files; the second run reported zero changes.

These articles also reach CRMLS or the default help center. As decided, every reader sees the Baldwin screenshots, CRMLS-labeled screenshots were left out, and links use `/baldwin/en/` paths. A CRMLS or default reader who follows a link to a Baldwin-only article may not be able to open it; the last column counts those links.

Five articles were re-prepped and pushed later in the day because Notion changed after the first prep: TRK-015, 016, 018, 046, and 072. TRK-046 went live on a later retry: the first two tries failed to re-host its header and tabs screenshot ("Image cannot be requested at URL"), and the retry worked with the same file once the signed links were sent without their `#notion_record` ending. TRK-070, 072, 073, and 074 replaced a live Arcade with the Loom in Notion.

### Dropped by decision

- TRK-049 Manage Listings Page Overview went live without the live "Share draft listings" section, by Tara's decision: a draft preview feature releasing November 10, 2026 replaces that workaround. The Export sentence also came out of the draft, since the Export button no longer exists.

### Ported articles

| TRK | Article | ID | Title before | Also reaches | Images | Baldwin-only links |
|---|---|---|---|---|---|---|
| TRK-005 | [Bulk Upload Contacts from a CSV File](https://support.perchwell.com/baldwin/en/articles/10732227-bulk-upload-contacts-from-a-csv-file) | 10732227 | Bulk Upload Contacts | CRMLS, default | 2 | 0 |
| TRK-008 | [Create and Manage Your Contacts in Perchwell](https://support.perchwell.com/baldwin/en/articles/14790755-create-and-manage-your-contacts-in-perchwell) | 14790755 | same | default | 5 | 2 |
| TRK-009 | [Export Contacts to a CSV File](https://support.perchwell.com/baldwin/en/articles/12896093-export-contacts-to-a-csv-file) | 12896093 | Export Your Contact List | CRMLS, default | 2 | 0 |
| TRK-010 | [Invite Clients to Perchwell and Resend Invitations](https://support.perchwell.com/baldwin/en/articles/11373895-invite-clients-to-perchwell-and-resend-invitations) | 11373895 | Invite Clients to Perchwell | CRMLS, default | 4 | 1 |
| TRK-011 | [Message Clients in Perchwell](https://support.perchwell.com/baldwin/en/articles/12541968-message-clients-in-perchwell) | 12541968 | same | CRMLS, default | 3 | 2 |
| TRK-012 | [Set Up Your Clients in Perchwell](https://support.perchwell.com/baldwin/en/articles/15521779-set-up-your-clients-in-perchwell) | 15521779 | Quick Guide: Getting Clients Started in Perchwell | default | 1 | 1 |
| TRK-014 | [Unsubscribe from Saved Search Alert Emails](https://support.perchwell.com/baldwin/en/articles/13602428-unsubscribe-from-saved-search-alert-emails) | 13602428 | Unsubscribe from Notifications (For Invited Clients) | CRMLS, default | 2 | 0 |
| TRK-015 | [Accept Your Agent's Perchwell Invitation](https://support.perchwell.com/baldwin/en/articles/15521326-accept-your-agent-s-perchwell-invitation) | 15521326 | Accept Your Agent’s Perchwell Invitation | default | 3 | 1 |
| TRK-016 | [Communicate with Your Agent via Messages in Perchwell](https://support.perchwell.com/baldwin/en/articles/11373888-communicate-with-your-agent-via-messages-in-perchwell) | 11373888 | Communicate with Your Agent in Perchwell | CRMLS, default | 2 | 0 |
| TRK-017 | [Receive Alerts About New Listings](https://support.perchwell.com/baldwin/en/articles/11373805-receive-alerts-about-new-listings) | 11373805 | same | CRMLS, default | 3 | 1 |
| TRK-018 | [Share Listings with Your Agent](https://support.perchwell.com/baldwin/en/articles/11373849-share-listings-with-your-agent) | 11373849 | same | CRMLS, default | 3 | 0 |
| TRK-020 | [Add a Hot Sheet to the Dashboard](https://support.perchwell.com/baldwin/en/articles/13893409-add-a-hot-sheet-to-the-dashboard) | 13893409 | same | default | 1 | 1 |
| TRK-021 | [Customize Your Dashboard](https://support.perchwell.com/baldwin/en/articles/13623904-customize-your-dashboard) | 13623904 | same | default | 3 | 0 |
| TRK-022 | [Dashboard FAQ](https://support.perchwell.com/baldwin/en/articles/15216626-dashboard-faq) | 15216626 | same | default | 1 | 2 |
| TRK-023 | [Dashboard Overview](https://support.perchwell.com/baldwin/en/articles/13903062-dashboard-overview) | 13903062 | same | default | 8 | 2 |
| TRK-024 | [Access Integrations from the Dashboard or a Listing](https://support.perchwell.com/baldwin/en/articles/13903183-access-integrations-from-the-dashboard-or-a-listing) | 13903183 | Integration Tools on the Dashboard | default | 3 | 2 |
| TRK-025 | [Find Listings in the Listings Widget](https://support.perchwell.com/baldwin/en/articles/13903171-find-listings-in-the-listings-widget) | 13903171 | Listings Widget Overview | default | 3 | 1 |
| TRK-044 | [Add and Edit Listings](https://support.perchwell.com/baldwin/en/articles/13627189-add-and-edit-listings) | 13627189 | same | default | 5 | 2 |
| TRK-045 | [Write a Listing Description with AI Scribe](https://support.perchwell.com/baldwin/en/articles/11801815-write-a-listing-description-with-ai-scribe) | 11801815 | AI Scribe | default | 2 | 0 |
| TRK-046 | [Listing Detail Page Overview](https://support.perchwell.com/baldwin/en/articles/14074994-listing-detail-page-overview) | 14074994 | same | default | 8 | 1 |
| TRK-049 | [Manage Listings Page Overview](https://support.perchwell.com/baldwin/en/articles/13623016-manage-listings-page-overview) | 13623016 | same | default | 4 | 0 |
| TRK-067 | [Create a Listing Report](https://support.perchwell.com/baldwin/en/articles/8955755-create-a-listing-report) | 8955755 | same | CRMLS, default | 5 | 0 |
| TRK-069 | [Create a Media Report](https://support.perchwell.com/baldwin/en/articles/8955781-create-a-media-report) | 8955781 | same | CRMLS, default | 5 | 0 |
| TRK-070 | [Create a Quick CMA Report](https://support.perchwell.com/baldwin/en/articles/13959293-create-a-quick-cma-report) | 13959293 | same | CRMLS, default | 6 | 1 |
| TRK-071 | [Create a Show Sheet](https://support.perchwell.com/baldwin/en/articles/8955767-create-a-show-sheet) | 8955767 | same | CRMLS, default | 5 | 0 |
| TRK-072 | [Create an Itinerary Report](https://support.perchwell.com/baldwin/en/articles/8955772-create-an-itinerary-report) | 8955772 | same | CRMLS, default | 6 | 0 |
| TRK-073 | [Create a Full Report](https://support.perchwell.com/baldwin/en/articles/12816757-create-a-full-report) | 12816757 | Create and Share Full Reports | CRMLS, default | 7 | 0 |
| TRK-074 | [Create a One Page Report](https://support.perchwell.com/baldwin/en/articles/12816780-create-a-one-page-report) | 12816780 | Create One Page Reports | CRMLS, default | 4 | 0 |

### Check in Intercom (wave 2)

- **Link text and slugs from before the renames.** One-Page Report links to Full Report as "Create and Share Full Reports" with the old slug. Accept Your Agent's Perchwell Invitation (TRK-015) and Message Clients (TRK-018) link to Communicate with Your Agent with its old slug. The links still open the right article.
- **One-Page Report (TRK-074)** gives two listing limits, 50 and 15.

## Re-port check

After both waves, each ported article's Notion page was compared with the body that went live. 45 pages were edited after their push; 36 were property-only edits. These 9 changed in the body and need a re-port through `/port-to-intercom`, one at a time, with the row set back to Ready to Transfer first:

- TRK-007 [Contacts Page Overview](https://app.notion.com/p/3f08b9e0143881a88e56c522774b0833): two Baldwin screenshots replaced.
- TRK-019 [View Shared Saved Searches](https://app.notion.com/p/3f98b9e01438810085e3f0a19dc5ff5f): a Loom added where the placeholder was.
- TRK-053 [Manage Contacts in the Perchwell Mobile App](https://app.notion.com/p/3ff8b9e01438815fba5fc63e648fae41): a Loom added, plus the line "This video can be used for all customers", which should come out first.
- TRK-054 [Listing Detail Page in the Perchwell Mobile App](https://app.notion.com/p/3ff8b9e01438810aaa55ddf7c6960be2): a Loom added.
- TRK-058 [Search in the Perchwell Mobile App](https://app.notion.com/p/3ff8b9e014388159bcbcf00f666677fb): a Loom added at the top.
- TRK-096 [Create and Edit a Tag](https://app.notion.com/p/3fb8b9e0143881349fd7ce5e4749fa5a): the Loom the port dropped is back in Notion.
- TRK-097 [Link a Saved Search to a Tag](https://app.notion.com/p/3fd8b9e0143881499020df4b5b281008): the Loom the port dropped is back in Notion.
- TRK-101 [Tags Page Overview](https://app.notion.com/p/3ff8b9e0143881b0a4cce4d39512740b): Loom swapped and the Status column screenshot replaced.
- TRK-103 [Listing Field Changes in Perchwell](https://app.notion.com/p/3fe8b9e01438814691d9f1936d30f4d6): largely rewritten to name Paragon, with a new description and reworked sections.

TRK-100 and TRK-114 from wave 1 also still need their port.
