import numpy as np
 
A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])

  
print("\nPrinting the Original square array:\n\n",A)


print("\nPrinting the Inverse of given square array:\n\n", np.linalg.inv(A))