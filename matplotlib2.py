import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = [1,2,3]
y = [2,4,1]
plt.xlabel("X-axis")
plt.ylabel("y-axis")
plt.title("FIrst Graph")
plt.plot(x,y,color = "green",ls = "-.",label = "Line-1",linewidth =5)
#plot is a function used to draw a 2d plot by using given value
x1 =[5,3,1]
y1 = [6,1,4]
plt.plot(x1,y1,color ="red",label ="Line-2",ls= ":",linewidth = 5)
# plt.legend()
plt.legend(loc = 4)
plt.show()
# linestyle
#'-' solid 
#'--' dashed
#lw = linewidth