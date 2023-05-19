from tkinter import*

root = Tk()
root.title('Perimeter/Area Calculator')
root.geometry("200x200")

shape = 0
tool = 0

#----------------- Functions -----------------
def select_shape(event):
    if clicked.get() == 'Square':
        square_input()
        del_triangle_input()
        shape = "Square"
        print(shape)
    if clicked.get() == 'Triangle':
        triangle_input()
        del_square_input()
        shape = "Triangle"
        print(shape)
    if clicked.get() == 'Circle':
        del_square_input()
        del_triangle_input()
        shape = "Circle"
        print(shape)
    if clicked.get() == 'Rectangle':
        del_square_input()
        del_triangle_input()
        shape = "Rectangle"
        print(shape)
    if clicked.get() == 'Paralellogram':
        del_square_input()
        del_triangle_input()
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
#------------ SQUARE --------------
def square_input():
    global squarelabel
    global square_input_box
    squarelabel = Label(text="Width/Length:")
    squarelabel.grid(row=3,column=1)
    square_input_box = Entry(root, width=10)
    square_input_box.grid(row=3,column=2)

def del_square_input():
    squarelabel.destroy()
    square_input_box.destroy()

#------------ TRIANGLE --------------
def triangle_input():
    global trianglelabelbase
    global trianglelabelheight
    global trianglelabelhypotenuse
    global triangle_input_box_base
    global triangle_input_box_height
    global triangle_input_box_hypotenuse
    trianglelabelbase = Label(text="Base:")
    trianglelabelbase.grid(row=3,column=1)
    trianglelabelheight = Label(text="Height:")
    trianglelabelheight.grid(row=4,column=1)
    trianglelabelhypotenuse = Label(text="Hypotenuse:")
    trianglelabelhypotenuse.grid(row=5,column=1)
    triangle_input_box_base = Entry(root, width=10)
    triangle_input_box_base.grid(row=3,column=2)
    triangle_input_box_height = Entry(root, width=10)
    triangle_input_box_height.grid(row=4,column=2)
    triangle_input_box_hypotenuse = Entry(root, width=10)
    triangle_input_box_hypotenuse.grid(row=5,column=2)

def del_triangle_input():
    trianglelabelbase.destroy()
    trianglelabelheight.destroy()
    trianglelabelhypotenuse.destroy()
    triangle_input_box_base.destroy()
    triangle_input_box_height.destroy()
    triangle_input_box_hypotenuse.destroy()


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
drop.grid(row=1,column=1)

var = IntVar()
Radiobutton(root, text="Perimeter", variable=var, value=1, command=select_tool).grid(row=2,column=1)
Radiobutton(root, text="Area",variable=var, value=2, command=select_tool).grid(row=2, column=2)

root.mainloop()