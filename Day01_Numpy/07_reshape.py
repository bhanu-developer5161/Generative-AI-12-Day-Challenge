import numpy as np

#=========================
#Example 1
#=========================
numbers = np.array([10, 20, 30, 40, 50, 60])

print(numbers.shape)  # Output: (6,)

#=========================
#Example 2
#=========================
numbers = np.array([10, 20, 30, 40, 50, 60])

reshaped = numbers.reshape(2, 3)
print(reshaped)

#=========================
#Example 3
#=========================
numbers = np.array([10, 20, 30, 40, 50, 60])

reshaped = numbers.reshape(3, 2)
print(reshaped)

#=========================
#Example 4      
#=========================
numbers = np.array([10, 20, 30, 40, 50, 60])

reshaped = numbers.reshape(3, 2)
print(reshaped)

#=========================
#Example 5  
#=========================
numbers = np.array([10, 20, 30, 40, 50, 60])

reshaped = numbers.reshaape(2, 4)
print(reshaped)  # This will raise a ValueError since the total number of elements (6) cannot be reshaped into a shape of (2, 4) which requires 8 elements.
