import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import seaborn as sns

# --- Global Data Storage ---
data_frame = None
SEABORN_DATASETS = sns.get_dataset_names()

# --- Functions for Data Loading ---

def set_load_mode(mode):
    """Sets the active loading mode: 'local' or 'seaborn'."""
    load_mode_var.set(mode)
    
def open_data_source():
    """
    Executes the loading action based on the selected mode.
    """
    global data_frame
    mode = load_mode_var.get()
    
    if mode == 'local':
        filepath = filedialog.askopenfilename(defaultextension=".csv", 
                                              filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx"), ("All files", "*.*")])
        if filepath:
            try:
                if filepath.endswith('.csv'):
                    data_frame = pd.read_csv(filepath)
                elif filepath.endswith('.xlsx'):
                    data_frame = pd.read_excel(filepath)
                else:
                    data_frame = pd.read_csv(filepath) # Default to csv
                    
                local_file_entry.config(state=tk.NORMAL)
                local_file_entry.delete(0, tk.END)
                local_file_entry.insert(0, filepath.split('/')[-1])
                local_file_entry.config(state=tk.DISABLED)
                display_data(data_frame, "Local File Loaded")
            except Exception as e:
                messagebox.showerror("Loading Error", f"Failed to load file: {e}")
    
    elif mode == 'seaborn':
        dataset_name = seaborn_dataset_var.get()
        if dataset_name == "Select Seaborn Dataset":
            messagebox.showwarning("Warning", "Please select a dataset from the list.")
            return
        try:
            data_frame = sns.load_dataset(dataset_name)
            display_data(data_frame, f"Dataset '{dataset_name}' Loaded")
        except Exception as e:
            messagebox.showerror("Loading Error", f"Failed to load dataset: {e}")

# --- Functions for Operation Logic ---

def apply_groupby():
    """
    Applies the GROUPBY operation based on user input fields.
    """
    global data_frame
    if data_frame is None:
        messagebox.showwarning("Warning", "Please load a dataset first!")
        return
        
    cols_input = groupby_cols_entry.get().strip()
    agg_func = groupby_agg_entry.get().strip()
    use_reset = reset_index_var.get()
    
    try:
        group_cols = [c.strip() for c in cols_input.split(',')]
        result_df = data_frame.groupby(group_cols).agg(agg_func)
        
        if use_reset:
            result_df = result_df.reset_index() 
        
        display_data(result_df, "GROUPBY Result")
            
    except Exception as e:
        messagebox.showerror("Operation Error", f"Error executing GROUPBY: {e}")

def apply_cut():
    """
    Applies the CUT operation based on user input fields.
    """
    global data_frame
    if data_frame is None:
        messagebox.showwarning("Warning", "Please load a dataset first!")
        return
        
    col_to_cut = cut_col_entry.get().strip()
    # In this context, 'Agg func' entry is used for the number of bins
    bins_input = cut_agg_entry.get().strip() 
    
    try:
        bins = int(bins_input)
        result_df = data_frame.copy()
        # Create a new column with the categorized data
        result_df[f'{col_to_cut}_cut'] = pd.cut(data_frame[col_to_cut], bins=bins)
        
        display_data(result_df, "CUT Result")
            
    except Exception as e:
        messagebox.showerror("Operation Error", f"Error executing CUT: {e}")

def plotting_action():
    """
    Placeholder for the plotting logic.
    """
    messagebox.showinfo("Plotting", "Plotting functionality needs to be implemented (e.g., using matplotlib/seaborn).")
        
# --- Functions for Display ---
        
def display_data(df_to_display, title):
    """
    Clears and populates the Treeview widget with data from the given DataFrame.
    """
    # Clear the Treeview content
    for item in tree.get_children():
        tree.delete(item)
    
    # Set columns and headings
    cols = list(df_to_display.columns)
    tree["columns"] = cols
    tree["show"] = "headings"
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor='w')

    # Insert data rows
    for index, row in df_to_display.iterrows():
        tree.insert("", "end", values=[str(val) for val in row])
    
    root.title(f"Data Processor ({title})")


# --- Main Application Setup ---
root = tk.Tk()
root.title("Data Processor (Design Adaptation)")
root.geometry("800x600")
root.config(bg="#E0E0E0") # Light grey background to match the design

# --- Variables ---
load_mode_var = tk.StringVar(root, value='local') # 'local' or 'seaborn'
seaborn_dataset_var = tk.StringVar(root)
seaborn_dataset_var.set("Select Seaborn Dataset")
reset_index_var = tk.BooleanVar(root, value=True)

# --- 1. Data Loading Section (Top Frame) ---
load_frame = tk.Frame(root, bg="#E0E0E0")
load_frame.pack(padx=20, pady=20, fill="x")

# --- Row 1: Open Data Frame (Local) ---
ttk.Radiobutton(load_frame, text="Open Data Frame", variable=load_mode_var, value="local", 
                command=lambda: set_load_mode('local')).grid(row=0, column=0, padx=5, pady=5, sticky='w')

