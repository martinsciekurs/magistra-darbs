---
sidebar_position: 296
---

# unified-search-app/app/ui/sidebar.py

## Overview

UI sidebar utilities for the unified search app.

Overview
Provides the Streamlit sidebar panel and a set of session-state helpers used to configure the dataset, the number of suggested questions, and which search modes are active. Functions operate on a SessionVariables container (sv) to read and update relevant UI state.

Exports
- update_basic_rag(sv: SessionVariables) -&gt; None
- reset_app() -&gt; None
- update_global_search(sv: SessionVariables) -&gt; None
- lookup_label(key: str, sv: SessionVariables) -&gt; str
- update_drift_search(sv: SessionVariables) -&gt; None
- update_local_search(sv: SessionVariables) -&gt; None
- create_side_bar(sv: SessionVariables) -&gt; None
- update_dataset(sv: SessionVariables) -&gt; None

Notes
- lookup_label uses dataset_name(key, sv) to resolve a user-facing label for a given dataset key.
- update_dataset clears the Streamlit cache via st.cache_data to reflect the newly selected dataset and reinitialize related UI state.
- Flags stored on sv include sv.include_basic_rag, sv.include_global_search, sv.include_drift_search, and sv.include_local_search.

## Functions

- [`update_basic_rag`](../api/functions/unified-search-app-app-ui-sidebar-update-basic-rag)
- [`reset_app`](../api/functions/unified-search-app-app-ui-sidebar-reset-app)
- [`update_global_search`](../api/functions/unified-search-app-app-ui-sidebar-update-global-search)
- [`lookup_label`](../api/functions/unified-search-app-app-ui-sidebar-lookup-label)
- [`update_drift_search`](../api/functions/unified-search-app-app-ui-sidebar-update-drift-search)
- [`update_local_search`](../api/functions/unified-search-app-app-ui-sidebar-update-local-search)
- [`create_side_bar`](../api/functions/unified-search-app-app-ui-sidebar-create-side-bar)
- [`update_dataset`](../api/functions/unified-search-app-app-ui-sidebar-update-dataset)

