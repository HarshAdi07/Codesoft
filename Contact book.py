import tkinter as tk
from tkinter import ttk, messagebox

class ContactBook(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contact Book")
        self.geometry("570x400")
        self.configure(bg="#f0f0f0")

        # Create frames
        self.frame_top = tk.Frame(self, bg="#f0f0f0")
        self.frame_top.pack(fill="x")

        self.frame_bottom = tk.Frame(self, bg="#f0f0f0")
        self.frame_bottom.pack(fill="both", expand=True)

        # Create labels and entries
        self.label_name = tk.Label(self.frame_top, text="Name:", bg="#f0f0f0")
        self.label_name.pack(side="left")

        self.entry_name = tk.Entry(self.frame_top, width=25)
        self.entry_name.pack(side="left")

        self.label_phone = tk.Label(self.frame_top, text="Phone:", bg="#f0f0f0")
        self.label_phone.pack(side="left")

        self.entry_phone = tk.Entry(self.frame_top, width=20)
        self.entry_phone.pack(side="left")

        # Create buttons
        self.button_add = tk.Button(self.frame_top, text="Add", command=self.add_contact)
        self.button_add.pack(side="left")

        self.button_delete = tk.Button(self.frame_top, text="Delete", command=self.delete_contact)
        self.button_delete.pack(side="left")

        # Create listbox
        self.listbox_contacts = tk.Listbox(self.frame_bottom, width=40)
        self.listbox_contacts.pack(fill="both", expand=True)

        # Create scrollbar
        self.scrollbar = tk.Scrollbar(self.frame_bottom)
        self.scrollbar.pack(side="right", fill="y")

        # Configure listbox and scrollbar
        self.listbox_contacts.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox_contacts.yview)

        # Load contacts
        self.contacts = []
        self.load_contacts()

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()

        if name and phone:
            self.contacts.append((name, phone))
            self.listbox_contacts.insert("end", f"{name} - {phone}")
            self.entry_name.delete(0, "end")
            self.entry_phone.delete(0, "end")
            self.save_contacts()
        else:
            messagebox.showerror("Error", "Please fill in both name and phone fields.")

    def delete_contact(self):
        try:
            index = self.listbox_contacts.curselection()[0]
            self.listbox_contacts.delete(index)
            self.contacts.pop(index)
            self.save_contacts()
        except IndexError:
            messagebox.showerror("Error", "Please select a contact to delete.")

    def load_contacts(self):
        try:
            with open("contacts.txt", "r") as file:
                for line in file:
                    name, phone = line.strip().split(" - ")
                    self.contacts.append((name, phone))
                    self.listbox_contacts.insert("end", f"{name} - {phone}")
        except FileNotFoundError:
            pass

    def save_contacts(self):
        with open("contacts.txt", "w") as file:
            for contact in self.contacts:
                file.write(f"{contact[0]} - {contact[1]}\n")

if __name__ == "__main__":
    app = ContactBook()
    app.mainloop()