import nltk
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

text = """
Python is a powerful programming language.
Python is easy to learn and Python is popular.
I am learning Python for Generative AI.
"""

# 1. Tokenization
words = text.lower().split()

print("Original Words:")
print(words)

# 2. Remove stopwords
stop_words = set(stopwords.words("english"))

filtered_words = [
    word.strip(".,!?")
    for word in words
    if word.strip(".,!?") not in stop_words
]

print("\nAfter Stopword Removal:")
print(filtered_words)

# 3. Word Frequency
frequency = Counter(filtered_words)

print("\nWord Frequency:")
print(frequency)

# 4. Lemmatization
lemmatizer = WordNetLemmatizer()

lemmatized_words = [
    lemmatizer.lemmatize(word)
    for word in filtered_words
]

print("\nLemmatized Words:")
print(lemmatized_words)

# 5. Most Common Words
print("\nTop 5 Most Common Words:")
print(frequency.most_common(5))