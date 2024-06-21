import matplotlib.pyplot as plt
x = [4,2,6,8,5,9]
y = [5,2,9,1,0,5]
plt.title("GARPH WITH MARKER")
plt.xlabel("X-Axis")
plt.ylabel("Y_Axis")
plt.plot(x,y,color = "blue",ls = "-.",marker = "*",markersize = 15,markerfacecolor ="red",label = "marker")
plt.legend()
plt.show()