class circle():
    pi = 3.14
    def __init__(self):
        self.radius = int(input("Enter the number: "))
    def area(self):
        return circle.pi*self.radius**2
    def circumference(self):
        return 2*circle.pi*self.radius
newcircle=circle()
print("area of circle",newcircle.area())
print("circumference",newcircle.circumference())