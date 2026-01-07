---
sidebar_position: 108
---

# graphrag/index/utils/dataframes.py

## Overview

Utilities for common pandas DataFrame operations used by Graphrag index utilities.

This module provides a collection of lightweight helpers to manipulate DataFrames
and Series, including unions, column selection and dropping, joins, anti-joins,
transforms, and conditional filtering.

Key exports:
- union(*frames: pd.DataFrame) -&gt; pd.DataFrame: Perform a union operation on the given set of dataframes.
- select(df: pd.DataFrame, *columns: str) -&gt; pd.DataFrame: Select columns from a DataFrame.
- drop_columns(df: pd.DataFrame, *column: str) -&gt; pd.DataFrame: Drop specified columns from a DataFrame.
- join(left: pd.DataFrame, right: pd.DataFrame, key: str, strategy: MergeHow = "left") -&gt; pd.DataFrame: Perform a table join.
- transform_series(series: pd.Series, fn: Callable[[Any], Any]) -&gt; pd.Series: Apply a transformation function to a Pandas Series.
- antijoin(df: pd.DataFrame, exclude: pd.DataFrame, column: str) -&gt; pd.DataFrame: Return an anti-joined dataframe.
- where_column_equals(df: pd.DataFrame, column: str, value: Any) -&gt; pd.DataFrame: Return a filtered DataFrame where a column equals a value.

## Functions

- [`union`](../api/functions/graphrag-index-utils-dataframes-union)
- [`select`](../api/functions/graphrag-index-utils-dataframes-select)
- [`drop_columns`](../api/functions/graphrag-index-utils-dataframes-drop-columns)
- [`join`](../api/functions/graphrag-index-utils-dataframes-join)
- [`transform_series`](../api/functions/graphrag-index-utils-dataframes-transform-series)
- [`antijoin`](../api/functions/graphrag-index-utils-dataframes-antijoin)
- [`where_column_equals`](../api/functions/graphrag-index-utils-dataframes-where-column-equals)

