#!/usr/bin/env python3
"""Test script to verify Langfuse integration is working."""

import os
from dotenv import load_dotenv
load_dotenv()

from docgen.llm.langfuse_client import is_langfuse_enabled, track_llm_generation, get_langfuse_client

def test_langfuse():
    """Test Langfuse connection and tracking."""
    print("Testing Langfuse integration...")
    print(f"LANGFUSE_PUBLIC_KEY: {'Set' if os.getenv('LANGFUSE_PUBLIC_KEY') else 'NOT SET'}")
    print(f"LANGFUSE_SECRET_KEY: {'Set' if os.getenv('LANGFUSE_SECRET_KEY') else 'NOT SET'}")
    print(f"LANGFUSE_HOST: {os.getenv('LANGFUSE_HOST', 'https://cloud.langfuse.com')}")
    print()
    
    if not is_langfuse_enabled():
        print("❌ Langfuse is NOT enabled. Check your .env file.")
        return False
    
    print("✓ Langfuse is enabled")
    
    # Test tracking a simple LLM call
    print("\nTesting LLM generation tracking...")
    gen_id = track_llm_generation(
        prompt="Test prompt: What is 2+2?",
        response="The answer is 4.",
        model="test-model",
        provider="test",
        token_usage={
            "prompt_tokens": 10,
            "completion_tokens": 5,
            "total_tokens": 15
        },
        generation_name="test_llm_call"
    )
    
    if gen_id:
        print(f"✓ LLM tracking succeeded! Generation ID: {gen_id}")
    else:
        print("❌ LLM tracking failed")
        return False
    
    # Flush and shutdown
    client = get_langfuse_client()
    if client:
        client.flush()
        # Give it a moment to send
        import time
        time.sleep(2)
        print("\n✓ Data flushed. Check your Langfuse dashboard!")
    
    return True

if __name__ == "__main__":
    success = test_langfuse()
    exit(0 if success else 1)



