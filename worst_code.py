import tkinter as tk
import random

# Function to handle button clicks
def button_click(button_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + button_text)
    if button_text.isdigit():
        update_button_text()

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the entry
def clear_entry():
    entry.delete(0, tk.END)

# Function to update button text
def update_button_text():
    for button in buttons:
        if button.cget('text').isdigit():
            button_text = str(random.randint(0, 9))
            button.config(text=button_text)

# Create the main window
root = tk.Tk()
root.title("Worst Calculator")

# Create the entry widget
entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button labels
button_labels = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

# Create and place buttons
buttons = []
for (text, row, col) in button_labels:
    if text.isdigit():
        button = tk.Button(root, text=str(random.randint(0, 9)), padx=20, pady=10, command=lambda t=text: button_click(t))
    elif text == 'C':
        button = tk.Button(root, text=text, padx=20, pady=10, command=clear_entry)
    elif text == "*" or text == ".":
        button = tk.Button(root, text=text, padx=20, pady=10, command=lambda t=text: button_click(t))
    else:
        button = tk.Button(root, text=text, padx=20, pady=10, command=evaluate)

    button.grid(row=row, column=col)
    buttons.append(button)

root.mainloop()
