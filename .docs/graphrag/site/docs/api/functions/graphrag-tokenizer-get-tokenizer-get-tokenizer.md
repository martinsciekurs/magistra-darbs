---
sidebar_position: 396
---

# get_tokenizer

**File:** `graphrag/tokenizer/get_tokenizer.py` (lines 13-41)

## Signature

```python
def get_tokenizer(
    model_config: LanguageModelConfig | None = None,
    encoding_model: str = ENCODING_MODEL,
) -> Tokenizer
```

## Description

Get the tokenizer for the given model configuration or fallback to a tiktoken based tokenizer.

Args:
    model_config: LanguageModelConfig | None, optional
        The model configuration. If not provided or model_config.encoding_model is manually set,
        use a tiktoken based tokenizer. Otherwise, use a LitellmTokenizer based on the model name.
        LiteLLM supports token encoding/decoding for the range of models it supports.
    encoding_model: str, optional
        A tiktoken encoding model to use if no model configuration is provided. Only used if a
        model configuration is not provided.

Returns:
    Tokenizer: An instance of a Tokenizer.

Raises:
    None

## Dependencies

This function calls:

- `graphrag/tokenizer/litellm_tokenizer.py::LitellmTokenizer`
- `graphrag/tokenizer/tiktoken_tokenizer.py::TiktokenTokenizer`

## Called By

This function is called by:

- `graphrag/api/prompt_tune.py::generate_indexing_prompts`
- `graphrag/index/operations/embed_text/strategies/openai.py::_get_splitter`
- `graphrag/index/operations/summarize_descriptions/description_summary_extractor.py::SummarizeExtractor.__init__`
- `graphrag/index/text_splitting/text_splitting.py::TokenTextSplitter.__init__`
- `graphrag/index/workflows/create_community_reports.py::create_community_reports`
- `graphrag/index/workflows/create_community_reports_text.py::create_community_reports_text`
- `graphrag/prompt_tune/generator/extract_graph_prompt.py::create_extract_graph_prompt`
- `graphrag/query/context_builder/community_context.py::build_community_context`
- `graphrag/query/context_builder/conversation_history.py::ConversationHistory.build_context`
- `graphrag/query/context_builder/local_context.py::build_entity_context`
- `graphrag/query/context_builder/local_context.py::build_covariates_context`
- `graphrag/query/context_builder/local_context.py::build_relationship_context`
- `graphrag/query/context_builder/source_context.py::build_text_unit_context`
- `graphrag/query/factory.py::get_local_search_engine`
- `graphrag/query/factory.py::get_global_search_engine`
- `graphrag/query/factory.py::get_drift_search_engine`
- `graphrag/query/factory.py::get_basic_search_engine`
- `graphrag/query/llm/text_utils.py::chunk_text`
- `graphrag/query/question_gen/base.py::BaseQuestionGen.__init__`
- `graphrag/query/structured_search/base.py::BaseSearch.__init__`
- `graphrag/query/structured_search/basic_search/basic_context.py::BasicSearchContext.__init__`
- `graphrag/query/structured_search/drift_search/drift_context.py::DRIFTSearchContextBuilder.__init__`
- `graphrag/query/structured_search/drift_search/primer.py::PrimerQueryProcessor.__init__`
- `graphrag/query/structured_search/drift_search/primer.py::DRIFTPrimer.__init__`
- `graphrag/query/structured_search/drift_search/search.py::DRIFTSearch.__init__`
- `graphrag/query/structured_search/global_search/community_context.py::GlobalCommunityContext.__init__`
- `graphrag/query/structured_search/local_search/mixed_context.py::LocalSearchMixedContext.__init__`
- `tests/unit/indexing/graph/extractors/community_reports/test_sort_context.py::test_sort_context`
- `tests/unit/indexing/graph/extractors/community_reports/test_sort_context.py::test_sort_context_max_tokens`
- `tests/unit/utils/test_encoding.py::test_encode_basic`
- `tests/unit/utils/test_encoding.py::test_num_tokens_empty_input`

