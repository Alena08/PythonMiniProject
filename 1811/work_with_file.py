import tkinter as tk
from tkinter import messagebox
import os

pfad = os.getcwd()

def open_function():

    file_name = file_entry.get()
    if not file_name:
        messagebox.showerror("Fehler! Please enter file name ")
        return

    try:
        with open(f"{pfad}/{file_name}","r") as file: 
            inhalt = file.read()
            text_field.delete("1.0", tk.END)
            text_field.insert("1.0", inhalt) # 1 Zeile, Zeichen index 0,  
    except Exception as e:
        text_field.delete("1.0", tk.END)
        text_field.insert("1.0", e)

def save_function():
    file_name = file_entry.get()
    new_text = text_field.get("1.0", tk.END)
    try:
        with open(f"{pfad}/{file_name}","w+") as file: 
            inhalt = file.read()
            file.write(f"{inhalt}\n {new_text}")

        text_field.insert("1.0", inhalt)
    except Exception as e:
        print(e)


root = tk.Tk()
root.title("Work with file")

tk.Label(root, text="File Name").grid(column=0, row=0,padx=20, pady=10)
file_entry = tk.Entry(root)
file_entry.grid(column=1, row=0,padx=20, pady=10)

btn_open = tk.Button(root, text="Open", command=open_function)
btn_open.grid(column=2,row=0,padx=20, pady=10)

btn_save = tk.Button(root, text="Save", command=save_function)
btn_save.grid(column=3,row=0,padx=20, pady=10)

text_field = tk.Text(root)
text_field.grid(column=0, row=1, columnspan=4, padx=20, pady=20, sticky="nsew")

lbl_text = tk.StringVar()
#lbl_text = tk.
root.mainloop()