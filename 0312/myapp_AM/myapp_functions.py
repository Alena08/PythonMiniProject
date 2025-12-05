import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- Global Data Storage ---
data_frame = None
last_result_df = None
last_agg_col_name = None
sns_datasets = sns.get_dataset_names()

def set_load_mode(mode, load_mode_var):
    """Sets the active loading mode: 'local' or 'seaborn'."""
    load_mode_var.set(mode)

def display_data(df_to_display, title, tree, root):
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

def open_data_source(local_file_entry, seaborn_dataset_var, load_mode_var, root, tree):
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

                display_data(data_frame, "Local File Loaded", tree, root)
            except Exception as e:
                messagebox.showerror("Loading Error", f"Failed to load file: {e}")
    
    elif mode == 'seaborn':
        dataset_name = seaborn_dataset_var.get()
        if dataset_name == "Select Seaborn Dataset":
            messagebox.showwarning("Warning", "Please select a dataset from the list.")
            return
        try:
            data_frame = sns.load_dataset(dataset_name)
            display_data(data_frame, f"Dataset '{dataset_name}' Loaded", tree, root)
        except Exception as e:
            messagebox.showerror("Loading Error", f"Failed to load dataset: {e}")

def apply_groupby(entries, reset_index_var, tree, root):
    """
    Applies the GROUPBY operation based on user input fields.
    """
    global data_frame, last_result_df, last_agg_col_name
    if data_frame is None:
        messagebox.showwarning("Warning", "Please load a dataset first!")
        return
        
    cols_input = entries['cols'].get().strip()
    target_col = entries['target'].get().strip()
    agg_func = entries['agg'].get().strip()
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

        display_data(result_df, "GROUPBY Result", tree, root)
        # Resetting GROUP BY fields
        entries['cols'].delete(0, tk.END)
        entries['cols'].insert(0, "Column names")
        entries['target'].delete(0, tk.END)
        entries['target'].insert(0, "Target Column")
        entries['agg'].delete(0, tk.END)
        entries['agg'].insert(0, "Agg func")
            
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

def apply_cut(entries, tree, root):
    """
    Applies the CUT operation based on user input fields.
    """
    global data_frame, last_result_df
    if data_frame is None:
        messagebox.showwarning("Warning", "Please load a dataset first!")
        return
        
    col_to_cut = entries['col'].get().strip()
    bins_input = entries['bins'].get().strip()
    labels_input = entries['labels'].get().strip()

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
        
        display_data(result_df, f"CUT Result", tree, root)
        last_result_df = result_df.copy()
        # Resetting CUT fields
        entries['col'].delete(0, tk.END)
        entries['col'].insert(0, "Column name")
        entries['bins'].delete(0, tk.END)
        entries['bins'].insert(0, "Bins (e.g., 0, 10, 20)")
        entries['labels'].delete(0, tk.END)
        entries['labels'].insert(0, "Labels (e.g., Low, High)")
            
    except KeyError:
        messagebox.showerror("Operation Error", f" {col_to_cut} not found")
    except Exception as e:
        messagebox.showerror("Operation Error", f"Error executing CUT: {e}")

def on_focus_in_groupby(event, entries):
    """
    Clears the entry field content when the widget receives focus, 
    if the content is the default placeholder text.
    """
    widget = event.widget
    if widget == entries['cols'] and widget.get() == "Column names":
        widget.delete(0, tk.END)
    elif widget == entries['target'] and widget.get() == "Target Column":
        widget.delete(0, tk.END)
    elif widget == entries['agg'] and widget.get() == "Agg func":
        widget.delete(0, tk.END)

def on_focus_out_groupby(event, entries):
    """Inserts placeholder if the field is left empty when losing focus."""
    widget = event.widget
    if not widget.get():
        if widget == entries['cols']:
            widget.insert(0, "Column names")
        elif widget == entries['target']:
            widget.insert(0, "Target Column")
        elif widget == entries['agg']:
            widget.insert(0, "Agg func")

def on_focus_in_cut(event, entries):
    """
    Clears the entry field content when the widget receives focus, 
    if the content is the default placeholder text.
    """
    widget = event.widget
    if widget == entries['col'] and widget.get() == "Column name":
        widget.delete(0, tk.END)
    elif widget == entries['bins'] and widget.get() == "Bins (e.g., 0, 10, 20)":
        widget.delete(0, tk.END)
    elif widget == entries['labels'] and widget.get() == "Labels (e.g., Low, High)":
        widget.delete(0, tk.END)

def on_focus_out_cut(event, entries):
    """Inserts placeholder if the field is left empty when losing focus."""
    widget = event.widget
    if not widget.get():
        if widget == entries['col']:
            widget.insert(0, "Column name")
        elif widget == entries['bins']:
            widget.insert(0, "Bins (e.g., 0, 10, 20)")
        elif widget == entries['labels']:
            widget.insert(0, "Labels (e.g., Low, High)")

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

def reset_treeView(tree):
    children = tree.get_children()
    if children:
        tree.delete(*children)
