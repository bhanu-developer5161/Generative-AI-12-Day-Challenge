
print("=== AI Prompt Assistant ===")

task = input("What task should the AI perform? ")
audience = input("Who is the target audience? ")
context = input("Enter any useful context: ")

role = "Act as a helpful AI assistant."
constraints = "Be accurate, clear, and do not invent missing information."
output_format = "Use numbered steps and include an example where useful."

prompt = f"""
ROLE:
{role}

TASK:
{task}

AUDIENCE:
{audience}

CONTEXT:
{context}

CONSTRAINTS:
{constraints}

OUTPUT FORMAT:
{output_format}
"""

print("\n=== Your Generated Prompt ===")
print(prompt)