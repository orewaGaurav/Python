x = int(input("enter the number: "))
s = 0
for i in range(2,x):
        if x%i == 0:
            s+=1
if x == 1:
    print("not a prime")
elif s== 0:
     print("prime no")
else:
     print("not a prime no.")
     

 

