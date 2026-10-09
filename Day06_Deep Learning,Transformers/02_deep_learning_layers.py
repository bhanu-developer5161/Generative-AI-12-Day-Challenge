# Day 06 - Deep Learning Layers

input_value = 5

layer1_weight = 0.5
layer2_weight = 0.8
layer3_weight = 1.2

layer1_output = input_value * layer1_weight
layer2_output = layer1_output * layer2_weight
layer3_output = layer2_output * layer3_weight

print("Input:", input_value)
print("Layer 1 Output:", layer1_output)
print("Layer 2 Output:", layer2_output)
print("Layer 3 Output:", layer3_output)