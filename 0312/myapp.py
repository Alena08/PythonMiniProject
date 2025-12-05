import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- Global Data Storage ---
data_frame = None
last_result_df = None
last_agg_col_name = None
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
        filepath = local_file_entry.get().strip()
        if filepath == "csv/xlsx" or not filepath:
            filepath = filedialog.askopenfilename(defaultextension=".csv", 
                                              filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx"), ("All files", "*.*")])
        if filepath and filepath != "csv/xlsx":
            try:
                if filepath.endswith('.csv'):
                    data_frame = pd.read_csv(filepath)
                elif filepath.endswith('.xlsx'):
                    data_frame = pd.read_excel(filepath)
                else:
                    data_frame = pd.read_csv(filepath) # Default to csv
                    
                local_file_entry.delete(0, tk.END)
                local_file_entry.insert(0, filepath.split('/')[-1])

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
    global last_result_df
    # Clear the Treeview content
    for item in tree.get_children():
        tree.delete(item)
    
    # Set columns and headings
    cols = list(df_to_display.columns)
    tree["columns"] = cols
    tree["show"] = "headings"
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor='center')

    # Insert data rows
    df_rows = df_to_display.astype(str).values.tolist()
    for row in df_rows:
        tree.insert('',tk.END, values=row)
    
    root.title(f"Data Processor ({title})")
    last_result_df = df_to_display.copy()

def apply_groupby():
    """
    Applies the GROUPBY operation based on user input fields.
    """
    global data_frame, last_result_df, last_agg_col_name
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
        result_series = data_frame.groupby(group_cols)[target_col].agg(agg_func)
        new_col_name = f'{target_col}_{agg_func}'
        result_series.name = new_col_name
        
        if use_reset:
            result_df = result_series.reset_index()
        else:
            result_df = result_series.to_frame()
        
        last_result_df = result_df.copy()
        last_agg_col_name = new_col_name

        display_data(result_df, "GROUPBY Result")
        # Resetting GROUP BY fields
        groupby_cols_entry.delete(0, tk.END)
        groupby_cols_entry.insert(0, "Column names")
        
        groupby_target_entry.delete(0, tk.END)
        groupby_target_entry.insert(0, "Target Column")
        
        groupby_agg_entry.delete(0, tk.END)
        groupby_agg_entry.insert(0, "Agg func")
            
    except Exception as e:
        messagebox.showerror("Operation Error", f"Error executing GROUPBY: {e}")

def plotting_action():
    """
    Plots the result of GroupBy operation.
    """
    global last_result_df, last_agg_col_name
    if last_result_df is None:
        messagebox.showwarning("Plotting Error", "No GroupBy results available for plotting. " \
        "Please run the Group By operation first.")
        return

    df = last_result_df
    
    try:
        if df.index.nlevels > 1 or df.index.name is not None: #reset_index = False
            plot_df = df.reset_index()
        else:
            #reset_index = True
            plot_df = df.copy()

        x_cols = plot_df.columns[:-1].tolist()
        if len(x_cols) > 1:
            plot_df['X_Axis'] = plot_df[x_cols].astype(str).agg(' - '.join, axis=1)
            x_axis = 'X_Axis'
        else:
            x_axis = x_cols[0]
        y_axis = last_agg_col_name
        
        plt.figure(figsize=(10, 6))
        plt.bar(plot_df[x_axis], plot_df[y_axis], color='green') 
        
        plt.xlabel(x_axis, fontsize=12)
        plt.ylabel(y_axis, fontsize=12)
        plt.title(f'Plot {y_axis} on {x_axis}', fontsize=14)
        plt.xticks(rotation=45, ha='right')
        plt.show()

    except Exception as e:
        messagebox.showerror("Plotting Error", f"Could not create plot. Ensure the result data is numeric for aggregation.\nDetails: {e}")

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

def on_focus_out_groupby(event):
    """Inserts placeholder if the field is left empty when losing focus."""
    widget = event.widget
    if not widget.get():
        if widget == groupby_cols_entry:
            widget.insert(0, "Column names")
        elif widget == groupby_target_entry:
            widget.insert(0, "Target Column")
        elif widget == groupby_agg_entry:
            widget.insert(0, "Agg func")

def on_focus_in_cut(event):
    """
    Clears the entry field content when the widget receives focus, 
    if the content is the default placeholder text.
    """
    widget = event.widget
    if widget == cut_col_entry and widget.get() == "Column name":
        widget.delete(0, tk.END)
    elif widget == cut_bins_entry and widget.get() == "Bins (e.g., 0, 10, 20)":
        widget.delete(0, tk.END)
    elif widget == cut_labels_entry and widget.get() == "Labels (e.g., Low, High)":
        widget.delete(0, tk.END)

def on_focus_out_cut(event):
    """Inserts placeholder if the field is left empty when losing focus."""
    widget = event.widget
    if not widget.get():
        if widget == cut_col_entry:
            widget.insert(0, "Column name")
        elif widget == cut_bins_entry:
            widget.insert(0, "Bins (e.g., 0, 10, 20)")
        elif widget == cut_labels_entry:
            widget.insert(0, "Labels (e.g., Low, High)")

