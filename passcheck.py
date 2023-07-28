

import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength():
    password = entry_password.get()

    if len(password) < 8:
        messagebox.showwarning("Weak Password", "Password should have at least 8 characters.")
    elif not re.search(r"[a-z]", password):
        messagebox.showwarning("Weak Password", "Password should contain lowercase letters.")
    elif not re.search(r"[A-Z]", password):
        messagebox.showwarning("Weak Password", "Password should contain uppercase letters.")
    elif not re.search(r"\d", password):
        messagebox.showwarning("Weak Password", "Password should contain numbers.")
    elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        messagebox.showwarning("Weak Password", "Password should contain special characters.")
    else:
        messagebox.showinfo("Strong Password", "Password is strong!")

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")

# Create and place widgets
label = tk.Label(root, text="Enter your password:")
label.pack(pady=10)

entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

check_button = tk.Button(root, text="Check Password", command=check_password_strength)
check_button.pack(pady=10)

root.mainloop()
