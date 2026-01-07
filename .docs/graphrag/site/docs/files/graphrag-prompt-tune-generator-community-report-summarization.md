---
sidebar_position: 171
---

# graphrag/prompt_tune/generator/community_report_summarization.py

## Overview

Utilities for generating and persisting prompts used in community report summarization.

Purpose:
Provide a simple interface to construct a prompt for community report summarization using a predefined template and to optionally write the resulting prompt to a file using the standard filename.

Key exports:
- create_community_summarization_prompt(persona: str, role: str, report_rating_description: str, language: str, output_path: Path | None = None) -&gt; str: Creates the prompt for community summarization. If output_path is provided, writes the prompt to a file at that location using COMMUNITY_SUMMARIZATION_FILENAME.
- COMMUNITY_SUMMARIZATION_FILENAME: str constant with the value "community_report_graph.txt"

Brief summary:
This module exposes a single entry point to generate a parameterized community summarization prompt and optionally persist it to disk.

## Functions

- [`create_community_summarization_prompt`](../api/functions/graphrag-prompt-tune-generator-community-report-summarization-create-community-summarization-prompt)

