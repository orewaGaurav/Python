#write a program to deposit or
#withdraw money in a bank account

# class account():
#     def __init__(self):
#         self.balance = 0
#         print("Acount open successfully")
#     def deposit(self):
#         amount = float(input("Enter the amount: "))
#         self.balance += amount
#     def withdraw(self):
class student():
    #class variable
    school_name = "NIET"
    def __init__(self,name,id):
        #instance method
        self.name = name
        self.id = id
    @classmethod
    def change_school(cls,new_name):
        cls.school_name = new_name
    def display_details(self):
        #instance method to display student details 
        print(f"School Name: {student.school_name}")
        print(f"Student Name: {self.name}")
        print(f"Student id: {self.id}")
s1 = student("Gaurav",23)
s1.display_details()
student.change_school("Galgotia University")

s2 = student("Lavesh",33)
s2.display_details()
student.change_school("GL Bajaj")
s3 = student("priyanshu",40)
s3.display_details()

print("______________________________________________________________________")
#change school name using class method
# student.change_school("GL Bajaj")

class Gaurav():
    def __init__(self):
        print("hlw Gaurav")
    def __init__(self):
        print("Tata Bye bye")
a = Gaurav()

# l  = list(map(int,input("x: ").split(" ")))
# print(*l,end = ",")
# print("hlw gobar")