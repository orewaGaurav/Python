# Day 8
# code1
from tkinter import *
root =Tk()
root.geometry('550x550')
root.title("Windows close Automatically")
mylabel = Label(root,text="Good Bye").pack(pady=20)
root.after(5000,lambda:root.destroy())
root.mainloop()

# code 2
from tkinter import *
root =Tk()
root.geometry('550x550')
root.title("List box")
lb =Listbox(root)
lb.insert(1,"CSE")
lb.insert(2,"AIML")
lb.insert(3,"CYS")
lb.insert(4,"AI")
lb.pack()

