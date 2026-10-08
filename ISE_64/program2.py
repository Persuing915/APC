import numpy as np

marks = np.array([
    [[70, 80], [60, 75], [85, 90]],
    [[65, 70], [75, 80], [80, 85]]
])

print("Marks:")
print(marks)

average = np.mean(marks, axis=(0, 2))

print("Subject-wise Average:")
print(average)