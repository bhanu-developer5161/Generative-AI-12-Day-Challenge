
task = "Classify the following review as Positive or Negative."
review = "The Python course was excellent and easy to understand."

prompt = f"""
{task}
Review: "{review}"
Return only the label.
"""

print("Zero-Shot Prompt:")
print(prompt)