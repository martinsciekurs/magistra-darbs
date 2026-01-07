---
sidebar_position: 195
---

# derive_from_rows

**File:** `graphrag/index/utils/derive_from_rows.py` (lines 34-55)

## Signature

```python
def derive_from_rows(
    input: pd.DataFrame,
    transform: Callable[[pd.Series], Awaitable[ItemType]],
    callbacks: WorkflowCallbacks | None = None,
    num_threads: int = 4,
    async_type: AsyncType = AsyncType.AsyncIO,
    progress_msg: str = "",
) -> list[ItemType | None]
```

## Description

Apply a generic transform function to each row in the input DataFrame.

 Any errors raised by the transform will be reported and thrown.

 Args:
   input: The input DataFrame to process; each row will be transformed.
   transform: Async function applied to a row's Series to produce an ItemType.
   callbacks: Workflow callbacks; used to report progress and handle events. If None, NoopWorkflowCallbacks is used.
   num_threads: Number of concurrent workers to use.
   async_type: Scheduling type to use for execution (AsyncIO or Threaded). Defaults to AsyncType.AsyncIO.
   progress_msg: Optional progress message to display during processing.

 Returns:
   list[ItemType | None]: A list containing the transformed results, one per input row; entries may be None.

 Raises:
   ValueError: If an unsupported scheduling type is provided.

## Dependencies

This function calls:

- `graphrag/callbacks/noop_workflow_callbacks.py::NoopWorkflowCallbacks`
- `graphrag/index/utils/derive_from_rows.py::derive_from_rows_asyncio`
- `graphrag/index/utils/derive_from_rows.py::derive_from_rows_asyncio_threads`

## Called By

This function is called by:

- `graphrag/index/operations/build_noun_graph/build_noun_graph.py::_extract_nodes`
- `graphrag/index/operations/extract_covariates/extract_covariates.py::extract_covariates`
- `graphrag/index/operations/extract_graph/extract_graph.py::extract_graph`
- `graphrag/index/operations/summarize_communities/summarize_communities.py::summarize_communities`

