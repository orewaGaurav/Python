from tkinter import *
def draw_shape():
    canvas.create_rectangle(50,50,150,150,fill = 'blue')
    canvas.create_oval(200,50,300,150,fill ='red')
    canvas.create_line(350,50,450,150,fill = 'green')
    
root = Tk()
canvas = Canvas(root,width=500,height=200)
canvas.pack()
button = Button(root,text="Draw",command = draw_shape)
button.pack()
root.mainloop()



