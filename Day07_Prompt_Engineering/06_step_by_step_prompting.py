
role = "Act as a Python project mentor."

task = "Help me build a student marks analyzer."

steps = """
1. Identify the project requirements.
2. Suggest a simple project structure.
3. Write the Python code.
4. Explain how to run the code.
5. Suggest test cases.
"""

prompt = f"""
Role: {role}
Task: {task}

Follow these steps in order:
{steps}

Explain each step in beginner-friendly language.
"""

print("Step-by-Step Prompt:")
print(prompt)