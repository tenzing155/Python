import tkinter as tk

def add_data():
    name = name_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if name and email and address:
        data.append((name, email, address))
        update_grid()
    
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def create_headers():
    headers = ["Name", "Email", "Address"]
    for col, text in enumerate(headers):
        tk.Label(data_frame, text=text, font=("Arial", 12), borderwidth=1, relief="solid", padx=10, pady=5).grid(row=0, column=col, sticky="nsew")

def add_rows():
    for i, (name, email, address) in enumerate(data, start=1):
        tk.Label(data_frame, text=name, borderwidth=1, relief="solid", padx=10, pady=5).grid(row=i, column=0, sticky="nsew")
        tk.Label(data_frame, text=email, borderwidth=1, relief="solid", padx=10, pady=5).grid(row=i, column=1, sticky="nsew")
        tk.Label(data_frame, text=address, borderwidth=1, relief="solid", padx=10, pady=5).grid(row=i, column=2, sticky="nsew")

def update_grid():
    for widget in data_frame.winfo_children():
        widget.destroy()
    
    create_headers()
    add_rows()

app = tk.Tk()
app.title("Form")
app.geometry("500x500")

name_label = tk.Label(app, text="Name:")
name_label.pack(pady=(5, 0))
name_entry = tk.Entry(app)
name_entry.pack(pady=(0, 5))

email_label = tk.Label(app, text="Email:")
email_label.pack(pady=(5, 0))
email_entry = tk.Entry(app)
email_entry.pack(pady=(0, 5))

address_label = tk.Label(app, text="Address:")
address_label.pack(pady=(5, 0))
address_entry = tk.Entry(app)
address_entry.pack(pady=(0, 5))

button = tk.Button(app, text="Add", command=add_data)
button.pack(pady=(5, 20))

data_frame = tk.Frame(app)
data_frame.pack(fill="both", expand=True, padx=130, pady=50)

data = []

app.mainloop()
