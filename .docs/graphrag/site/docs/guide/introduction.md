---
sidebar_position: 2
---

# Introduction

GraphRAG is a Python-based data pipeline and knowledge-graph augmentation framework designed to help you index unstructured private text, extract entities and relations, and build a hierarchical knowledge graph. It then uses large language models (LLMs) to answer questions with context-augmented prompts, enabling retrieval-augmented reasoning over private datasets. The project provides modular components for indexing, prompt tuning, querying, and visualization, making it suitable for researchers and developers who want to experiment with graph-enabled reasoning on proprietary text.

Key concepts and workflow at a glance:
- Indexing: Slice input text into fine-grained TextUnits, use LLM-driven prompts to extract entities (with configurable entity types), relationships, and optionally claims (factual assertions linked to source text), and organize them into a knowledge graph.
- Prompt templates: Customizable prompt files for entity extraction, relationship extraction, and community report generation. Templates use token substitution (e.g., {entity_types}, {tuple_delimiter}) for domain adaptation.
- Ontology: Represent documents, entities, relationships, and communities with a coherent data model and schemas.
- Graph structure: Build a hierarchical community graph with summaries, enabling holistic and domain-focused reasoning.
- Prompt augmentation: Leverage the graph, community summaries, and entity context to augment LLM prompts at query time. Default prompts can be overridden via custom prompt files.
- AI orchestration: Abstracted LLM providers and tokenization backends enable flexible model backends and lifecycle management. Supports OpenAI-compatible endpoints via api_base and proxy configuration for non-OpenAI models.
- Storage and retrieval: Pluggable storage backends and vector stores support private data handling and scalable retrieval.
- End-to-end workflows: Clear workflows for data ingestion, graph construction, embedding, updates, and answering questions.

This documentation summarizes the project, its goals, and the core concepts behind GraphRAG, with a focus on how its modular components come together to enable sophisticated retrieval-augmented reasoning over private text.
