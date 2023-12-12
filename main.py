# The PasswordGenerator is a tkinter-based GUI application that generates random password based on user input.
import tkinter as tk
from tkinter import Entry, Label, Button, ttk
from random import choice, shuffle

class PassGen:
    def __init__(self, master):
        self.master = master
        self.master.title("Random Password Generator")

        self.light_theme = True
        self.master.option_add("*Font", "Helvetica 12")

        try:
            self.master.iconphoto(True, tk.PhotoImage(file="lock.png"))
        except tk.TclError:
            pass

        self.label = Label(master, text="Password Length:")
        self.label.pack(pady=10)

        self.entry = Entry(master, width=20)
        self.entry.pack(pady=10)

        self.generate_button = Button(master, text="Generate Password", command=self.generate_password, bg="#4CAF50", fg="white", relief=tk.GROOVE)
        self.generate_button.pack(pady=10)

        self.result_label = Label(master, text="", wraplength=300, bg="white", borderwidth=0, highlightthickness=0)
        self.result_label.pack(pady=10)

        self.dark_mode_button = ttk.Button(master, text="Dark Mode", command=self.toggle_dark_mode)
        self.dark_mode_button.place(relx=1, rely=0, anchor='ne')

        self.update_theme()

    def toggle_dark_mode(self):
        self.light_theme = not self.light_theme
        self.update_theme()

    def update_theme(self):
        if self.light_theme:
            self.master.configure(bg="white")
            self.result_label.configure(bg="white", fg="black")
            self.label.configure(fg="black")
        else:
            self.master.configure(bg="#2E2E2E")
            self.result_label.configure(bg="#2E2E2E", fg="white")
            self.label.configure(fg="black")

    def generate_password(self):
        try:
            length = int(self.entry.get())
            if length <= 0:
                raise ValueError("Length should be a positive integer.")
            
            characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+"
            password = ''.join(choice(characters) for _ in range(length))
            password_list = list(password)
            shuffle(password_list)
            password = ''.join(password_list)

            self.result_label.config(text=f"Generated Password:\n{password}")
        except ValueError as e:
            self.result_label.config(text=str(e))

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300")
    password_generator = PassGen(root)
    root.mainloop()
