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

def show():
    filewin = Toplevel(root)
    button = Button(filewin, text = "Hello")
    button.pack()


root = Tk()

menubar = Menu(root)
fileMenu = Menu(menubar, tearoff = 0)       #tearoff assigns the position
fileMenu.add_command(label = "New", command = show)
fileMenu.add_command(label = "Open", command = show)
fileMenu.add_command(label = "Save", command = show)
fileMenu.add_command(label = "Save As", command = show)
fileMenu.add_command(label = "Exit", command = show)
fileMenu.add_separator()        #the lines present after each option
fileMenu.add_command(label = "Quit", command = root.quit)
menubar.add_cascade(label = "File", menu = fileMenu)


editMenu = Menu(menubar, tearoff = 0)
editMenu.add_command(label = "Undo", command = show)
editMenu.add_separator()
editMenu.add_command(label = "Cut", command = show)
editMenu.add_command(label = "Copy", command = show)
editMenu.add_command(label = "Paste", command = show)
editMenu.add_command(label = "Select All", command = show)
editMenu.add_command(label = "Delete", command = show)
menubar.add_cascade(label = "Edit", menu = editMenu)


helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label = "Help Details", command = show)
helpmenu.add_command(label = "About Textpad", command = show)
menubar.add_cascade(label = "Help", menu = helpmenu)


root.configure(menu = menubar)


root.title("Notepad")
root.mainloop()