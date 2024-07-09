import random
import pyperclip
from tkinter import *
from tkinter.ttk import *

def generate_password():
    entry.delete(0, END)

    length = password_length.get()
    include_lower = include_lowercase.get()
    include_upper = include_uppercase.get()
    include_digit = include_digits.get()
    include_symbol = include_symbols.get()

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = "!@#$%^&*()"

    all_characters = ""
    if include_lower:
        all_characters += lower
    if include_upper:
        all_characters += upper
    if include_digit:
        all_characters += digits
    if include_symbol:
        all_characters += symbols

    if all_characters:
        password = "".join(random.choice(all_characters) for _ in range(length))
        entry.insert(10, password)
    else:
        entry.insert(10, "Select at least one option")

def copy_password():
    random_password = entry.get()
    pyperclip.copy(random_password)

root = Tk()

root.title("Random Password Generator")


root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)

style = Style()
style.configure("Green.TLabel", foreground="green", background="black", font=("Helvetica", 22, "bold"))
style.configure("Green.TCheckbutton", foreground="green", background="black")
style.configure("Green.TButton", foreground="green", background="black")

root.configure(background="black")

welcome_label = Label(root, text="Welcome to Password Generator", style="Green.TLabel")
welcome_label.grid(row=0, column=0, columnspan=5, pady=50, sticky="ew")
label_password = Label(root, text="Password", style="Green.TLabel")
label_password.grid(row=1, column=0, pady=10, sticky="e")
entry = Entry(root)
entry.grid(row=1, column=1, columnspan=3, pady=10, sticky="ew")
label_length = Label(root, text="Length", style="Green.TLabel")
label_length.grid(row=2, column=0, pady=5, sticky="e")
password_length = IntVar(value=8)
combo_length = Combobox(root, textvariable=password_length)
combo_length['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                          17, 18, 19, 20, 21, 22, 23, 24, 25,
                          26, 27, 28, 29, 30, 31, 32)
combo_length.current(0)
combo_length.grid(column=1, row=2, pady=5, sticky="w")
include_lowercase = BooleanVar(value=True)
include_uppercase = BooleanVar(value=False)
include_digits = BooleanVar(value=False)
include_symbols = BooleanVar(value=False)

check_lowercase = Checkbutton(root, text="Include Lowercase", variable=include_lowercase, style="Green.TCheckbutton")
check_lowercase.grid(row=3, column=0, pady=10, padx=5, sticky='w')
check_uppercase = Checkbutton(root, text="Include Uppercase", variable=include_uppercase, style="Green.TCheckbutton")
check_uppercase.grid(row=3, column=1, pady=10, padx=5, sticky='w')
check_digits = Checkbutton(root, text="Include Digits", variable=include_digits, style="Green.TCheckbutton")
check_digits.grid(row=3, column=2, pady=10, padx=5, sticky='w')
check_symbols = Checkbutton(root, text="Include Symbols", variable=include_symbols, style="Green.TCheckbutton")
check_symbols.grid(row=3, column=3, pady=10, padx=5, sticky='w')
button_copy = Button(root, text="Copy", command=copy_password, style="Green.TButton")
button_copy.grid(row=1, column=4, pady=5, padx=5, sticky="w")
button_generate = Button(root, text="Generate", command=generate_password, style="Green.TButton")
button_generate.grid(row=2, column=4, pady=5, padx=5, sticky="w")
root.mainloop()
