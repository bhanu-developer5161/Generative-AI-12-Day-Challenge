
role = "Act as a Python tutor."
task = "Explain Python functions."
context = "I am a beginner learning Python."
constraints = "Use simple language and stay under 150 words."
output_format = "Use bullet points and include one code example."

prompt = f"""
Role: {role}
Task: {task}
Context: {context}
Constraints: {constraints}
Output Format: {output_format}
"""

print(prompt)