---
sidebar_position: 104
---

# graphrag/index/update/communities.py

## Overview

Utilities to update and merge communities and their reports during Graphrag's indexing process.

Purpose:
Provide internal helpers to consolidate old and delta data into final, schema-aligned structures for downstream processing.

Key exports:
- _update_and_merge_communities(old_communities, delta_communities) -&gt; tuple[pd.DataFrame, dict]
- _update_and_merge_community_reports(old_community_reports, delta_community_reports, community_id_mapping) -&gt; pd.DataFrame

Summary:
This module contains two internal functions:
1) _update_and_merge_communities: mutates the provided DataFrames to ensure required structure, remaps delta community IDs to avoid collisions with old data, and merges them into a single DataFrame aligned to COMMUNITIES_FINAL_COLUMNS. It also returns the mapping from original delta community IDs to the new IDs assigned during the merge.
2) _update_and_merge_community_reports: updates and merges old and delta community reports into a single DataFrame aligned to the final columns, using the provided community_id_mapping to translate delta IDs to final IDs.

Args:
  - For _update_and_merge_communities:
      old_communities: The old communities DataFrame.
      delta_communities: The delta communities DataFrame.

  - For _update_and_merge_community_reports:
      old_community_reports: The old community reports DataFrame.
      delta_community_reports: The delta community reports DataFrame.
      community_id_mapping: The mapping from original delta community IDs to final IDs.

Returns:
  - For _update_and_merge_communities: A tuple consisting of (merged_communities: pd.DataFrame, community_id_mapping: dict)
  - For _update_and_merge_community_reports: A single pd.DataFrame containing the updated community reports aligned to COMMUNITY_REPORTS_FINAL_COLUMNS.

Raises:
  - May raise exceptions propagated from pandas operations used within these functions.

## Functions

- [`_update_and_merge_communities`](../api/functions/graphrag-index-update-communities-update-and-merge-communities)
- [`_update_and_merge_community_reports`](../api/functions/graphrag-index-update-communities-update-and-merge-community-reports)

