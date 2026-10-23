---
name: rename-drive-images
description: Rename every image in a Google Drive folder to the team's screenshot naming convention (Baldwin-Page-Description, for example Baldwin-Search-Lot-Description.png). Use whenever a teammate types /rename-drive-images, pastes a Google Drive folder link and says "rename these images," "fix the screenshot names," "clean up the file names in this folder," or asks to make a folder of screenshots match the naming convention. Only changes file names. Never adds, removes, moves, copies, or edits an image.
---

# Rename Drive images

A teammate gives you a Google Drive folder of screenshots. You look at each image, work out which Perchwell page it shows and what it is showing, and rename it to the convention below. The teammate is not technical, so keep every message plain.

## The one hard rule

Change names only. The folder must hold exactly the same files before and after, with the same contents, in the same place.

- The only write tool you may call is the Drive connector's `update_file`, and only with `fileId` and `title`. Never pass `parentId`, `description`, `readOnly`, or anything else.
- Never call `create_file`, `copy_file`, `trash_file`, `share_file`, or any other Drive write tool, for any reason, including "fixing" a duplicate or a broken image.
- Leave non-image files (docs, PDFs, videos, subfolders) alone. Do not rename them and do not open subfolders unless the teammate asks.

The Drive tools come from a claude.ai connector, and the server ID in the tool name differs per teammate. Match on the tool's own name, the part after the last `__`. If no Drive tools are in the session, say: "Google Drive is not connected yet. In claude.ai, open Settings, then Connectors, and connect Google Drive, then start a new session."

## The naming convention

`Baldwin-<Page>-<Description>.<ext>`

1. **MLS name first.** Always `Baldwin`.
2. **Page name.** The Perchwell page or area the screenshot was taken on, spelled the way the screen spells it: `Search`, `Listing-Detail`, `Add-Edit`, `Saved-Searches`, `Hotsheets`, `Dashboard`, `Contacts`, `Reports`, `Settings`. Use the vocabulary in `docs/product-context.md`.
3. **Description.** What the image shows, in 1 to 4 words. When the image is about one specific option whose on-screen label is longer, use that label in full, as in the third example.
4. Every part is separated by a single `-`. No spaces, underscores, or other punctuation. Capitalize the first letter of each word.
5. Keep the original file extension, lowercased (`.png`, `.jpg`, `.webp`, `.gif`).

Examples from the team:

- `Baldwin-Search-Lot-Description`
- `Baldwin-Search-Start-New-highlighted`
- `Baldwin-Search-Allow-added-Contacts-to-see-and-edit-search`

## Steps

### 1. Read the folder

Take the folder ID from the link (the part after `/folders/`, stopping at `?` if there is one). List its images with `search_files`, query `parentId = '<folder ID>' and mimeType contains 'image/'`, `excludeContentSnippets: true`, following `next_page_token` until a page comes back empty. Results can repeat across pages, so dedupe by file ID.

Run the same listing once more without the `mimeType` clause, so you know every name already in the folder (needed for the duplicate check) and can tell the teammate how many non-image files you are leaving alone.

Write down the starting inventory: the count of images and each image's file ID and current name. This is what you check against at the end.

If the folder has no images, say so and stop.

### 2. Look at each image

For each image, call `download_file_content`. The result is too big to show inline, so it is saved to a JSON file whose path the tool returns; pull out the `content` field with `jq`, decode the base64 into a `.png` in your scratchpad directory, and open it with Read so you can see it. Use the current file name as a hint only; screenshots are often named `Screenshot 2026-10-12 at 3.41.07 PM.png`, which says nothing.

Request at most three downloads at a time. More than that in parallel times out, even for small files.

**Images over 10 MB.** `download_file_content` refuses any file over 10 MB, and the `fileSize` from step 1 tells you which ones those are. Do not try other Drive tools for them. Instead, open each one's Drive preview at `https://drive.google.com/thumbnail?id=<file ID>&sz=w1600` in Claude in Chrome and take a screenshot. That route needs the teammate's own Chrome, which is normally already signed in to Google; the browser pane inside the desktop app is not, and signing in there may not stick. Ask the teammate before switching to Claude in Chrome, and close the tab when you are done. If Chrome is not available, list those images under "needs your call" with their timestamps so the teammate can name them.

**Exact duplicates.** When two images have the same `fileSize`, compare the decoded files with `md5`. Identical copies keep both files: name the second one with `-2`, and tell the teammate it is a copy.

Decide the page and the description from what is on screen: the page header, the highlighted control, the open window or menu. When you cannot tell which page it is, do not guess; mark it "needs your call" in the plan.

### 3. Build the rename plan

For each image, produce the new name. Then check:

- **Already correct.** If the current name already follows the convention, keep it and mark it "no change".
- **Duplicates.** No two files in the folder may end up with the same name, including the non-image files. When two images would collide, make the descriptions more specific first (`Baldwin-Search-Actions-Menu` and `Baldwin-Search-Actions-Menu-Print-Highlighted`). Only if they are truly the same view, add `-2`, `-3`.
- **Count.** The plan has exactly one row per image from step 1, no more and no fewer.

Show the plan as a table: current name, new name, and a few words on what the image shows. List "no change" and "needs your call" rows separately at the bottom. Then ask once: "Rename these N images?" Wait for a clear yes. If the teammate edits any names, update the plan, run the duplicate check again, and show the changed rows before going ahead.

### 4. Rename

For each row that changes, call `update_file` with the file ID and the new title. Nothing else. If one call fails, note it and carry on with the rest; do not retry with a different tool.

### 5. Verify

List the folder again exactly as in step 1 and compare with the starting inventory:

- the same number of images,
- the same set of file IDs, none missing and none new,
- each file now carries its planned name.

Report in plain language: "Renamed N of M images. The folder still has M images, nothing added or removed." List anything that failed or still needs a decision. If the counts or IDs do not match, say so right away and do not try to repair it yourself; show the teammate what differs.

Finish with the old-to-new table so the teammate can rename anything back by hand if needed. Delete the downloaded copies from your scratchpad.
