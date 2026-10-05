import math


actual = 1
prediction = 0.9

loss = -(
    actual * math.log(prediction)
    + (1 - actual) * math.log(1 - prediction)
)

print("Actual:", actual)
print("Prediction:", prediction)
print("Loss:", loss)