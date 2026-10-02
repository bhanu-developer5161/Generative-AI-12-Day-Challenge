import matplotlib.pyplot as plt

subjects = ["Python", "SQL", "React"]
marks = [90, 78, 90]

bars = plt.bar(subjects, marks)

plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        str(bar.get_height()),
        ha="center",
        va="bottom"
    )

plt.show()