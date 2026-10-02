import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y, marker="o", linestyle="--")

plt.title("Student Performance")
plt.xlabel("Student Number")
plt.ylabel("Marks")

plt.show()