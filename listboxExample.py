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

    list = Listbox(root)
    list.insert(1 , "Python")
    list.insert(2 , "C++")
    list.insert(3 , "Java")
    list.insert(4 , "PHP")
    list.insert(5 , "C")
    list.insert(6 , "Perl")
    list.insert(7 , "Ruby")

    list.pack()


    root.title("ListBox Example")
    root.mainloop()