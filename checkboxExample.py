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
    checkVar1 = IntVar()
    checkVar2 = IntVar()
    checkVar3 = IntVar()

    c1 = Checkbutton(root, text = "Dancing", variable = checkVar1, onvalue = 1, offvalue = 0, height = 5, width = 20)
    c2 = Checkbutton(root, text = "Reading", variable = checkVar2, onvalue = 1, offvalue = 0, height = 5, width = 20)
    c3 = Checkbutton(root, text = "Singing", variable = checkVar3, onvalue = 1, offvalue = 0, height = 5, width = 20)

    c1.pack()
    c2.pack()
    c3.pack()


    root.title("Checkbox Example")
    root.mainloop()