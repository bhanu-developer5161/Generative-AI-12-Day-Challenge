prompt = "Explain generative AI"

tokens = prompt.split()

print("User Prompt:", prompt)
print("Tokens:", tokens)
print("Token Count:", len(tokens))

print("\nSimplified next-token generation:")
generated_tokens = ["Generative", "AI", "creates", "new", "content"]

response = ""

for token in generated_tokens:
    response += token + " "
    print("Generated:", response.strip())

print("\nFinal Response:", response.strip())