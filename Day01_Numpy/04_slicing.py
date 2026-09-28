import numpy as np

numbers =np.array([10, 20, 30, 40, 50, 60])

print(numbers[1:3])  # Output: [20, 30]
print(numbers[2:])  # Output: [30, 40, 50, 60]
print(numbers[0:3])  # Output: [10, 20, 30]

#=========================
#Slicing with a Step
#=========================

numbers = np.array([10, 20, 30, 40, 50, 60])

print(numbers[::2])  # Output: [10, 30, 50]
print(numbers[1:6:2])  # Output: [20, 40, 60]
print(numbers[-1:-7:-1])  # Output: [60, 50, 40, 30, 20, 10]
