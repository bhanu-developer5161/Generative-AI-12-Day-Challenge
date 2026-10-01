import pandas as pd

data = {
    "Name": ["Anu", "Ravi", "Priya", "Kiran"],
    "Python": [90, 77, 100, 88],
    "SQL": [78, 88, 91, 84],
    "React": [90, 80, 89, 92]
}

df = pd.DataFrame(data)

df.to_csv("students.csv", index=False)

print("CSV file created successfully!")

students = pd.read_csv("students.csv")

print("\nData read from CSV:")
print(students)