import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# u = 25
# a =5
# t = np.arange(2,21)
# v=[]
# for i in t:
#     v.append(u+a*i)
# print(t)
# print(v)
# plt.plot(t,v)
# plt.xlabel("X-Axis")
# plt.ylabel("y-axis")
# plt.show()

# u = int(input("Enter the u: "))
# a = int(input("Enter a:"))
u = 25#can not take user input in matplotlib
a =5
t = np.arange(2,21)
s =[]
for i in t:
    s.append(u*i +0.5*a*i*i)
print(t)
print(s)
plt.title("MOTION EQN")
plt.xlabel("TIME")
# plt.xlim(5,15)#limit for the x axis
# plt.ylim(20,15)#limit for the y axis
plt.ylabel("DISTANCE")
plt.plot(t,s,label = "VELOCITY",color ="pink")
plt.legend()
plt.show()