import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("My App!")
root.geometry("500x400")
#root.configure(bg="red")

def button_clicked():
    text_from_entry = ent_name.get()
    list_item = list1.curselection()
    #print(list_item)
    item_text = list1.get(list_item) if list_item else "Kein Element Selected"
    #print(item_text)
    checked = "Ja" if var_check.get() else "Nein"
    radio = var_radio.get()

    # insert in der liste von Entry 
    list1.insert(tk.END, text_from_entry)

    auswahlt_option = var_option.get()

    info = f"Test: Entry: {text_from_entry}\nListe:{item_text}\nCheckBox: {checked}\nRadio:{radio}\nOption:{auswahlt_option}"
    messagebox.showinfo("Meine Eingeben",info)


# Label
tk.Label(root, text="Your Name:").pack(pady=5)

#Entry
ent_name = tk.Entry(root)
ent_name.pack(pady=5)

#Listbox
list1 = tk.Listbox(root,height=4)
for item in ["Banana","Milch","Eier"]:
    list1.insert(tk.END, item) # 0 start from top
list1.pack(pady=5)

#Checkbutton
var_check = tk.BooleanVar()
checkBx = tk.Checkbutton(root, text="Check Me!", variable=var_check)
checkBx.pack(pady=5)

#print("Ja" if var_check.get() else "Nein")

#RadioButtons
var_radio = tk.StringVar(value="Answer 1")
radio1 = tk.Radiobutton(root, text="Option 1", variable=var_radio, value="Answer 1")
radio2 = tk.Radiobutton(root, text="Option 2", variable=var_radio, value="Answer 2")
radio1.pack()
radio2.pack()

#print(f"This is the right answer: {var_radio.get()}")

# Button
btn = tk.Button(root, text="Click Me!" ,command=button_clicked )
btn.pack(pady=5)

#Textfield
textfield = tk.Text(root, height= 5, width=30)
textfield.insert(tk.END,"Hello from inside") # we can start from the front using '1.0'
textfield.pack(pady=5)

# OptionMenu
var_option = tk.StringVar(value="Mo")
tage = ["Mo","Di","Mi","Do","Fi","Sa","So"]
option = tk.OptionMenu(root,var_option,*tage)
option.pack(pady=5)

root.mainloop()
