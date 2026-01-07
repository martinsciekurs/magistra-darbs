---
sidebar_position: 8
---

# AI Orchestration & LLM Providers

GraphRAG abstracts language models, tokenization, and LLM service management to decouple model backends from the rest of the system. This enables flexible selection of providers, lifecycle management, and plug-and-play experimentation with different model families.

Architectural purpose
- Registry-based framework to register, instantiate, and manage chat-based and embedding LLM backends.
- Decoupling of model providers from GraphRAG’s core logic to support on-demand creation and lifecycle management.

Key components and responsibilities
- language_model/__init__.py: Public surface exposing the language-model stack.
- language_model/factory.py: Factory for creating model backends based on configuration.
- language_model/manager.py: Orchestrates model lifecycles, hot swapping, and resource management.
- language_model/providers/fnllm/models.py and utils.py: Implementations and utilities for the FNLLM provider (functions for model interaction, tokenization, etc.).
- language_model/providers/litellm/*: Providers and utilities for LiteLLM-based backends.
- Callback integration: Hooks for LLM responses, streaming, and logging (e.g., graphrag/callbacks/*).

What this enables
- Runtime choice of LLM provider (OpenAI, Azure OpenAI, local/offline models, etc.).
- Independent tokenization and prompt handling suited to different backends.
- Safe lifecycle management including initialization, warm-up, and shutdown of model instances.

Note: The actual provider implementations live under graphrag/language_model and graphrag/language_model/providers. This section documents the intended role and integration points rather than concrete provider details.
