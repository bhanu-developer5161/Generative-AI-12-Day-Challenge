import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

text = "I am learning Python and I am building Generative AI applications"

words = text.split()

stop_words = set(stopwords.words("english"))

filtered_words = [
    word for word in words
    if word.lower() not in stop_words
]

print("Original Words:")
print(words)

print("\nStopwords:")
print([word for word in words if word.lower() in stop_words])

print("\nAfter Removing Stopwords:")
print(filtered_words)