import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


x1 = 3
x2 = 4

w1 = 2
w2 = 0.5

bias = 1

z = (x1 * w1) + (x2 * w2) + bias

output = sigmoid(z)

print("Weighted Sum:", z)
print("Final Output:", output)