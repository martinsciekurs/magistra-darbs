---
sidebar_position: 179
---

# graphrag/prompt_tune/generator/persona.py

## Overview

Generate LLM personas for GraphRAG prompts.

Purpose:
This module provides a simple interface to generate a persona string for a given domain and task by invoking a ChatModel with a predefined prompt (GENERATE_PERSONA_PROMPT). It relies on DEFAULT_TASK as the default task value.

Key exports:
- generate_persona(model: ChatModel, domain: str, task: str = DEFAULT_TASK) -&gt; str

Summary:
The generate_persona function returns a generated persona string suitable for GraphRAG prompts, produced by the underlying language model.

## Functions

- [`generate_persona`](../api/functions/graphrag-prompt-tune-generator-persona-generate-persona)

