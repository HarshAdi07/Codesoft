import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.entry = tk.Entry(root, width=20, borderwidth=5, font=("Arial", 25, "bold"), justify="right", bg="#000", fg="#fff")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self.root, text=button, width=5, height=2, command=lambda button=button: self.on_click(button), bg="#000", fg="#fff", font=("Arial", 18, "bold")).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        tk.Button(self.root, text="Clear", width=20, height=2, command=self.clear, bg="#000", fg="#fff", font=("Arial", 18, "bold")).grid(row=row_val, column=0, columnspan=4, padx=5, pady=5)

    def on_click(self, button):
        if button == '=':
            try:
                result = str(eval(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, button)

    def clear(self):
        self.entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")
root.configure(bg="#000")
root.geometry("390x520")
calculator = Calculator(root)
root.mainloop()