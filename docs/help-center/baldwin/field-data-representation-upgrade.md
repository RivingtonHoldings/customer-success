---
intercom_id: "14459773"
content_id: "16905918"
title: "Field & Data Representation Upgrade"
description: "In this article, you will learn how the Baldwin REALTORS\u00ae MLS listing database is changing in Perchwell and what those changes mean for the fields you see, search, and report on."
url: "http://support.perchwell.com/baldwin/en/articles/14459773-field-data-representation-upgrade"
help_center: baldwin
help_center_id: 4755399
collection: "Then vs. Now"
collection_ids: [19197859]
collections: ["Then vs. Now"]
state: published
author_id: 9490228
created_at: 2026-04-06T05:42:28Z
updated_at: 2026-07-02T02:39:34Z
labels: []
body_source: public-help-center
synced_at: 2026-09-04T16:50:44Z
---

# Field & Data Representation Upgrade

# What's changing in your day-to-day workflow

Your Baldwin REALTORS® MLS team is upgrading the structure of your listing database to align with modern best practices adopted across the industry and RESO (Real Estate Standards Organization).

These updates help your data work more reliably with third-party products and services, improve your search results and reports, and create a more consistent experience across MLS platforms.

Field and data model updates include changes to field names, property classifications, and how listing data is organized in Perchwell.

## **Field name updates that match RESO standards**

The field names you see in Perchwell follow the RESO Data Dictionary standard. This is the same terminology used by modern MLS platforms and many third-party tools, so the labels you see match the language used across the industry.

| **Paragon Field Name** | **Paragon Sub-Options (examples)** | **Perchwell Field Name** |
|---|---|---|
| **Class** | Residential Single-Family, Lease, Lots and Land | Property type |
| **Property Type** | Residential Attached, Residential Detached, Multi-Family, Mobile Home | Property sub type |

## **How listing data is represented differently in Perchwell**

Baldwin and Perchwell coordinated on the changes below to improve data accuracy, search precision, and fair housing compliance. Review the **Why** column for the reason behind each update.

| **Field Name** | **What Changed** | **In Paragon** | **In Perchwell** | **Why** |
|---|---|---|---|---|
| **Property Type (FKA Class)** | 'Other' Property Type merged into Residential-Single Family | Boat Slip, Fractional Ownership, and Garage were subtypes under 'Other.' | These are now subtypes under the ‘Residential-Single Family’ Property Type | RESO does not include an 'Other' property type. Additionally, the ‘Other’ property type was frequently misunderstood or overlooked. |
| **Property Status** | Active New Construction merged into Active | 'Active New Construction' was a distinct status. | ANC listings in Paragon will appear ‘Active’ with ‘Construction Status’ set to ‘Under Construction’. | ANC was only created due to Paragon limitations that prevented accurate DOM calculation without the addition of an auxiliary status. |
| **Area** | Area field removed | Agents selected an 'Area' when entering a listing. | No Area field. Location is defined by address, geography filters (city, ZIP, draw boundary), or school district. | Fair housing compliance requires geographic data based on neutral, recognized standards. Baldwin replaced Area with objective boundaries (municipalities, ZIP codes, school districts). |
| **More than 2 Pets Allowed?** | Field is now a lookup under Community Amenities | ‘More than 2 Pets Allowed?’ is a Yes/No field. | ‘More than 2 pets allowed’ is a lookup selectable under Community Amenities | As all other pets-related fields are under Community Amenities, this improves the flow of Add/Edit. |
| **Pool Features** | Pool-related Community Amenity and Property Amenity options were consolidated under Pool Features. | Pool-related attributes split across Community Amenities, Property Amenities, and Pool Features. | All pool attributes grouped under one 'Pool Features' section. | One section makes pool attributes easier to find when entering and searching listings. |
| **Year Built** | Year Built now must be a valid year. | Any integer accepted as a year (e.g. 99999). | Only years between 1500 and 2030 accepted. If unknown, contact the county. If records were destroyed (e.g., hurricane), use the best available year (e.g., year the foundation was built). | Placeholder values reduce data quality. This ensures the most accurate year available is recorded. |
