class A():
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    #1. Create Public method to access private value
    def display(self):
        print(self.__salary)
e1=A("Ram",2500000)
e1.display()
print(e1.name)#it will throw name error 
#print(e1.__salary)#it will not show salary because salary is private
#There are two methods to access private value 
#2. Use name mangling
print(e1._A__salary)
#Objectname._classname__variable  syntax