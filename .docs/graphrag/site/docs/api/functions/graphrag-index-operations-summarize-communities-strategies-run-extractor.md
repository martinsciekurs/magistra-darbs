---
sidebar_position: 147
---

# _run_extractor

**File:** `graphrag/index/operations/summarize_communities/strategies.py` (lines 46-85)

## Signature

```python
def _run_extractor(
    model: ChatModel,
    community: str | int,
    input: str,
    level: int,
    args: StrategyConfig,
) -> CommunityReport | None
```

## Description

Run the CommunityReportsExtractor to produce a CommunityReport from the given input.

Args:
  model (ChatModel): The chat model instance used to perform extraction.
  community (str | int): Identifier for the community being processed.
  input (str): The input text to extract information from.
  level (int): The reporting level to assign to the resulting CommunityReport.
  args (StrategyConfig): Strategy configuration containing optional keys such as extraction_prompt and max_report_length.

Returns:
  CommunityReport | None: The constructed CommunityReport, or None if no structured report is produced or an error occurs during extraction.

## Dependencies

This function calls:

- `graphrag/index/operations/summarize_communities/community_reports_extractor.py::CommunityReportsExtractor`
- `graphrag/index/operations/summarize_communities/typing.py::CommunityReport`
- `graphrag/index/operations/summarize_communities/typing.py::Finding`

## Called By

This function is called by:

- `graphrag/index/operations/summarize_communities/strategies.py::run_graph_intelligence`

