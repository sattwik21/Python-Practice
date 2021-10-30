# To make a calculator using tkinter

from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Calculator")
root.geometry("450x400")

def Addition():
    n1 = eval(num_1.get())
    n2 = eval(num_2.get())
    result = n1 + n2
    messagebox.showinfo("Sum" , result)

def Subtraction():
    n1 = eval(num_1.get())
    n2 = eval(num_2.get())
    result = n1 - n2
    messagebox.showinfo("Difference" , result)

def Multiplication():
    n1 = eval(num_1.get())
    n2 = eval(num_2.get())
    if (n1 == 0 or n2 == 0):
        messagebox.showinfo("Product" , "0")
    else:
        result = n1 * n2
        messagebox.showinfo("Product" , result)
        
def Division():
    n1 = eval(num_1.get())
    n2 = eval(num_2.get())
    if (n2 == 0):
        messagebox.showinfo("Division" , "Error")
    elif (n1 == 0 and n2 != 0):
        messagebox.showinfo("Division" , "0")
    else:
        result = n1 / n2
        messagebox.showinfo("Division" , result)
        
def Percentage():
    n1 = eval(num_1.get())
    result = n1 / 100
    messagebox.showinfo("Percentage" , result)

def Square():
    n1 = eval(num_1.get())
    result = n1 ** 2
    messagebox.showinfo("Square" , result)

def Cube():
    n1 = eval(num_1.get())
    result = n1 ** 3
    messagebox.showinfo("Cube" , result)

def Power():
    n1 = eval(num_1.get())
    n2 = eval(num_2.get())
    result = n1 ** n2
    messagebox.showinfo("Power" , result)

def Pi():
    n1 = eval(num_1.get())
    n2 = eval(num_2.get())
    result = n1 * n2 * 3.14159265
    messagebox.showinfo("Pi" , result)

def Square_root():
    n1 = eval(num_1.get())
    result = n1 ** (1/2)
    messagebox.showinfo("SquareRoot" , result)

def Cube_root():
    n1 = eval(num_1.get())
    result = n1 ** (1/3)
    messagebox.showinfo("CubeRoot" , result)

def Power_root():
    n1 = eval(num_1.get())
    n2 = eval(num_2.get())
    result = n1 ** (1/n2)
    messagebox.showinfo("PowerRoot" , result)

def Reciprocal():
    n1 = eval(num_1.get())
    result = 1 / n1
    messagebox.showinfo("Reciprocal" , result)

def Factorial():
    n1 = eval(num_1.get())
    fact = 1
    for i in range(n1,0,-1):
        fact = fact * i
    result = fact
    messagebox.showinfo("Factorial" , result)

def Exponential():
    n1 = eval(num_1.get())
    result = pow(2.7182 , n1)
    messagebox.showinfo("Exponent" , result)
    
    
first_num = Label(root , text = "Enter the 1st number : " , font = "bold")
second_num = Label(root , text = "Enter the 2nd number : " , font = "bold")
num_1 = Entry(root)
num_2 = Entry(root)

add = Button(root , text = "   +   " , font = "bold" , command = Addition)
subtract = Button(root , text = "   -   " , font = "bold" , command = Subtraction)
multiply = Button(root , text = "   *   " , font = "bold" , command = Multiplication)
divide = Button(root , text = "   /   " , font = "bold" , command = Division)
percent = Button(root , text = "   %   " , font = "bold" , command = Percentage)
sqr = Button(root , text = " x^2 " , font = "bold" , command = Square)
cube = Button(root , text = " x^3 " , font = "bold" , command = Cube)
power = Button(root , text = " x^y " , font = "bold" , command = Power)
pi = Button(root , text = "   pi   " , font = "bold" , command = Pi)
sqr_root = Button(root , text = "x^(1/2)" , font = "bold" , command = Square_root)
cube_root = Button(root , text = "x^(1/3)" , font = "bold" , command = Cube_root)
power_root = Button(root , text = "x^(1/y)" , font = "bold" , command = Power_root)
reciprocal = Button(root , text = " 1/x " , font = "bold" , command = Reciprocal)
factorial = Button(root , text = " x! " , font = "bold" , command = Factorial)
exp = Button(root , text = " e^x " , font = "bold" , command = Exponential)

first_num.grid(row = 0 , column = 0)
second_num.grid(row = 2 , column = 0)
num_1.grid(row = 0 , column = 3)
num_2.grid(row = 2 , column = 3)

add.place(x = 10 , y = 70)
subtract.place(x = 200 , y = 70)
multiply.place(x = 10 , y = 120)
divide.place(x = 200 , y = 120)
percent.place(x = 390 , y = 70)
pi.place(x = 390 , y = 120)
sqr.place(x = 10 , y = 170)
cube.place(x = 200 , y = 170)
power.place(x = 390 , y = 170)
sqr_root.place(x = 10 , y =  220)
cube_root.place(x = 200 , y = 220)
power_root.place(x = 390 , y = 220)
reciprocal.place(x = 10 , y = 270)
factorial.place(x = 200 , y = 270)
exp.place(x = 390 , y = 270)

root.mainloop()
