from tkinter import*

root = Tk()
root.title('Perimeter/Area Calculator')
root.geometry("400x400")

shape = 0
tool = 0

#----------------- Functions -----------------
def select_shape(event):
    if clicked.get() == 'Square':
        square_input()
        shape = "Square"
        print(shape)
    if clicked.get() == 'Triangle':
        del_square_input()
        shape = "Triangle"
        print(shape)
    if clicked.get() == 'Circle':
        del_square_input()
        shape = "Circle"
        print(shape)
    if clicked.get() == 'Rectangle':
        del_square_input()
        shape = "Rectangle"
        print(shape)
    if clicked.get() == 'Paralellogram':
        del_square_input()
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

#---------------  INPUT FUNCTIONS  -------------------
def square_input():
    global mylabel
    global a
    mylabel = Label(text="Width/Length:")
    mylabel.pack()
    a = Entry(root, width=10)
    a.pack()

def del_square_input():
    mylabel.destroy()
    a.destroy()


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