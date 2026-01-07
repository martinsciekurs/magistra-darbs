---
sidebar_position: 194
---

# graphrag/query/input/retrieval/community_reports.py

## Overview

Utilities for retrieving related community reports and converting them to tabular form.

Purpose
Provide helpers to extract candidate communities related to a set of Entity objects and to transform a collection of CommunityReport objects into a pandas DataFrame for analysis.

Exports
- to_community_report_dataframe(reports: list[CommunityReport], include_community_rank: bool = False, use_community_summary: bool = False) -&gt; pandas.DataFrame
  Convert a list of CommunityReport objects to a pandas DataFrame.

- get_candidate_communities(selected_entities: list[Entity], community_reports: list[CommunityReport], include_community_rank: bool = False, use_community_summary: bool = False) -&gt; pandas.DataFrame
  Get all communities related to the provided selected entities. This function collects all community IDs from the provided entities, filters the given community_reports to those IDs, and returns a DataFrame produced by to_community_report_dataframe using the specified options.

Summary
The module bridges the data model (CommunityReport, Entity) with tabular representations for downstream analysis and processing.

## Functions

- [`to_community_report_dataframe`](../api/functions/graphrag-query-input-retrieval-community-reports-to-community-report-dataframe)
- [`get_candidate_communities`](../api/functions/graphrag-query-input-retrieval-community-reports-get-candidate-communities)

