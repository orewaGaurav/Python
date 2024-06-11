#factorial
def factorial(x):
    a = 1
    for i in range(1,x+1):
        a*=i
    print(a)
factorial(int(input("enter the num: ")))


