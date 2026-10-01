import pandas as pd

marks = pd.Series([85, 90, 78, 92, 88])

print(marks)
print("First mark:", marks[0])
print("Third mark:", marks[2])
print("Last mark:", marks[4])

#============================
#Custom Index
#============================
import pandas as pd

marks = pd.Series(
    [85, 78, 92, 88],
    index=["Python", "SQL", "React", "Django"]
)

print(marks)