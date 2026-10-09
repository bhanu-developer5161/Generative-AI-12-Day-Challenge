sentence = "Generative AI is powerful"

tokens = sentence.split()

print("Original Sentence:", sentence)
print("Tokens:", tokens)
print("Number of Tokens:", len(tokens))

print("\nProcessing Tokens:")
for position, token in enumerate(tokens, start=1):
    print(f"Position {position}: {token}")