#Tuple
tup = ("abcd",786,23.34,"John",70.2)
print(tup)
print(type(tup))
list1 = list(tup)

list1[0] = "Ram"
tup2 = tuple(list1)
print(tup2)

list1 = ['ram',24,"sita",42.3,2+3j]
list1.append("T")
#print(list1)
print(list1.pop())
print(list1[2][2])
