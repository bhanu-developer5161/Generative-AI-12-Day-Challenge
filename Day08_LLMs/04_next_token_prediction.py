
text = "Python is a"

# Illustrative next-token predictions, not from a real LLM
possible_next_tokens = [
    "programming",
    "popular",
    "powerful"
]

print("Existing Text:", text)
print("\nIllustrative Possible Next Tokens:")

for token in possible_next_tokens:
    print("-", token)

predicted_token = possible_next_tokens[0]
generated_text = text + " " + predicted_token

print("\nExample Generated Text:", generated_text)
print("\nNote: These predictions are predefined examples,")
print("not predictions from a trained language model.")