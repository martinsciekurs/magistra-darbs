---
sidebar_position: 35
---

# graphrag/data_model/community_report.py

## Overview

Community report data model for Graphrag.

This module defines a dataclass-based model representing a community report, storing identifiers, metadata, and content for a specific community. The CommunityReport class inherits from Named and offers a convenient from_dict constructor for building instances from dictionaries.

Exports:
- CommunityReport: Dataclass-based model representing a community report; inherits from Named.
- from_dict: Classmethod that creates a CommunityReport instance from a dictionary, with configurable dictionary keys.

Args:
- cls: The class.
- d: The source dictionary containing the values for the CommunityReport fields.
- id_key: Key in d for the report's identifier. Defaults to "id".
- title_key: Key in d for the report title. Defaults to "title".
- community_id_key: Key in d for the associated community's id. Defaults to "community".
- short_id_key: Key in d for the human-readable identifier. Defaults to "human_readable_id".
- summary_key: Key in d for the summary. Defaults to "summary".
- full_content_key: Key in d for the full content. Defaults to "full_content".
- rank_key: Key in d for the rank. Defaults to "rank".
- attributes_key: Key in d for the attributes. Defaults to "attributes".
- size_key: Key in d for the size. Defaults to "size".
- period_key: Key in d for the period. Defaults to "period".

Returns:
- CommunityReport: The constructed CommunityReport instance.

Raises:
- None documented.

Summary:
The module centralizes the data model for a community report and exposes a simple API to instantiate it from a dictionary.

## Classes

- [`CommunityReport`](../api/classes/graphrag-data-model-community-report-communityreport)

## Functions

- [`from_dict`](../api/functions/graphrag-data-model-community-report-from-dict)

