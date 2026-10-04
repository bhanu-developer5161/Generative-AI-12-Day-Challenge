from sklearn.feature_extraction.text import CountVectorizer

sentences = [
    "I like Python",
    "I like AI",
    "Python is powerful"
]

vectorizer = CountVectorizer()

bow = vectorizer.fit_transform(sentences)

print("Vocabulary:")
print(vectorizer.get_feature_names_out())

print("\nBag of Words:")
print(bow.toarray())