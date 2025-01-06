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
    
    frame = Frame(root)
    label = Label(frame, text = "User Name : ")
    label.pack(side = LEFT)
    user = Entry(frame, bd = 5)
    user.pack(side = LEFT)
    frame.pack()

    frame2 = Frame(root)
    label2 = Label(frame2, text = "Password :")
    label2.pack(side = LEFT)
    passw = Entry(frame2, bd = 5)
    passw.pack(side = LEFT)
    frame2.pack(side = BOTTOM)





    root.title("Entry Example")
    root.mainloop()
