#slicing
#find the area of triangle using herons formula
a = int(input("Enter value of 1st side: "))
b = int(input("Enter value of 2nd side: "))
c = int(input("Enter value of 3rd side: "))
s = (a+b+c)/2
a = (s*(s-a)*(s-b)*(s-c))**(1/2)
print("Area of the given triangle is: ",a)

