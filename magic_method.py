# class xyz():
#     def __init__(self):
#         print("init function")
#     def display(self):
#         print("another method")
# xyz()

# #__new__method
# class person():
#     def __new__(self):
#         print("new method")
#     def __init__(self):
#         print("Init method")
# person()

class myClass():
    def __init__(self,value):
        self.value = value 
    def display(obj):
        print("Value of x:",obj.value)
obj = myClass(10)
obj.display()
