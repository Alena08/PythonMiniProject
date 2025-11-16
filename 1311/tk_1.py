import tkinter as tk
from tkinter import messagebox

def sayHi():
    name = username_entry.get()
    message_lable.config(text=f"Hello {name}")
    messagebox.showinfo("Login",f"Hello {name}")
    #print("Hello",name)

root = tk.Tk()

root.title("My App!")
root.geometry("500x400")

tk.Label(root, text="User name:").grid(column=1, row=0,columnspan=2)
username_entry = tk.Entry()
username_entry.grid(column=3,row=0, sticky="ew")

tk.Label(root, text="Password:").grid(column=1, row=1,columnspan=2)
password_entry = tk.Entry()
password_entry.grid(column=3,row=1)

message_lable=tk.Label(root)
message_lable.grid(column=1,row=3)

tk.Button(root, text="Login", command=sayHi).grid(column=3,row=2)
root.mainloop()