"""try:
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

root1 = Toplevel()
root1.title("Frame 2")

root2 = Toplevel()
root2.title("Frame 3")


root.title("Top Level Example")
root.mainloop()
"""

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

def popup():
    root1 = Toplevel(root)
    root1.mainloop()

button = Button(root, text = "Show PopUp", command = popup)
button.pack()

root.mainloop()