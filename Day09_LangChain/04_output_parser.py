
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

# Simulated response from an LLM
model_response = "Generative AI creates new content from learned patterns."

parsed_output = parser.parse(model_response)

print("=== Output Parser Demo ===")
print("Original response:", model_response)
print("Parsed output:", parsed_output)
print("Output type:", type(parsed_output).__name__)