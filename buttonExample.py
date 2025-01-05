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


    root = Tk()         #root is main frame

    def show():
        print("Button was clicked....")



    buttonok = Button(root)
    buttonok.place(relx = 0.18, rely = 0.17, relheight = 0.15, relwidth = 0.18)
    buttonok.configure(activebackground = "#89CFF0")
    buttonok.configure(text = "OK")
    buttonok.configure(background = "#add8e6")
    buttonok.configure(command = show)

    root.title("Button Example")
    root.mainloop()