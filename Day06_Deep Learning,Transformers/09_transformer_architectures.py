architectures = {
    "BERT": "Encoder-only",
    "GPT": "Decoder-only",
    "T5": "Encoder-decoder"
}

for model, architecture in architectures.items():
    print(f"{model}: {architecture}")

print("\nExample use cases:")
print("BERT: Text classification")
print("GPT: Text generation")
print("T5: Text summarization")