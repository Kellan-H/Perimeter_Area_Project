from tkinter import*

root = Tk()
root.title('Perimeter/Area Calculator')
root.geometry("400x400")

shape = 0
tool = 0

#----------------- Functions -----------------
def select_shape(event):
    if clicked.get() == 'Square':
        shape = "Square"
        print(shape)
    if clicked.get() == 'Triangle':
        shape = "Triangle"
        print(shape)
    if clicked.get() == 'Circle':
        shape = "Circle"
        print(shape)
    if clicked.get() == 'Rectangle':
        shape = "Rectangle"
        print(shape)
    if clicked.get() == 'Paralellogram':
        shape = "Paralellogram"
        print(shape)

def select_tool():
    global tool
    if var.get() == 1:
        tool = "perimeter"
        print(tool)
    else:
        tool = "area"
        print(tool)

options = [
    "Square",
    "Triangle",
    "Circle",
    "Rectangle",
    "Paralellogram",
]

clicked = StringVar()
clicked.set("Choose Shape")

drop = OptionMenu(root, clicked, *options, command=select_shape)
drop.pack(pady=20)

var = IntVar()
Radiobutton(root, text="Perimeter", variable=var, value=1, command=select_tool).pack()
Radiobutton(root, text="Area",variable=var, value=2, command=select_tool).pack()


root.mainloop()