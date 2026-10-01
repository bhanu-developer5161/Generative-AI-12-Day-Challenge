import pandas as pd

data = {
    "Name": ["Anu", "Ravi", "Priya", "Kiran"],
    "Python": [90, 77, 100, 88],
    "SQL": [78, 88, 91, 84],
    "React": [90, 80, 89, 92]
}

df = pd.DataFrame(data)

print(df)

high_python = df[df["Python"] > 85]

print("\nStudents with Python marks above 85:")
print(high_python)

high_students = df[
    (df["Python"] > 85) &
    (df["SQL"] > 80)
]

print("\nStudents with Python > 85 and SQL > 80:")
print(high_students)

selected_students = df[
    (df["Python"] > 95) |
    (df["SQL"] > 90)
]

print("\nStudents with Python > 95 OR SQL > 90:")
print(selected_students)