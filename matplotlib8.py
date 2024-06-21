import matplotlib.pyplot as plt
branch =['AILM','CSE','CYS','CS','IT','IOT','DS','AI','ECE','BT']
no_of_boys = [23,25,26,56,54,51,53,61,54,45]
no_of_girls =[11,13,15,10,17,21,23,34,43,26]
plt.pie(no_of_boys,labels =branch,autopct="%1.1f%%")
plt.title("N0. OF BOYS")
plt.show()
plt.pie(no_of_girls,labels =branch,autopct="%1.1f%%")
plt.title("N0. OF GIRLS")
plt.show()

plt.stackplot(branch,no_of_boys,no_of_girls,labels=["Boys","Girls"])
plt.legend()
plt.grid()
plt.show()

plt.bar(branch,no_of_girls)
plt.title("Gender Ratio")
plt.xlabel("Name of Branch")
plt.ylabel("No. of girls")
plt.grid()
plt.show()


plt.bar(branch,no_of_boys)
plt.title("Gender Ratio")
plt.xlabel("Name of Branch")
plt.ylabel("No. of boys")
plt.grid()
plt.show()