---
sidebar_position: 108
---

# extract_covariates

**File:** `graphrag/index/operations/extract_covariates/extract_covariates.py` (lines 32-76)

## Signature

```python
def extract_covariates(
    input: pd.DataFrame,
    callbacks: WorkflowCallbacks,
    cache: PipelineCache,
    column: str,
    covariate_type: str,
    strategy: dict[str, Any] | None,
    async_mode: AsyncType = AsyncType.AsyncIO,
    entity_types: list[str] | None = None,
    num_threads: int = 4,
)
```

## Description

Process a DataFrame by applying covariate extraction to the text in a specified column for each row, returning covariate rows as a DataFrame.

Args:
  input: The input DataFrame to process.
  callbacks: Workflow callbacks for progress reporting and events.
  cache: Cache to use for model and data storage.
  column: The name of the column containing text to extract covariates from.
  covariate_type: The type/tag to assign to produced covariate rows.
  strategy: Strategy configuration for covariate extraction; if None, an empty configuration is used.
  async_mode: Asynchronous mode to use when applying the strategy (default: AsyncType.AsyncIO).
  entity_types: Entity types to consider when extracting covariates; defaults to DEFAULT_ENTITY_TYPES if None.
  num_threads: Number of concurrent workers to use.

Returns:
  A DataFrame containing the extracted covariate rows, where each input row may contribute zero or more covariate rows. Each covariate row includes the original row fields, covariate data fields, and a covariate_type column.

Raises:
  Propagates exceptions raised by underlying operations (e.g., derive_from_rows, run_extract_claims).

## Dependencies

This function calls:

- `graphrag/index/utils/derive_from_rows.py::derive_from_rows`

## Called By

This function is called by:

- `graphrag/index/workflows/extract_covariates.py::run_workflow`

