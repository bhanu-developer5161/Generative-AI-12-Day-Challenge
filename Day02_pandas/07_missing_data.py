import pandas as pd

data = {
    "Name": ["Anu", "Ravi", "Priya", "Kiran"],
    "Python": [90, 77, None, 88],
    "SQL": [78, 88, 91, None],
    "React": [90, 80, 89, 92]
}

df = pd.DataFrame(data)

print(df)

print("\nMissing values:")
print(df.isna())

missing_count = df.isna().sum()

print("\nNumber of missing values:")
print(missing_count)

df_filled = df.fillna(0)

print("\nDataFrame after filling missing values:")
print(df_filled)

python_mean = df["Python"].mean()

df["Python"] = df["Python"].fillna(python_mean)

print("\nPython missing value filled with mean:")
print(df)

sql_mean = df["SQL"].mean()

df["SQL"] = df["SQL"].fillna(sql_mean)

print("\nSQL missing value filled with mean:")
print(df)