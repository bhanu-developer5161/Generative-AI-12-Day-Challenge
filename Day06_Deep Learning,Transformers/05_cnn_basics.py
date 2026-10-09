# Day 06 - CNN Basics

image = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

filter_values = [
    [1, 0],
    [0, -1]
]

print("Input Image:")
for row in image:
    print(row)

print("\nFilter:")
for row in filter_values:
    print(row)

# Apply the filter to the top-left 2x2 region
result = (
    image[0][0] * filter_values[0][0]
    + image[0][1] * filter_values[0][1]
    + image[1][0] * filter_values[1][0]
    + image[1][1] * filter_values[1][1]
)

print("\nConvolution Result:", result)