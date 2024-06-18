# lis = [1,2,3,4,5,6,7,8]
# print(type(lis))
# for i in lis:
#     print(i)
# x = iter(lis)
# print(type(x))
# print(x)
# y = "GAURAV"
# z = iter(y)
# print(dir(y))
# print(dir(z))


# x = "PYTHON TIWARI"
# y = iter(x)#iterator
# # print(type(y))
# # print(y)
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))

# class xyz():
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         x = self.a
#         self.a +=1
#         return x
# p1 = xyz()
# myiter = iter(p1)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

def xyz():
    i = 1
    while(i<=10):
        return i
print(xyz())
print(type(xyz))

def xyz():
    i = 1
    while(i<=10):
        yield i
print(xyz())
print(type(xyz))