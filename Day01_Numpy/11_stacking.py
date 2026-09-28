import numpy as np

a = np.array([10, 20, 30])
b = np.array([40, 50, 60])

result = np.vstack((a, b))

print(result)
print(result.shape)

#=========================
#Example 2-hstack()
#=========================

a = np.array([[10, 20, 30],
              [40, 50, 60]])

b = np.array([[70, 80, 90],
              [100, 110, 120]])

result = np.hstack((a, b))

print(result)
print(result.shape)