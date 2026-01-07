---
sidebar_position: 262
---

# tests/unit/litellm_services/utils.py

## Overview

Time-based value validation helpers used in litellm services tests.

This module provides small utilities to validate and bin time-based test data,
specifically for enforcing minimum gaps between consecutive times, binning
time values into fixed-size intervals, and ensuring per-period value limits.

Exports:
    - assert_stagger(time_values: list[float], stagger: float)
        Assert that consecutive time values are at least the specified stagger apart.
        Raises AssertionError if any consecutive pair is closer than stagger.
    - bin_time_intervals(time_values: list[float], time_interval: int) -&gt; list[list[float]]
        Bin time values into consecutive time-based intervals. Returns a list of bins.
    - assert_max_num_values_per_period(periods: list[list[float]], max_values_per_period: int)
        Assert the maximum number of values per period. Raises AssertionError if any period
        contains more values than max_values_per_period.

## Functions

- [`assert_stagger`](../api/functions/tests-unit-litellm-services-utils-assert-stagger)
- [`bin_time_intervals`](../api/functions/tests-unit-litellm-services-utils-bin-time-intervals)
- [`assert_max_num_values_per_period`](../api/functions/tests-unit-litellm-services-utils-assert-max-num-values-per-period)

