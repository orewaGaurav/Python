class Employee():
    def __init__(self,name,salary,age):
        self.name = name
        self.salary = salary
        self.age = age
    def display(self):
        print("Name of the employee:",self.name)
        print("Salary of the employee:",self.salary)
        print("Age of the employee:",self.age)
class All_employess(Employee):
    def __init__(self,name,salary,age,id):
        super().__init__(name,salary,age)
        self.id = id
    def display1(self):
        self.display()
        print("employee id:",self.id)
g = Employee("Gaurav","$900",24)
p  =Employee("Lavesh","$2k",30) 
l = Employee("Priyanshu","$1k",26)
g.display()
p.display()
l.display()


#code 
