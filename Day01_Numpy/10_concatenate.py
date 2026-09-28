import numpy as np

a = np.array([10, 20, 30])
b = np.array([40, 50, 60])

result = np.concatenate((a, b))

print(result)

#=========================
#Example 2  
#=========================
a = np.array([[10, 20, 30],
              [40, 50, 60]])

b = np.array([[70, 80, 90],
              [100, 110, 120]])

result = np.concatenate((a, b), axis=0)

print(result)