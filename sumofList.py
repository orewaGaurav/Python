#1
'''x = [1,2,3,4,5,6,7,8,9]
print(sum(x))
summ = 0
for i in range(len(x)):
    summ+=x[i]
print(summ)

'''
#2

x = [1,2,3,4,5,6,7,8,9]
l = []
for i in range(len(x)):
    l.append(x[i]**3)
print(l)
print(*l)
print(*l,sep = "\n")
    
#3

x = [1,2,3,4,5,6,7,8,9]
product = 1
for i in range(len(x)):
    product *= x[i]
print(product)
