---
sidebar_position: 112
---

# graphrag/index/utils/hashing.py

## Overview

Hashing utilities for generating deterministic SHA-512 digests from item fields.

Purpose:
Provide a simple utility to compute a SHA-512 digest by concatenating string representations of selected fields from a dictionary item, in a specified order.

Key exports:
- gen_sha512_hash(item: dict[str, Any], hashcode: Iterable[str]) -&gt; str

Brief summary:
The gen_sha512_hash function takes an input item and an iterable of keys (hashcode). It concatenates the string representations of the values item[k] for each key in hashcode, in order, then computes and returns the hexadecimal digest using SHA-512. If any key in hashcode is missing from the item, a KeyError will be raised by the function.

## Functions

- [`gen_sha512_hash`](../api/functions/graphrag-index-utils-hashing-gen-sha512-hash)

