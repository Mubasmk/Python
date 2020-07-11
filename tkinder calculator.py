# import everything using tkinter module
from tkinter import *

# create a GUI window
frame = Tk()


# set the size GUI window
frame.geometry("354x440+0+0")


# title for GUI window
frame.title("Calculator")

#  a label for upside of entry field
frame_label = Label(frame, text="crossroads", bg="black", fg="gray", font=("Times", 20, 'bold'))
frame_label.pack(side=TOP)
frame.config(background="#050505")

# StringVar() is a class variable,we create an instance of this class
text_in = StringVar()
# we declare a variable as globally
operator = ""


# function to update operator in the entry field
def click_button(number):
    global operator
    operator = operator + str(number)
    # update the operator using set method
    text_in.set(operator)


def equal_button():
    global operator
    # we using eval function for evaluate operator
    total = str(eval(operator))
    text_in.set(total)
    # initialize the operator variable by empty string
    operator = ""


# function for substraction
def sub_button():
    global operator
    sub = str(eval(operator))
    text_in.set(sub)
    operator = ""


# function for multiplication
def mul_button():
    global operator
    mul = str(eval(operator))
    text_in.set(mul)
    operator = ""


# function for division
def div_button():
    global operator
    div = str(eval(operator))
    text_in.set(div)
    operator = ""


# function for clear entry field
def clr_button():
    global operator
    operator = ""
    text_in.set("")


# creating a entry box for showing operations
me_text = Entry(frame, font=("courier New", 28, 'bold'), textvar=text_in, width=14, bd=8, bg="powder blue")
me_text.pack()


"""creating buttons and place that particular location
inside the root window.when we press the each button,the
command and function will be executed"""

check_button = Button(frame, bd=4, bg="#48a0cf", width=8, command=lambda :click_button("not yet solved"), text="CHECK",
                      font=("courier New", 12, 'bold'))
check_button.place(x=14, y=108)

clear_button = Button(frame, bd=4, bg="#48a0cf", width=8, command=lambda: clr_button(), text="CLEAR",
                      font=("courier New", 12, 'bold'))
clear_button.place(x=112, y=108)

ac_button = Button(frame, bd=4, width=5, bg="#48a0cf", command=lambda: clr_button(), text="AC",
                   font=("courier New", 12, 'bold'))
ac_button.place(x=278, y=108)

gt_button = Button(frame, bd=4, bg="gray", width=5, command=lambda: click_button("not yet solved"), text="GT",
                   font=("courier New", 15, 'bold'))
gt_button.place(x=14, y=150)

plmin_button = Button(frame, bd=4, bg="gray", width=5, command=lambda: click_button("not yet solved"), text="+/-",
                      font=("courier New", 15, 'bold'))
plmin_button.place(x=14, y=247)

mc_button = Button(frame, bd=4, bg="black", fg="white", width=5, command=lambda: click_button("not yet solved"), text="MC",
                   font=("courier New", 15, 'bold'))
mc_button.place(x=14, y=297)

mu_button = Button(frame, bd=4, bg="gray", width=5, command=lambda: click_button("not yet solved"), text="MU",
                   font=("courier New", 15, 'bold'))
mu_button.place(x=14, y=198)

mplus_button = Button(frame, bd=4, bg="black", fg="white", width=5, command=lambda: click_button("not yet solved"), text="M+",
                      font=("courier New", 15, 'bold'))
mplus_button.place(x=14, y=345)

mmin_button = Button(frame, bd=4, bg="black", fg="white", width=5, command=lambda: click_button("not yet solved"), text="M-",
                     font=("courier New", 15, 'bold'))
mmin_button.place(x=14, y=393)
seven_button = Button(frame, padx=12, pady=6, bd=4, bg="black", fg="red", command=lambda: click_button(7), text="7",
                      font=("courier New", 16, 'bold'))
seven_button.place(x=95, y=150)

eight_button = Button(frame, padx=12, pady=6, bd=4, bg="black", fg="red", command=lambda: click_button(8), text="8",
                      font=("courier New", 16, 'bold'))
