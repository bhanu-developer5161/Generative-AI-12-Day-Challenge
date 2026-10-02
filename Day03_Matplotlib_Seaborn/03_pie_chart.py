import matplotlib.pyplot as plt

subjects = ["Python", "SQL", "React"]
marks = [90, 78, 90]

plt.pie(
    marks,
    labels=subjects,
    autopct="%1.1f%%"
)

plt.title("Student Marks Distribution")

plt.show()