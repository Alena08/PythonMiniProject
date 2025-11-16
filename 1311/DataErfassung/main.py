import tkinter as tk
from tkinter import ttk, PhotoImage,messagebox


from person import Person

root = tk.Tk()
root.title("Complete your profile")
root.geometry("500x400")
customFont= ("Helvetica", 20)

def submit():
    name = name_entry.get()
    gender_val = gender.get()
    eye_color_val = eyeColor.get()
    height = height_entry.get()
    weight = weight_entry.get()
    p = Person(name, gender_val, eye_color_val, height, weight)
    messagebox.showinfo("Person Data",p)

image_frame = tk.Frame(root, width=50, height=50)
image_frame.grid(column=0, row=0, rowspan=5)
# image load
image = PhotoImage(file="person_bild.png")
image = image.subsample(5,5)
# show image
image_lable = tk.Label(image_frame, image=image)
image_lable.pack(padx=5, pady=5)

for i,elemnt in enumerate(["Name","Gender","Eye Color","Height (cm)","Weight (kg)"]):
    tk.Label(root, text=f"{elemnt}:", font=customFont).grid(column=1, row=i, sticky="w")

name_entry = tk.Entry(font=customFont)
name_entry.grid(column=2, row=0, columnspan=2)

gender = tk.StringVar()
gender_combx = ttk.Combobox(root,width=20, textvariable=gender, font=customFont)
gender_combx['values']=("Male", "Female")
gender_combx.grid(column=2, row=1, columnspan=2)
gender_combx.current(0)

eyeColor = tk.StringVar()
eyeColor_combx = ttk.Combobox(root,width=20, textvariable=eyeColor, font=customFont)
eyeColor_combx['values']=("Brown","Black","Blue","Green","Red","Hony","Olive")
eyeColor_combx.grid(column=2,row=2, columnspan=2)

height_entry = tk.Entry(font=customFont)
height_entry.grid(column=2, row=3, columnspan=2)

weight_entry = tk.Entry(font=customFont)
weight_entry.grid(column=2, row=4, columnspan=2)

submit_btn = tk.Button(root, text="Submit",font=customFont, command=submit)
submit_btn.grid(column=3, row=5, columnspan=2)
root.mainloop()