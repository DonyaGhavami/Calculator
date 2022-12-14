'''
Simple Calculator GUI
by Donya Ghavami

'''
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path
import math 
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



window = Tk()

window.geometry("336x476")
window.configure(bg = "#FFFFFF")
window.iconbitmap("calculator.ico")
window.title("Calculator")

def click(print_number): 
    num = my_entry.get()
    my_entry.delete(0 , "end")
    my_entry.insert(0 , num+print_number)
    return


def sin(): 
    result = math.sin(math.radians(float(my_entry.get())))
    my_entry.delete(0 , "end")
    my_entry.insert(0 , result)

def cos(): 
    result_1 = math.cos(math.radians(float(my_entry.get())))
    my_entry.delete(0 , "end")
    my_entry.insert(0 , result_1)

def tan(): 
    result_2 = math.tan(math.radians(float(my_entry.get())))
    my_entry.delete(0 , "end")
    my_entry.insert(0 , result_2)


def sqrt(): 
    result_3 = math.sqrt(float(my_entry.get()))
    my_entry.delete(0 , "end")
    my_entry.insert(0 , result_3)


def clear(): 
    my_entry.delete(0 , "end")
    return

def evaluate(): 
    equal = my_entry.get()
    equal = eval(equal)
    my_entry.delete(0 , "end")
    my_entry.insert(0 , equal)



canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 476,
    width = 336,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click("0"),
    relief="flat"
)
button_1.place(
    x=89.0,
    y=427.0,
    width=77.0,
    height=46.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:click("1"),
    relief="flat"
)
button_2.place(
    x=7.0,
    y=369.0,
    width=77.0,
    height=46.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click("2"),
    relief="flat"
)
button_3.place(
    x=89.0,
    y=369.0,
    width=77.0,
    height=46.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click("3"),
    relief="flat"
)
button_4.place(
    x=171.0,
    y=369.0,
    width=77.0,
    height=46.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click("4"),
    relief="flat"
)
button_5.place(
    x=7.0,
    y=311.0,
    width=77.0,
    height=46.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click("5"),
    relief="flat"
)
button_6.place(
    x=89.0,
    y=311.0,
    width=77.0,
    height=46.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click("6"),
    relief="flat"
)
button_7.place(
    x=171.0,
    y=311.0,
    width=77.0,
    height=46.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click("7"),
    relief="flat"
)
button_8.place(
    x=7.0,
    y=253.0,
    width=77.0,
    height=46.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command= sqrt,
    relief="flat"
)
button_9.place(
    x=7.0,
    y=195.0,
    width=76.0,
    height=45.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:click("8"),
    relief="flat"
)
button_10.place(
    x=89.0,
    y=253.0,
    width=77.0,
    height=46.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click("9"),
    relief="flat"
)
button_11.place(
    x=171.0,
    y=253.0,
    width=77.0,
    height=46.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=evaluate,
    relief="flat"
)
button_12.place(
    x=171.0,
    y=427.0,
    width=77.0,
    height=46.0
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click("."),
    relief="flat"
)
button_13.place(
    x=7.0,
    y=427.0,
    width=79.0,
    height=46.0
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click("*"),
    relief="flat"
)
button_14.place(
    x=253.0,
    y=311.0,
    width=77.0,
    height=46.0
)

button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click("+"),
    relief="flat"
)
button_15.place(
    x=253.0,
    y=427.0,
    width=77.0,
    height=46.0
)

button_image_16 = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click("-"),
    relief="flat"
)
button_16.place(
    x=253.0,
    y=369.0,
    width=77.0,
    height=46.0
)

button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click("/"),
    relief="flat"
)
button_17.place(
    x=253.0,
    y=253.0,
    width=76.0,
    height=45.0
)

button_image_18 = PhotoImage(
    file=relative_to_assets("button_18.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command = sin ,
    relief="flat"
)
button_18.place(
    x=89.0,
    y=195.0,
    width=77.0,
    height=45.0
)





button_image_19 = PhotoImage(
    file=relative_to_assets("button_19.png"))
button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=cos,
    relief="flat"
)
button_19.place(
    x=171.0,
    y=195.0,
    width=77.0,
    height=46.0
)

button_image_20 = PhotoImage(
    file=relative_to_assets("button_20.png"))
button_20 = Button(
    image=button_image_20,
    borderwidth=0,
    highlightthickness=0,
    command= tan,
    relief="flat"
)
button_20.place(
    x=253.0,
    y=195.0,
    width=77.0,
    height=46.0
)

button_image_21 = PhotoImage(
    file=relative_to_assets("button_21.png"))
button_21 = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click("("),
    relief="flat"
)
button_21.place(
    x=7.0,
    y=137.0,
    width=65.0,
    height=46.0
)

button_image_22 = PhotoImage(
    file=relative_to_assets("button_22.png"))
button_22 = Button(
    image=button_image_22,
    borderwidth=0,
    highlightthickness=0,
    command=clear,
    relief="flat"
)
button_22.place(
    x=248.0,
    y=137.0,
    width=81.0,
    height=46.0
)

canvas.create_rectangle(
    25.0,
    25.0,
    311.0,
    118.0,
    fill="#D2D8E3",
    outline="")

button_image_23 = PhotoImage(
    file=relative_to_assets("button_23.png"))
button_23 = Button(
    image=button_image_23,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click(")"),
    relief="flat"
)
button_23.place(
    x=81.0,
    y=137.0,
    width=65.0,
    height=46.0
)

button_image_24 = PhotoImage(
    file=relative_to_assets("button_24.png"))
button_24 = Button(
    image=button_image_24,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click("**"),
    relief="flat"
)
button_24.place(
    x=157.0,
    y=138.0,
    width=81.0,
    height=46.0
)


my_entry = Entry(window , width = 20 , border = 0 , foreground = "black" , background = "#D2D9E3" , font =( "Franklin Gothic Medium Cond" , 20))
my_entry.place(x = 27 , y = 55)

window.resizable(False, False)
window.mainloop()
