
role = "Act as an experienced Python interview coach."
task = "Explain the difference between a list and a tuple."
audience = "A beginner preparing for a fresher interview."
formatting = "Use a comparison table and one short code example."

prompt = f"""
Role: {role}
Task: {task}
Audience: {audience}
Output requirements: {formatting}
"""

print("Role-Based Prompt:")
print(prompt)