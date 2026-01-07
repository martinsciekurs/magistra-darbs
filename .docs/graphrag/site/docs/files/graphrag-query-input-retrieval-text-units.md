---
sidebar_position: 198
---

# graphrag/query/input/retrieval/text_units.py

## Overview

Utilities to retrieve and convert text units for query input.

Purpose
This module provides helpers to convert lists of TextUnit objects into a pandas DataFrame and to obtain the text units associated with a set of Entity objects for downstream query processing.

Key exports
- to_text_unit_dataframe(text_units: list[TextUnit]) -&gt; pd.DataFrame
  Args: text_units: The text units to convert into a DataFrame. If the list is empty, an empty DataFrame is returned.
  Returns: pd.DataFrame: A DataFrame where each row corresponds to a text unit. The columns are: "id": the text unit's short_id; "text": the text of the text unit; and any additional columns as present.

- get_candidate_text_units(selected_entities: list[Entity], text_units: list[TextUnit]) -&gt; pd.DataFrame
  Args: selected_entities: Entities whose text_unit_ids (if any) are used to select text units. text_units: The pool of TextUnit objects to search.
  Returns: pd.DataFrame: A DataFrame containing the text units associated with the selected entities. The DataFrame is produced by converting the selected text units.

Summary
These utilities are lightweight and operate on TextUnit and Entity objects to prepare DataFrame representations for further processing in retrieval workflows.

## Functions

- [`to_text_unit_dataframe`](../api/functions/graphrag-query-input-retrieval-text-units-to-text-unit-dataframe)
- [`get_candidate_text_units`](../api/functions/graphrag-query-input-retrieval-text-units-get-candidate-text-units)

