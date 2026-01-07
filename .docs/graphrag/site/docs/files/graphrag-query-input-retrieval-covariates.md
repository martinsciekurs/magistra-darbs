---
sidebar_position: 195
---

# graphrag/query/input/retrieval/covariates.py

## Overview

Utilities to retrieve and convert covariates related to entities for GraphRAG queries.

This module exposes helpers to identify covariates associated with a given set of entities and to transform covariate data into a pandas DataFrame suitable for query inputs.

Public API:
- get_candidate_covariates(selected_entities: list[Entity], covariates: list[Covariate]) -&gt; list[Covariate]
  Return the covariates that are related to any of the selected entities.
  Args:
    selected_entities: List[Entity] representing the selected entities.
    covariates: List[Covariate] objects to filter.
  Returns:
    List[Covariate] covariates related to the selected entities.

- to_covariate_dataframe(covariates: list[Covariate]) -&gt; pd.DataFrame
  Convert a list of Covariate objects into a pandas DataFrame suitable for query inputs.
  Args:
    covariates: List[Covariate] with each covariate expected to expose short_id, subject_id, and attributes (a dict).
  Returns:
    pandas.DataFrame: A DataFrame with columns:
      - short_id
      - subject_id
      - one column per attribute key found in the covariates' attributes (excluding short_id and subject_id).
    Values are strings or empty strings. If a covariate lacks an attribute key present in others, its cell is an empty string.

Notes:
- The DataFrame schema aligns with the Covariate model by using short_id/subject_id instead of generic id/entity terminology.
- If covariates is empty, to_covariate_dataframe returns an empty DataFrame with the base columns (short_id, subject_id).
- Empty or missing fields are represented as empty strings to preserve a consistent string-based input format for queries.

Error handling:
- TypeError is raised if inputs are not lists of the expected types (Entity/Covariate).
- ValueError is raised for structurally invalid Covariate data (e.g., non-dict attributes).

Example:
- Given selected_entities = [Entity(short_id="s1")] and covariates = [Covariate(short_id="s1", subject_id="e1", attributes=&#123;"score": "9"&#125;)], get_candidate_covariates(...) returns the matching covariate; to_covariate_dataframe(...) yields a DataFrame with columns ["short_id", "subject_id", "score"].

References:
- Covariate and Entity data models used by GraphRAG.

## Functions

- [`get_candidate_covariates`](../api/functions/graphrag-query-input-retrieval-covariates-get-candidate-covariates)
- [`to_covariate_dataframe`](../api/functions/graphrag-query-input-retrieval-covariates-to-covariate-dataframe)

