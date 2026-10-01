import pandas as pd

marks = pd.Series(
    [85, 78, 92, 88],
    index=["Python", "SQL", "React", "Django"]
)

print("All marks:")
print(marks)

print("\nMarks greater than 80:")
print(marks[marks > 80])