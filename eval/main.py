import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
api_key = os.getenv("KIMI_API_KEY")

llm = ChatOpenAI(model="kimi-k2-turbo-preview", api_key=api_key, base_url="https://api.moonshot.ai/v1")
messages = [
    ("system", "You are a helpful assistant that translates English to French. Translate the user sentence."),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)

print(ai_msg.text)
