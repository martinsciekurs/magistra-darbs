---
sidebar_position: 329
---

# build_community_context

**File:** `graphrag/query/context_builder/community_context.py` (lines 24-186)

## Signature

```python
def build_community_context(
    community_reports: list[CommunityReport],
    entities: list[Entity] | None = None,
    tokenizer: Tokenizer | None = None,
    use_community_summary: bool = True,
    column_delimiter: str = "|",
    shuffle_data: bool = True,
    include_community_rank: bool = False,
    min_community_rank: int = 0,
    community_rank_name: str = "rank",
    include_community_weight: bool = True,
    community_weight_name: str = "occurrence weight",
    normalize_community_weight: bool = True,
    max_context_tokens: int = 8000,
    single_batch: bool = True,
    context_name: str = "Reports",
    random_state: int = 86,
) -> tuple[str | list[str], dict[str, pd.DataFrame]]
```

## Description

Build context data from community reports for use in a system prompt.

If entities are provided, compute per-community weights from the number of text units associated with entities within each community. The computed weight is added to each CommunityReport's attributes and included in the context data table.

Args:
- community_reports (list[CommunityReport]): Reports representing each community to be included in the context.
- entities (list[Entity] | None): Optional entities used to derive weights by counting text units linked to each community.
- tokenizer (Tokenizer | None): Tokenizer to use for estimating token counts. If None, a default tokenizer is obtained.
- use_community_summary (bool): If True, include report.summary in the context line; otherwise include report.full_content.
- column_delimiter (str): Delimiter used to join fields when constructing per-report context lines.
- shuffle_data (bool): If True, shuffle the selected reports before batching.
- include_community_rank (bool): If True, append a rank value to each line and include a rank column in the header.
- min_community_rank (int): Minimum rank for a report to be included.
- community_rank_name (str): Header name for the rank column when included.
- include_community_weight (bool): If True, include a weight column (occurrence weight) for each report.
- community_weight_name (str): Attribute name used to store the weight on each report.
- normalize_community_weight (bool): If True, apply normalization to computed weights.
- max_context_tokens (int): Maximum token budget per batch; when exceeded, a new batch is started.
- single_batch (bool): If True, produce a single batch; otherwise accumulate multiple batches up to the token limit.
- context_name (str): Name used as the batch header for the context section.
- random_state (int): Seed for deterministic shuffling when shuffle_data is True.

Returns:
- tuple[str | list[str], dict[str, pd.DataFrame]]: A pair containing the generated context text(s) and a mapping from the lower-cased context name to a pandas DataFrame with the compiled context records. The first element is either a single string or a list of strings representing the context segments produced; the second element is a dictionary like &#123;"reports": &lt;DataFrame&gt;&#125; containing the concatenated context data.

Raises:
- May raise exceptions from the underlying tokenizer, pandas operations, or user-provided data models if inputs are invalid or internal processing fails.

Notes:
- When no reports pass the inclusion filter, an empty context is returned as ([], &#123;&#125;).
- The function is designed to support batching for large contexts and to prefer deterministic outputs when a random_state is provided.

## Dependencies

This function calls:

- `graphrag/query/context_builder/community_context.py::_compute_community_weights`
- `graphrag/query/context_builder/community_context.py::_cut_batch`
- `graphrag/query/context_builder/community_context.py::_get_header`
- `graphrag/query/context_builder/community_context.py::_init_batch`
- `graphrag/query/context_builder/community_context.py::_is_included`
- `graphrag/query/context_builder/community_context.py::_report_context_text`
- `graphrag/tokenizer/get_tokenizer.py::get_tokenizer`

## Called By

This function is called by:

- `graphrag/query/structured_search/global_search/community_context.py::GlobalCommunityContext.build_context`
- `graphrag/query/structured_search/local_search/mixed_context.py::LocalSearchMixedContext._build_community_context`

