---
sidebar_position: 91
---

# TestIndexer

**File:** `tests/smoke/test_fixtures.py`

## Overview

TestIndexer is a test helper that coordinates setup, execution, and validation of smoke-test fixtures for the indexer and its queries. It encapsulates helpers to run the indexer, issue queries, verify indexer outputs against a workflow configuration, and prepare blob-storage backed test data for fixtures used by the test suite. The class orchestrates test preparation, execution, and validation within the tests/smoke/test_fixtures.py module.

Attributes:
- The class does not expose explicit attributes in the excerpt; it relies on internal helpers and runtime parameters to perform operations.

Methods:
__assert_indexer_outputs(self, root: Path, workflow_config: dict[str, dict[str, Any]]) -&gt; None
- Asserts that the indexer outputs under root conform to the provided workflow_config.
- Returns: None
- Raises: AssertionError if outputs do not match; ValueError for invalid inputs.

__run_indexer(self, root: Path, input_file_type: str) -&gt; subprocess.CompletedProcess
- Runs the indexer command for the given root and input_file_type and returns the subprocess result.
- Returns: CompletedProcess representing the executed command.
- Raises: subprocess.CalledProcessError if the command fails.

__run_query(self, root: Path, query_config: dict[str, str]) -&gt; subprocess.CompletedProcess
- Runs a query against the indexer using the provided root and query_config and returns the subprocess result.
- Returns: CompletedProcess of the query command.
- Raises: subprocess.CalledProcessError on failure.

test_fixture(self, input_path: str, input_file_type: str, workflow_config: dict[str, dict[str, Any]], query_config: list[dict[str, str]]) -&gt; Callable[[], None]
- Prepares test fixture data in the blob-storage-like backend used by the tests, uploading data from the specified input_path and configuring the test run as described by workflow_config and query_config.
- Returns: A no-argument callable that cleans up the created resources when invoked.
- Raises: ValueError if inputs are invalid; RuntimeError for storage-related failures.

## Methods

### `__assert_indexer_outputs`

```python
def __assert_indexer_outputs(
        self, root: Path, workflow_config: dict[str, dict[str, Any]]
    )
```

### `__run_indexer`

```python
def __run_indexer(
        self,
        root: Path,
        input_file_type: str,
    )
```

### `__run_query`

```python
def __run_query(self, root: Path, query_config: dict[str, str])
```

### `test_fixture`

```python
def test_fixture(
        self,
        input_path: str,
        input_file_type: str,
        workflow_config: dict[str, dict[str, Any]],
        query_config: list[dict[str, str]],
    )
```

