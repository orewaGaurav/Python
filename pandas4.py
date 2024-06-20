#create the data DataFrame using list of lists
import pandas as pd
import numpy as np
lol =[["amit",201,34],['bunty',301,56],['chintu',401,453]]
df8 = pd.DataFrame(lol,columns=['name','roll','marks'])
print(df8)

#creating dataframe using list of dictionary
list_of_dict = [
    {'name':"Gaurav",'rollno':14,"marks":69},
    {'name':"Lavesh",'rollno':34,"marks":101},
    {'name':"Priyanshu",'rollno':7,"marks":94}
]
df9 = pd.DataFrame(list_of_dict)
print(df9)

#creating DataFrame using Dictionary of Series
s1 = pd.Series(['Akshansh','Shasank','Lavesh'])
s2 = pd.Series([201,202,203])
s3 =pd.Series([97,78,69])
dict={"name":s1,"roll":s2,"marks":s3}
df10 =pd.DataFrame(dict)
print(df10)
print(df10.columns)

# inserting a new column in existing DataFrame
df10['addres']=['Noida',"Delhi","pune"]
print(df10)

df10['status']=df10['marks']>50
print(df10)

#inserting a new column at desired position
df10.insert(1,"branch",["cse","AIML","CYS"])
print(df10)
del df10['status']
print(df10)
df10["hobbies"]=['GYM','play',"coding"]
print(df10)
df10.insert(3,"contact",[62069,85399,78707])
print(df10)
del df10['contact']
print(df10)

del df10["hobbies"]
print(df10)

df10["dekh"]=[23,32,43]
print(df10)
del df10["dekh"]
print(df10)

df10.insert(2,"dekhleya",["gau",45,"pri"])
print(df10)
del df10["dekhleya"]
print(df10)

#pop method
df11 = df10.pop("marks")
print(df11)
# print(df10)
df10.drop("addres",axis=1,inplace=True)
print(df10)

#drop the row
df12=df8.drop(1,inplace =True)
print(df8)
print(df12)

#rename the existing column
df10.rename(columns={"name":"std_name"},inplace =True)
print(df10)

#creating a dataframe using numpy random function
dfa = pd.DataFrame(np.random.rand(250,5))
print(dfa)
print(dfa.head())#it will print first five value
print(dfa.tail())#it will print last five value
print(dfa.head(10))

