#to use reduce we have to import it first
from functools import reduce 
l = [1,2,3,4,1,1,23,45]
def sumof(x,y):
    return x+y
sum = reduce(sumof,l)
print(sum)