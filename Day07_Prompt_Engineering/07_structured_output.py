
task = "Describe a Python course."

output_format = """
Return the information in JSON format with these keys:
- course_name
- language
- difficulty
- duration_weeks
"""

prompt = f"""
Task: {task}

Output requirements:
{output_format}

Return valid JSON only.
"""

print("Structured Output Prompt:")
print(prompt)