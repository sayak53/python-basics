import numpy as np

# Creating a 2-D array
data = np.array([
[80, 70, 90],
[60, 75, 85],
[90, 88, 95],
[70, 65, 72]
])

print("Original Dataset:")
print(data)

# Display shape
print("\nShape of Dataset:", data.shape)

# Sum of all elements
print("\nTotal Sum:", np.sum(data))

# Sum column-wise
print("\nColumn-wise Sum:")
print(np.sum(data, axis=0))

# Sum row-wise
print("\nRow-wise Sum:")
print(np.sum(data, axis=1))

# Mean column-wise
print("\nColumn-wise Mean:")
print(np.mean(data, axis=0))

# Mean row-wise
print("\nRow-wise Mean:")
print(np.mean(data, axis=1))

# Maximum value from each column
print("\nColumn-wise Maximum:")
print(np.max(data, axis=0))

# Minimum value from each column
print("\nColumn-wise Minimum:")
print(np.min(data, axis=0))