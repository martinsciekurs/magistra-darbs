---
sidebar_position: 562
---

# test_encode_basic

**File:** `tests/unit/utils/test_encoding.py` (lines 7-11)

## Signature

```python
def test_encode_basic()
```

## Description

Get a tokenizer configured for the provided model configuration or encoding model.

This function returns a Tokenizer suitable for the given model configuration or for the specified encoding model. If a model_config is not provided, or if model_config.encoding_model is explicitly set, a tiktoken-based tokenizer is returned using the encoding_model. If a model_config is provided and encoding_model is not set, a LitellmTokenizer is instantiated based on the model name found in the configuration.

Parameters:
- model_config (LanguageModelConfig | None): The model configuration to determine which tokenizer to instantiate. If None or if model_config.encoding_model is set, a tiktoken-based tokenizer is returned.
- encoding_model (str): The tiktoken encoding to use when falling back to a tiktoken-based tokenizer.

Returns:
- Tokenizer: The tokenizer instance configured for the provided model configuration or encoding model.

Raises:
- ValueError, TypeError: If the inputs are invalid or incompatible with the available tokenizers.

Examples:
    # Use tiktoken tokenizer with a specified encoding
    tokenizer = get_tokenizer(encoding_model="cl100k_base")
    tokens = tokenizer.encode("abc def")

    # Use LitellmTokenizer based on a model configuration
    cfg = LanguageModelConfig(name="my-model", encoding_model=None)
    tokenizer2 = get_tokenizer(model_config=cfg)
    tokens2 = tokenizer2.encode("hello world")

## Dependencies

This function calls:

- `graphrag/tokenizer/get_tokenizer.py::get_tokenizer`

