import numpy as np

m = np.array([[1, 2,3,4],
              [2, 3,5,6],
              [2, 3,5,6],
              [2, 3,5,6]])
  
print("\nPrinting the Original square array:\n\n",m)
  
w, v = np.linalg.eig(m)

print("\nPrinting the Eigen values of the given square array:\n\n", w)