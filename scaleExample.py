try:
    from tkinter import *
except:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


def getValue():
    output = "Value is : " + str(var.get())
    label.config(text = output)

root = Tk()

var = DoubleVar()      #why doublevar, because we are getting data in limitations

scale = Scale(root, variable = var)
scale.pack(anchor = CENTER)

button = Button(root, text = "Get Value", command =  getValue)
button.pack(anchor=CENTER)

label = Label(root)
label.pack()

root.title("Scale Example")
root.mainloop()