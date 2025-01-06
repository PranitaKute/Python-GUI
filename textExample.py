try:
    from tkinter import *
except ImportError:
    from tkinter import *


try:
    import ttk 
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 =True


root= Tk()  #frame


text = Text(root)
text.insert(INSERT,"Hello python coders!")
text.insert(END, "Python GUI is Fun!")
text.pack()

text.tag_add("add","1.0","1.8")
text.tag_add("demo","1.22","1.30")

text.tag_config("add", background = "yellow", foreground = "red")
text.tag_config("demo", background = "aqua", foreground = "red")


root.title("Text Example")
root.mainloop()