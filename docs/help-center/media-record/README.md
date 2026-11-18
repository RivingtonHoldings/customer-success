# Media record

A receipt of what `/port-to-intercom` last pushed to Intercom, one file per article: `<tracker-id>.json`, for example `TRK-095.json`. It lets the next publish tell a replaced screenshot from an unchanged one and say what changed since the last publish.

It is not a content store. It holds no article text and no image files, nothing drafts or edits from it, and if it disagrees with Notion, Notion is right and the record is rewritten after the next confirmed push. Only `/port-to-intercom` writes here, after a confirmed push. Do not edit these files by hand. An article with no file here has never been pushed under this scheme; the skill handles that as a first publish.

## Shape

```json
{
  "tracker_id": "TRK-095",
  "article_name": "Universal Search Bar",
  "records": {
    "baldwin": {
      "intercom_article_id": 11002620,
      "title": "Universal Search Bar",
      "intercom_updated_at": "2026-11-18T15:04:00Z",
      "published_on": "2026-11-18",
      "notion_last_edited": "2026-11-17T21:10:00Z",
      "media": [
        {
          "position": "When to use the Universal Search Bar, 1",
          "kind": "image",
          "caption_label": "Baldwin",
          "identity": "file:7f2c0c1e-0000-0000-0000-000000000000",
          "published_as": "https://perchwell.intercom-attachments-1.com/example/path.png"
        }
      ]
    }
  }
}
```

The values above are an illustration of the shape only, not a real article.

- `records` has one entry per MLS slug from `mls-registry.md`. A push writes only the target MLS's entry and leaves the others as they are.
- `intercom_updated_at` is the article's `updated_at` read with `get_article` right after the push. The edited-in-Intercom check compares the live `updated_at` with it.
- `notion_last_edited` is the Notion page's last-edited time when the body was converted.
- `position` is the section heading plus the order within it, so a moved item can be told from a new one.
- `kind` is `image` or `video`.
- `caption_label` is the label as read (`Baldwin`, `CRMLS`, or empty).
- `identity` is how the item is recognized:
  - Uploaded image: `file:<fileId>`, the ID inside `notion-file-block://<blockId>/<fileId>?name=...`. A new upload gets a new file ID even with the same filename. The block ID is never used, because a replaced screenshot shows up as a new block.
  - External image: `url:<path>`, the URL path with any signature removed.
  - Video: `video:<Loom or Arcade URL>`.
  - `unknown`: an item kept from the live body that was not verified against Notion in that push. Never guessed from a filename or date. The next run treats it as Cannot be verified.
  - Signed download URLs expire after five minutes and are never recorded.
- `published_as` is the Intercom CDN URL (signature removed) or the video embed URL the item became.
- Items left out on purpose (labeled for another MLS, unlabeled video not counted for this MLS) are not recorded.
