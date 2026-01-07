---
sidebar_position: 321
---

# _report_context_text

**File:** `graphrag/query/context_builder/community_context.py` (lines 65-80)

## Signature

```python
def _report_context_text(
        report: CommunityReport, attributes: list[str]
    ) -> tuple[str, list[str]]
```

## Description

Builds a single-line context text for a CommunityReport using the given attributes.

This helper relies on global flags to determine content and formatting:
- use_community_summary: if True, include report.summary; otherwise include report.full_content.
- include_community_rank: if True, append the report.rank to the line.
- column_delimiter: string used to join fields into the line.

Args:
- report (CommunityReport): The report to extract data from.
- attributes (list[str]): Attribute field names to include from report.attributes (in order).

Returns:
- tuple[str, list[str]]: A pair where the first element is the single-line text (with a trailing newline) formed by joining the context fields with column_delimiter, and the second element is the raw list of context fields used to build that line.

Notes:
- report.short_id is included as "" when missing.
- report.title is included as a string; if it can be None, behavior is undefined.
- For each field in attributes, the value is str(report.attributes.get(field, "")) if report.attributes is not None; otherwise "".
- If include_community_rank is True, report.rank is appended as a string.

## Example 💡 Generated

```python
from module import _report_context_text
import module as mod
r = type("R", (), {})()
r.short_id = "C-123"; r.title = "Ex"
r.attributes = {"a":"A"}; r.summary = "S"; r.rank = 5
mod.use_community_summary = True
mod.include_community_rank = True
mod.column_delimiter = " | "
txt, ctx = _report_context_text(r, ["a"])
print(txt)
print(ctx)
```

## Called By

This function is called by:

- `graphrag/query/context_builder/community_context.py::build_community_context`

