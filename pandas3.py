#creating a dataframe using lists
import pandas as pd
import numpy as np
data = {
    "Name":['Ravi','Kavi','Gaurav'],
    "Roll_no":[100,101,102],
    "marks":[56,32,96]
}
df = pd.DataFrame(data)
print(df)
df1 = pd.DataFrame(data,index = ['std1','std2','std3'])
print(df1)

#loc attribute
print(df1.loc['std2'])
print(df1['Name'])
print(df1.loc[['std1','std2','std3']])

#creating DataFrame using numpy array
arr =np.array([['amit','ajay','ram'],[123,231,321],[45,65,36]])
df6 = pd.DataFrame(arr,columns = ['id1','id2','id3'],index =["Name","RollNo","Marks"])
print(df6)

#creating a DataFrame using numpy dictionary
arr =np.array([['amit','ajay','ram'],[123,231,321],[45,56,78]])
# print(arr)
np_dict = {"Name":arr[0],"Roll":arr[1],'Marks':arr[2]}
df7= pd.DataFrame(np_dict)
print(df7)