---
sidebar_position: 249
---

# tests/unit/indexing/graph/extractors/community_reports/test_sort_context.py

## Overview

Tests for the sort_context function used in the community reports graph context.

Purpose
- Validate that sort_context returns a non-null context object.
- Verify that the token count of the produced context aligns with platform-dependent expectations and respects the tokenizer in use.
- Ensure that sort_context respects the max_context_tokens constraint when provided.

Summary
Two unit tests are included:
- test_sort_context: checks basic correctness of the produced context and that token budgeting matches platform behavior.
- test_sort_context_max_tokens: verifies that the context token count does not exceed the specified maximum.

Key exports
- sort_context: the function under test, imported from graphrag.index.operations.summarize_communities.graph_context.sort_context.

Examples
- Example 1: On platforms with a larger tokenizer, test_sort_context yields a non-null context whose token_count is within the expected platform-specific range.
- Example 2: When max_context_tokens is provided to sort_context, test_sort_context_max_tokens ensures the returned context token_count is less than or equal to the maximum.

Returns
- None. This module contains unit tests and does not return a value.

Raises
- AssertionError: If any assertion in the tests fails.

## Functions

- [`test_sort_context`](../api/functions/tests-unit-indexing-graph-extractors-community-reports-test-sort-context-test-sort-context)
- [`test_sort_context_max_tokens`](../api/functions/tests-unit-indexing-graph-extractors-community-reports-test-sort-context-test-sort-context-max-tokens)

