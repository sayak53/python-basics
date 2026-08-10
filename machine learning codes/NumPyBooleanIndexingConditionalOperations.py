import numpy as np

# Creating an array of marks
marks = np.array([45, 67, 32, 89, 76, 54, 91, 38, 82, 60])

print("Original Marks:")
print(marks)

# Boolean condition
print("\nBoolean Array (Marks >= 50):")
print(marks >= 50)

# Selecting marks greater than or equal to 50
passed = marks[marks >= 50]

print("\nMarks greater than or equal to 50:")
print(passed)

# Selecting marks below 50
failed = marks[marks < 50]

print("\nMarks below 50:")
print(failed)

# Selecting marks greater than 80
high_marks = marks[marks > 80]

print("\nMarks greater than 80:")
print(high_marks)

# Counting students who passed
print("\nNumber of students who passed:", np.sum(marks >= 50))

# Counting students who failed
print("Number of students who failed:", np.sum(marks < 50))

# Replacing marks below 40 with 40
marks[marks < 40] = 40

print("\nMarks after replacing values below 40 with 40:")
print(marks)