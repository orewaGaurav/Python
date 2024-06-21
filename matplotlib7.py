#pie chart : it is To show percentage distribution of 
# different different entities in a whole data
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd 

# marks = [34,67,63,86,78]
# ex =[0,0,1.0,0,1.0]#controls the sepration
# subject = ['physics','maths','electrical','english','language']
# plt.pie(marks,labels=subject,autopct="%1.1f%%",explode =ex,startangle=180)
# plt.show()

# stacked plot: it is used to for compare two areas


# months =['jan','feb','mar','apr','may','june','july','aug','sep','oct','nov','dec']
# sales_car =[12,23,34,56,12,45,67,89,13,45,56,34]
# sales_bike=[32,34,14,67,81,63,45,67,80,24,19,27]
# plt.stackplot(months,sales_car,sales_bike,labels=["car","bike"])
# plt.legend()
# plt.show()

#plotting curves of given
# x =np.arange(0,2*(np.pi),0.1)
# print(x)
# y = np.sin(x)
# plt.plot(x,y)
# plt.show()

x1 = np.arange(0,20,1.0)
y1 = x1**2
plt.plot(x1,y1)
plt.show()