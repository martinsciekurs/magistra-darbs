---
sidebar_position: 91
---

# graphrag/index/operations/summarize_communities/text_unit_context/prep_text_units.py

## Overview

Text unit context preparation for community summarization.

Purpose
Provide utilities to prepare text unit data by computing degrees from the node dataset and concatenating text unit details to support downstream summarization tasks.

Exports
prep_text_units(text_unit_df: pd.DataFrame, node_df: pd.DataFrame) -&gt; pd.DataFrame
    Calculate text unit degree and concatenate text unit details. Returns a DataFrame with enriched text unit information ready for further processing.

Brief summary
This module exposes prep_text_units which processes input DataFrames to enrich text unit data with degree information and merged fields for downstream processing in the summarize_communities workflow.

## Functions

- [`prep_text_units`](../api/functions/graphrag-index-operations-summarize-communities-text-unit-context-prep-text-units-prep-text-units)

