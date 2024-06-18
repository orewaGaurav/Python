#1st program
# from tkinter import *
# root = Tk()
# root.geometry("450x550")
# root.title("Adding label")
# mylabel1 =Label(root,text="Hello students",foreground="red",background = "blue")
# mylabel2 = Label(root,text="Niet welcomes you all",background = 'green')
# mylabel1.pack()
# mylabel2.pack()
# def click():
#     mylabel = Label(root,text = "Welcome")
#     mylabel.pack()
# mybutton = Button(root,text= "click",padx =50,command = click)
# mybutton.pack(pady=100)
# root.mainloop()

#second program

# from tkinter import *
# root = Tk()
# root.geometry("450x550")
# root.title("Counter Button")
# counter = 0
# def click():
#     global counter
#     counter +=1
#     mylabel.configure(text=f"you clicked {counter} times")
#     if counter>10:
#         mybutton.configure(state = DISABLED)
#         mylabel.configure(text = "shut up!")

# mylabel = Label(root,text = "no click")
# mylabel.pack()
# mybutton = Button(root,text= "click",padx =50,command = click)
# mybutton.pack(pady=100)
# root.mainloop()

#third program
# from tkinter import *
# root  = Tk()
# root.title = ("Entry Widgets")
# ent = Entry(root,width = 30,borderwidth = 5)
# ent.pack()
# root.mainloop()

#program 4
# from tkinter import *
# root  = Tk()
# root.geometry("550x550")
# root.title = ("Entry Widgets")
# ent = Entry(root,width = 30,borderwidth = 5,fg = 'red',bg = 'yellow')
# ent.pack()
# def click():
#     x = ent.get()
#     mylabel = Label(root,text = x)
#     mylabel.pack()
#     ent.delete(0,END)
# mybutton = Button(root,text = "Click",command=click)
# mybutton.pack()
# root.mainloop()


#slight change in output
# from tkinter import *
# root  = Tk()
# root.geometry("550x550")
# root.title = ("Entry Widgets")
# ent = Entry(root,width = 30,borderwidth = 5,fg = 'red',bg = 'yellow')
# ent.pack()
# ent.insert(0,"Write Your Name:")
# def click():
#     x = ent.get()
#     mylabel = Label(root,text = x)
#     mylabel.pack()
#     ent.delete(0,END)
# mybutton = Button(root,text = "Click",command=click)
# mybutton.pack()
# root.mainloop()

#program 5
#TEXT widgets(text feild) for multiple user input

# from tkinter import *
# root  = Tk()
# root.geometry("550x550")
# root.title = ("Text Widgets")
# myframe = LabelFrame(root,padx = 5,pady =5,text = 'Myframe')
# myframe.pack()
# mylabel= Label(myframe,text = "My name")
# mylabel.pack()
# mybutton = Button(myframe,text = "My name")
# mylabel.pack()
# mybutton = Button(myframe,text = "click")
# mybutton.pack()
# root.mainloop()

