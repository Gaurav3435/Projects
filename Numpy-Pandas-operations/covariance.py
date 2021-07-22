import numpy as np


x = np.array([1, 2, 3])
y = np.array([1, 3, 5])
print("\nPrinting the Original Metrics array:\n")
print("x =", x)
print("\ny =", y)

print("\nTHe covariance of two metrics are :\n")
print(np.cov(x,y))