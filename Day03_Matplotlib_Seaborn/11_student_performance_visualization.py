import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Name": ["Anu", "Ravi", "Priya", "Kiran", "Sita"],
    "Department": ["Python", "Web", "Python", "Web", "Python"],
    "Python": [90, 77, 100, 88, 92],
    "SQL": [78, 88, 91, 84, 89],
    "React": [90, 80, 89, 92, 94]
}

df = pd.DataFrame(data)

print("========== STUDENT DATA ==========")
print(df)

df["Average"] = (
    df["Python"] +
    df["SQL"] +
    df["React"]
) / 3

print("\n========== AVERAGE MARKS ==========")
print(df[["Name", "Average"]])

top_student = df.loc[df["Average"].idxmax(), "Name"]
highest_average = df["Average"].max()

print("\n========== TOP STUDENT ==========")
print("Top Student:", top_student)
print("Highest Average:", round(highest_average, 2))

# Average Marks Bar Chart

plt.figure(figsize=(8, 5))

sns.barplot(
    data=df,
    x="Name",
    y="Average"
)

plt.title("Student Average Marks")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.ylim(0, 100)

plt.show()

# Subject-wise Performance Comparison

subjects = ["Python", "SQL", "React"]

plt.figure(figsize=(8, 5))

x = range(len(df))

plt.bar(
    [i - 0.25 for i in x],
    df["Python"],
    width=0.25,
    label="Python"
)

plt.bar(
    x,
    df["SQL"],
    width=0.25,
    label="SQL"
)

plt.bar(
    [i + 0.25 for i in x],
    df["React"],
    width=0.25,
    label="React"
)

plt.title("Subject-wise Student Performance")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(x, df["Name"])
plt.ylim(0, 100)
plt.legend()

plt.show()

# Correlation Heatmap

correlation = df[["Python", "SQL", "React"]].corr()

plt.figure(figsize=(7, 5))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)

plt.title("Subject Marks Correlation")
plt.show()

# Pairplot

sns.pairplot(
    df[["Python", "SQL", "React"]]
)

plt.show()

# Department-wise Average Performance

department_average = df.groupby("Department")["Average"].mean()

print("\n========== DEPARTMENT-WISE AVERAGE ==========")
print(department_average)

plt.figure(figsize=(7, 5))

sns.barplot(
    x=department_average.index,
    y=department_average.values
)

plt.title("Department-wise Average Performance")
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.ylim(0, 100)

plt.show()