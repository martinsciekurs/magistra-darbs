---
sidebar_position: 184
---

# graphrag/query/context_builder/conversation_history.py

## Overview

Module for constructing and manipulating conversation histories for QA prompts in GraphRag.

Purpose
This module defines data structures and helpers to manage a conversation history as a sequence of turns and to convert that history into QA-turns suitable for downstream processing, as well as to build a context payload for system prompts. It relies on role constants (SYSTEM, USER, ASSISTANT) and tokenizer facilities when constructing context.

Key exports
- SYSTEM, USER, ASSISTANT: strings representing the three roles
- QATurn: dataclass representing a single QA turn with user_query and optional assistant_answers
- ConversationHistory: helper for storing and manipulating an ordered list of turns and providing conversion utilities
- ConversationTurn: representation of a single turn with a role and content
- ConversationRole: enum for SYSTEM, USER, ASSISTANT with helper constructors

Brief usage summary
- Create a ConversationHistory, add_turn for roles, and call to_qa_turns to obtain QA turns.
- Use from_list to build a history from a plain list of &#123;"role": ..., "content": ...&#125; dictionaries.
- Build a prompt context with build_context, optionally restricting to user turns and limiting tokens.

Notes
- ConversationRole.from_string(value) converts a string like "system", "user", or "assistant" to the corresponding enum member and raises ValueError for invalid values.
- QATurn.get_answer_text concatenates assistant_answers with newline separators when available.

## Classes

- [`QATurn`](../api/classes/graphrag-query-context-builder-conversation-history-qaturn)
- [`ConversationHistory`](../api/classes/graphrag-query-context-builder-conversation-history-conversationhistory)
- [`ConversationTurn`](../api/classes/graphrag-query-context-builder-conversation-history-conversationturn)
- [`ConversationRole`](../api/classes/graphrag-query-context-builder-conversation-history-conversationrole)

## Functions

- [`get_answer_text`](../api/functions/graphrag-query-context-builder-conversation-history-get-answer-text)
- [`to_qa_turns`](../api/functions/graphrag-query-context-builder-conversation-history-to-qa-turns)
- [`from_list`](../api/functions/graphrag-query-context-builder-conversation-history-from-list)
- [`__init__`](../api/functions/graphrag-query-context-builder-conversation-history-init)
- [`__str__`](../api/functions/graphrag-query-context-builder-conversation-history-str)
- [`add_turn`](../api/functions/graphrag-query-context-builder-conversation-history-add-turn)
- [`__str__`](../api/functions/graphrag-query-context-builder-conversation-history-str)
- [`from_string`](../api/functions/graphrag-query-context-builder-conversation-history-from-string)
- [`__str__`](../api/functions/graphrag-query-context-builder-conversation-history-str)
- [`get_user_turns`](../api/functions/graphrag-query-context-builder-conversation-history-get-user-turns)
- [`build_context`](../api/functions/graphrag-query-context-builder-conversation-history-build-context)

