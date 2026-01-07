---
sidebar_position: 175
---

# graphrag/prompt_tune/generator/entity_summarization_prompt.py

## Overview

Entity summarization prompt generator.

Purpose
This module provides utilities to produce a prompt for entity summarization by formatting
a template with a given persona and language, and optionally persisting the result to disk.

Exports
- create_entity_summarization_prompt(persona: str, language: str, output_path: Path | None = None) -&gt; str
  Generate the prompt by formatting ENTITY_SUMMARIZATION_PROMPT and, if output_path is supplied,
  write the prompt to a file named summarize_descriptions.txt within output_path, creating any
  missing directories.
- ENTITY_SUMMARIZATION_FILENAME: The filename used when writing the prompt to disk ("summarize_descriptions.txt").

Summary
The create_entity_summarization_prompt function formats the imported ENTITY_SUMMARIZATION_PROMPT using the
provided persona and language. If an output_path is provided, the function writes the resulting prompt
to a file named summarize_descriptions.txt inside that directory, ensuring directories exist.

## Functions

- [`create_entity_summarization_prompt`](../api/functions/graphrag-prompt-tune-generator-entity-summarization-prompt-create-entity-summarization-prompt)

