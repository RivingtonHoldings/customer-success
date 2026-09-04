# Perchwell Customer Success workspace

This is the shared Claude Code workspace for the Perchwell Customer Success team. You do not need to know anything about terminals or code to use it. Claude does the technical parts; you tell it what you need in plain English.

Setup takes about ten minutes. Do it once.

## Setup

### 1. Install the Claude Code desktop app and sign in

1. Download the Claude desktop app from [claude.ai/download](https://claude.ai/download) and install it.
2. Open it and sign in with your Perchwell Google account (the same one you use for claude.ai).
3. Click the **Code** tab in the left sidebar. This is where the workspace lives.

### 2. Get access to the repository

The workspace is stored in a private GitHub repository, which is a shared folder with a full history of every change. Ask Leo to add your GitHub account. If you do not have a GitHub account, create one at [github.com](https://github.com) with your Perchwell email first, then send Leo your username.

### 3. Clone the repository

"Clone" means download a copy of the shared folder to your computer. The copy stays connected to the shared one so it can send and receive changes.

The easiest way is to let Claude do it:

1. In the **Code** tab, start a new session. When it asks which folder to work in, choose to continue without a folder (the option is labeled something like **No folder** or **Skip**).
2. Paste this message and send it:

   > Clone https://github.com/RivingtonHoldings/customer-success.git into my Documents folder as perchwell-customer-success, then move this session into that folder.

3. Claude may ask you to sign in to GitHub in your browser the first time. Approve it.
4. When Claude says it is done, you have the workspace at **Documents > perchwell-customer-success**.

If your version of the app shows a **Clone repository** button on the new-session screen instead, you can use that: paste the same URL, choose your Documents folder, and name it `perchwell-customer-success`.

### 4. Open the folder and approve the trust prompt

1. Start a new session in the **Code** tab and choose **Open folder** (or the folder picker).
2. Pick **Documents > perchwell-customer-success**.
3. Claude Code will ask whether you trust this folder. Click **Yes, I trust this folder**. This is Claude asking permission to read the files in it, which is what you want.

### 5. Connect Notion and Intercom

Claude reaches Notion and Intercom through connectors, which are secure links between your Claude account and those tools. You set them up once and they work everywhere you use Claude, in the claude.ai website and in Claude Code.

1. Go to [claude.ai](https://claude.ai) in your browser.
2. Click your name in the bottom left, then **Settings**, then **Connectors**.
3. Find **Notion** and click **Connect**. Sign in to Notion if asked and approve access.
4. Find **Intercom** and click **Connect**. Sign in to Intercom if asked and approve access.
5. Back in the Claude Code desktop app, start a fresh session so it picks up the new connectors.

### 6. Run the setup check

In your session, type this and press Enter:

```
/setup-check
```

A passing result looks like this: Claude says it pulled the latest changes (or that you were already up to date), confirms it can see both the Notion and Intercom tools, lists the five most recently updated Baldwin help center articles from the local copy, and ends with a short paragraph saying you are ready to work. If any line says something is missing, jump to Troubleshooting below.

Run `/setup-check` at the start of every session. It takes a few seconds and makes sure you are working from the latest version of everything.

## What you can ask Claude to do here

Talk to it the way you would talk to a capable colleague. Some examples tied to the help center project:

- "Refresh the help center mirror so I am looking at the latest Baldwin articles." (Claude runs `/sync-help-center`.)
- "Pull the member questions from the two weeks after the Baldwin cutover and group them into golden questions." (Claude runs `/golden-questions`.)
- "Draft a help center article for the new saved search alert frequency options. Here are the release notes." (Claude runs `/article-draft` and creates a Notion draft for review.)
- "Rewrite the Baldwin Dashboard Overview article to match our content standards." (Claude runs `/article-rewrite` on the mirrored article.)
- "Write macros the support team can paste when members ask how to print search results." (Claude runs `/intercom-macros` and saves the drafts in the repo.)

You can also just ask questions: "Which Baldwin articles mention Tags?" or "What did we decide about Fin labels?"

## Workstreams

Work is organized into folders called workstreams.

- **workstreams/help-center-overhaul/** is the September 2026 project to standardize the Baldwin and CRMLS help centers and get Fin's human-intervention rate down. Inside it: `docs/` for status and decisions, `audit/` for the article audit, `golden-questions/` for the member question set, `qa/` for checklists and test results, `fin-reports/` for weekly Fin numbers, `outputs/` for finished deliverables, and `confidential/` (see below).
- **workstreams/support-ops/** is for support content that outlives any single project, mainly macro drafts. One file per feature, indexed in `macros/README.md`.

## The confidential folder rule

Anything that includes a member's name, email, phone number, or address goes in a `confidential/` folder and nowhere else. Those folders stay on your computer and are never sent to the shared repository. Claude follows this rule automatically: it strips identifiers before saving anything outside `confidential/`. If you paste a member conversation into a chat, tell Claude to keep the raw text in `confidential/`.

## How syncing works, in plain language

The shared repository lives on GitHub. Your computer has a copy. "Pull" means fetch your teammates' latest changes into your copy. "Commit and push" means save your changes and send them up so teammates get them.

You never have to do any of this yourself. `/setup-check` pulls at the start of a session. At the end of a session, Claude offers to save and send your work; say yes. If two people edit the same file on the same day, Claude will sort it out and tell you what happened.

The help center mirror in `docs/help-center/` is a separate kind of sync: it is a read-only copy of what is live in Intercom. `/sync-help-center` refreshes it. Editing the mirror files by hand does nothing to Intercom.

## Troubleshooting

**Claude says it has no Notion or Intercom tools.**
The connector is not set up on your account yet, or the session started before you connected it. Go to claude.ai, then Settings, then Connectors, and check that both show as connected. Then start a brand new session in the desktop app and run `/setup-check` again.

**A connector asks to be reconnected.**
This happens when the link expires, usually after a password change or a few months of use. Go to claude.ai, then Settings, then Connectors, click the connector, choose **Disconnect**, then **Connect** again and approve access. Start a new session afterward.

**Claude asks for a permission you do not understand.**
Claude Code checks before doing anything that changes something outside the repo. If the request mentions Intercom `create_article` or `update_article`, it is asking to write to the live help center; say no unless you meant to publish and have already reviewed the diff. If it mentions reading Notion or Intercom, or running `git`, it is safe to allow. If you are unsure, say no and ask Claude to explain what it was about to do in plain language. Saying no never breaks anything.

Still stuck? Message Leo.
