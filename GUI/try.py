import tkinter as tk

#obj as app
app = tk.Tk()
app.title("My app") #title
app.geometry("500x400") #size

#label naming
flabel = tk.Label(app, text="First Number")
flabel.pack() #display
fnum = tk.Entry(app) #entry input
fnum.pack()
slabel = tk.Label(app, text="Second Number")
slabel.pack()
snum = tk.Entry(app)
snum.pack()
result = tk.Label(app, text="Result")
result.pack()

def add():
    num1 = int(fnum.get())
    num2 = int(snum.get())
    res = num1 + num2
    result.config(text=str(res))

button = tk.Button(app, text="Add", command=add)#command = function call
button.pack()
app.mainloop() #display gui