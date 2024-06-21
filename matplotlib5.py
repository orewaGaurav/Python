import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd 
#BAR PLOT
data=pd.read_excel(r"/Users/gauravkumar/Desktop/Telegram/dic.xlsx")
print(data)
plt.bar(data["RollNo"],data["Marks"],color = "RED",label ="VENOM",ls = "-.")
plt.xlabel("Roll_No.")
plt.ylabel("Marks")
plt.title("RESULT")
plt.legend()
plt.grid()
plt.show()