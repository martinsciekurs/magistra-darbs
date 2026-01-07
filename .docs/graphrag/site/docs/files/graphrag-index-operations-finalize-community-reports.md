---
sidebar_position: 73
---

# graphrag/index/operations/finalize_community_reports.py

## Overview

Finalizes community reports by merging input reports with metadata from the communities dataset.

Purpose
- Provide a single, final DataFrame for reporting on communities by enriching input reports with community metadata.

Key exports
- finalize_community_reports: Merge input reports with communities to create final community reports.

Summary
- This module implements the finalize_community_reports function, which merges the input reports DataFrame with the communities DataFrame to produce a final DataFrame that includes community-level metadata. The final shape is driven by COMMUNITY_REPORTS_FINAL_COLUMNS.

Function details
finalize_community_reports
    Args:
        reports: The input reports data to be enriched with community metadata.
        communities: The communities dataset containing metadata used for enrichment (including fields used for the merge: 'community', 'parent', 'children', 'size', 'period').
    Returns:
        The finalized community reports DataFrame containing the merged data, adhering to the columns defined by COMMUNITY_REPORTS_FINAL_COLUMNS.

## Functions

- [`finalize_community_reports`](../api/functions/graphrag-index-operations-finalize-community-reports-finalize-community-reports)

