import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6]
marks = [45, 50, 58, 65, 72, 85]

plt.scatter(study_hours, marks)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()