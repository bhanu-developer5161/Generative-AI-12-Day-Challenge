import pandas as pd

data = {
    "Name": ["Anu", "Ravi", "Priya"],
    "Python": [85, 72, 95],
    "SQL": [78, 88, 91],
    "React": [90, 80, 89]
}

df = pd.DataFrame(data)

print(df)
print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nIndex:")
print(df.index)

print("\nData types:")
print(df.dtypes)
print("\nFirst rows:")
print(df.head())

print("\nLast rows:")
print(df.tail())

print("\nDataFrame information:")
df.info()

print("\nStatistical summary:")
print(df.describe())

print("\nPython marks:")
print(df["Python"])

print("\nName and Python:")
print(df[["Name", "Python"]])

print("\nPython marks:")
print(df["Python"])

print("\nName and Python:")
print(df[["Name", "Python"]])

print("\nFirst student:")
print(df.loc[0])

print("\nAnu's Python mark:")
print(df.loc[0, "Python"])

print("\nRavi's SQL mark:")
print(df.loc[1, "SQL"])

print("First row:")
print(df.iloc[0])

print("\nPython mark of first student:")
print(df.iloc[0, 1])

print("\nFirst two rows:")
print(df.iloc[0:2])

print("\nDataFrame with Average:")

df["Average"] = (
    df["Python"] +
    df["SQL"] +
    df["React"]
) / 3

print(df)

df["Python"] = df["Python"] + 5

print("\nUpdated Python marks:")
print(df)

df.loc[len(df)] = ["Kiran", 88, 84, 92, 88]

print("\nAfter adding new student:")
print(df)

df_without_average = df.drop(columns=["Average"])

print("\nDataFrame without Average:")
print(df_without_average)

df_without_kiran = df.drop(index=3)

print("\nDataFrame without Kiran:")
print(df_without_kiran)