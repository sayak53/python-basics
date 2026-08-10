import numpy as np

# Creating a 1-D array
a = np.array([10, 20, 30, 40, 50])

print("1-D Array:")
print(a)

# Creating a 2-D array
b = np.array([[10, 20, 30],
[40, 50, 60]])

print("\n2-D Array:")
print(b)

# Displaying array properties
print("\nShape of 1-D array:", a.shape)
print("Number of dimensions:", a.ndim)
print("Size of array:", a.size)
print("Data type:", a.dtype)

# Basic arithmetic operations
print("\nAddition:", a + 5)
print("Subtraction:", a -5)
print("Multiplication:", a * 2)
print("Division:", a / 2)

# Statistical operations
print("\nSum:", np.sum(a))
print("Mean:", np.mean(a))
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))
print("Standard Deviation:", np.std(a))