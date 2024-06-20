from scipy import special as sp
from scipy import constants as cs
from numpy import poly1d
a = sp.exp10(30)
print(a)
b= sp.exp10(6)
print(b)

import numpy as np
a = np.array([3,5])
b = np.array([10,12])
x = sp.perm(b,a)
print(x)
print(len(dir(sp)))
print(cs.pi)
v = poly1d([3,4,7])
print(v)
u = poly1d([3,4])
print(u)
w =poly1d([3,4,7,1])
print(w)
x =poly1d([3,4,7,1],variable ="y")
print(x)
print(x.deriv())