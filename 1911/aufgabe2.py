import csv
import tkinter as tk

def add_function():
    try:
        with open("my1.csv","a",newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name_entry.get(), age_entry.get(), city_entry.get()])

    except Exception as e:
        print(e)
        # with open("my1.csv","w",newline="") as file:
        #     writer = csv.writer(file)
        #     writer.writerow(["Name","Age", "City"])
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    city_entry.delete(0, tk.END)
        
def show_all():
    info_frame.delete("1.0", "end")
    try:
        with open("my1.csv","r") as file:
            reader = csv.reader(file)
            for line in reader:
                text_i= ", ".join(line)
                info_frame.insert("end",text_i+'\n')
    except Exception as e:
        print(e)

# def show_all():
#     info_frame.delete("1.0", "end")
 
#     try:
#         with open("my1.csv", "r") as file:
#             for line in file:
#                 info_frame.insert("end", line)
#     except FileNotFoundError:
#         info_frame.insert("end", "Keine CSV Datei gefunden.")


root= tk.Tk()
root.title("Datei info einfügen")
root.geometry("500x400")


tk.Label(root, text="Name").grid(column=0, row=0)
name_entry = tk.Entry(root)
name_entry.grid(column=1,row=0)

tk.Label(root, text="Age").grid(column=0, row=1)
age_entry = tk.Entry(root)
age_entry.grid(column=1,row=1)

tk.Label(root, text="City").grid(column=0, row=2)
city_entry = tk.Entry(root)
city_entry.grid(column=1,row=2)

btn_add = tk.Button(root, text="Add", command=add_function)
btn_add.grid(column=0, row=3, columnspan=2)

btn_show = tk.Button(root, text="Show all", command=show_all)
btn_show.grid(column=0, row=4, columnspan=2)

info_frame = tk.Text(root, width=50, height=50)
info_frame.grid(column=0, row=5, columnspan=4)

root.mainloop()