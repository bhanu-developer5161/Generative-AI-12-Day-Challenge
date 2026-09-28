import numpy as np

marks = np.array([78, 92, 65, 88, 95, 71])

print(marks > 80)
print(marks < 70)
print(marks == 95)
print(marks != 71)
print(marks >= 90)
print(marks <= 78)
print((marks > 80) & (marks < 95))
print((marks < 70) | (marks > 90))
print(marks[(marks > 80) & (marks < 95)])
print(marks[(marks < 70) | (marks > 90)])


#=========================
#np.where() example1
#=========================
import numpy as np

marks = np.array([78, 32, 65, 25, 95, 38])

result = np.where(marks >= 40, "Pass", "Fail")
print(result)


#=========================
#np.where() example2
#=========================

import numpy as np

marks = np.array([78, 32, 65, 25, 95, 38])

result = np.where(marks >= 80, "High", "low")
print(result)

#=========================
#np.where() example3
#=========================
import numpy as np

marks = np.array([78, 32, 65, 25, 95, 38])

result = np.where(marks >= 50, "Good", "Needs Improvement")
print(result)
