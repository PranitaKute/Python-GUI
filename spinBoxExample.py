try:
    from tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk 
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


root = Tk() 

numberBox = Spinbox(root, from_ = 0, to=100)
numberBox.pack()


root.title("SpinBox Example")
root.mainloop()