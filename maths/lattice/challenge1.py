import numpy as np

v = np.asarray((2,6,3)) 
w = np.asarray((1,0,0))
u = np.asarray((7,7,2))
print(sum(3*(2*v - w) * 2*u))
