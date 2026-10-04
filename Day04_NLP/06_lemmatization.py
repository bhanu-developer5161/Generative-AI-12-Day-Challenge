import nltk
from nltk.stem import WordNetLemmatizer

nltk.download("wordnet")
nltk.download("omw-1.4")

lemmatizer = WordNetLemmatizer()

words = [
    "playing",
    "played",
    "plays",
    "studies",
    "studying",
    "better"
]

print("Original Words:")
print(words)

print("\nLemmatized Words:")

for word in words:
    print(word, "->", lemmatizer.lemmatize(word))