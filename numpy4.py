import numpy as np
a1 = np.arange(9)
print(a1)
a2 = np.empty_like(a1)
print(a2)
print(a1)
a1[1]=200
print(a1)
print(a2)

