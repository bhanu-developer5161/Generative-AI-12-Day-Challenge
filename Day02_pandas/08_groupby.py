import pandas as pd

data = {
    "Name": ["Anu", "Ravi", "Priya", "Kiran"],
    "Department": ["Python", "Web", "Python", "Web"],
    "Marks": [90, 77, 100, 88]
}

df = pd.DataFrame(data)

print(df)

print("\nAverage marks by department:")

result = df.groupby("Department")["Marks"].mean()

print(result)

print("\nHighest marks:")
print(df.groupby("Department")["Marks"].max())

print("\nLowest marks:")
print(df.groupby("Department")["Marks"].min())

print("\nTotal marks:")
print(df.groupby("Department")["Marks"].sum())