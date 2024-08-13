import tkinter as tk

def update_expression(symbol):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + symbol)

def calculate(event=None):  # event parameter added to allow binding
    try:
        expression = entry.get()
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=calculate)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=lambda t=text: update_expression(t))
    button.grid(row=row, column=col)

clear_button = tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 18), command=clear)
clear_button.grid(row=4, column=3)

root.bind('<Return>', calculate)  # Bind the Enter key to the calculate function

root.mainloop()
