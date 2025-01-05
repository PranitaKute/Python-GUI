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
    frame.pack()    #coverup whole screen
    
    frame2 = Frame(root)
    frame2.pack(side = BOTTOM)


    fileBtn = Button(frame, text = "File", fg = "red")
    fileBtn.pack(side = LEFT)

    editBtn = Button(frame, text = "Edit", fg = "red")
    editBtn.pack(side = LEFT)

    optionBtn = Button(frame, text = "Option", fg = "red")
    optionBtn.pack(side = LEFT)

    viewBtn = Button(frame2, text = "View", fg= "blue")
    viewBtn.pack(side = BOTTOM)



    root.title("Frame Example")
    root.mainloop()
