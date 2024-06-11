'''def add() :
    x = 10
    y =20
    c = x + y
    print(c)
add()
'''
'''
def disp():
    def show():
        print("Show Function")
    print("Disp Function")
    show()
disp()

'''
'''
def add(x,y):
    c = x+y
    print(c)
add(10,20)
#add(10,20,10)
#add(30)
'''

'''
def xyz(*x):
    print(x[0]+x[1]+x[2]+x[3])
xyz(10,20,30,40)
'''

def add(**num):
    x = num["a"]+num["b"]+num["c"]
    print(x)
add(a=2,b=3,c=4)



