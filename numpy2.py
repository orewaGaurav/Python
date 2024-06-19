# import numpy as np
# import sys
# l = [1,2,3,4,5,6,7]
# arr1 = np.array(l)
# print(arr1)
# print(type(arr1))
# print(sys.getsizeof(arr1))
# list1 = [1,2,3,4,5]
# print(list1)
# print(type(list1))
# print(sys.getsizeof(list1))


#1D array
import numpy as np
arr1 = np.array([1,2,3,4,5,6],np.int32)
print(arr1)
print(arr1.dtype)
print(arr1.ndim)
print(arr1.nbytes)
print(arr1.size)
print(arr1.shape)