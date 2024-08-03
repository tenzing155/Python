from tkinter import *

def button_press(num):
    global equation_text
    equation_text += str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text

    try:
        total = str(eval(equation_text))
        equation_label.set(total)

        equation_text = total
    except ZeroDivisionError:
        equation_label.set("Arithmetic error.")
        equation_text = ""
    except SyntaxError:
        equation_label.set("Syntax error.")
        equation_text = ""

def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

window = Tk()
window.title("Calculator Program")
window.resizable(0, 0)
window.geometry("300x450")

equation_text = ""
equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas', 20), bg="white", highlightbackground="black", highlightcolor="black", highlightthickness=1, width=16, height=2)
label.pack(padx=5,pady=10)

frame = Frame(window)
frame.pack(pady=10)

button1 = Button(frame, text=1, height=2, width=4, font=16, command=lambda: button_press(1))
button1.grid(row=2, column=0, padx=1, pady=1)

button2 = Button(frame, text=2, height=2, width=4, font=16, command=lambda: button_press(2))
button2.grid(row=2, column=1, padx=1, pady=1)

button3 = Button(frame, text=3, height=2, width=4, font=16, command=lambda: button_press(3))
button3.grid(row=2, column=2, padx=1, pady=1)

button4 = Button(frame, text=4, height=2, width=4, font=16, command=lambda: button_press(4))
button4.grid(row=1, column=0, padx=1, pady=1)

button5 = Button(frame, text=5, height=2, width=4, font=16, command=lambda: button_press(5))
button5.grid(row=1, column=1, padx=1, pady=1)

button6 = Button(frame, text=6, height=2, width=4, font=16, command=lambda: button_press(6))
button6.grid(row=1, column=2, padx=1, pady=1)

button7 = Button(frame, text=7, height=2, width=4, font=16, command=lambda: button_press(7))
button7.grid(row=0, column=0, padx=1, pady=1)

button8 = Button(frame, text=8, height=2, width=4, font=16, command=lambda: button_press(8))
button8.grid(row=0, column=1, padx=1, pady=1)

button9 = Button(frame, text=9, height=2, width=4, font=16, command=lambda: button_press(9))
button9.grid(row=0, column=2, padx=1, pady=1)

button0 = Button(frame, text=0, height=2, width=4, font=16, command=lambda: button_press(0))
button0.grid(row=3, column=0, padx=1, pady=1)

plus = Button(frame, text="+", height=2, width=4, font=16, command=lambda: button_press("+"))
plus.grid(row=3, column=3, padx=1, pady=1)

minus = Button(frame, text="-", height=2, width=4, font=16, command=lambda: button_press("-"))
minus.grid(row=2, column=3, padx=1, pady=1)

multiply = Button(frame, text="*", height=2, width=4, font=16, command=lambda: button_press("*"))
multiply.grid(row=1, column=3, padx=1, pady=1)

divide = Button(frame, text="/", height=2, width=4, font=16, command=lambda: button_press("/"))
divide.grid(row=0, column=3, padx=1, pady=1)

equal = Button(frame, text="=", height=2, width=4, font=16, command=equals)
equal.grid(row=3, column=2, padx=1, pady=1)

decimal = Button(frame, text=".", height=2, width=4, font=16, command=lambda: button_press("."))
decimal.grid(row=3, column=1, padx=1, pady=1)

clear_button = Button(window, text="Clear", height=2, width=16, font=16, command=clear)
clear_button.pack(padx=1, pady=1)

window.mainloop()