def apply_cut():
    """
    Applies the CUT operation based on user input fields.
    """
    global data_frame, last_result_df
    if data_frame is None:
        messagebox.showwarning("Warning", "Please load a dataset first!")
        return
        
    col_to_cut = cut_col_entry.get().strip()
    bins_input = cut_bins_entry.get().strip()
    labels_input = cut_labels_entry.get().strip()

    if not col_to_cut or not bins_input:
        messagebox.showwarning("Input Error", "Please specify Column name and Bins.")
        return

    result_df = pd.DataFrame(data_frame[col_to_cut])
    new_col_name = f'{col_to_cut}_cut'
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
                    messagebox.showwarning("Input Error", f"The number of labels ({len(labels_list)}) must be exactly one less than the number of boundaries ({len(bins)}).")
                    return
                labels = labels_list
            else:
                labels = False
        
        result_df[new_col_name] = pd.cut(
            x=data_frame[col_to_cut], 
            bins=bins,
            labels=labels, 
            include_lowest=True
        )
        
        display_data(result_df, f"CUT Result")
        last_result_df = result_df.copy()
        # Resetting CUT fields
        cut_col_entry.delete(0, tk.END)
        cut_col_entry.insert(0, "Column name")
        
        cut_bins_entry.delete(0, tk.END)
        cut_bins_entry.insert(0, "Bins (e.g., 0, 10, 20)")

        cut_labels_entry.delete(0, tk.END)
        cut_labels_entry.insert(0, "Labels (e.g., Low, High)")
            
    except KeyError:
        messagebox.showerror("Operation Error", f" {col_to_cut} not found")
    except Exception as e:
        messagebox.showerror("Operation Error", f"Error executing CUT: {e}")

def reset_treeView():
    global tree
    children = tree.get_children()
    if children:
        tree.delete(*children)

def save_result_to_csv():
    """
    Saves the currently displayed DataFrame (last_result_df) to a CSV file.
    """
    global last_result_df
    if last_result_df is None:
        messagebox.showwarning("Save Error")
        return
    
    filepath = filedialog.asksaveasfile(defaultextension=".csv", filetypes=[("Csv files","*.csv")])
    last_result_df.to_csv(filepath, index=True)



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
local_file_entry.insert(0, "csv/xlsx")
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
groupby_cols_entry.bind('<FocusOut>', on_focus_out_groupby)

groupby_target_entry = ttk.Entry(groupby_frame, width=15)
groupby_target_entry.insert(0, "Target Column") 
groupby_target_entry.grid(row=0, column=2, padx=5, pady=5)
groupby_target_entry.bind('<FocusIn>', on_focus_in_groupby)
groupby_target_entry.bind('<FocusOut>', on_focus_out_groupby)

groupby_agg_entry = ttk.Entry(groupby_frame, width=15)
groupby_agg_entry.insert(0, "Agg func")
groupby_agg_entry.grid(row=0, column=3, padx=5, pady=5)
groupby_agg_entry.bind('<FocusIn>', on_focus_in_groupby)
groupby_agg_entry.bind('<FocusOut>', on_focus_out_groupby)

ttk.Checkbutton(groupby_frame, text="With reset_index", variable=reset_index_var).grid(row=0, column=4, padx=15, pady=5, sticky='w')

btn_grp = ttk.Button(groupby_frame, text="Apply", command=apply_groupby, style='Accent.TButton')
btn_grp.grid(row=0, column=5, padx=(25, 5), pady=5)

btn_plot = ttk.Button(groupby_frame, text="Plot", command=plotting_action, style='Accent.TButton')
btn_plot.grid(row=1, column=5, padx=(25, 5), pady=5)

# --- 3. Cut Section ---
cut_frame = tk.Frame(root)
cut_frame.pack(padx=20, pady=10, fill="x")

tk.Label(cut_frame, text="Cut").grid(row=0, column=0, padx=5, pady=5, sticky='w')

cut_col_entry = ttk.Entry(cut_frame, width=20)
cut_col_entry.insert(0, "Column name")
cut_col_entry.grid(row=0, column=1, padx=5, pady=5)
cut_col_entry.bind('<FocusIn>', on_focus_in_cut)
cut_col_entry.bind('<FocusOut>', on_focus_out_cut)

cut_bins_entry = ttk.Entry(cut_frame, width=15)
cut_bins_entry.insert(0, "Bins (e.g., 0, 10, 20)")
cut_bins_entry.grid(row=0, column=2, padx=5, pady=5)
cut_bins_entry.bind('<FocusIn>', on_focus_in_cut)
cut_bins_entry.bind('<FocusOut>', on_focus_out_cut)

cut_labels_entry = ttk.Entry(cut_frame, width=15)
cut_labels_entry.insert(0, "Labels (e.g., Low, High)")
cut_labels_entry.grid(row=0, column=3, padx=5, pady=5)
cut_labels_entry.bind('<FocusIn>', on_focus_in_cut)
cut_labels_entry.bind('<FocusOut>', on_focus_out_cut)

ttk.Button(cut_frame, text="Apply", command=apply_cut, 
           style='Accent.TButton').grid(row=0, column=5, padx=215, pady=5)

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

tk.Button(root,text="Delete TView",command=reset_treeView).pack()
ttk.Button(root, text="Save Result to CSV", command=save_result_to_csv,
           style='Accent.TButton').pack(pady=10)

root.mainloop()