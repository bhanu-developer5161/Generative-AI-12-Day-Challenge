import pandas as pd

marks = pd.Series(
    [85, 78, 92, 88],
    index=["Python", "SQL", "React", "Django"]
)

print("Total:", marks.sum())
print("Average:", marks.mean())
print("Highest:", marks.max())
print("Lowest:", marks.min())