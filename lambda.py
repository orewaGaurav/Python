# gaurav = lambda a,b : a*b
# print(gaurav(2,4))

# sum = lambda a,b,c:(a+b+c)/2
# x = sum(3,4,5)
# print(x)



# list = list(map(int,input("Enter the list: ").split(",")))
# print(list)



# l = [2,3,4,5,6,7,8,9]
# l1 = []
# for i in l:
#     l1.append(i**2)
# print(l1)

l = [2,3,4,5,6,7,8,9]
l1 = []
for i in range(len(l)):
    l1.append((l[i])**2)
print(l1)
print(len(l))

#map
# l =[1,2,3,4,5,6,7,8,9]
# sqrl = list(map(lambda x:x**2,l))
# print(sqrl)


#filter
# l =[1,2,3,4,5,6,7,8,9]
# evenl = list(filter(lambda x:x%2 == 0,l))#har function k liye true or false dega pr kwal true wla ko print karega
# print(evenl)

