import tkinter as tk
from tkinter import messagebox
from data_window import open_person_data_window

def sayHi():
    name = username_entry.get()
    password = password_entry.get()
    #message_lable.config(text=f"Hello {name}")
    if password == name + "password":
        messagebox.showinfo("Login successful",f"Welcome {name}!")
        open_person_data_window(root)
    else:
        messagebox.showerror("Login failed", "Invalid username or password")

root = tk.Tk()

root.title("My App!")
root.geometry("500x400")

tk.Label(root, text="User name:").grid(column=1, row=0,columnspan=2)
username_entry = tk.Entry()
username_entry.grid(column=3,row=0)

tk.Label(root, text="Password:").grid(column=1, row=1,columnspan=2)
password_entry = tk.Entry()
password_entry.grid(column=3,row=1)

message_lable=tk.Label(root)
message_lable.grid(column=1,row=3)

tk.Button(root, text="Login", command=sayHi).grid(column=3,row=2)
if __name__ == "__main__":
    root.mainloop()