---
sidebar_position: 255
---

# tests/unit/indexing/operations/chunk_text/test_strategies.py

## Overview

Unit tests for chunk_text strategies used by the indexing module.

This module contains unit tests for sentence-based chunking (RunSentences) and token-based chunking (RunTokens), as well as tests for encoding function retrieval (get_encoding_fn) and bootstrap initialization.

Public exports:
- TestRunSentences: Test class validating sentence-splitting behavior and chunk origins.
- TestRunTokens: Test class validating token-based chunking behavior.
- get_encoding_fn: Function under test for obtaining encode/decode functions from an encoding model.
- bootstrap: Setup utility used to initialize test resources.
- TextChunk: TextChunk type used by the tests.

Test focus summary:
- Basic functionality of sentence splitting into TextChunk objects; verify text content, source_doc_indices, and that the progress ticker is invoked as expected.
- Handling of multiple documents with per-document chunk origins.
- Mixed whitespace handling in sentence splitting.
- Encoding retrieval tests for encode/decode behavior, using mocked encodings.
- Non-string input handling during tokenization tests.

Args: None
Returns: None
Raises: None

## Classes

- [`TestRunSentences`](../api/classes/tests-unit-indexing-operations-chunk-text-test-strategies-testrunsentences)
- [`TestRunTokens`](../api/classes/tests-unit-indexing-operations-chunk-text-test-strategies-testruntokens)

## Functions

- [`setup_method`](../api/functions/tests-unit-indexing-operations-chunk-text-test-strategies-setup-method)
- [`test_basic_functionality`](../api/functions/tests-unit-indexing-operations-chunk-text-test-strategies-test-basic-functionality)
- [`test_multiple_documents`](../api/functions/tests-unit-indexing-operations-chunk-text-test-strategies-test-multiple-documents)
- [`test_mixed_whitespace_handling`](../api/functions/tests-unit-indexing-operations-chunk-text-test-strategies-test-mixed-whitespace-handling)
- [`test_get_encoding_fn_encode`](../api/functions/tests-unit-indexing-operations-chunk-text-test-strategies-test-get-encoding-fn-encode)
- [`test_get_encoding_fn_decode`](../api/functions/tests-unit-indexing-operations-chunk-text-test-strategies-test-get-encoding-fn-decode)
- [`test_basic_functionality`](../api/functions/tests-unit-indexing-operations-chunk-text-test-strategies-test-basic-functionality)
- [`test_non_string_input`](../api/functions/tests-unit-indexing-operations-chunk-text-test-strategies-test-non-string-input)

