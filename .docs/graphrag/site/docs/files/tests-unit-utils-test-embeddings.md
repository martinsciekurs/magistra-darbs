---
sidebar_position: 265
---

# tests/unit/utils/test_embeddings.py

## Overview

Unit tests for the embedding index name creation helper used by the embedding store.

Overview:
This module contains unit tests for graphrag.config.embeddings.create_index_name, imported in tests/unit/utils/test_embeddings.py. The tests verify the correct construction of the embedding index name and the validation behavior when validating embedding names.

Key exports:
- test_create_index_name
- test_create_index_name_invalid_embedding_throws
- test_create_index_name_invalid_embedding_does_not_throw

Function under test:
create_index_name(container_name: str, embedding_name: str, validate: bool = True) -&gt; str

Behavior and format:
The index name is formed by prefixing container_name to the embedding index and replacing dots in embedding_name with dashes, to accommodate vector stores that do not support dots. embedding_name must be one of the supported embedding names defined in graphrag.config.embeddings. If validate is True and the embedding_name is invalid, a ValueError is raised; if validate is False, invalid names do not raise and the function returns a constructed index name.

Notes:
- Correct module path: graphrag.config.embeddings (not graphrag.index.config.embeddings).
- Tests in this module do not return values; they assert expected outcomes.

## Functions

- [`test_create_index_name`](../api/functions/tests-unit-utils-test-embeddings-test-create-index-name)
- [`test_create_index_name_invalid_embedding_throws`](../api/functions/tests-unit-utils-test-embeddings-test-create-index-name-invalid-embedding-throws)
- [`test_create_index_name_invalid_embedding_does_not_throw`](../api/functions/tests-unit-utils-test-embeddings-test-create-index-name-invalid-embedding-does-not-throw)

