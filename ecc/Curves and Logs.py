from ecc_functions import *
from hashlib import sha1
# E: Y2 = X3 + 497 X + 1768, p: 9739, G: (1804,5368)
G = (1804, 5368)
p = 9739
Qa = (815, 3190)
Nb = 1829
a = 497
b = 1768
x = Qa
for i in range(Nb-1):
    x = addition_P(x, Qa, a, b, p)
print(x)
hash = sha1(str(x[0]).encode())
x_hexdigest = hash.hexdigest()
print(x_hexdigest)
