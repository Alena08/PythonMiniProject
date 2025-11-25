import json
import csv
import os
import tkinter as tk
from tkinter import messagebox, ttk
from typing import List, Dict, Any, Optional

# --- 1. Data Structure for a Person ---
class Person:
    """Represents a single employee with basic personnel information."""
    def __init__(self, first_name: str, last_name: str, personnel_id: str):
        self.first_name = first_name
        self.last_name = last_name
        self.personnel_id = personnel_id

    def __str__(self) -> str:
        """Returns a readable string representation for display in the list."""
        return f"ID: {self.personnel_id:10} | Last Name: {self.last_name:15} | First Name: {self.first_name:10}"

    def to_dict(self) -> Dict[str, str]:
        """Converts the Person object into a dictionary (for JSON/CSV)."""
        return {
            "First Name": self.first_name,
            "Last Name": self.last_name,
            "Personnel ID": self.personnel_id
        }

# --- 2. Data Storage and Serialization Logic ---
class DataStorage:
    """Manages saving and loading personnel data in various formats."""
    
    STORAGE_FORMAT = "JSON"
    FILENAME = "personnel_data"
    
    @staticmethod
    def set_format(format_choice: str):
        """Sets the storage format (CSV, TXT, JSON)."""
        valid_formats = ["CSV", "TXT", "JSON"]
        if format_choice.upper() in valid_formats:
            DataStorage.STORAGE_FORMAT = format_choice.upper()
        
    @staticmethod
    def get_filepath() -> str:
        """Returns the full file path based on the selected format."""
        ext = DataStorage.STORAGE_FORMAT.lower()
        return f"{DataStorage.FILENAME}.{ext}"

    @staticmethod
    def save(persons: List[Person]):
        """Saves the list of persons in the chosen format."""
        filepath = DataStorage.get_filepath()
        data = [p.to_dict() for p in persons]
        fieldnames = ["First Name", "Last Name", "Personnel ID"]

        try:
            if DataStorage.STORAGE_FORMAT == "JSON":
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
            
            elif DataStorage.STORAGE_FORMAT == "CSV":
                with open(filepath, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')
                    writer.writeheader()
                    writer.writerows(data)
            
            elif DataStorage.STORAGE_FORMAT == "TXT":
                # Using '|' as a separator for TXT
                with open(filepath, 'w', encoding='utf-8') as f:
                    for item in data:
                        f.write(f"{item['First Name']}|{item['Last Name']}|{item['Personnel ID']}\n")
            
            return f"Data successfully saved in {DataStorage.STORAGE_FORMAT} format to '{filepath}'."
        
        except Exception as e:
            return f"Error saving data: {e}"

    @staticmethod
    def load() -> List[Person]:
        """Loads persons from the file in the chosen format."""
        filepath = DataStorage.get_filepath()
        persons = []
        
        if not os.path.exists(filepath):
            return []

        try:
            data: List[Dict[str, str]] = []
            
            if DataStorage.STORAGE_FORMAT == "JSON":
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            
            elif DataStorage.STORAGE_FORMAT == "CSV":
                with open(filepath, 'r', newline='', encoding='utf-8') as f:
                    reader = csv.DictReader(f, delimiter=';')
                    data = list(reader)
            
            elif DataStorage.STORAGE_FORMAT == "TXT":
                with open(filepath, 'r', encoding='utf-8') as f:
                    for line in f:
                        parts = line.strip().split('|')
                        if len(parts) == 3:
                            data.append({
                                "First Name": parts[0],
                                "Last Name": parts[1],
                                "Personnel ID": parts[2]
                            })
            
            # Convert loaded dictionaries back to Person objects
            for item in data:
                persons.append(Person(
                    item["First Name"],
                    item["Last Name"],
                    item["Personnel ID"]
                ))
            
            return persons

        except Exception:
            # If loading fails (e.g., corrupt file), return an empty list
            return []

# --- 3. Personnel Management (CRUD Operations) ---
class PersonnelManager:
    """Manages the list of employees and performs CRUD operations."""
    def __init__(self):
        self.persons = DataStorage.load()
        self.next_id = 1000 + len(self.persons)

    def _get_next_id(self) -> str:
        """Generates a unique employee ID."""
        current_id = self.next_id
        self.next_id += 1
        return f"P{current_id:04d}"

    def create_person(self, first_name: str, last_name: str):
        """Creates a new employee and adds them to the list."""
        personnel_id = self._get_next_id()
        new_person = Person(first_name, last_name, personnel_id)
        self.persons.append(new_person)
        return f"Employee '{first_name} {last_name}' (ID: {personnel_id}) added."

    def display_person(self, personnel_id: str) -> Optional[Person]:
        """Searches for and returns an employee by ID."""
        for p in self.persons:
            if p.personnel_id == personnel_id:
                return p
        return None

    def edit_person(self, personnel_id: str, new_first_name: str, new_last_name: str) -> bool:
        """Updates the data of an existing employee."""
        for p in self.persons:
            if p.personnel_id == personnel_id:
                p.first_name = new_first_name
                p.last_name = new_last_name
                return True
        return False

    def delete_person(self, personnel_id: str) -> bool:
        """Deletes an employee by their ID."""
        initial_len = len(self.persons)
        self.persons = [p for p in self.persons if p.personnel_id != personnel_id]
        return len(self.persons) < initial_len

    def find_person(self, search_term: str, search_field: str) -> List[Person]:
        """Searches for employees based on a given criterion."""
        results = []
        search_term = search_term.lower()

        for p in self.persons:
            if search_field == "First Name" and p.first_name.lower().startswith(search_term):
                results.append(p)
            elif search_field == "Last Name" and p.last_name.lower().startswith(search_term):
                results.append(p)
            elif search_field == "Personnel ID" and p.personnel_id.lower().startswith(search_term):
                results.append(p)
        
        return results

# --- 4. GUI Application with Tkinter ---

class PersonnelApp(tk.Tk):
    """The main application for personnel management with a graphical interface."""
    def __init__(self):
        super().__init__()
        self.title("Personnel Management Program")
        self.geometry("800x600")
        
        # State variables
        self.manager = PersonnelManager()
        self.storage_format_var = tk.StringVar(value=DataStorage.STORAGE_FORMAT)

        # Create Notebook (tabs)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, padx=10, fill="both", expand=True)

        # Create tabs
        self.tab_management = ttk.Frame(self.notebook)
        self.tab_settings = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_management, text=" Personnel Management ")
        self.notebook.add(self.tab_settings, text=" Settings and Saving ")

        # Initialize controls
        self._setup_management_tab()
        self._setup_settings_tab()
        
        # Update the list upon startup
        self._update_listbox()
        
        # Display welcome message
        if not self.manager.persons:
             messagebox.showinfo("Information", "Employee list is empty. Add new employees.")
        else:
             messagebox.showinfo("Information", f"Loaded {len(self.manager.persons)} employees from {DataStorage.STORAGE_FORMAT}.")

    # --- Setup Management Tab ---
    def _setup_management_tab(self):
        # Frame for data input (left)
        input_frame = ttk.LabelFrame(self.tab_management, text=" Employee Data ")
        input_frame.pack(side="left", padx=10, pady=10, fill="y")
        
        # Input fields
        self.first_name_var = tk.StringVar()
        self.last_name_var = tk.StringVar()
        self.personnel_id_var = tk.StringVar(value="ID") # Used to display ID of the selected employee

        ttk.Label(input_frame, text="First Name:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(input_frame, textvariable=self.first_name_var, width=25).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(input_frame, text="Last Name:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(input_frame, textvariable=self.last_name_var, width=25).grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(input_frame, text="ID (Selected):").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        ttk.Label(input_frame, textvariable=self.personnel_id_var, width=15, anchor="w").grid(row=2, column=1, sticky="w", padx=5, pady=5)

        # CRUD Buttons
        btn_frame = ttk.Frame(input_frame)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=10)
        
        ttk.Button(btn_frame, text="Add", command=self._create_person).pack(fill="x", padx=5, pady=5)
        ttk.Button(btn_frame, text="Update", command=self._edit_person).pack(fill="x", padx=5, pady=5)
        ttk.Button(btn_frame, text="Delete", command=self._delete_person).pack(fill="x", padx=5, pady=5)
        ttk.Button(btn_frame, text="Clear Fields", command=self._clear_input_fields).pack(fill="x", padx=5, pady=5)


        # Frame for list and search (right)
        list_search_frame = ttk.Frame(self.tab_management)
        list_search_frame.pack(side="right", padx=10, pady=10, fill="both", expand=True)
        
        # Search
        search_frame = ttk.LabelFrame(list_search_frame, text=" Search ")
        search_frame.pack(fill="x", padx=5, pady=5)
        
        self.search_term_var = tk.StringVar()
        self.search_field_var = tk.StringVar(value="Last Name") # Default search by Last Name
        
        ttk.Label(search_frame, text="Field:").pack(side="left", padx=5)
        ttk.Combobox(search_frame, textvariable=self.search_field_var, 
                     values=["First Name", "Last Name", "Personnel ID"], state="readonly", width=12).pack(side="left", padx=5)
                     
        ttk.Label(search_frame, text="Term:").pack(side="left", padx=5)
        ttk.Entry(search_frame, textvariable=self.search_term_var, width=25).pack(side="left", padx=5, fill="x", expand=True)
        
        ttk.Button(search_frame, text="Find", command=self._find_person).pack(side="left", padx=5)
        ttk.Button(search_frame, text="Reset", command=self._update_listbox).pack(side="left", padx=5)


        # Employee List
        ttk.Label(list_search_frame, text="Employee List:").pack(fill="x", padx=5, pady=(10, 0))
        self.listbox = tk.Listbox(list_search_frame, height=20, font=("Courier", 10))
        self.listbox.pack(fill="both", expand=True, padx=5, pady=5)
        self.listbox.bind('<<ListboxSelect>>', self._item_selected)

    # --- Setup Settings Tab ---
    def _setup_settings_tab(self):
        settings_frame = ttk.LabelFrame(self.tab_settings, text=" Data Format Selection ")
        settings_frame.pack(padx=20, pady=20, fill="x")

        # Radiobuttons for format selection
        formats = [("CSV", "CSV"), ("TXT", "TXT"), ("JSON", "JSON")]
        
        for text, mode in formats:
            ttk.Radiobutton(settings_frame, text=text, variable=self.storage_format_var, 
                            value=mode, command=self._set_storage_format).pack(anchor="w", padx=10, pady=5)
                            
        ttk.Label(settings_frame, textvariable=self.storage_format_var).pack(anchor="w", padx=10, pady=10)

        # Save/Load buttons
        save_load_frame = ttk.LabelFrame(self.tab_settings, text=" File Management ")
        save_load_frame.pack(padx=20, pady=10, fill="x")
        
        ttk.Button(save_load_frame, text="Save Data", command=self._save_data).pack(fill="x", padx=10, pady=5)
        ttk.Button(save_load_frame, text="Load Data (Switch Format)", command=self._load_data).pack(fill="x", padx=10, pady=5)

    # --- GUI Logic Methods ---

    def _update_listbox(self, persons_list: Optional[List[Person]] = None):
        """Updates the content of the Listbox."""
        self.listbox.delete(0, tk.END)
        
        if persons_list is None:
            persons_list = self.manager.persons

        for p in persons_list:
            self.listbox.insert(tk.END, str(p))
            
    def _clear_input_fields(self):
        """Clears the input fields."""
        self.first_name_var.set("")
        self.last_name_var.set("")
        self.personnel_id_var.set("ID")
            
    def _item_selected(self, event):
        """Handles the selection of an item in the list."""
        selected_indices = self.listbox.curselection()
        if not selected_indices:
            return
            
        selected_item_index = selected_indices[0]
        
        # Get data from the listbox to find the ID
        listbox_text = self.listbox.get(selected_item_index)
        # Extract the ID (e.g., P1000)
        selected_id = listbox_text.split('|')[0].strip().split(': ')[1]
        
        person = self.manager.display_person(selected_id)
        if person:
            self.first_name_var.set(person.first_name)
            self.last_name_var.set(person.last_name)
            self.personnel_id_var.set(person.personnel_id)

    # --- CRUD Methods (linked to the manager) ---

    def _create_person(self):
        """Creates a new Person."""
        first_name = self.first_name_var.get().strip()
        last_name = self.last_name_var.get().strip()
        
        if not first_name or not last_name:
            messagebox.showerror("Error", "First Name and Last Name cannot be empty.")
            return

        result_message = self.manager.create_person(first_name, last_name)
        messagebox.showinfo("Success", result_message)
        self._clear_input_fields()
        self._update_listbox()
        
    def _edit_person(self):
        """Edits the selected Person."""
        pid = self.personnel_id_var.get()
        new_first_name = self.first_name_var.get().strip()
        new_last_name = self.last_name_var.get().strip()

        if pid == "ID" or not pid:
            messagebox.showerror("Error", "No employee selected for update.")
            return

        if self.manager.edit_person(pid, new_first_name, new_last_name):
            messagebox.showinfo("Success", f"Employee data for ID {pid} updated.")
            self._clear_input_fields()
            self._update_listbox()
        else:
            messagebox.showerror("Error", f"Could not find employee with ID {pid}.")
            
    def _delete_person(self):
        """Deletes the selected Person."""
        pid = self.personnel_id_var.get()
        
        if pid == "ID" or not pid:
            messagebox.showerror("Error", "No employee selected for deletion.")
            return
            
        if messagebox.askyesno("Confirmation", f"Are you sure you want to delete employee ID {pid}?"):
            if self.manager.delete_person(pid):
                messagebox.showinfo("Success", f"Employee ID {pid} deleted.")
                self._clear_input_fields()
                self._update_listbox()
            else:
                messagebox.showerror("Error", f"Could not find employee with ID {pid}.")

    def _find_person(self):
        """Finds Person based on given parameters."""
        term = self.search_term_var.get().strip()
        field = self.search_field_var.get()
        
        if not term:
            messagebox.showinfo("Search", "Enter a search term.")
            self._update_listbox() # Show full list
            return

        results = self.manager.find_person(term, field)
        
        if results:
            self._update_listbox(results)
            messagebox.showinfo("Search", f"Found {len(results)} employees.")
        else:
            self.listbox.delete(0, tk.END)
            self.listbox.insert(tk.END, "No results found.")
            messagebox.showinfo("Search", "No results found.")

    # --- Save/Load Methods ---

    def _set_storage_format(self):
        """Updates the storage format in the DataStorage class."""
        DataStorage.set_format(self.storage_format_var.get())
        messagebox.showinfo("Format Changed", f"Storage format set to {DataStorage.STORAGE_FORMAT}.")

    def _save_data(self):
        """Saves data in the current format and file."""
        message = DataStorage.save(self.manager.persons)
        messagebox.showinfo("Saving Data", message)

    def _load_data(self):
        """Loads data using the current format (if it was just changed)."""
        # First, set the format from the RadioButton
        self._set_storage_format() 
        
        # Reload the manager
        old_count = len(self.manager.persons)
        self.manager = PersonnelManager()
        
        # Update the GUI
        self._update_listbox()
        new_count = len(self.manager.persons)
        
        messagebox.showinfo("Loading Data", 
                            f"Loading complete. Loaded {new_count} employees from {DataStorage.STORAGE_FORMAT}. (Previous list had {old_count} employees.)")


# --- Program Execution ---

if __name__ == "__main__":
    app = PersonnelApp()
    app.mainloop()