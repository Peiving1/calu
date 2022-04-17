from tkinter import *

root = Tk()


#Width to change the width of the entry box
#borderwidth to change to size of the border around the entry box
#fg and bg to change colors

gunnis = LabelFrame(root, text="Enter your stupid name...", padx=50, pady=50)
gunnis.grid(padx=10, pady=10)

e = Entry(gunnis, width=20, borderwidth=1)
e.grid(row=0,column=0)

e.insert(0, "Enter your name: ")

def myClick():
    Hello = "Hello " + e.get() + "!"
    myLabel = Label(gunnis, text=Hello)
    myLabel.grid(row=3,column=0, columnspan=2)
    myButton = Button(gunnis, text="Hey, " + e.get(), state=DISABLED)
    myButton.grid(row=2, column=1)


myButton = Button(gunnis, text="Enter your name", command=myClick, fg="blue", bg="pink")
myButton.grid(row=2,column=1)

root.mainloop()