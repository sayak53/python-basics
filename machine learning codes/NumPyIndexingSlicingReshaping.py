import numpy as np

# Creating a 1-D NumPy array
a = np.array([10, 20, 30, 40, 50, 60])

print("Original 1-D Array:")
print(a)

# Indexing
print("\nFirst element:", a[0])
print("Third element:", a[2])
print("Last element:", a[-1])

# Slicing
print("\nFirst three elements:")
print(a[0:3])

print("\nElements from index 2 to 4:")
print(a[2:5])

print("\nEvery alternate element:")
print(a[::2])

# Creating a 2-D array
b = np.array([[10, 20, 30],
[40, 50, 60]])

print("\nOriginal 2-D Array:")
print(b)

# 2-D indexing
print("\nElement at row 1, column 2:")
print(b[0, 1])

print("Element at row 2, column 3:")
print(b[1, 2])

# 2-D slicing
print("\nFirst row:")
print(b[0, :])

print("\nSecond column:")
print(b[:, 1])

# Reshaping
c = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print("\nOriginal Array:")
print(c)

# Reshape 1-D array into 3 x 4
d = c.reshape(3, 4)

print("\nReshaped Array (3 x 4):")
print(d)

# Reshape into 4 x 3
e = c.reshape(4, 3)

print("\nReshaped Array (4 x 3):")
print(e)