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

    var = StringVar()
    var2 = StringVar()

    text1 = Label(root, textvariable = var, relief = RAISED)
    var.set("Bonjour Python coders! We love python programming")
    text1.pack()

    text2 = Label(root, textvariable = var2, relief = RAISED)
    var2.set("Hello coders..... Hello developers!")
    text2.pack()


    root.title("Label Example")
    root = mainloop()