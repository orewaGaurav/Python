#histogram
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd 
data=pd.read_excel(r"/Users/gauravkumar/Desktop/Telegram/dic.xlsx")
print(data)
marks =[21,23,4,5,67,87,34,56,78,13,84,36,26,69]
range=(0,12)
inter = 3
plt.hist(marks,inter,range,color='red')
# plt.show()
data.hist()
plt.show()

