a = ['a','v','c','d','e','w','i','p','a']
def remove (x):
    b = ['a','e','i','o','u']
    if x in b:
        return False
    else:
        return True
vowelout = filter(remove,a)
print(list(vowelout))
