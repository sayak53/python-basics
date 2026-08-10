import numpy as np

# Array of zeros
a = np.zeros(5)
print("Array of zeros:")
print(a)

# Array of ones
b = np.ones(5)
print("\nArray of ones:")
print(b)

# Array using arange()
c = np.arange(1, 11)
print("\nArray using arange():")
print(c)

# Array using linspace()
d = np.linspace(0, 10, 6)
print("\nArray using linspace():")
print(d)

# Statistical operations
marks = np.array([65, 78, 82, 91, 56, 74, 88, 69])

print("\nMarks:")
print(marks)

print("\nSum:", np.sum(marks))
print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))
print("Standard Deviation:", np.std(marks))