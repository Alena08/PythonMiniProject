import tkinter as tk

def results():
    math_grade = int(math_entry.get())
    d_grage = int(d_entry.get())
    b_grade = int(b_entry.get())
    e_grade = int(e_entry.get())
    grades = [math_grade, d_grage, b_grade, e_grade]
    return grades
    
def summe_func():
    total_sum = sum(results())
    old_text = result1["text"]
    if "Average:" in old_text and "Summe:" not in old_text:
        result1.config(text=f"Summe: {total_sum}, {old_text}")
    else:
        result1.config(text=f"Summe:  {total_sum}")

def avg_func():
    avg_grade = sum(results())/ len(results())
    old_text = result1["text"]
    if "Summe:" in old_text and "Average:" not in old_text:
        result1.config(text=f"Average: {avg_grade:.2f}, {old_text}")
    else:
        result1.config(text=f"Average: {avg_grade:.2f}")

root = tk.Tk()
root.title("Programm to calculate sum and average")
root.geometry("500x400")

tk.Label(root, text="Mathe:").grid(column=1, row=0,columnspan=2)
math_entry = tk.Entry()
math_entry.grid(column=3,row=0)

tk.Label(root, text="Deutcht:").grid(column=1, row=1,columnspan=2)
d_entry = tk.Entry()
d_entry.grid(column=3,row=1)

tk.Label(root, text="Bio:").grid(column=1, row=2,columnspan=2)
b_entry = tk.Entry()
b_entry.grid(column=3,row=2)

tk.Label(root, text="Englisch:").grid(column=1, row=3,columnspan=2)
e_entry = tk.Entry()
e_entry.grid(column=3,row=3)

btn_sum = tk.Button(root, text="Calculate Summe", command=summe_func)
btn_sum.grid(column=3,row=6)

btn_avg = tk.Button(root, text="Calculate AVG", command=avg_func)
btn_avg.grid(column=6,row=6)

result1 = tk.Label(root)
result1.grid(column=1,row=7, columnspan=4)



root.mainloop()