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

menubutton = Menubutton(root, text="Drop Down")
menubutton.grid()
menubutton.menu = Menu(menubutton, tearoff=0)
menubutton["menu"] = menubutton.menu

fileVar = IntVar
editVar = IntVar
helpVar = IntVar

menubutton.menu.add_checkbutton(label = "File", variable = fileVar)
menubutton.menu.add_checkbutton(label = "Edit", variable = editVar)
menubutton.menu.add_checkbutton(label = "Help", variable = helpVar)

menubutton.pack()


root.title("Menu Button Example")
root.mainloop()