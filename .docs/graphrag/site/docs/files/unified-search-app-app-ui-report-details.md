---
sidebar_position: 293
---

# unified-search-app/app/ui/report_details.py

## Overview

Unified search report details UI module.

Purpose:
Provide UI components for rendering details of the currently selected report in the unified search app, using Streamlit. The module defines the main export create_report_details_ui, which loads the selected report JSON from sv.selected_report.value.full_content_json and renders the report title, summary, priority, and explanation. It also collects citations for entities and relationships to highlight in the graph, leveraging helpers such as display_graph_citations, format_response_hyperlinks, and get_ids_per_key. If no report is selected, it displays an appropriate message.

Key exports:
- create_report_details_ui(sv: SessionVariables) -&gt; None

Brief summary:
Exposes a function that renders the report details panel for the currently selected report and integrates with citation extraction utilities to support graph highlighting.

## Functions

- [`create_report_details_ui`](../api/functions/unified-search-app-app-ui-report-details-create-report-details-ui)

