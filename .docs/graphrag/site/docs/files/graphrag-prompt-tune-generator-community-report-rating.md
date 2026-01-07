---
sidebar_position: 170
---

# graphrag/prompt_tune/generator/community_report_rating.py

## Overview

Module to generate prompts for community report ratings using a language model.

This module exposes generate_community_report_rating, which constructs a rating description for a community report by rendering the GENERATE_REPORT_RATING_PROMPT template and invoking a ChatModel. The rating is contextualized by the target domain, the intended persona, and optional documentation context provided via docs.

Key exports:
- generate_community_report_rating(model: ChatModel, domain: str, persona: str, docs: str | list[str]) -&gt; str

Overview:
- The function accepts a language model instance, a domain, a persona, and docs (a string or a list of strings). It uses the GENERATE_REPORT_RATING_PROMPT template to assemble a prompt and queries the model, returning the generated rating description as a string.

Notes:
- GENERATE_REPORT_RATING_PROMPT is a prompt template used to guide the model. The function handles prompt construction and model invocation; no internal implementation details are exposed here.
- Input validation and error handling are performed by the function: TypeError for invalid argument types, ValueError for empty or invalid docs, and RuntimeError for failures when communicating with the model.

## Functions

- [`generate_community_report_rating`](../api/functions/graphrag-prompt-tune-generator-community-report-rating-generate-community-report-rating)

