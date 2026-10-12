
# Day 09: Introduction to LangChain

user_question = "What is Generative AI?"

prompt_template = """
You are a helpful AI tutor.
Explain the following topic to a beginner:

Topic: {question}
"""

prompt = prompt_template.format(question=user_question)

print("=== LangChain Workflow Concept ===")
print("\n1. User Question:")
print(user_question)

print("\n2. Formatted Prompt:")
print(prompt)

print("\n3. Next Step:")
print("Send the prompt to a language model.")

print("\nNote: This is a plain Python demonstration.")
print("It does not call LangChain or a real AI model yet.")