from person import Person
import tkinter as tk
from tkinter import ttk, PhotoImage

root = tk.Tk()
# def submit():

#     p = Person()

root.title("Complete your profile")
root.geometry("500x400")
#image load
image = PhotoImage(file="")
image_label = tk.Label(root, image=image)
image_label.grid(column=0, row=0, rowspan=5)

# tk.Label(root, text="Name").grid(column=1, row=0)
# name_entry = tk.Entry()
# name_entry.grid(column=2,row=0)

# gender = tk.StringVar()
# combx = ttk.Combobox(root,width=20, textvariable=gender)
# combx['values']=("Male", "Female")
# combx.grid(column=2, row=1) 

# tk.Label(root, text="eye Color").grid(column=1, row=2)

# tk.Label(root, text="Height").grid(column=1, row=3)
# height = tk.Entry()
# height.grid(column=3, row=4 )

# tk.Label(root, text="weight").grid(column=1, row=4)
# weight = tk.Entry()
# weight.grid(column=3, row=4 )

for i, ele in enumerate(["Name","Gender","Eye Color","Height","Weight"]):
    tk.Label(root, text=f"{ele}").grid(column=1, row=i)
name_entry = tk.Entry()
name_entry.grid(column=2,row=0)

gender = tk.StringVar()
gender_combx = ttk.Combobox(root,width=20, textvariable=gender)
gender_combx['values']=("Male", "Female")
gender_combx.grid(column=2, row=1, columnspan=2) 
gender_combx.current(0)



root.mainloop()