#Calculator using GUI
#THIS IS MY CODE FOR CALCULATOR 
from tkinter import *
root=Tk()
root.title("Hello it's me Calculator")
root.geometry("700x500")
def startnow():
    label=Label(root,text="Basic operation calculator",font=("arial",20),bg="white",fg="black")
    label.grid(row=0,column=1)
    def close():
        exit()
    def add():
        a=float(entry1.get())
        b=float(entry2.get())
        result.config(text=f"Sum : {a+b}")
    def sub():
        a=float(entry1.get())
        b=float(entry2.get())
        result.config(text=f"Difference : {a-b}")
    def mul():
        a=float(entry1.get())
        b=float(entry2.get())
        result.config(text=f"Multiply : {a*b}")
    def div():
        a=float(entry1.get())
        b=float(entry2.get())
        if(b>0):
            result.config(text=f"Division : {(a/b):.2f}")
        else:
            result.config(text="Divisor is zero")
    label1=Label(root,text="Number 1",font=("arial",20),bg="white",fg="black")
    label1.grid(row=2,column=0,padx=10,pady=5)
    entry1=Entry(root,text="Enter first number",font=("arial",20))
    entry1.grid(row=2,column=1,padx=10,pady=5)
    label2=Label(root,text="Number 2",font=("arial",20),bg="white",fg="black")
    label2.grid(row=3,column=0,padx=10,pady=5)
    entry2=Entry(root,text="Enter second number",font=("arial",20))
    entry2.grid(row=3,column=1,padx=10,pady=5)
    addlabel=Label(root,text="Add",font=("arial",20),bg="white",fg="black")
    addlabel.grid(row=4,column=0)
    sublabel=Label(root,text="Substract",font=("arial",20),bg="white",fg="black")
    sublabel.grid(row=5,column=0)
    mullabel=Label(root,text="Multiply",font=("arial",20),bg="white",fg="black")
    mullabel.grid(row=6,column=0)
    divlabel=Label(root,text="Divide",font=("arial",20),bg="white",fg="black")
    divlabel.grid(row=7,column=0)
    addbutton=Button(root,text="+",command=add,font=("arial",20),bg="white",fg="black")
    subbutton=Button(root,text="-",command=sub,font=("arial",20),bg="white",fg="black")
    mulbutton=Button(root,text="*",command=mul,font=("arial",20),bg="white",fg="black")
    divbutton=Button(root,text="/",command=div,font=("arial",20),bg="white",fg="black")

    addbutton.grid(row=4,column=1)
    subbutton.grid(row=5,column=1)
    mulbutton.grid(row=6,column=1)
    divbutton.grid(row=7,column=1)
    button=Button(root,text="Close",command=close,font=("arial",20),bg="white",fg="black")
    button.grid(row=0,column=4)
    result=Label(root,text="Result : ",font=("arial",20),bg="white",fg="black")
    result.grid(row=4,column=2)
label=Label(root,text="Basic operation calculator",font=("arial",20),bg="white",fg="black")
label.grid(row=0,column=1)
start=Button(root,text="Start",font=("arial",20),bg="white",fg="black",command=startnow)
start.grid(row=1,column=4)
root.mainloop()
