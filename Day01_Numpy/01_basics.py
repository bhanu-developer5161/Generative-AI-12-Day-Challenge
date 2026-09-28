import numpy as np
# =========================
# Example 1
# =========================


numbers = np.array([10, 20, 30, 40, 50])

print(numbers)
print(numbers.shape)
print(numbers.ndim)
print(numbers.size)

# =========================
# Example 2
# =========================

marks = np.array([85, 72, 91, 68, 95, 88])

print("Example 2")
print(marks)
print(marks.shape)
print(marks.ndim)
print(marks.size)


# =========================
# Example 3
# =========================

prices = np.array([100, 250, 500, 750])

print("Example 3")
print(prices)
print(prices.shape)
print(prices.ndim)
print(prices.size)

#========================
# Example 4
#========================

student_marks = np.array([78, 92, 65, 88, 95, 71])

print(student_marks)
print(student_marks.shape)  # This will raise an AttributeError since student_marks is a list, not a numpy array
print(student_marks.ndim)   # This will also raise an AttributeError
print(student_marks.size)   # This will raise an AttributeError as well


#========================
# Example 5
#========================

temperature_readings = np.array([28, 31, 29, 33, 30, 27, 32])

print(temperature_readings)
print(temperature_readings.shape)
print(temperature_readings.ndim)
print(temperature_readings.size)

#========================
# Example 6
#========================

prices = np.array([100, 200, 300, 400, 500])

print(prices + 50)  # Adding 50 to each element
print(prices - 20)   # Subtracting 20 from each element
print(prices * 2)   # Multiplying each element by 2
print(prices / 2)  # Dividing each element by 10

#========================
# Example 7     
#========================

marks = np.array([78, 92, 65, 88, 95, 71])

print(marks.sum())  # Sum of all elements
print(marks.mean())  # Mean of all elements
print(marks.max())  # Maximum element
print(marks.min())  # Minimum element