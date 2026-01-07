---
sidebar_position: 10
---

# Indexing & Query Workflows

End-to-end workflows define how data flows from ingestion to answering questions against the knowledge graph. The workflows coordinate multiple components to build, update, and query the index. Incremental indexing is supported for updating indices with new data while preserving existing outputs.

Core workflows and components
- load_input_documents.py: Ingests input sources (Plain Text, CSV, JSON) with schema validation via InputConfig and prepares documents for indexing.
- create_base_text_units.py: Splits documents into TextUnits with configurable chunk size and overlap; supports document boundary alignment.
- update_text_embeddings.py: Computes and updates embeddings for text units, feeding the vector store.
- update_entities_relationships.py: Extracts and updates entities and relationships in the graph, maintaining graph integrity.
- create_graph.py: Creates the graph structure from entities and relationships, including community hierarchies.
- embed_graph/embed_graph.py: Embeds graph-level representations and prepares graph-aware context for queries.
- embed_graph/embed_node2vec.py: Optional node2vec embeddings for enhanced graph embeddings.
- compute_degree.py: Computes node degrees and centrality metrics for ranking and visualization.
- prune_graph.py: Prunes the graph to remove duplicates or low-quality edges/nodes.
- snapshot_graphml.py: Outputs a GraphML snapshot for visualization tools.
- validate_config.py: Validates configuration in settings to ensure end-to-end workflows can run.
- state.py: Internal state definitions for workflow orchestration.

End-to-end lifecycle
1) Ingestion: Load input documents and create base text units.
2) Embedding: Compute embeddings and push to the vector store; store text/metadata artifacts.
3) Graph construction: Build the knowledge graph from entities, relationships, and communities; update degrees and prune if necessary.
4) Description summarization: Summarize entity and relationship descriptions using an LLM. Since entities/relationships may be found in many text units, each with its own description, these are combined into a single concise summary per entity/relationship.
5) Graph enrichment: Generate community reports (LLM-generated summaries of each community's entities, relationships, and claims) and graph-level features.
6) Query-time preparation: Assemble context using global (map-reduce over community reports), local (entity-based context), or DRIFT strategies.
7) Question answering: Use LLM prompts augmented with context to generate answers.
8) Visualization and inspection: Export graph snapshots and enable exploration via UI or GraphML files.

This orchestration enables researchers and developers to iterate on indexing strategies, graph structures, and prompt design while maintaining a consistent workflow and data model.
