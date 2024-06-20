import numpy as np
a = np.array([[2,0,3],[3,5,8],[6,4,1]])
print(a)
a1=np.where(a>3,True,False)
print(a1)
a2 = np.where(a>0,a,0)
print(a2)

# code 2
b= np.array([[2,5,7,9],[3,0,-2,6],[2,4,5,1],[3,2,-7,6]])
print(b)
b1 = np.where(b>3,b*3,b**3)
print(b1)
np.savetxt(r'/Users/gauravkumar/Desktop/Telegram/filehandling.txt',b1,fmt="%d")
#we are saving this program at desired location
# so that we can call it later