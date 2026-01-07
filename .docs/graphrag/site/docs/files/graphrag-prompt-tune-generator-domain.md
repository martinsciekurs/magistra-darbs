---
sidebar_position: 173
---

# graphrag/prompt_tune/generator/domain.py

## Overview

Utilities to generate a domain-specific LLM persona for GraphRAG prompts.

Purpose
This module exposes a function to generate a domain persona by querying a chat-based language model using a predefined domain prompt template (GENERATE_DOMAIN_PROMPT).

Key exports
- generate_domain(model: ChatModel, docs: str | list[str]) -&gt; str: Generate a domain persona for GraphRAG prompts by invoking the provided ChatModel with the GENERATE_DOMAIN_PROMPT and the given docs.

Brief summary
Provides a convenient entry point to create domain prompts for GraphRAG via a language model.

## Functions

- [`generate_domain`](../api/functions/graphrag-prompt-tune-generator-domain-generate-domain)

