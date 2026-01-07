---
sidebar_position: 622
---

# create_full_graph_ui

**File:** `unified-search-app/app/ui/full_graph.py` (lines 12-56)

## Signature

```python
def create_full_graph_ui(sv: SessionVariables)
```

## Description

Create and render the full graph UI from the provided session variables.

Args:
    sv (SessionVariables): Container with entities, communities, and graph_community_level used to construct and filter the graph.

Returns:
    alt.Chart: The Altair chart object representing the full graph UI. The function also renders the chart via Streamlit.

