from tkinter import *

root = Tk()
root.title('Perimeter/Area Calculator')
root.geometry("400x400")
shape = 0

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


def select_shape(event):
    if clicked.get() == 'Square':
        shape = "Square"
        print(shape)
        square_input()
    if clicked.get() == 'Triangle':
        del_square_input()
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


root.mainloop()