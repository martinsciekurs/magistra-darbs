---
sidebar_position: 7
---

# Data Model & Ontology

Core data structures and schemas define how GraphRAG represents content inside the knowledge graph. The ontology enables serialization/deserialization and consistent data modeling across the GraphRAG domain. Key data model components and their roles include:

- Document: Represents a source document or input corpus with metadata and text content. Provides a factory to build Document instances from dictionaries and maps to the internal storage/graph structures.
- TextUnit: Fine-grained analyzable units derived from documents, used for extraction and indexing granularity.
- Entity: Represents an identified entity such as a person, place, organization, or object, with attributes including title/name and identifiers.
- Relationship: Captures connections between entities with semantic typing (e.g., description of the relationship), edge weights for ranking, and source/target references.
- Community: Represents clusters or groups within the graph discovered via hierarchical Leiden algorithm, used to summarize and structure the graph hierarchy.
- CommunityReport: LLM-generated summaries of each community containing key entities, relationships, and claims. Used as context for global search (map-reduce) queries.
- Schemas & Types: Shared schemas and type definitions that ensure consistent data structures across modules.

Files involved (examples):
- graphrag/graphrag/data_model/document.py
- graphrag/graphrag/data_model/entity.py
- graphrag/graphrag/data_model/relationship.py
- graphrag/graphrag/data_model/community.py
- graphrag/graphrag/data_model/community_report.py
- graphrag/graphrag/data_model/text_unit.py
- graphrag/graphrag/data_model/schemas.py
- graphrag/graphrag/data_model/types.py

How the ontology is used
- Ingested documents are broken into TextUnits and mapped to Document metadata.
- Entities and relationships populate a graph, which is organized into communities with summaries.
- The graph and community information are leveraged to construct context windows for LLM prompts during queries, enabling more grounded and interpretable answers.

Output tables
- Documents table: Source documents with metadata and provenance.
- Entities table: Extracted entities with attributes, descriptions, and embeddings.
- Relationships table: Entity connections with semantic types and weights.
- Communities table: Hierarchical community clustering data from Leiden.
- Community reports table: LLM-generated summaries with metadata for each community.
