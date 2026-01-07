---
sidebar_position: 220
---

# create_base_text_units

**File:** `graphrag/index/workflows/create_base_text_units.py` (lines 53-163)

## Signature

```python
def create_base_text_units(
    documents: pd.DataFrame,
    callbacks: WorkflowCallbacks,
    group_by_columns: list[str],
    size: int,
    overlap: int,
    encoding_model: str,
    strategy: ChunkStrategyType,
    prepend_metadata: bool = False,
    chunk_size_includes_metadata: bool = False,
) -> pd.DataFrame
```

## Description

Converts input documents into base text units by grouping, chunking, and optional metadata preprocessing.

Args:
    documents (pd.DataFrame): Input table containing documents. Expected to contain at least the columns "id" and "text". May also include optional "metadata".
    callbacks (WorkflowCallbacks): Callbacks used during the chunking process.
    group_by_columns (list[str]): Columns to group documents by before text chunking. If empty, all documents are treated as a single group.
    size (int): Maximum number of tokens per chunk (excluding any metadata unless chunk_size_includes_metadata is True).
    overlap (int): Number of tokens to overlap between consecutive chunks.
    encoding_model (str): Encoding model name used to compute token lengths for chunking.
    strategy (ChunkStrategyType): Strategy used by the underlying chunk_text operation.
    prepend_metadata (bool): If True, prepend the document metadata to each generated chunk.
    chunk_size_includes_metadata (bool): If True, metadata is counted towards the per-chunk size. When True, metadata tokens are subtracted from size and may raise ValueError if they exceed the per-chunk limit.

Returns:
    pd.DataFrame: A dataframe containing one row per chunk. Columns include the grouping keys from group_by_columns, "id" (SHA-512 hash of the chunk), "text" (the chunk text), "document_ids" (list of document ids contributing to the chunk), and "n_tokens" (token length of the chunk). The exact set of columns may also include the original grouping keys.

Raises:
    ValueError: If prepend_metadata is enabled and chunk_size_includes_metadata is True and the computed metadata token length exceeds the per-chunk size.

Notes:
    The function logs progress during processing. It sorts documents by id, aggregates text with ids, chunks large text units into smaller chunks, optionally prepends metadata to chunks, and computes a stable hash id for each chunk.

## Dependencies

This function calls:

- `graphrag/index/utils/hashing.py::gen_sha512_hash`
- `graphrag/index/workflows/create_base_text_units.py::chunker_with_logging`

## Called By

This function is called by:

- `graphrag/index/workflows/create_base_text_units.py::run_workflow`
- `graphrag/prompt_tune/loader/input.py::load_docs_in_chunks`

