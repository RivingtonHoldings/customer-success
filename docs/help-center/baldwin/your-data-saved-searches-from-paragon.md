---
intercom_id: "14725825"
content_id: "17292991"
title: "Your Data: Saved Searches from Paragon"
description: "In this article, you will learn how your Saved Searches are migrated from Paragon to Perchwell."
url: "http://support.perchwell.com/baldwin/en/articles/14725825-your-data-saved-searches-from-paragon"
help_center: baldwin
help_center_id: 4755399
collection: "Then vs. Now"
collection_ids: [19197859]
collections: ["Then vs. Now"]
state: published
author_id: 9490228
created_at: 2026-04-22T18:00:17Z
updated_at: 2026-07-30T11:54:10Z
labels: []
body_source: public-help-center
synced_at: 2026-09-04T16:50:44Z
---

# Your Data: Saved Searches from Paragon

# **Saved Searches**

All saved searches made available by Paragon were imported into Perchwell and linked to contacts in **a one-time sync at the beginning of each cohort. Any saved searches created after that will need to be recreated in Paragon.**

However, the **migrated searches will require review by all Baldwin members** for two reasons:
1. **Arbitrary Filter Elimination:** As of April 20th, 2026, the saved search information made available to Perchwell by Paragon unpredictably drops certain search filters, corrupting the integrity of your saved search data.
​
2. **Filter Translation:** The Baldwin REALTORS® MLS team is upgrading the structure of your listing database to align with modern best practices adopted across the industry and RESO (Real Estate Standards Organization). As a result, certain filters do not cleanly translate between systems (e.g. grouping “Other” property types under “Residential - Single Family”).

Despite these two challenges, your saved searches will nonetheless appear in Perchwell upon first login, marked for manual review with the prefix of **[From Paragon: Unreviewed]** in the name of the search in Perchwell.

You will be able to open, update these saved searches in Perchwell, and remove the label by changing the name as they are reviewed.

If you are updating a saved search in Perchwell and do not want the search criteria to refresh if/when Paragon’s data share is fixed pre-cutover, please update the name of the saved search to remove [From Paragon: Unreviewed].

[![image](https://downloads.intercomcdn.com/i/o/trq7czv5/2307775998/04bf2dfa49b1395249aa4d0e040c/saved+searches+pic.png)](https://downloads.intercomcdn.com/i/o/trq7czv5/2307775998/04bf2dfa49b1395249aa4d0e040c/saved+searches+pic.png?expires=1788542100&signature=4c78121adfa5c3b50128e4634053f39d0a97deca5a58f822db1eedb6a2a5764f&req=diMnEc55mIhWUfMW1HO4zQFhTxunb4NOt3fQatwzGc2YLjTato0DaXOrD95B%0A7HEd285b8J%2BUCARtA6U%3D%0A)

Importantly, Paragon has informed us they are working to fix the underlying issue impacting their system by May 6th, 2026.

If Paragon is able to rectify their data share, following that date, **Perchwell will refresh all saved searches that still contain [From Paragon: Unreviewed] in their names**.

From that point forward, any saved searches with this prefix will still need to be reviewed and updated manually as there may still be discrepancies due to filter translation challenges.

# **Arbitrary Filter Elimination**

Perchwell accesses your saved searches via a data share with Paragon. While all saved searches appear to be available from Paragon, our team has observed inconsistent data that does not match the actual filters/criteria applied within Paragon.

The table below illustrates a possible filter elimination taking place between the criteria entered in the Paragon system directly versus what Perchwell receives from Paragon:

| **Search Criteria You Entered** (in Paragon) | **Search Criteria Perchwell Receives **(from Paragon) |
|---|---|
| • Class: Residential-Single Family • Structure Style: Condo • *Bedrooms: 2+* • City: Gulf Shores | • Class: Residential-Single Family • Structure Style: Condo • City: Gulf Shores |

Unfortunately, there is no consistent pattern for how or why certain filters are being eliminated in data Perchwell receives from Paragon.

As a result, though Perchwell will create and link all saved searches to contacts in Perchwell, we cannot guarantee that the filters applied fully align with what was entered in Paragon.

# **Filter Translation**

Approximately 92% of saved search criteria available in the Paragon system are fully translatable to Perchwell. However, though these searches are translatable, due to the arbitrary elimination of filters in the Paragon system (outlined above), not all criteria may be applied in Perchwell.

There are multiple reasons a saved search may not be translatable, most due to differences between the two systems.

#### The most common causes are:
1. Searches using the ‘All Features’ filter in Paragon with an ‘or’ relationship between features under different groupings.
2. Searches filtering on ‘Other’ property types (Boat Slip, Fractional Ownership, Garage)
3. Searches filtering on the ‘Active New Construction’ status
4. Searches using fields that have changed to accurately portray which feature grouping a specific feature should live under (e.g. More than 2 pets allowed?)

# **Linking Saved Searches & Contacts**

The Perchwell team has also worked to **link your saved searches to your contacts** as they were in Paragon. These linkages will be visible in Perchwell in two places:
- First, contact detail pages on the “Shared Searches” tab on the left panel where all saved searches linked to that contact are displayed.
- Second, the saved search menu on the search page, where the contacts associated with each saved search will appear in the “Contacts” column.

[![image](https://downloads.intercomcdn.com/i/o/trq7czv5/2307792258/7045854550be0f4b7a087f88411b/saved+searches2.png)](https://downloads.intercomcdn.com/i/o/trq7czv5/2307792258/7045854550be0f4b7a087f88411b/saved+searches2.png?expires=1788542100&signature=5f989a0f442d2ef249f313be6d400ce8322366f40c98380d8e280649ee9cad29&req=diMnEc53n4NaUfMW1HO4zew2ZepOwnhofIPGRTLWYJmq3fyWSPLJyxge81VZ%0A1xDGdfL4YW1WUNn7cgc%3D%0A)

Note that the integrity of these linkages is fully dependent on the data made available by Paragon. If Perchwell receives both a contact and a saved search with a valid association between them, they will be linked in Perchwell on your access date.
