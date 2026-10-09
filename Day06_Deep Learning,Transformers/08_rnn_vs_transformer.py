sentence = "AI makes learning easier"
tokens = sentence.split()

print("Sentence:", sentence)
print("\nRNN-style sequential processing:")

for token in tokens:
    print("Processing:", token)

print("\nTransformer-style token access:")
print("Tokens available for attention:", tokens)