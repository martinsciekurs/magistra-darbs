---
sidebar_position: 107
---

# graphrag/index/update/relationships.py

## Overview

Utilities for updating and merging relationship data during index updates.

This module provides a helper to apply delta relationships to existing ones and return a DataFrame conforming to the final relationship schema defined by RELATIONSHIPS_FINAL_COLUMNS.

Key exports
- _update_and_merge_relationships(old_relationships: pd.DataFrame, delta_relationships: pd.DataFrame) -&gt; pd.DataFrame

Args
- old_relationships: The old relationships DataFrame.
- delta_relationships: The delta relationships DataFrame.

Returns
- The updated relationships, containing the final columns as defined by RELATIONSHIPS_FINAL_COLUMNS.

Raises
- KeyError: If required columns are missing from the input DataFrames.
- TypeError: If the inputs are invalid or cannot be processed.

## Functions

- [`_update_and_merge_relationships`](../api/functions/graphrag-index-update-relationships-update-and-merge-relationships)

