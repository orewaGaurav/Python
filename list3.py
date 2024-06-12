number = [2,5,8,32,64,7,47,38,74,97,53]
print(f"Given List is:{number}")
def even(number):
    for i in range(1,len(number)):
        if i %2 == 0:
            return True
        else:
            return False
        

