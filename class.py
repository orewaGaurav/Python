# class class_name:
#     x = 67
# c =class_name()
# print(c.x)

# class student:
#     def __init__(self,name,age):
#         self.name1 = name
#         self.age = age
# s1 = student("Gaurav",19)
# print(s1.name1)
# print(s1.age)

# class student:
#     def __init__(self):
#         self.name1 = input("Enter the name student")
#         self.age = int(input("enter the students age"))
#         self.roll = int(input("enter"))
# s1 = student()
# print(s1.name1)
# print(s1.age)
# print(s1.roll)

# class circle():
#     pi=3.14
#     def __init__(self):
#         self.radius=int(input('enter the radius:'))
#     def area(self):
#         return circle.pi*self.radius**2
#     def circumference(self):
#         return 2*circle.pi*self.radius
# newcircle=circle()
# print('area of circle',newcircle.area())
# print('circumference of circle',newcircle.circumference())

# class circle():
#     pi = 3.14
#     def __init__(self):
#         self.radius = int(input("Enter the number: "))
#     def area(self):
#         return circle.pi*self.radius**2
#     def circumference(self):
#         return 2*circle.pi*self.radius
# newcircle=circle()
# print("area of circle",newcircle.area())
# print("circumference",newcircle.circumference())

# class Rectangle():
#     def __init__(self,length,width):
#         # self.length = float(int(input("Enter the length: ")))
#         self.length = length
#         self.width = width
#     def area(self):
#        print("area is :",self.length* self.width)
#     def perimeter(self):
#         print("Perimeter is:",2*(self.length+self.width))
# a = Rectangle(8,5)
# a.area()
# a.perimeter()

class rectangle():
    def __init__(self,length,width):
        self.length = length 
        self.width = width
    def area(self):
        return self.length*self.width
a = rectangle(8,5)
print(a.area())