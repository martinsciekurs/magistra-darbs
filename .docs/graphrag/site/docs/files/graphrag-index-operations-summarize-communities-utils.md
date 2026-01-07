---
sidebar_position: 94
---

# graphrag/index/operations/summarize_communities/utils.py

## Overview

Utilities for summarizing communities in Graphrag.

Purpose
Provide helper functions for extracting and processing community level information from data frames used in the summarize_communities workflow.

Key exports
- get_levels(df: pd.DataFrame, level_column: str = schemas.COMMUNITY_LEVEL) -&gt; list[int]

Brief summary
- get_levels returns a descending-ordered list of integer levels, ignoring -1 and NaN values. It may raise KeyError if level_column is not a column in the input DataFrame.

## Functions

- [`get_levels`](../api/functions/graphrag-index-operations-summarize-communities-utils-get-levels)

