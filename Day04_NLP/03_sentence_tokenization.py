import nltk
from nltk.tokenize import sent_tokenize

nltk.download("punkt")
nltk.download("punkt_tab")

text = "I am learning Python. NLP is interesting. I want to build AI applications."

sentences = sent_tokenize(text)

print("Original Text:")
print(text)

print("\nSentence Tokens:")
print(sentences)

print("\nNumber of Sentences:")
print(len(sentences))