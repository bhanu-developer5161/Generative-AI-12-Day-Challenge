from collections import Counter

text = """
Python is easy to learn.
Python is powerful and Python is popular.
"""

words = text.lower().split()

word_frequency = Counter(words)

print("Words:")
print(words)

print("\nWord Frequency:")
print(word_frequency)

print("\nMost Common Words:")
print(word_frequency.most_common(3))