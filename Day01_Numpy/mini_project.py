import numpy as np

# ==========================================
# STUDENT MARKS ANALYZER - NUMPY MINI PROJECT
# ==========================================

# Student marks:
# Columns → Python, SQL, React
marks = np.array([
    [85, 78, 92],
    [65, 88, 75],
    [90, 95, 89],
    [72, 68, 80],
    [95, 91, 96]
])

print("=" * 45)
print("       STUDENT MARKS ANALYZER")
print("=" * 45)

# Display marks
print("\nStudent Marks:")
print(marks)

# 1. Shape
print("\n1. Shape of marks:")
print(marks.shape)

# 2. Total marks of each student
total_marks = marks.sum(axis=1)

print("\n2. Total marks of each student:")
print(total_marks)

# 3. Average marks of each student
average_marks = marks.mean(axis=1)

print("\n3. Average marks of each student:")
print(average_marks)

# 4. Highest mark in each subject
highest_marks = marks.max(axis=0)

print("\n4. Highest mark in each subject:")
print(highest_marks)

# 5. Lowest mark in each subject
lowest_marks = marks.min(axis=0)

print("\n5. Lowest mark in each subject:")
print(lowest_marks)

# 6. Students with average above 80
high_average = average_marks[average_marks > 80]

print("\n6. Averages above 80:")
print(high_average)

# 7. Classify students
result = np.where(
    average_marks >= 80,
    "Good",
    "Needs Improvement"
)

print("\n7. Student performance:")
print(result)

# 8. Overall average
overall_average = marks.mean()

print("\n8. Overall class average:")
print(overall_average)

# 9. Unique marks
unique_marks = np.unique(marks)

print("\n9. Unique marks:")
print(unique_marks)

# 10. Sorted unique marks
sorted_marks = np.sort(unique_marks)

print("\n10. Sorted unique marks:")
print(sorted_marks)

print("\n" + "=" * 45)
print("          ANALYSIS COMPLETED")
print("=" * 45)