from tkinter import *

root = Tk()
tool = 0


def select_tool():
    global tool
    if var.get() == 1:
        tool = "perimeter"
        print(tool)
    else:
        tool = "area"
        print(tool)

var = IntVar()
Radiobutton(root, text="Perimeter", variable=var, value=1, command=select_tool).pack()
Radiobutton(root, text="Area",variable=var, value=2, command=select_tool).pack()

mainloop()