eight_button.place(x=157, y=150)

nine_button = Button(frame, padx=12, pady=6, bd=4, bg="black", fg="red", command=lambda: click_button(9), text="9",
                     font=("courier New", 16, 'bold'))
nine_button.place(x=219, y=150)

percentage_button = Button(frame, padx=12, pady=6, bd=4, bg="black", fg="white", command=lambda: click_button("%"),
                           text="%",
                           font=("courier New", 16, 'bold'))
percentage_button.place(x=282, y=150)

four_button = Button(frame, padx=12, pady=6, bd=4, bg="black", fg="red", command=lambda: click_button(4), text="4",
                     font=("courier New", 16, 'bold'))
four_button.place(x=95, y=207)

five_button = Button(frame, padx=12, pady=6, bd=4, bg="black", fg="red", command=lambda: click_button(5), text="5",
                     font=("courier New", 16, 'bold'))
five_button.place(x=157, y=207)

six_button = Button(frame, padx=12, pady=6, bd=4, bg="black", fg="red", command=lambda: click_button(6), text="6",
                    font=("courier New", 16, 'bold'))
six_button.place(x=219, y=207)

multi_button = Button(frame, padx=12, pady=6, bd=4, bg="black", fg="white", command=lambda: click_button("*"), text="x",
                      font=("courier New", 16, 'bold'))
multi_button.place(x=282, y=207)

one_button = Button(frame, padx=12, pady=6, bd=4, bg="black", fg="red", command=lambda: click_button(1), text="1",
                    font=("courier New", 16, 'bold'))
one_button.place(x=95, y=265)

two_button = Button(frame, padx=12, pady=6, bd=4, bg="black", fg="red", command=lambda: click_button(2), text="2",
                    font=("courier New", 16, 'bold'))
two_button.place(x=157, y=265)

three_button = Button(frame, padx=12, pady=6, bd=4, bg="black", fg="red", command=lambda: click_button(3), text="3",
                      font=("courier New", 16, 'bold'))
three_button.place(x=219, y=265)

division_button = Button(frame, padx=12, pady=6, bd=4, bg="black", fg="white", command=lambda: click_button("/"),
                         text="/",
                         font=("courier New", 16, 'bold'))
division_button.place(x=282, y=265)

zero_button = Button(frame, padx=12, pady=6, bd=4, bg="black", fg="red", command=lambda: click_button(0), text="0",
                     font=("courier New", 16, 'bold'))
zero_button.place(x=95, y=323)

doublezero_button = Button(frame, padx=5, pady=6, bd=4, bg="black", fg="red", command=lambda: click_button(00),
                           text="00",
                           font=("courier New", 16, 'bold'))
doublezero_button.place(x=157, y=323)

plus_button = Button(frame, padx=12, pady=35, bd=4, bg="black", fg="white", command=lambda: click_button("+"), text="+",
                     font=("courier New", 16, 'bold'))
plus_button.place(x=219, y=323)

minuse_button = Button(frame, padx=12, pady=6, bd=4, bg="black", fg="white", command=lambda: click_button("-"),
                       text="-",
                       font=("courier New", 16, 'bold'))
minuse_button.place(x=282, y=323)

mr_button = Button(frame, padx=6, pady=6, bd=4, bg="black", fg="white", command=lambda: click_button("not yet solved"), text="MR",
                   font=("courier New", 16, 'bold'))
mr_button.place(x=95, y=382)

dot_button = Button(frame, padx=12, pady=6, bd=4, bg="black", fg="red", command=lambda: click_button("."), text=".",
                    font=("courier New", 16, 'bold'))
dot_button.place(x=157, y=382)

equa_button = Button(frame, padx=12, pady=6, bd=4, bg="black", fg="white", command=equal_button, text="=",
                     font=("courier New", 16, 'bold'))
equa_button.place(x=282, y=382)

# okay,let's start the GUI

frame.mainloop()
