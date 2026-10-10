
context = """
Course: Python Fundamentals
Duration: 6 weeks
Topics: Variables, loops, functions, lists
"""

question = "What is the course duration, and does it teach Django?"

prompt = f"""
Use only the information in the context below.

Context:
{context}

Question:
{question}

Constraints:
1. Do not invent missing information.
2. If the answer is not in the context, say "Not specified".
3. Keep the answer under 50 words.
"""

print("Grounded Prompt:")
print(prompt)