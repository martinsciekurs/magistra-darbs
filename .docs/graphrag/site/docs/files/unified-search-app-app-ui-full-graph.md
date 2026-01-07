---
sidebar_position: 291
---

# unified-search-app/app/ui/full_graph.py

## Overview

Full graph UI for the Unified Search app.

This module provides the UI components used to render the complete graph visualization based on the current session state. It relies on Altair for chart construction, Pandas for data handling, and Streamlit for rendering in the app. The primary entry point is create_full_graph_ui, which builds and renders the chart using the provided SessionVariables.

Public API:
    create_full_graph_ui(sv: SessionVariables)

Args:
    sv (SessionVariables): Container with entities, communities, and graph_community_level used to construct and filter the graph.

Returns:
    alt.Chart: The Altair chart object representing the full graph UI. The function also renders the chart via Streamlit.

## Functions

- [`create_full_graph_ui`](../api/functions/unified-search-app-app-ui-full-graph-create-full-graph-ui)

