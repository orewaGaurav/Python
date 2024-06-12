def factorial(x):
    a = 1
    for i in range(1,x+1):
        a*=i
    return a

#factorial(int(input("Enter the number: ")))
n = int(input("Enter the number: "))
r = int(input("Enter the number: "))
a = factorial(n)
b = factorial(r)
c = factorial(n-r)
print((a)/(b*c))
