#works on IDLE

# #import module
# from tkinter import *
# #create root window
# root = Tk()
# #root window title and dimension
# root.title("welcome to GeekForGeeks")
# # set geometry(width x height)
# root.geometry("350x200")
# root.mainloop()

#Import Module

from tkinter import*

#create root window

root=Tk()
root.title("Welcome to root ")

#set geometry (width x height)

root.geometry('350x200')

mylabel1=Label(root,text="hello students",background='pink')
mylabel2=Label(root,text="NIET",background='green')

mylabel1.pack(padx=50)
mylabel2.pack(padx=120)

root.mainloop()