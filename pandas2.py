import pandas as pd
import numpy as np
a = [10,'Ram',20,30]
mycol = pd.Series(a)
print(a)
print(mycol)
print(mycol[2])
mycol1 = pd.Series(a,index=['i','ii','iii','iv'])
print(mycol1)
print(mycol1['ii'])
print(mycol1[1])

data = np.array([5,6,7,8])
ds = pd.Series(data,index=[10,20,30,40])
print(ds)

#creating a series using Dictionary
dict = {'a':10,'b':20,'c':30}
ds1 = pd.Series(dict)
print(ds1)
ds2 = pd.Series(dict,index =['a','b','1'])
print(ds2)

#index are not unique

da = pd.Series(20,index=[1,2,3,4,5])
print(da)

ds4 = pd.Series(np.ones(7))
print(ds4)

ds5 = pd.Series(np.arange(12,23))
print(ds5)

