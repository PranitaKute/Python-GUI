# Canvas: It is a tool which is used for drawing in our programming

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

    canvas = Canvas(root)
    canvas.place(relx = 0.01, rely = 0.01, relheight = 1, relwidth = 1)
    canvas.configure(background= "pink")
    canvas.configure(height = 150)
    canvas.configure(width = 150)


    coord = 10,50,240,210
    arc = canvas.create_arc(coord, start = 0, extent = 150, fill = "red")
    text = canvas.create_text(100, 10, fill = "darkblue", font = "Times 20 italic bold", text = "Python GUI")


    root.title("Canvas Example")
    root.mainloop()