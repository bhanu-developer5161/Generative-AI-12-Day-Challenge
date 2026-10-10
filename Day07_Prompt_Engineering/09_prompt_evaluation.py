
original_prompt = "Explain Python."

improved_prompt = """
Explain Python to a complete beginner.
Use exactly three bullet points.
Include one simple code example.
Use clear, easy-to-understand language.
"""

evaluation_checklist = [
    "Is the answer accurate?",
    "Is it suitable for a beginner?",
    "Does it contain exactly three bullet points?",
    "Does it include a code example?"
]

print("Original Prompt:")
print(original_prompt)

print("\nImproved Prompt:")
print(improved_prompt)

print("\nEvaluation Checklist:")
for item in evaluation_checklist:
    print("-", item)