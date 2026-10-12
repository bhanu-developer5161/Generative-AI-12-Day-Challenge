
from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template(
    "Explain {topic} to a {audience} using a {style} explanation."
)

examples = [
    {
        "topic": "Generative AI",
        "audience": "beginner",
        "style": "simple"
    },
    {
        "topic": "Neural Networks",
        "audience": "college student",
        "style": "technical"
    },
    {
        "topic": "RAG",
        "audience": "job interviewer",
        "style": "professional"
    }
]

for example in examples:
    prompt = template.format(**example)
    print("\n--- Generated Prompt ---")
    print(prompt)