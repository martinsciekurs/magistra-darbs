---
sidebar_position: 150
---

# _generate_report

**File:** `graphrag/index/operations/summarize_communities/summarize_communities.py` (lines 97-114)

## Signature

```python
def _generate_report(
    runner: CommunityReportsStrategy,
    callbacks: WorkflowCallbacks,
    cache: PipelineCache,
    strategy: dict,
    community_id: int,
    community_level: int,
    community_context: str,
) -> CommunityReport | None
```

## Description

Generate a report for a single community.

Args:
  runner: The strategy function used to generate the report for the community.
  callbacks: Callbacks to use during report generation.
  cache: Cache instance used by the report generation process.
  strategy: Strategy configuration for the report generation.
  community_id: Identifier of the community for which to generate the report.
  community_level: Level of the community.
  community_context: Context string describing the community.
Returns:
  CommunityReport | None
      The generated CommunityReport, or None if no report was produced.
Raises:
  Exception: Propagates exceptions raised by the underlying runner.

## Called By

This function is called by:

- `graphrag/index/operations/summarize_communities/summarize_communities.py::run_generate`

