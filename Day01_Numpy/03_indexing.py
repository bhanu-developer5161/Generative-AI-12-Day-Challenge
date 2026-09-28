#===================================
#Example 1
#===================================


import numpy as np

marks = np.array([78, 92, 65, 88, 95, 71])

print(marks[0])
print(marks[2])
print(marks[5])

# =========================
# Negative Indexing
# =========================

marks = np.array([78, 92, 65, 88, 95, 71])

print(marks[-1])  # Last element
print(marks[-2])  # Second to last element
print(marks[-6])  # First element


# =========================
# 2D Array Indexing
# =========================

import numpy as np

marks = np.array([
      [80, 85, 90],
      [70, 75, 80],
      [90, 95, 100] 
])

print(marks)
print(marks[0, 0])  # First row, first column
print(marks[1, 2])  # Second row, third column
print(marks[2, 1])  # Third row, second column