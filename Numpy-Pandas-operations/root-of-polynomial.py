# import numpy library
import numpy as np
  
#  the coefficients of poly(x^2   + 4x +3)
p = np.poly1d([ 1, 4, 3])

# the roots
root_of_poly = p.r
print("THe root for the given euation are:\n")
print(root_of_poly)