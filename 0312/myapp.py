import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import seaborn as sns

# --- Global Data Storage ---
data_frame = None

# Global variable to hold the list of available seaborn datasets
sns_datasets = sns.get_dataset_names()

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

def display_data(df_to_display, title):
    """
    the Treeview widget with data from the given DataFrame.
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
    df_rows = df_to_display.astype(str).values.tolist()
    for row in df_rows:
        tree.insert('',tk.END, values=row)
    
    root.title(f"Data Processor ({title})")

def apply_groupby():
    """
    Applies the GROUPBY operation based on user input fields.
    """
    global data_frame
    if data_frame is None:
        messagebox.showwarning("Warning", "Please load a dataset first!")
        return
        
    cols_input = groupby_cols_entry.get().strip()
    target_col = groupby_target_entry.get().strip()
    agg_func = groupby_agg_entry.get().strip()
    use_reset = reset_index_var.get()
    if not target_col or target_col in ["Target Column"]:
        messagebox.showwarning("Input Error", "Please specify the Target Column for aggregation.")
        return
    
    try:
        group_cols = [c.strip() for c in cols_input.split(',')]
        result_df = data_frame.groupby(group_cols)[target_col].agg(agg_func)
        
        if use_reset:
            result_df = result_df.reset_index() 
        
        display_data(result_df, "GROUPBY Result")
            
    except Exception as e:
        messagebox.showerror("Operation Error", f"Error executing GROUPBY: {e}")

def on_focus_in_groupby(event):
    """
    Clears the entry field content when the widget receives focus, 
    if the content is the default placeholder text.
    """
    widget = event.widget
    
    if widget == groupby_cols_entry and widget.get() == "Column names":
        widget.delete(0, tk.END)
    elif widget == groupby_target_entry and widget.get() == "Target Column":
        widget.delete(0, tk.END)
    elif widget == groupby_agg_entry and widget.get() == "Agg func":
        widget.delete(0, tk.END)

def on_focus_in_cut(event):
    """
    Clears the entry field content when the widget receives focus, 
    if the content is the default placeholder text.
    """
    widget = event.widget
    if widget == cut_col_entry and widget.get() == "Category":
        widget.delete(0, tk.END)
    elif widget == cut_bins_entry and widget.get() == "Bins (e.g., 0, 10, 20)":
        widget.delete(0, tk.END)
    elif widget == cut_labels_entry and widget.get() == "Labels (e.g., Low, High)":
        widget.delete(0, tk.END)

def apply_cut():
    """
    Applies the CUT operation based on user input fields.
    """
    global data_frame
    if data_frame is None:
        messagebox.showwarning("Warning", "Please load a dataset first!")
        return
        
    col_to_cut = cut_col_entry.get().strip()
    bins_input = cut_bins_entry.get().strip()
    labels_input = cut_labels_entry.get().strip()

    if not col_to_cut or not bins_input:
        messagebox.showwarning("Input Error", "Please specify Column name and Bins.")
        return

    result_df = data_frame.copy()
    
    bins = None
    labels = None
    
    try:
        # is bins number? 
        try:
            bins = int(bins_input)
            labels = False 
            
        # is Bins list?
        except ValueError:
            bins = [float(b.strip()) for b in bins_input.split(',')]
            if len(bins) < 2:
                raise ValueError("Manual bins must have at least two values (boundaries).")
            
            labels_list = [l.strip() for l in labels_input.split(',') if l.strip()]
            
            if labels_list:
                if len(labels_list) != len(bins) - 1:
                    messagebox.showwarning("Input Error", f"The number of labels ({len(labels_list)}) must be exactly one less than the number of boundaries ({len(bins_list)}).")
                    return
                labels = labels_list
            else:
                labels = False
        
        result_df[f'{col_to_cut}_cut'] = pd.cut(
            x=data_frame[col_to_cut], 
            bins=bins,
            labels=labels, 
            include_lowest=True
        )
        
        display_data(result_df, f"CUT Result")
            
    except KeyError:
        messagebox.showerror("Operation Error", f" {col_to_cut} not found")
    except Exception as e:
        messagebox.showerror("Operation Error", f"Error executing CUT: {e}")

def reset_treeView():
    global tree
    children = tree.get_children()
    if children:
        tree.delete(*children)


# --- Main ---

# Initialize the main window
root = tk.Tk()
root.geometry("900x600")
root.title("Data Processor (Tkinter + Pandas)")

load_mode_var = tk.StringVar(root, value='local') # 'local' or 'seaborn'
seaborn_dataset_var = tk.StringVar(root)
seaborn_dataset_var.set("Select Seaborn Dataset")
reset_index_var = tk.BooleanVar(root, value=True)

# --- 1. Data Loading Section (Top Frame) ---
load_frame = tk.Frame(root)
load_frame.pack(padx=20, pady=20, fill="x")

ttk.Radiobutton(load_frame, text="Open Data Frame", variable=load_mode_var, value="local", 
                command=lambda: set_load_mode('local')).grid(row=0, column=0, padx=5, pady=5, sticky='w')

local_file_entry = ttk.Entry(load_frame, width=30)
# local_file_entry.insert(0, "csv/xlsx")
local_file_entry.config(state=tk.DISABLED)
local_file_entry.grid(row=0, column=1, padx=10, pady=5)

ttk.Radiobutton(load_frame, text="Choose Data Frame From SNS", variable=load_mode_var, value="seaborn", 
                command=lambda: set_load_mode('seaborn')).grid(row=1, column=0, padx=5, pady=5, sticky='w')

# Dropdown for Seaborn datasets
seaborn_menu = ttk.OptionMenu(load_frame, seaborn_dataset_var, *([seaborn_dataset_var.get()] + sns_datasets))
seaborn_menu.config(width=28)
seaborn_menu.grid(row=1, column=1, padx=10, pady=5)

ttk.Button(load_frame, text="OPEN", command=open_data_source, 
           style='Accent.TButton').grid(row=0, column=2, rowspan=2, padx=0, pady=5, sticky='ns')

# --- 2. Group By Section ---
groupby_frame = tk.Frame(root)
groupby_frame.pack(padx=20, pady=10, fill="x")

tk.Label(groupby_frame, text="Group By").grid(row=0, column=0, padx=5, pady=5, sticky='w')

groupby_cols_entry = ttk.Entry(groupby_frame, width=20)
groupby_cols_entry.insert(0, "Column names")
groupby_cols_entry.grid(row=0, column=1, padx=5, pady=5)
groupby_cols_entry.bind('<FocusIn>', on_focus_in_groupby)

groupby_target_entry = ttk.Entry(groupby_frame, width=15)
groupby_target_entry.insert(0, "Target Column") 
groupby_target_entry.grid(row=0, column=2, padx=5, pady=5)
groupby_target_entry.bind('<FocusIn>', on_focus_in_groupby)

groupby_agg_entry = ttk.Entry(groupby_frame, width=15)
groupby_agg_entry.insert(0, "Agg func")
groupby_agg_entry.grid(row=0, column=3, padx=5, pady=5)
groupby_agg_entry.bind('<FocusIn>', on_focus_in_groupby)

ttk.Checkbutton(groupby_frame, text="With reset_index", variable=reset_index_var).grid(row=0, column=4, padx=15, pady=5, sticky='w')

btn_grp = ttk.Button(groupby_frame, text="Apply", command=apply_groupby, style='Accent.TButton')
btn_grp.grid(row=0, column=5, padx=(25, 5), pady=5)

# --- 3. Cut Section ---
cut_frame = tk.Frame(root)
cut_frame.pack(padx=20, pady=10, fill="x")

tk.Label(cut_frame, text="Cut").grid(row=0, column=0, padx=5, pady=5, sticky='w')

cut_col_entry = ttk.Entry(cut_frame, width=20)
cut_col_entry.insert(0, "Category")
cut_col_entry.grid(row=0, column=1, padx=5, pady=5)
cut_col_entry.bind('<FocusIn>', on_focus_in_cut)

cut_bins_entry = ttk.Entry(cut_frame, width=15)
cut_bins_entry.insert(0, "Bins (e.g., 0, 10, 20)")
cut_bins_entry.grid(row=0, column=2, padx=5, pady=5)
cut_bins_entry.bind('<FocusIn>', on_focus_in_cut)

cut_labels_entry = ttk.Entry(cut_frame, width=15)
cut_labels_entry.insert(0, "Labels (e.g., Low, High)")
cut_labels_entry.grid(row=0, column=3, padx=5, pady=5)
cut_labels_entry.bind('<FocusIn>', on_focus_in_cut)

ttk.Button(cut_frame, text="Apply", command=apply_cut, 
           style='Accent.TButton').grid(row=0, column=4, padx=5, pady=5)

# --- TreeView Result Frame (Bottom) ---
result_frame = tk.LabelFrame(root, text="")
result_frame.pack(padx=20, pady=(0, 20), fill="both", expand=True)

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

#tk.Label(result_frame, text="Tree View", background='white').place(relx=0.5, rely=0.5, anchor=tk.CENTER)

tk.Button(root,text="Delete TViewI",command=reset_treeView).pack()

root.mainloop()