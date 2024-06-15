#code 1
# def xyz():
#     print("Hello")
# def decor(fun):
#     fun()
#     print("How are you?")
# decor(xyz)


#code 2
# def decor(xyz):
#     def innerfunction():
#         xyz()
#         print("GAURAV")
#     return innerfunction
# @decor 
# def xyz():
#     print("HELLO")
# xyz()

#code3
# def decor(add):
#     def inner():
#         result = add()
#         z = int(input("Enter the third no: "))
#         result += z
#         return result
#     return inner

# def gaurav(add):
#     def secondinner():
#         newResult = add()
#         p = int(input("enter the 4th num: "))
#         newResult -= p
#         return newResult
#     return secondinner
# @gaurav
# @decor

# def add():
#     x = int(input("enter the first no: "))
#     y = int(input("Enter the secoond number: "))
#     return x+y
# print(add())
  

# code 4
def decor(name):
    def inner():
        print("*************")
        name()
        print("*************")
    return inner
@decor
def name():
    print("GAURAV KUMAR")
name()

# #code 4 method 2
# def decor(name):
#     def inner():
#         print("*************")
#         print(name())
#         print("*************")
#     return inner
# @decor
# def name():
#     return "GAURAV KUMAR"
# name()