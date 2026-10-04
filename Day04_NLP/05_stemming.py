import nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = [
    "play",
    "playing",
    "played",
    "plays",
    "learning",
    "learned",
    "learns"
]

print("Original Words:")
print(words)

print("\nStemmed Words:")

for word in words:
    print(word, "->", stemmer.stem(word))