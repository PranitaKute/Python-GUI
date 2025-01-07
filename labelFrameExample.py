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

labelframe = LabelFrame(root, text = "Basic Information")
labelframe.pack(fill=BOTH, expand = YES)
label = Label(labelframe, text = "Name : ")
label.pack()
label2 = Label(labelframe, text = "Contact Number : ")
label2.pack()
label3 = Label(labelframe, text = "Email : ")
label3.pack()


labelframe2 = LabelFrame(root, text = "Qualification Information")
labelframe2.pack(fill=BOTH, expand = YES)
label4 = Label(labelframe2, text = "Education Qualification : ")
label4.pack()
label5 = Label(labelframe2, text = "Additional Qualification : ")
label5.pack()
label6 = Label(labelframe2, text = "Certification : ")
label6.pack()


root.title("Label Frame Example")
root.mainloop()