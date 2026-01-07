---
sidebar_position: 220
---

# graphrag/tokenizer/get_tokenizer.py

## Overview

Tokenizer factory for GraphRag.

Summary
Provide a factory function get_tokenizer that returns a Tokenizer instance appropriate for the given LanguageModelConfig, or falls back to a tiktoken-based tokenizer using ENCODING_MODEL as default.

Exports
- get_tokenizer(model_config: LanguageModelConfig | None = None, encoding_model: str = ENCODING_MODEL) -&gt; Tokenizer
  Factory function to obtain a Tokenizer depending on the provided model_config and encoding_model.

Details
This module selects between LitellmTokenizer and TiktokenTokenizer based on the provided configuration. If no model_config is provided, or if the LanguageModelConfig indicates that encoding_model has been manually set/overridden, a TiktokenTokenizer is used with the specified encoding_model. Otherwise, a LitellmTokenizer is created that relies on the model name included in the LanguageModelConfig.

Parameters
- model_config: LanguageModelConfig | None
  The model configuration. If None, a tiktoken-based tokenizer is used.
- encoding_model: str
  The encoding model name used for the tiktoken-based tokenizer. Defaults to ENCODING_MODEL.

Returns
- Tokenizer
  An instance of TiktokenTokenizer or LitellmTokenizer as determined by the input configuration.

Raises
- TypeError
  If model_config is provided and is not an instance of LanguageModelConfig.
- ValueError
  If encoding_model is empty or invalid, or the combination of inputs is unsupported.

## Functions

- [`get_tokenizer`](../api/functions/graphrag-tokenizer-get-tokenizer-get-tokenizer)

