---
sidebar_position: 107
---

# CommunityReport

**File:** `graphrag/data_model/community_report.py`

## Overview

Dataclass-based model representing a community report, storing identifiers, metadata, and content for a specific community. The class inherits from Named and acts as a lightweight data container with a convenient from_dict constructor.

Args:
- id (str): The report's identifier.
- title (str): The report title.
- community_id (str): The associated community's id.
- human_readable_id (Optional[str]): A short, human-friendly identifier.
- summary (Optional[str]): A brief summary of the report.
- full_content (Optional[str]): The full content of the report.
- rank (Optional[int]): The report's ranking or order.
- attributes (Optional[dict[str, Any]]): Additional arbitrary attributes.
- size (Optional[int]): A size-related metric.
- period (Optional[str]): The time period the report covers.

Returns:
- CommunityReport: A new CommunityReport instance.

Raises:
- ValueError: If required fields are missing or have invalid types.

From_dict:
- cls (type): The class used for construction (typically CommunityReport).
- d (dict[str, Any]): Source dictionary containing field values.
- id_key (str): Key in d for the report's identifier. Defaults to 'id'.
- title_key (str): Key in d for the report title. Defaults to 'title'.
- community_id_key (str): Key in d for the associated community's id. Defaults to 'community'.
- short_id_key (str): Key in d for the human-readable id. Defaults to 'human_readable_id'.
- summary_key (str): Key in d for the summary. Defaults to 'summary'.
- full_content_key (str): Key in d for the full content. Defaults to 'full_content'.
- rank_key (str): Key in d for the rank. Defaults to 'rank'.
- attributes_key (str): Key in d for additional attributes. Defaults to 'attributes'.
- size_key (str): Key in d for the size. Defaults to 'size'.
- period_key (str): Key in d for the period. Defaults to 'period'.

Returns:
- CommunityReport: A new instance constructed from d.

Raises:
- KeyError or ValueError: If required keys are missing or values are invalid.

## Methods

### `from_dict`

```python
def from_dict(
        cls,
        d: dict[str, Any],
        id_key: str = "id",
        title_key: str = "title",
        community_id_key: str = "community",
        short_id_key: str = "human_readable_id",
        summary_key: str = "summary",
        full_content_key: str = "full_content",
        rank_key: str = "rank",
        attributes_key: str = "attributes",
        size_key: str = "size",
        period_key: str = "period",
    ) -> "CommunityReport"
```

