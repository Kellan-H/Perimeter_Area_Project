from tkinter import*

root = Tk()
root.title('Perimeter/Area Calculator')
root.geometry("400x400")

shape = 0

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