# import numpy library
import numpy as np
  
#  the coefficients of poly( x^3 +3 x^2   + 2x +1)
p = np.poly1d([1, 3, 2, 1])

# the roots
root_of_poly = p.r

print(root_of_poly)