---
sidebar_position: 178
---

# graphrag/prompt_tune/generator/language.py

## Overview

Language detection utility for GraphRAG prompt tuning. This module provides a small utility to detect the language of input documentation so GraphRAG prompts can be generated in the appropriate language. The detection is performed by issuing DETECT_LANGUAGE_PROMPT to the supplied ChatModel.

Exports:
- detect_language(model, docs)

Brief summary:
The detect_language function accepts a model and docs (string or list[str]), uses the model to determine the language, and returns the language as a string. It may raise Exception if the underlying model API raises an error during language detection.

## Functions

- [`detect_language`](../api/functions/graphrag-prompt-tune-generator-language-detect-language)

