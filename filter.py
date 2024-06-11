val = [1,3,4,6,8,9,65,45,32,42,68]
def even(x):
    if x%2 ==0:
        return True
    else :
        return False

a = filter(even,val)
for i in a:
    print(i)
