def relu(x):
    return max(0, x)


values = [-5, -2, 0, 3, 7]

for value in values:
    print(value, "->", relu(value))