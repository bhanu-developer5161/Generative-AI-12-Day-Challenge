
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI interview coach."),
    (
        "human",
        "Explain {topic} for a {level} learner. "
        "Give {points} key points."
    )
])

print("=== LangChain Prompt Builder ===")

topic = input("Enter a topic: ").strip()
level = input("Enter level (beginner/intermediate/advanced): ").strip().lower()
points_text = input("Number of key points (1-5): ").strip()

if not topic:
    print("Error: Topic cannot be empty.")
elif level not in {"beginner", "intermediate", "advanced"}:
    print("Error: Choose a valid learning level.")
elif not points_text.isdigit() or not 1 <= int(points_text) <= 5:
    print("Error: Enter a number from 1 to 5.")
else:
    messages = prompt.format_messages(
        topic=topic,
        level=level,
        points=int(points_text)
    )

    print("\n=== Formatted Messages ===")
    for message in messages:
        print(f"\nRole: {message.type}")
        print(f"Content: {message.content}")

    print("\nNo LLM was called; these are prepared messages.")