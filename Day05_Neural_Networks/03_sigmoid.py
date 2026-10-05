import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


values = [-5, -2, 0, 2, 5]

for value in values:
    print(value, "->", sigmoid(value))