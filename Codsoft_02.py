from tkinter import *
import math
import re

# Function to update the display with the button value
def button_click(value):
    current = db.get()
    if value.isdigit():
        # If the current value is "0", replace it with the new value
        if current == "0":
            current = ""
        # If the last entered value is "0" and the new value is a digit, replace the "0"
        if len(current) > 0 and current[-1] == "0":
            if len(current) == 1 or (len(current) > 1 and not current[-2].isdigit()):
                current = current[:-1]
    db.delete(0, END)
    db.insert(0, current + value)

# Function to clear the display
def clear_display():
    db.delete(0, END)

# Function to evaluate the expression
def evaluate_expression():
    try:
        expression = db.get()
        # Remove leading zeros in numbers within the expression
        expression = re.sub(r'\b0+(\d)', r'\1', expression)
        result = eval(expression)
        db.delete(0, END)
        db.insert(0, str(result))
    except:
        db.delete(0, END)
        db.insert(0, "Error")

# Function to calculate the square root
def calculate_sqrt():
    try:
        current = db.get()
        result = math.sqrt(float(current))
        db.delete(0, END)
        db.insert(0, str(result))
    except:
        db.delete(0, END)
        db.insert(0, "Error")

root = Tk()
root.title('Simple Calculator')

# Entry field for the display
db = Entry(root, width=20, font=('Arial', 26), justify=RIGHT, bd=10)
db.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button creation with black background and white text
button_0 = Button(root, text='0', padx=36, pady=10, font=('Arial', 14), bg='black', fg='white', command=lambda: button_click('0'))
button_1 = Button(root, text='1', padx=36, pady=10, font=('Arial', 14), bg='black', fg='white', command=lambda: button_click('1'))
button_2 = Button(root, text='2', padx=36, pady=10, font=('Arial', 14), bg='black', fg='white', command=lambda: button_click('2'))
button_3 = Button(root, text='3', padx=36, pady=10, font=('Arial', 14), bg='black', fg='white', command=lambda: button_click('3'))
button_4 = Button(root, text='4', padx=36, pady=10, font=('Arial', 14), bg='black', fg='white', command=lambda: button_click('4'))
button_5 = Button(root, text='5', padx=36, pady=10, font=('Arial', 14), bg='black', fg='white', command=lambda: button_click('5'))
button_6 = Button(root, text='6', padx=36, pady=10, font=('Arial', 14), bg='black', fg='white', command=lambda: button_click('6'))
button_7 = Button(root, text='7', padx=36, pady=10, font=('Arial', 14), bg='black', fg='white', command=lambda: button_click('7'))
button_8 = Button(root, text='8', padx=36, pady=10, font=('Arial', 14), bg='black', fg='white', command=lambda: button_click('8'))
button_9 = Button(root, text='9', padx=36, pady=10, font=('Arial', 14), bg='black', fg='white', command=lambda: button_click('9'))

clear_button = Button(root, text='C', padx=36, pady=10, font=('Arial', 14), bg='black', fg='white', command=clear_display)
add_button = Button(root, text='+', padx=36, pady=10, font=('Arial', 14), bg='black', fg='white', command=lambda: button_click('+'))
sub_button = Button(root, text='-', padx=36, pady=10, font=('Arial', 14), bg='black', fg='white', command=lambda: button_click('-'))
div_button = Button(root, text='/', padx=40, pady=10, font=('Arial', 14), bg='black', fg='white', command=lambda: button_click('/'))
equalto_button = Button(root, text='=', padx=36, pady=10, font=('Arial', 14), bg='black', fg='white', command=evaluate_expression)
mul_button = Button(root, text='x', padx=36, pady=10, font=('Arial', 14), bg='black', fg='white', command=lambda: button_click('*'))
dot_button = Button(root, text='.', padx=36, pady=10, font=('Arial', 14), bg='black', fg='white', command=lambda: button_click('.'))
sqrt_button = Button(root, text='√', padx=36, pady=10, font=('Arial', 14), bg='black', fg='white', command=calculate_sqrt)
left_par_button = Button(root, text='(', padx=36, pady=10, font=('Arial', 14), bg='black', fg='white', command=lambda: button_click('('))
right_par_button = Button(root, text=')', padx=36, pady=10, font=('Arial', 14), bg='black', fg='white', command=lambda: button_click(')'))

# Placing buttons on the grid
button_7.grid(row=1, column=0, padx=2, pady=2)
button_8.grid(row=1, column=1, padx=2, pady=2)
button_9.grid(row=1, column=2, padx=2, pady=2)
button_4.grid(row=2, column=0, padx=2, pady=2)
button_5.grid(row=2, column=1, padx=2, pady=2)
button_6.grid(row=2, column=2, padx=2, pady=2)
button_1.grid(row=3, column=0, padx=2, pady=2)
button_2.grid(row=3, column=1, padx=2, pady=2)
button_3.grid(row=3, column=2, padx=2, pady=2)
button_0.grid(row=4, column=0, padx=2, pady=2)
clear_button.grid(row=4, column=2, padx=2, pady=2)
add_button.grid(row=5, column=0, padx=2, pady=2)
sub_button.grid(row=5, column=1, padx=2, pady=2)
div_button.grid(row=5, column=2, padx=2, pady=2)
mul_button.grid(row=4, column=3, padx=2, pady=2)
dot_button.grid(row=4, column=1, padx=2, pady=2)
equalto_button.grid(row=5, column=3, padx=2, pady=2)
sqrt_button.grid(row=1, column=3, padx=2, pady=2)
left_par_button.grid(row=2, column=3, padx=2, pady=2)
right_par_button.grid(row=3, column=3, padx=2, pady=2)

root.mainloop()
