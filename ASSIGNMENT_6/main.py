
from tkinter import *
import tkinter.messagebox as messagebox
window = Tk()

window.title("My Window")
window.geometry("500x500")
window.configure(bg="skyblue")
inp = Label(window , text = "hello world")
inp.pack()

button =Button(window,text="LOGIN",command="Log_entry",width=12,bg="red",fg="white",font=("Arial",12,"bold"),
               activebackground="black",activeforeground="white")
button.pack()

menu = Menu(window)
file = Menu(menu ,tearoff=False)
file.add_command(label="New")
file.add_command(label="open")
file.add_command(label="Save")
file.add_command(label="Save as")
file.add_separator()
file.add_command(label="Exit",command=window.quit)
menu.add_cascade(label="File",menu=file)
window.config(menu=menu)

messagebox.showwarning("Message","Hello World")
messagebox.askyesnocancel("Message","Hello World")

c = Canvas(window,width=500,height=500)
c.pack()
c.create_line(0,0,500,500,width=5,fill="green",dash=(2,2))
c.create_line(0,500,500,0,width=5,fill="blue",dash=(2,2))
c.create_rectangle(200,200,300,300,fill="red",outline="yellow",width=5)


button =Button(window, text = "Helo" )
button.place(x=20,y=40)

window.mainloop()


