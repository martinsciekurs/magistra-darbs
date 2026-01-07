---
sidebar_position: 258
---

# tests/unit/indexing/verbs/entities/extraction/strategies/graph_intelligence/test_gi_entity_extraction.py

## Overview

Tests for graph intelligence entity extraction strategies used by run_extract_graph.

Purpose
This module contains unit tests for extracting graph-based representations of entities and their relationships from documents using the graph_intelligence_strategy. A mocked LLM is used to provide deterministic outputs for testing.

Key exports
- TestRunChain: unittest.TestCase subclass that validates the graph intelligence entity extraction workflow exercised by run_extract_graph, including entity extraction, edge creation, and cross-document source_id mappings.

Brief summary
The tests cover single and multiple-document scenarios to ensure correct entity titles, correct edges, and consistent mapping of entity and edge source_ids across documents.

Public test functions
- test_run_extract_graph_single_document_correct_entities_returned
- test_run_extract_graph_multiple_documents_correct_entities_returned
- test_run_extract_graph_multiple_documents_correct_edges_returned
- test_run_extract_graph_multiple_documents_correct_entity_source_ids_mapped
- test_run_extract_graph_multiple_documents_correct_edge_source_ids_mapped

Notes
- Uses create_mock_llm to simulate LLM responses.
- Imports include run_extract_graph, Document typing, and mock_llm helper.

## Classes

- [`TestRunChain`](../api/classes/tests-unit-indexing-verbs-entities-extraction-strategies-graph-intelligence-test-gi-entity-extraction-testrunchain)

## Functions

- [`test_run_extract_graph_single_document_correct_entities_returned`](../api/functions/tests-unit-indexing-verbs-entities-extraction-strategies-graph-intelligence-test-gi-entity-extraction-test-run-extract-graph-single-document-correct-entities-returned)
- [`test_run_extract_graph_multiple_documents_correct_entities_returned`](../api/functions/tests-unit-indexing-verbs-entities-extraction-strategies-graph-intelligence-test-gi-entity-extraction-test-run-extract-graph-multiple-documents-correct-entities-returned)
- [`test_run_extract_graph_multiple_documents_correct_edges_returned`](../api/functions/tests-unit-indexing-verbs-entities-extraction-strategies-graph-intelligence-test-gi-entity-extraction-test-run-extract-graph-multiple-documents-correct-edges-returned)
- [`test_run_extract_graph_multiple_documents_correct_entity_source_ids_mapped`](../api/functions/tests-unit-indexing-verbs-entities-extraction-strategies-graph-intelligence-test-gi-entity-extraction-test-run-extract-graph-multiple-documents-correct-entity-source-ids-mapped)
- [`test_run_extract_graph_multiple_documents_correct_edge_source_ids_mapped`](../api/functions/tests-unit-indexing-verbs-entities-extraction-strategies-graph-intelligence-test-gi-entity-extraction-test-run-extract-graph-multiple-documents-correct-edge-source-ids-mapped)

