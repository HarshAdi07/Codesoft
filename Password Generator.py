import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    all_characters = string.ascii_lowercase
    if use_uppercase:
        all_characters += string.ascii_uppercase
    if use_numbers:
        all_characters += string.digits
    if use_special_chars:
        all_characters += string.punctuation
    if length < 4:
        messagebox.showerror("Error", "Your password should be at least 4 characters long.")
        return None
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def generate_and_display_password():
    length = int(length_entry.get())
    use_uppercase = uppercase_var.get()
    use_numbers = numbers_var.get()
    use_special_chars = special_chars_var.get()
    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    if password:
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

root = tk.Tk()
root.title("Password Generator")
root.configure(background="#f0f0f0")  # light gray background

main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.pack(fill="both", expand=True)

tk.Label(main_frame, text="Password Generator", font=("Helvetica", 24), bg="#f0f0f0").pack(pady=20)

length_frame = tk.Frame(main_frame, bg="#f0f0f0")
length_frame.pack(fill="x", pady=10)
tk.Label(length_frame, text="Password Length:", font=("Helvetica", 14), bg="#f0f0f0").pack(side=tk.LEFT, padx=10)
length_entry = tk.Entry(length_frame, width=10, font=("Helvetica", 14))
length_entry.pack(side=tk.LEFT, padx=10)

options_frame = tk.Frame(main_frame, bg="#f0f0f0")
options_frame.pack(fill="x", pady=10)
tk.Label(options_frame, text="Options:", font=("Helvetica", 14), bg="#f0f0f0").pack(side=tk.LEFT, padx=10)

uppercase_var = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(options_frame, text="Uppercase", variable=uppercase_var, bg="#f0f0f0")
uppercase_checkbox.pack(side=tk.LEFT, padx=10)

numbers_var = tk.BooleanVar()
numbers_checkbox = tk.Checkbutton(options_frame, text="Numbers", variable=numbers_var, bg="#f0f0f0")
numbers_checkbox.pack(side=tk.LEFT, padx=10)

special_chars_var = tk.BooleanVar()
special_chars_checkbox = tk.Checkbutton(options_frame, text="Special Characters", variable=special_chars_var, bg="#f0f0f0")
special_chars_checkbox.pack(side=tk.LEFT, padx=10)

generate_button = tk.Button(main_frame, text="Generate Password", command=generate_and_display_password, font=("Helvetica", 14), bg="#4CAF50", fg="white")
generate_button.pack(pady=20)

password_frame = tk.Frame(main_frame, bg="#f0f0f0")
password_frame.pack(fill="x", pady=10)
tk.Label(password_frame, text="Generated Password:", font=("Helvetica", 14), bg="#f0f0f0").pack(side=tk.LEFT, padx=10)
password_entry = tk.Entry(password_frame, width=30, font=("Helvetica", 14))
password_entry.pack(side=tk.LEFT, padx=10)

root.mainloop()