local_file_entry = ttk.Entry(load_frame, width=30)
local_file_entry.insert(0, "csv/xlsx")
local_file_entry.config(state=tk.DISABLED)
local_file_entry.grid(row=0, column=1, padx=10, pady=5)

# --- Row 2: Choose Data Frame From SNS (Seaborn) ---
ttk.Radiobutton(load_frame, text="Choose Data Frame From SNS", variable=load_mode_var, value="seaborn", 
                command=lambda: set_load_mode('seaborn')).grid(row=1, column=0, padx=5, pady=5, sticky='w')

# Dropdown for Seaborn datasets
seaborn_menu = ttk.OptionMenu(load_frame, seaborn_dataset_var, *([seaborn_dataset_var.get()] + SEABORN_DATASETS))
seaborn_menu.config(width=28)
seaborn_menu.grid(row=1, column=1, padx=10, pady=5)

# --- OPEN Button (Shared) ---
ttk.Button(load_frame, text="OPEN", command=open_data_source, 
           style='Accent.TButton').grid(row=0, column=2, rowspan=2, padx=10, pady=5, sticky='ns')

# --- 2. Group By Section ---
groupby_frame = tk.Frame(root, bg="#E0E0E0")
groupby_frame.pack(padx=20, pady=10, fill="x")

tk.Label(groupby_frame, text="Group By", bg="#E0E0E0").grid(row=0, column=0, padx=5, pady=5, sticky='w')

groupby_cols_entry = ttk.Entry(groupby_frame, width=20)
groupby_cols_entry.insert(0, "Column names")
groupby_cols_entry.grid(row=0, column=1, padx=5, pady=5)

groupby_agg_entry = ttk.Entry(groupby_frame, width=15)
groupby_agg_entry.insert(0, "Agg func")
groupby_agg_entry.grid(row=0, column=2, padx=5, pady=5)

ttk.Checkbutton(groupby_frame, text="With reset_index", variable=reset_index_var).grid(row=0, column=3, padx=15, pady=5, sticky='w')

ttk.Button(groupby_frame, text="Apply", command=apply_groupby, 
           style='Accent.TButton').grid(row=0, column=4, padx=(25, 5), pady=5)


# --- 3. Cut Section ---
cut_frame = tk.Frame(root, bg="#E0E0E0")
cut_frame.pack(padx=20, pady=10, fill="x")

tk.Label(cut_frame, text="Cut", bg="#E0E0E0").grid(row=0, column=0, padx=5, pady=5, sticky='w')
tk.Label(cut_frame, text=" " * 10, bg="#E0E0E0").grid(row=0, column=0) # Spacer

cut_col_entry = ttk.Entry(cut_frame, width=20)
cut_col_entry.insert(0, "Column names")
cut_col_entry.grid(row=0, column=1, padx=5, pady=5)

cut_agg_entry = ttk.Entry(cut_frame, width=15)
cut_agg_entry.insert(0, "Bins (Agg func)")
cut_agg_entry.grid(row=0, column=2, padx=5, pady=5)

# --- Apply and Plotting Buttons (Grouped) ---
button_group_frame = tk.Frame(cut_frame, bg="#E0E0E0")
button_group_frame.grid(row=0, column=3, padx=5, pady=5)

ttk.Button(button_group_frame, text="Apply", command=apply_cut, 
           style='Accent.TButton').pack(pady=2, fill='x')

ttk.Button(button_group_frame, text="Plotting", command=plotting_action, 
           style='Accent.TButton').pack(pady=2, fill='x')


# --- 4. TreeView Result Frame (Bottom) ---
result_frame = tk.LabelFrame(root, text="")
result_frame.pack(padx=20, pady=(0, 20), fill="both", expand=True)

# Styling for a cleaner look (optional, but good for design)
style = ttk.Style(root)
# Set a custom style for the green 'Accent' buttons
style.configure('Accent.TButton', background='#60D394', foreground='white', font=('Arial', 10, 'bold'), borderwidth=0)
style.map('Accent.TButton', background=[('active', '#50C384')])

# Treeview with scrollbars
tree = ttk.Treeview(result_frame, show='headings')

# Vertical Scrollbar
vsb = ttk.Scrollbar(result_frame, orient="vertical", command=tree.yview)
vsb.pack(side='right', fill='y')
tree.configure(yscrollcommand=vsb.set)

# Horizontal Scrollbar
hsb = ttk.Scrollbar(result_frame, orient="horizontal", command=tree.xview)
hsb.pack(side='bottom', fill='x')
tree.configure(xscrollcommand=hsb.set)

tree.pack(fill="both", expand=True, padx=5, pady=5)

tk.Label(result_frame, text="Tree View", background='white').place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Start the Tkinter event loop
root.mainloop()