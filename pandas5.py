import pandas as pd
from openpyxl.workbook import Workbook
dic = {"Stu_Name":["Luffy","Zoro","sanji","Nami","Robin","Franky","Chopper","Brook","Gimbe","Shanks"],
       "RollNo":[1,2,3,4,5,6,7,8,9,10],
       "Branch":["CYS","AIML","DS",'CSE',"BT","CSBS","CYS","MECH","ECE","CSE"],
       "ContactNo":[2341,1234,5467,2378,9878,6712,1278,9865,1209,4554],
       "Marks":[30,50,23,56,78,45,97,90,64,78],
       "Address":["noida",'delhi','mumbai','noida','pune','bihar','ranchi','garhwa','patna',"delhi"]}
dc =pd.DataFrame(dic)
print(dc)

# to make a excel file
dc.to_excel(r"/Users/gauravkumar/Desktop/Telegram/dic.xlsx")

# to call a excel file
variable =pd.read_excel(r"/Users/gauravkumar/Desktop/Telegram/dic.xlsx")
print(variable)

#to make txtfile
# np.savetxt(r'/Users/gauravkumar/Desktop/Telegram/dataframe.txt',dc,fmt="%s")
# variable= np.loadtxt(r'/Users/gauravkumar/Desktop/Telegram/filehandling.txt')

# to make csv file
dc.to_csv(r'/Users/gauravkumar/Desktop/Telegram/dic1.csv')
# to import csv file
variable1 = pd.read_csv(r"/Users/gauravkumar/Desktop/Telegram/dic1.csv")
print(variable1)