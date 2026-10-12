
from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template(
    "You are an AI tutor. Explain {topic} to a beginner in {style} style."
)

prompt = template.format(
    topic="Generative AI",
    style="simple"
)

print("=== Real LangChain Prompt Template ===")
print(prompt)