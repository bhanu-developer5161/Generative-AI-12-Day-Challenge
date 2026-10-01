import pandas as pd

# ==========================================
# 1. Create Student Data
# ==========================================

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


# ==========================================
# 2. Calculate Average Marks
# ==========================================

df["Average"] = (
    df["Python"] +
    df["SQL"] +
    df["React"]
) / 3

print("\n========== AVERAGE MARKS ==========")
print(df)


# ==========================================
# 3. Find Students With Python > 85
# ==========================================

high_python = df[df["Python"] > 85]

print("\n========== PYTHON > 85 ==========")
print(high_python)


# ==========================================
# 4. Find Students With Python > 85
#    AND SQL > 80
# ==========================================

high_students = df[
    (df["Python"] > 85) &
    (df["SQL"] > 80)
]

print("\n========== PYTHON > 85 AND SQL > 80 ==========")
print(high_students)


# ==========================================
# 5. Sort Students By Average
#    Highest → Lowest
# ==========================================

sorted_students = df.sort_values(
    by="Average",
    ascending=False
)

print("\n========== SORTED BY AVERAGE ==========")
print(sorted_students)


# ==========================================
# 6. Find Highest Marks
# ==========================================

print("\n========== HIGHEST MARKS ==========")

print("Highest Python:", df["Python"].max())
print("Highest SQL:", df["SQL"].max())
print("Highest React:", df["React"].max())
print("Highest Average:", df["Average"].max())


# ==========================================
# 7. Find Lowest Marks
# ==========================================

print("\n========== LOWEST MARKS ==========")

print("Lowest Python:", df["Python"].min())
print("Lowest SQL:", df["SQL"].min())
print("Lowest React:", df["React"].min())


# ==========================================
# 8. Department-wise Average
# ==========================================

department_average = df.groupby("Department")["Average"].mean()

print("\n========== DEPARTMENT AVERAGE ==========")
print(department_average)


# ==========================================
# 9. Department-wise Highest Marks
# ==========================================

department_highest = df.groupby("Department")["Average"].max()

print("\n========== DEPARTMENT HIGHEST AVERAGE ==========")
print(department_highest)


# ==========================================
# 10. Department-wise Total Marks
# ==========================================

department_total = df.groupby("Department")["Average"].sum()

print("\n========== DEPARTMENT TOTAL ==========")
print(department_total)


# ==========================================
# 11. Save Data to CSV
# ==========================================

df.to_csv(
    "student_performance.csv",
    index=False
)

print("\n========== CSV ==========")
print("Student performance data saved successfully!")


# ==========================================
# 12. Read CSV File
# ==========================================

student_data = pd.read_csv(
    "student_performance.csv"
)

print("\n========== DATA FROM CSV ==========")
print(student_data)


# ==========================================
# 13. Final Summary
# ==========================================

print("\n========== FINAL SUMMARY ==========")

print("Number of students:", len(df))

print(
    "Overall average:",
    round(df["Average"].mean(), 2)
)

top_student = df.loc[
    df["Average"].idxmax(),
    "Name"
]

print("Top student:", top_student)

print("Highest average:", round(df["Average"].max(), 2))