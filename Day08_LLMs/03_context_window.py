
prompt = "Explain Python"
conversation_history = [
    "What is a variable?",
    "Explain a Python loop.",
    "What is a function?"
]

print("Current Prompt:", prompt)
print("\nConversation History:")

for message in conversation_history:
    print("-", message)

print("\nTotal history messages:", len(conversation_history))
print("\nNote: Message count is not token count.")