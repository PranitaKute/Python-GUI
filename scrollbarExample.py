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


root = Tk()

scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)


datalist = Listbox(root, yscrollcommand = scrollbar.set)

for nos in range(101):
    datalist.insert(END, str(nos)+"Welcome Python GUI Developers!!.. We love Coding!")
datalist.pack(side =LEFT, fill= BOTH)
scrollbar.configure(command = datalist.yview)   #adds scrollbar within the listbox

root.title("Scrollbar Example")
root.mainloop()