# str =  "RAMA"
# print(str[1])
# str[1] = "d"
# print(str)

# def outerfunction(text):
#     def innerfunction():
#         print(text)
#     return innerfunction
# myfunction = outerfunction("Gaurav")
# myfunction()


def xyz():
    count = 0
    def counter():
        nonlocal count
        count  +=1
        return count
    return counter
p1 = xyz()
p2 = xyz()
print(p1())
print(p1())
print(p1())
print(p1())
print(p2())
print(p2())
print(p2())
