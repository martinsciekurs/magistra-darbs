---
sidebar_position: 3
---

# generate_indexing_prompts

**File:** `graphrag/api/prompt_tune.py` (lines 56-202)

## Signature

```python
def generate_indexing_prompts(
    config: GraphRagConfig,
    chunk_size: PositiveInt = graphrag_config_defaults.chunks.size,
    overlap: Annotated[
        int, annotated_types.Gt(-1)
    ] = graphrag_config_defaults.chunks.overlap,
    limit: PositiveInt = 15,
    selection_method: DocSelectionType = DocSelectionType.RANDOM,
    domain: str | None = None,
    language: str | None = None,
    max_tokens: int = MAX_TOKEN_COUNT,
    discover_entity_types: bool = True,
    min_examples_required: PositiveInt = 2,
    n_subset_max: PositiveInt = 300,
    k: PositiveInt = 15,
    verbose: bool = False,
) -> tuple[str, str, str]
```

## Description

Generate indexing prompts.

Parameters
----------
config: GraphRagConfig
    The GraphRag configuration.
chunk_size: PositiveInt
    The chunk token size to use for input text units.
overlap: Annotated[int, annotated_types.Gt(-1)]
    The number of tokens to overlap between consecutive chunks (must be greater than -1).
limit: PositiveInt
    The limit of chunks to load.
selection_method: DocSelectionType
    The chunk selection method.
domain: str | None
    The domain to map the input documents to.
language: str | None
    The language to use for the prompts.
max_tokens: int
    The maximum number of tokens to use on entity extraction prompts.
discover_entity_types: bool
    Generate entity types.
min_examples_required: PositiveInt
    The minimum number of examples required for entity extraction prompts.
n_subset_max: PositiveInt
    The number of text chunks to embed when using auto selection method.
k: PositiveInt
    The number of documents to select when using auto selection method.
verbose: bool
    Whether to enable verbose logging.

Returns
-------
tuple[str, str, str]
    entity extraction prompt, entity summarization prompt, community summarization prompt

Raises
------
ValidationError
    If input arguments fail validation (thrown by pydantic’s validate_call).
RuntimeError
    If any underlying operation (loading docs, language model calls, or prompt generation steps) fails.

## Dependencies

This function calls:

- `graphrag/callbacks/noop_workflow_callbacks.py::NoopWorkflowCallbacks`
- `graphrag/language_model/manager.py::ModelManager`
- `graphrag/logger/standard_logging.py::init_loggers`
- `graphrag/prompt_tune/generator/community_report_rating.py::generate_community_report_rating`
- `graphrag/prompt_tune/generator/community_report_summarization.py::create_community_summarization_prompt`
- `graphrag/prompt_tune/generator/community_reporter_role.py::generate_community_reporter_role`
- `graphrag/prompt_tune/generator/domain.py::generate_domain`
- `graphrag/prompt_tune/generator/entity_relationship.py::generate_entity_relationship_examples`
- `graphrag/prompt_tune/generator/entity_summarization_prompt.py::create_entity_summarization_prompt`
- `graphrag/prompt_tune/generator/entity_types.py::generate_entity_types`
- `graphrag/prompt_tune/generator/extract_graph_prompt.py::create_extract_graph_prompt`
- `graphrag/prompt_tune/generator/language.py::detect_language`
- `graphrag/prompt_tune/generator/persona.py::generate_persona`
- `graphrag/prompt_tune/loader/input.py::load_docs_in_chunks`
- `graphrag/tokenizer/get_tokenizer.py::get_tokenizer`

