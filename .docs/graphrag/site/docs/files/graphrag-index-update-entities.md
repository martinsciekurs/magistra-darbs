---
sidebar_position: 105
---

# graphrag/index/update/entities.py

## Overview

Utilities for updating entities by merging existing data with delta updates and resolving conflicts by title.

Purpose
This module provides helpers to group existing and delta entity data, resolve conflicts by title, and return a
merged entities DataFrame with a consistent column order defined by ENTITIES_FINAL_COLUMNS. It also returns
a mapping from delta entity IDs to existing entity IDs for overlapping titles.

Key exports
- _group_and_resolve_entities(old_entities_df: pd.DataFrame, delta_entities_df: pd.DataFrame) -&gt; tuple[pd.DataFrame, dict]
  Merge the old and delta entities, build the delta-to-existing ID mapping for overlapping titles, and return
  the resolved DataFrame ordered according to ENTITIES_FINAL_COLUMNS.

Notes
- The inputs must include the required entity columns; missing columns will raise KeyError.
- The returned DataFrame uses the fixed column order ENTITIES_FINAL_COLUMNS to ensure downstream consistency.

Usage example
Given old_entities_df and delta_entities_df, call _group_and_resolve_entities(old_entities_df, delta_entities_df) to obtain
(a) the merged entities DataFrame and (b) a dictionary mapping delta IDs to existing IDs for titles that existed.

## Functions

- [`_group_and_resolve_entities`](../api/functions/graphrag-index-update-entities-group-and-resolve-entities)

