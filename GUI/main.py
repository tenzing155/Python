import tkinter as tk

app = tk.Tk()
app.title("Calculator")
app.geometry("500x400")

flabel = tk.Label(app, text="First Number")
flabel.pack()
fnum = tk.Entry(app)
fnum.pack()

olabel = tk.Label(app, text="Operator (+, -, *, /)")
olabel.pack()
operator = tk.Entry(app)
operator.pack()

slabel = tk.Label(app, text="Second Number")
slabel.pack()
snum = tk.Entry(app)
snum.pack()

result = tk.Label(app, text="Result")
result.pack()

def calculate():
    num1 = float(fnum.get())
    op = operator.get()
    num2 = float(snum.get())
    
    if op == '+':
        res = num1 + num2
    elif op == '-':
        res = num1 - num2
    elif op == '*':
        res = num1 * num2
    elif op == '/':
        res = num1 / num2
    else:
        res = "Invalid operator"
    
    result.config(text=str(res))

button = tk.Button(app, text="Calculate", command=calculate)
button.pack()

app.mainloop()
