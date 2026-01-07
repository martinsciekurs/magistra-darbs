---
sidebar_position: 172
---

# graphrag/prompt_tune/generator/community_reporter_role.py

## Overview

Module to generate a domain-specific community reporter role prompt for GraphRAG prompts.

Purpose
This module provides a function to assemble a tailored community reporter role for a given domain and persona, contextualized by provided documents. It uses a ChatModel to interact with the underlying LLM and a predefined prompt template (GENERATE_COMMUNITY_REPORTER_ROLE_PROMPT).

Key exports
- generate_community_reporter_role(model: ChatModel, domain: str, persona: str, docs: str | list[str]) -&gt; str

Notes
- The prompt template GENERATE_COMMUNITY_REPORTER_ROLE_PROMPT is imported for construction of the prompt.

## Functions

- [`generate_community_reporter_role`](../api/functions/graphrag-prompt-tune-generator-community-reporter-role-generate-community-reporter-role)

