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

text = StringVar()
label = Message(root, textvariable = text, relief = RAISED)
text.set("Hello Python Coders!!.. We love Python Programming!!..")
label.pack()

root.title("Message Example")
root.mainloop()