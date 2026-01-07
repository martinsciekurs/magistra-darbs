---
sidebar_position: 152
---

# TestRunChain

**File:** `tests/unit/indexing/verbs/entities/extraction/strategies/graph_intelligence/test_gi_entity_extraction.py`

## Overview

TestRunChain is a unittest.TestCase subclass that validates the graph intelligence entity extraction workflow exercised by run_extract_graph. The tests focus on ensuring that, given a set of input Document objects and a mocked LLM, the resulting graph contains the expected entities and edges, and that entity/edge source_ids are consistently mapped across multiple documents. The class provides a high-level overview of the testing goal and the scope of what is being verified, without enumerating individual test methods.

Purpose
- Verify that the graph produced by run_extract_graph correctly captures entities and relationships for single- and multi-document inputs.
- Ensure that source_id mappings for both entities and edges are propagated across documents as expected.

Scope and responsibilities
- Uses a controlled mock LLM to simulate responses and drive deterministic results.
- Exercises the graph-building behavior of the Graph Intelligence strategy, not the LLM implementation itself.

Key attributes
- mock_llm: a mock language model used to supply deterministic responses during tests.
- documents: input Document objects used to drive run_extract_graph.
- expected_graph: abstracted expectations used to verify correctness of the produced graph.

Usage
- Part of the unit test suite, discovered and run via standard unittest discovery.
- Requires no external resources beyond the provided mock LLM.

Note
- This class documents the overall testing goal and scope rather than listing individual test methods.

## Methods

### `test_run_extract_graph_single_document_correct_entities_returned`

```python
def test_run_extract_graph_single_document_correct_entities_returned(self)
```

### `test_run_extract_graph_multiple_documents_correct_entities_returned`

```python
def test_run_extract_graph_multiple_documents_correct_entities_returned(
        self,
    )
```

### `test_run_extract_graph_multiple_documents_correct_edges_returned`

```python
def test_run_extract_graph_multiple_documents_correct_edges_returned(self)
```

### `test_run_extract_graph_multiple_documents_correct_entity_source_ids_mapped`

```python
def test_run_extract_graph_multiple_documents_correct_entity_source_ids_mapped(
        self,
    )
```

### `test_run_extract_graph_multiple_documents_correct_edge_source_ids_mapped`

```python
def test_run_extract_graph_multiple_documents_correct_edge_source_ids_mapped(
        self,
    )
```

