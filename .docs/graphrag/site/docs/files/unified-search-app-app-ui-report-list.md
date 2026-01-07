---
sidebar_position: 294
---

# unified-search-app/app/ui/report_list.py

## Overview

Module for rendering and managing the report list UI in the unified search app.

Purpose:
This module renders the report list using Streamlit and updates the selected report in the session state via the SessionVariables data model.

Imports:
This module uses Streamlit (st) and SessionVariables from state.session_variables.

Key exports:
- create_report_list_ui(sv: SessionVariables): Renders the report list UI and updates the selected report in the session state based on user selection. Returns None.

Brief summary:
Provides the single interface to display available community reports and handle user-driven changes to the selected report, integrating with the session state.

## Functions

- [`create_report_list_ui`](../api/functions/unified-search-app-app-ui-report-list-create-report-list-ui)

