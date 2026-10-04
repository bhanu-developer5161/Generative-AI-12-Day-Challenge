from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "Python is easy to learn",
    "Python is powerful",
    "I love learning Python"
]

vectorizer = TfidfVectorizer()

tfidf = vectorizer.fit_transform(documents)

print("Vocabulary:")
print(vectorizer.get_feature_names_out())

print("\nTF-IDF Matrix:")
print(tfidf.toarray())