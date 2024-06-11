#map
def mysquare(x):
    return x**2
mylist = [10,11,12,13,14]
mob = map(mysquare,mylist)
mylist1 = list(mob)
print("original is",mylist)
print("new is",mylist1)
