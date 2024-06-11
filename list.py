#list
list =["abcd",342,2.34,"john",70.7]
tinylist = [123,"john"]
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(list*2)
print(list+tinylist)
#list is mutable
list[0] = "GAurab"
print(list)
list[1:4] = ["Lavesh","priyanshu",69]
print(list)
list2= [i**3 for i in range(11)]
print(list2)
