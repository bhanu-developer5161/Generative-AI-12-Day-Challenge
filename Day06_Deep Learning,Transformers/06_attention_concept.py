# Day 06 - Attention Concept

words = ["student", "studied", "she"]

# Illustrative attention scores for the word "she"
scores = [0.7, 0.2, 0.1]

print("Words:", words)
print("Attention Weights:", scores)

for word, weight in zip(words, scores):
    print(f"{word}: {weight * 100:.0f}%")