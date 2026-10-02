import seaborn as sns
import matplotlib.pyplot as plt

subjects = ["Python", "SQL", "React"]
marks = [90, 78, 90]

sns.barplot(x=subjects, y=marks)

plt.title("Student Marks")

plt.show()