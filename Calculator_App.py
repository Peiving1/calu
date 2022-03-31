from tkinter import *
import math

root = Tk()
root.title("A Normal Calculator")

e = Entry(root, width=30, borderwidth=10)
e.grid(row=0, column=0, columnspan=5)


def button_click(number):
    # e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    num1 = e.get()
    num1 = int(num1)
    global f_num
    global math
    math = "addition"
    f_num = num1
    e.delete(0, END)

def button_multiply():
    num1 = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(num1)
    e.delete(0, END)

def button_divide():
    num1 = e.get()
    global f_num
    global math
    math = "divide"
    f_num = int(num1)
    e.delete(0, END)

def button_subtract():
        num1 = e.get()
        global f_num
        global math
        math = "subtract"
        f_num = int(num1)
        e.delete(0, END)

def button_equal():
    num2 = e.get()
    e.delete(0, END)
    # e.insert(0, f_num + int(num2))

    if math == "multiply":
        e.insert(0,f_num * int(num2))
    elif math == "addition":
        e.insert(0, f_num + int(num2))
    elif math == "divide":
        e.insert(0, f_num / int(num2))
    elif math == "subtract":
        e.insert(0, f_num - int(num2))

def button_sqrt():
    num1 = e.get()
    e.delete(0, END)
    num1 = int(num1)
    num2 = math.sqrt(num1)
    e.insert(0, str(num2))



# Define Buttons

button_1 = Button(root, text="1", padx=25, pady=20,
                  command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=25, pady=20,
                  command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=25, pady=20,
                  command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=25, pady=20,
                  command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=25, pady=20,
                  command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=25, pady=20,
                  command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=25, pady=20,
                  command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=25, pady=20,
                  command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=25, pady=20,
                  command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=25, pady=20,
                  command=lambda: button_click(0))
button_add = Button(root, text="+", padx=28, pady=20,
                    command=button_add)
button_clear = Button(root, text="C", padx=24, pady=20,
                      command=button_clear, fg="red")
button_equal = Button(root, text="=", padx=25, pady=20,
                      command=button_equal)
button_subtract = Button(root, text="-", padx=29, pady=20,
                    command=button_subtract)
button_divide = Button(root, text="/", padx=29, pady=20,
                    command=button_divide)
button_multiply = Button(root, text="*", padx=29, pady=20,
                    command=button_multiply)
button_sqrt = Button(root, text="√", padx=25, pady=20,
                     command=button_sqrt)


# Put buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_equal.grid(row=4, column=2)
button_clear.grid(row=4, column=1)
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_sqrt.grid(row=5, column=0)


root.mainloop()
