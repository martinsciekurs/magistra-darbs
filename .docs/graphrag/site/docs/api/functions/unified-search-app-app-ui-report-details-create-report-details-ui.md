---
sidebar_position: 624
---

# create_report_details_ui

**File:** `unified-search-app/app/ui/report_details.py` (lines 18-98)

## Signature

```python
def create_report_details_ui(sv: SessionVariables)
```

## Description

Render the report details UI for the currently selected report using Streamlit; this function does not return a value.

It loads the selected report JSON from sv.selected_report.value.full_content_json and renders the report title, summary, priority, and explanation, collecting citations for entities and relationships to highlight in the graph.

If no report is selected, it writes No report selected to the UI.

Notes:
- JSONDecodeError is caught locally; in case of invalid JSON, error messages and the raw JSON content are written to the UI.
- Missing keys in the loaded JSON may raise KeyError since the code directly accesses required fields such as title, summary, rating, rating explanation, and findings.
- The function handles findings as a list or as a string; it gathers citations and renders hyperlinks accordingly.
- The UI text is post-processed to replace internal tokens for display friendliness and then rendered via Markdown; finally, a graph citation visualization is shown for the selected entities and relationships.

## Example 💡 Generated

```python
from ui_components import create_report_details_ui
from types import SimpleNamespace
sv = SimpleNamespace()
sv.selected_report = SimpleNamespace(value=None)
sv.entities = SimpleNamespace(value=None)
sv.relationships = SimpleNamespace(value=None)
create_report_details_ui(sv)  # Expected: No report selected
```

