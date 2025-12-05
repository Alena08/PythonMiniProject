import tkinter as tk
from tkinter import filedialog as fd
from os import path

def open_file_dialog():
    filename = fd.askopenfilename(title="Open a File")
    if filename:
        if path.isfile(filename):
            print("It existiert!")
        print(f"Selected file : {filename}")
    else:
        print("No file selected.")

root = tk.Tk()

root.title("Open FIle App")
root.geometry("400x300")

tk.Button(root, text="Click to Open File", command=open_file_dialog).pack(expand=True)

root.mainloop()