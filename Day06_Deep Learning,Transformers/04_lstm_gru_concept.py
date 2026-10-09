# Day 06 - LSTM and GRU Concept

previous_memory = 10
new_information = 4

# Imagine a gate value between 0 and 1
memory_gate = 0.8
input_gate = 0.2

updated_memory = (
    memory_gate * previous_memory
    + input_gate * new_information
)

print("Previous Memory:", previous_memory)
print("New Information:", new_information)
print("Memory Gate:", memory_gate)
print("Updated Memory:", updated_memory)