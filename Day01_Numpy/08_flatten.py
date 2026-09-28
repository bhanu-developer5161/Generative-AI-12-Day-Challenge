import numpy as np

numbers = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(numbers)
print(numbers.shape)

flat = numbers.flatten()

print(flat) 

raveled = numbers.ravel()
print(raveled)