#code1
class person():
    def __init__(self):
        self.name = input("enter the name: ")
        self.money = int(input("enter the money: "))
        print(self.name)
        print(self.money)
class pinku(person):
    def __init__(self):
        self.id = int(input("enter the id: "))
        self.roll_no = int(input("enter the roll_no: "))
        print(self.id)
        print(self.roll_no)
    
# p =pinku()
# q = person()

#code 2

# class person():
#     def __init__(self,name,money):
#         self.name = name
#         self.money = money
#         print(f"{self.name} has {self.money} money")

# class pinku(person):
#     def __init__(self,name,money):
#         super().__init__(name,money)
#         print("inside pinku class statement")
#     pass
# p = pinku("ram",4000)


#code3


# class Father():
#     money = 10000
#     def show(self):
#         print("parent class instance method")
#     @classmethod
#     def showmoney(cls):
#         print("parent class class method: ",cls.money)
#     @staticmethod
#     def stat():
#         a = 10
#         print("parent class static method",a)
# class son(Father):
#     def disp(self):
#         print("child class instance method")
# s = son()
# s.disp()
# s.show()
# s.showmoney()
# s.stat()

# s1 = Father() #this will through a error
# s1.disp()


#code 4 #multilevel inheritance program

# class Father():
#     def __init__(self):
#         print("Father class constructor")
    
#     def showF(self):
#         print("father class method")
    
# class son(Father):
#     def __init__(self):
#         print("constructor of son class")
#     def showS(self):
#         print("son class method")

# class grandson(son):
#     def __init__(self):
#         #super().__init__()
#         print("grandson constructor")
#     def showG(self):
#         print("class method of grandson")
# p = grandson()#prints constructor of this class
# p.showF()
# p.showS()
# p.showG()

#using super().__init__()

# class Father():
#     def __init__(self):
#         print("Father class constructor")
    
#     def showF(self):
#         print("father class method")
    
# class son(Father):
#     def __init__(self):
#         super().__init__()
#         print("constructor of son class")
#     def showS(self):
#         print("son class method")

# class grandson(son):
#     def __init__(self):
#         super().__init__()
#         print("grandson constructor")
#     def showG(self):
#         print("class method of grandson")
# p = grandson()
# p.showF()
# p.showS()
# p.showG()

#CODE 5
# class x:
#     pass
# class y:
#     pass
# class z:
#     pass
# class a(x,y):
#     pass
# class b(y,z):
#     pass
# class d(a,b,z):
#     pass
# for i in d.mro():
#     print(i)
