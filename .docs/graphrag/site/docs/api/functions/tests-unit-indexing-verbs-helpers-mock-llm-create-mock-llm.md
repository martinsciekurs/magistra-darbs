---
sidebar_position: 539
---

# create_mock_llm

**File:** `tests/unit/indexing/verbs/helpers/mock_llm.py` (lines 9-13)

## Signature

```python
def create_mock_llm(responses: list[str | BaseModel], name: str = "mock") -> ChatModel
```

## Description

Creates a mock LLM that returns the given responses.

Args:
    responses (list[str | BaseModel]): The responses to be returned by the mock LLM.
    name (str): The name of the mock LLM. Defaults to "mock".

Returns:
    ChatModel: A mock ChatModel configured to return the provided responses.

Raises:
    Exception: If an error occurs while creating or retrieving the mock chat model via ModelManager.

## Dependencies

This function calls:

- `graphrag/language_model/manager.py::ModelManager`

## Called By

This function is called by:

- `tests/unit/indexing/verbs/entities/extraction/strategies/graph_intelligence/test_gi_entity_extraction.py::TestRunChain.test_run_extract_graph_single_document_correct_entities_returned`
- `tests/unit/indexing/verbs/entities/extraction/strategies/graph_intelligence/test_gi_entity_extraction.py::TestRunChain.test_run_extract_graph_multiple_documents_correct_entities_returned`
- `tests/unit/indexing/verbs/entities/extraction/strategies/graph_intelligence/test_gi_entity_extraction.py::TestRunChain.test_run_extract_graph_multiple_documents_correct_edges_returned`
- `tests/unit/indexing/verbs/entities/extraction/strategies/graph_intelligence/test_gi_entity_extraction.py::TestRunChain.test_run_extract_graph_multiple_documents_correct_entity_source_ids_mapped`
- `tests/unit/indexing/verbs/entities/extraction/strategies/graph_intelligence/test_gi_entity_extraction.py::TestRunChain.test_run_extract_graph_multiple_documents_correct_edge_source_ids_mapped`

