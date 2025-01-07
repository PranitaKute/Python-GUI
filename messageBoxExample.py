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

from tkinter import messagebox

# import tkMessageBox   (Before python 3)

root = Tk()

def msg():
    messagebox.showinfo("Important Message", "This is an example of MessageBox in Python")
    messagebox.askquestion("Your Name", "Value")
    messagebox.askokcancel("Your Name", "Value")
    messagebox.askretrycancel("Your Name", "Value")
    messagebox.showerror("Your Name", "Value")

#   tkMessageBox.showInfo("Important Message", "Example")


button = Button(root, text = "Show Message", command = msg)
button.pack()



root.title("Message Box Example")
root.mainloop()