from tkinter import Tk, StringVar, IntVar, BooleanVar, messagebox, ttk, Text, END
import json
import os
from dataclasses import dataclass, asdict
from typing import List, Dict, Any

JSON_FILE = "person_records.json"

@dataclass
class Address:
    city: str
    zipCode: int

@dataclass
class Person:
    name: str
    age: int
    married: bool
    hobby: List[str]
    address: Address

def save_to_json():
    name = name_var.get().strip()
    age_str = age_var.get().strip()
    married = married_var.get()
    hobby_str = hobby_var.get("1.0", END).strip()
    city = city_var.get().strip()
    zip_code_str = zip_code_var.get().strip()

    if not all([name, age_str, city, zip_code_str]):
        messagebox.showerror("Save Error", "All fields must be filled out.")
        return

    try:
        age = int(age_str)
        zipCode = int(zip_code_str)
    except ValueError:
        messagebox.showerror("Input Error", "Age and Zip Code must be valid numbers.")
        return

    hobbies = [h.strip() for h in hobby_str.split(',') if h.strip()]

    try:
        address = Address(city=city, zipCode=zipCode)
        person = Person(
            name=name,
            age=age,
            married=married,
            hobby=hobbies,
            address=address
        )
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create data structure: {e}")
        return

    data: List[Dict[str, Any]] = []
    if os.path.exists(JSON_FILE):
        try:
            with open(JSON_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            data = []
            
    data.append(asdict(person))

    try:
        with open(JSON_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            
        messagebox.showinfo("Success", f"Data successfully saved to file: {JSON_FILE}")
        
        name_var.set("")
        age_var.set("")
        married_var.set(False)
        hobby_var.delete("1.0", END)
        city_var.set("")
        zip_code_var.set("")
        
    except Exception as e:
        messagebox.showerror("I/O Error", f"Failed to save data: {e}")

root = Tk()
root.title("Complex Data Entry Form")
root.geometry("550x450")
style = ttk.Style()
style.configure('TLabel', font=('Arial', 10))

# --- Variables ---
name_var = StringVar()
age_var = StringVar()
married_var = BooleanVar()
city_var = StringVar()
zip_code_var = StringVar()

# --- Layout ---
main_frame = ttk.Frame(root, padding="15")
main_frame.pack(fill="both", expand=True)

# Left Side: Person Details
person_frame = ttk.LabelFrame(main_frame, text="Personal Details", padding="10")
person_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")

ttk.Label(person_frame, text="Name:").grid(row=0, column=0, sticky="w", pady=5)
ttk.Entry(person_frame, textvariable=name_var, width=25).grid(row=0, column=1, padx=5, pady=5)

ttk.Label(person_frame, text="Age:").grid(row=1, column=0, sticky="w", pady=5)
ttk.Entry(person_frame, textvariable=age_var, width=25).grid(row=1, column=1, padx=5, pady=5)

ttk.Label(person_frame, text="Married:").grid(row=2, column=0, sticky="w", pady=5)
ttk.Checkbutton(person_frame, variable=married_var).grid(row=2, column=1, sticky="w", padx=5, pady=5)

# Right Side: Address and Hobby
details_frame = ttk.Frame(main_frame)
details_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")

# Address Sub-Frame
address_frame = ttk.LabelFrame(details_frame, text="Address", padding="10")
address_frame.pack(fill="x", pady=5)

ttk.Label(address_frame, text="City:").grid(row=0, column=0, sticky="w", pady=5)
ttk.Entry(address_frame, textvariable=city_var, width=20).grid(row=0, column=1, padx=5, pady=5)

ttk.Label(address_frame, text="Zip Code:").grid(row=1, column=0, sticky="w", pady=5)
ttk.Entry(address_frame, textvariable=zip_code_var, width=20).grid(row=1, column=1, padx=5, pady=5)

# Hobby Frame
hobby_frame = ttk.LabelFrame(details_frame, text="Hobbies (Comma separated)", padding="10")
hobby_frame.pack(fill="both", expand=True, pady=10)

hobby_var = Text(hobby_frame, height=5, width=25, font=('Arial', 10))
hobby_var.pack(fill="both", expand=True)

# Save Button
ttk.Button(main_frame, text="Save to JSON", command=save_to_json, style='TButton').grid(
    row=1, column=0, columnspan=2, pady=15, ipadx=20, ipady=5
)

root.mainloop()