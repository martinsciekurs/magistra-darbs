---
sidebar_position: 106
---

# graphrag/index/update/incremental_index.py

## Overview

Utilities for incremental index updates in graphrag.

This module provides helpers to compute the delta between an input dataset and the final documents stored in pipeline storage, and to produce an output dataset by concatenating previously stored documents with the delta.

Key exports:
- get_delta_docs
- concat_dataframes

Functions:
- get_delta_docs(input_dataset: pd.DataFrame, storage: PipelineStorage) -&gt; InputDelta
  Compute the delta between the input_dataset and the final documents stored in the pipeline storage. The function compares the input_dataset against the documents currently stored and returns the delta as an InputDelta with new_inputs and deleted_inputs. Note: new_inputs correspond to documents in input_dataset whose titles are not present in the stored final documents.

- concat_dataframes(
  name: str,
  previous_storage: PipelineStorage,
  delta_storage: PipelineStorage,
  output_storage: PipelineStorage
) -&gt; pd.DataFrame
  Concatenate dataframes from previous and delta storages. Load from previous_storage and delta_storage, append delta to old after assigning sequential human_readable_id values to delta rows, and write the final dataframe to output_storage as &#123;name&#125;.parquet.
  Returns: The final concatenated pandas DataFrame.

Raises:
- Exceptions that may be raised by underlying storage operations.

## Functions

- [`get_delta_docs`](../api/functions/graphrag-index-update-incremental-index-get-delta-docs)
- [`concat_dataframes`](../api/functions/graphrag-index-update-incremental-index-concat-dataframes)

