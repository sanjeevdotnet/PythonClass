from tkinter import *
import tkinter.messagebox as messagebox

window = Tk()
window.title("Sanjeev Calculator")
window.geometry("300x210")
window.configure(bg = "lightgray")
window.resizable(width=False, height=False)

e = Entry(window, width = 38, borderwidth = 5)
e.place(x = 10, y = 10)
math =""
i = 0
#Buttons
def button_clicked(num):
    result = e.get()
    e.delete(0, END)
    num_result =  "".join(filter(str.isdigit, result))
    e.insert(0, str(num_result) + str(num))

def add():
    n1 = e.get()
    num_n1 = "".join(filter(str.isdigit, n1))
    global math
    math = "Addition"
    global i
    if num_n1 != "":
        i=int(num_n1)
    e.delete(0, END)

def sub():
    n1 = e.get()
    num_n1 = "".join(filter(str.isdigit, n1))
    global math
    math = "Subtraction"
    global i
    if num_n1 != "":
        i = int(num_n1)
    e.delete(0, END)

def mul():
    n1 = e.get()
    num_n1 = "".join(filter(str.isdigit, n1))
    global math
    math = "Multiplication"
    global i
    if num_n1 != "":
        i=int(num_n1)
    e.delete(0, END)

def div():
    n1 = e.get()
    num_n1 = "".join(filter(str.isdigit, n1))
    global math
    math = "Division"
    global i
    if num_n1!="" :
        i=int(num_n1)
    e.delete(0, END)

def clear():
    e.delete(0, END)

def Equals():
    n2 = e.get()
    num_n2 = "".join(filter(str.isdigit, n2))
    e.delete(0, END)
    if math == "Addition":
        e.insert(0, i + int(num_n2))
    elif math == "Subtraction":
        e.insert(0, i - int(num_n2))
    elif math == "Multiplication":
        e.insert(0, i * int(num_n2))
    elif math == "Division":
        if int(n2)!=0:
            e.insert(0, i / int(num_n2))
        else:
            e.insert(0, int(num_n2))
    else :
        e.delete(0, END)

Btn1 = Button(window, width = 8, text = '1', command=lambda: button_clicked(1))
Btn1.place(x = 10, y = 50)
Btn2 = Button(window, width = 8, text = '2', command=lambda: button_clicked(2))
Btn2.place(x = 80, y = 50)
Btn3 = Button(window, width = 8, text = '3', command=lambda: button_clicked(3))
Btn3.place(x = 150, y = 50)
BtnAdd = Button(window, width = 8, text = '+',bg = "lightblue", command= add)
BtnAdd.place(x = 220, y = 50)
Btn4 = Button(window, width = 8, text = '4', command=lambda: button_clicked(4))
Btn4.place(x = 10, y = 90)
Btn5 = Button(window, width = 8, text = '5', command=lambda: button_clicked(5))
Btn5.place(x = 80, y = 90)
Btn6 = Button(window, width = 8, text = '6', command=lambda: button_clicked(6))
Btn6.place(x = 150, y = 90)
BtnSubtract = Button(window, width = 8, text = '-',bg = "lightblue", command= sub)
BtnSubtract.place(x = 220, y = 90)
Btn7 = Button(window, width = 8, text = '7', command=lambda: button_clicked(7))
Btn7.place(x = 10, y = 130)
Btn8 = Button(window, width = 8, text = '8', command=lambda: button_clicked(8))
Btn8.place(x = 80, y = 130)
Btn9 = Button(window, width = 8, text = '9', command=lambda: button_clicked(9))
Btn9.place(x = 150, y = 130)
BtnMultiply = Button(window, width = 8, text = '*',bg = "lightblue", command= mul)
BtnMultiply.place(x = 220, y = 130)
BtnClear = Button(window, width = 8, text = 'Clear', bg = "red",fg = "white", command= clear)
BtnClear.place(x = 10, y = 170)
Btn0 = Button(window, width = 8, text = '0', command=lambda: button_clicked(0))
Btn0.place(x = 80, y = 170)
BtnEqual = Button(window, width = 8, text = '=',bg = "green",fg = "white",command= Equals)
BtnEqual.place(x = 150, y = 170)
BtnDivide = Button(window, width = 8, text = '/',bg = "lightblue", command= div)
BtnDivide.place(x = 220, y = 170)

window.mainloop()