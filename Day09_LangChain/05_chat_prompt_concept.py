
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful Python tutor."),
    ("human", "Explain {topic} in simple language.")
])

messages = prompt.format_messages(
    topic="Large Language Models"
)

print("=== Chat Prompt Template ===")

for message in messages:
    print(f"\nRole: {message.type}")
    print(f"Content: {message.content}")

print("\nNote: No LLM was called.")