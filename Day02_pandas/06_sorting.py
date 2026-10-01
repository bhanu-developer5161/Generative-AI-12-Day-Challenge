import pandas as pd

data = {
    "Name": ["Anu", "Ravi", "Priya", "Kiran"],
    "Python": [90, 77, 100, 88],
    "SQL": [78, 88, 91, 84],
    "React": [90, 80, 89, 92]
}

df = pd.DataFrame(data)

sorted_students = df.sort_values(
    by="Python",
    ascending=False
)

print("\nStudents sorted by Python marks:")
print(sorted_students)

sorted_students = df.sort_values(
    by="Python",
    ascending=True
)

print("\nStudents sorted by Python marks (lowest to highest):")
print(sorted_students)