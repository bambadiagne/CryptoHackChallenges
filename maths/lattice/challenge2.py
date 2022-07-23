import numpy as np
v = (4, 6, 2, 5)
v_square=np.asarray(v)*np.asarray(v)
print(f"The size of {v} is {np.sqrt(sum(v_square))}")