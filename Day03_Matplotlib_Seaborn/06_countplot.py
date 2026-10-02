import seaborn as sns
import matplotlib.pyplot as plt

departments = [
    "Python",
    "Web",
    "Python",
    "Web",
    "Python"
]

sns.countplot(x=departments)

plt.title("Students by Department")
plt.xlabel("Department")
plt.ylabel("Number of Students")

plt.show()