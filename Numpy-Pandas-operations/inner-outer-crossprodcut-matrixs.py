import numpy as np


x = np.array([[1, 2, 3], [4, 5, 6],[4, 5, 6]])
y = np.array([[1, 3, 5], [7, 9, 11],[4, 5, 6]])
print("\nPrinting the Original Metrics array:\n")
print("x =", x)
print("\ny =", y)

print("\nInner product of matrices x and y =")
print(np.inner(x, y))

print("\Outer product of matrices x and y =")
print(np.outer(x, y))

print("\Cross product of matrices x and y =")
print(np.dot(x, y))