import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


# Student input
study_hours = 6
attendance = 85

# Weights
w1 = 0.4
w2 = 0.03

# Bias
bias = -4

# Forward propagation
z = (study_hours * w1) + (attendance * w2) + bias

prediction = sigmoid(z)

print("Study Hours:", study_hours)
print("Attendance:", attendance)
print("Weighted Sum:", z)
print("Pass Probability:", prediction)

if prediction >= 0.5:
    print("Prediction: PASS")
else:
    print("Prediction: FAIL")