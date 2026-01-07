---
sidebar_position: 109
---

# graphrag/index/utils/derive_from_rows.py

## Overview

Utilities for deriving values from DataFrame rows in parallel or asynchronously with progress reporting and error handling.

This module provides a parallel/async processing framework for applying per-row transforms to a pandas DataFrame. It defines a ParallelizationError to aggregate errors, type aliases for the per-row execution and gathering functions, and a set of helpers to run transforms concurrently with optional threading and progress reporting.

Args:
  None: The module does not take arguments at import time.

Returns:
  A public API consisting of:
  - ParallelizationError, ItemType, ExecuteFn, GatherFn
  - execute_task, execute, execute_row_protected, gather
  - _derive_from_rows_base, derive_from_rows_asyncio_threads, derive_from_rows_asyncio, derive_from_rows

Raises:
  Runtime exceptions raised by the per-row transforms, asyncio management, or user code may propagate to callers.

## Classes

- [`ParallelizationError`](../api/classes/graphrag-index-utils-derive-from-rows-parallelizationerror)

## Functions

- [`__init__`](../api/functions/graphrag-index-utils-derive-from-rows-init)
- [`execute_task`](../api/functions/graphrag-index-utils-derive-from-rows-execute-task)
- [`execute`](../api/functions/graphrag-index-utils-derive-from-rows-execute)
- [`execute_row_protected`](../api/functions/graphrag-index-utils-derive-from-rows-execute-row-protected)
- [`gather`](../api/functions/graphrag-index-utils-derive-from-rows-gather)
- [`_derive_from_rows_base`](../api/functions/graphrag-index-utils-derive-from-rows-derive-from-rows-base)
- [`derive_from_rows_asyncio_threads`](../api/functions/graphrag-index-utils-derive-from-rows-derive-from-rows-asyncio-threads)
- [`derive_from_rows_asyncio`](../api/functions/graphrag-index-utils-derive-from-rows-derive-from-rows-asyncio)
- [`derive_from_rows`](../api/functions/graphrag-index-utils-derive-from-rows-derive-from-rows)

