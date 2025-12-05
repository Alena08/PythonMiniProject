import tkinter as tk
from tkinter import ttk
import myapp_functions

def build_gui(root):
    """
    Builds the entire Tkinter interface.
    """
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
                    command=lambda: myapp_functions.set_load_mode('local', load_mode_var)).grid(row=0, column=0, padx=5, pady=5, sticky='w')

    local_file_entry = ttk.Entry(load_frame, width=30)
    local_file_entry.insert(0, "csv/xlsx")
    local_file_entry.grid(row=0, column=1, padx=10, pady=5)

    ttk.Radiobutton(load_frame, text="Choose Data Frame From SNS", variable=load_mode_var, value="seaborn", 
                    command=lambda: myapp_functions.set_load_mode('seaborn', load_mode_var)).grid(row=1, column=0, padx=5, pady=5, sticky='w')

    # Dropdown for Seaborn datasets
    seaborn_menu = ttk.OptionMenu(load_frame, seaborn_dataset_var, *([seaborn_dataset_var.get()] + myapp_functions.sns_datasets))
    seaborn_menu.config(width=28)
    seaborn_menu.grid(row=1, column=1, padx=10, pady=5)

    ttk.Button(load_frame, text="OPEN", command=lambda: myapp_functions.open_data_source(local_file_entry, seaborn_dataset_var, load_mode_var, root, tree), 
            style='Accent.TButton').grid(row=0, column=2, rowspan=2, padx=0, pady=5, sticky='ns')

    # --- 2. Group By Section ---
    groupby_frame = tk.Frame(root)
    groupby_frame.pack(padx=20, pady=10, fill="x")

    tk.Label(groupby_frame, text="Group By").grid(row=0, column=0, padx=5, pady=5, sticky='w')
    groupby_entries = {}

    groupby_entries['cols'] = ttk.Entry(groupby_frame, width=15)
    groupby_entries['cols'].insert(0, "Column names")
    groupby_entries['cols'].grid(row=0, column=1, padx=5, pady=5)
    groupby_entries['cols'].bind('<FocusIn>', lambda e: myapp_functions.on_focus_in_groupby(e, groupby_entries))
    groupby_entries['cols'].bind('<FocusOut>', lambda e: myapp_functions.on_focus_out_groupby(e, groupby_entries))
    
    groupby_entries['target'] = ttk.Entry(groupby_frame, width=15)
    groupby_entries['target'].insert(0, "Target Column") 
    groupby_entries['target'].grid(row=0, column=2, padx=5, pady=5)
    groupby_entries['target'].bind('<FocusIn>', lambda e: myapp_functions.on_focus_in_groupby(e, groupby_entries))
    groupby_entries['target'].bind('<FocusOut>', lambda e: myapp_functions.on_focus_out_groupby(e, groupby_entries))

    groupby_entries['agg'] = ttk.Entry(groupby_frame, width=15)
    groupby_entries['agg'].insert(0, "Agg func")
    groupby_entries['agg'].grid(row=0, column=3, padx=5, pady=5)
    groupby_entries['agg'].bind('<FocusIn>', lambda e: myapp_functions.on_focus_in_groupby(e, groupby_entries))
    groupby_entries['agg'].bind('<FocusOut>', lambda e: myapp_functions.on_focus_out_groupby(e, groupby_entries))

    ttk.Checkbutton(groupby_frame, text="With reset_index", variable=reset_index_var).grid(row=0, column=4, padx=15, pady=5, sticky='w')

    btn_grp = ttk.Button(groupby_frame, text="Apply", command=lambda: myapp_functions.apply_groupby(groupby_entries, reset_index_var,tree, root))
    btn_grp.grid(row=0, column=5, padx=(25, 5), pady=5)

    btn_plot = ttk.Button(groupby_frame, text="Plot", command=myapp_functions.plotting_action)
    btn_plot.grid(row=1, column=5, padx=(25, 5), pady=5)

        # --- 3. Cut Section ---
    cut_frame = tk.Frame(root)
    cut_frame.pack(padx=20, pady=10, fill="x")

    tk.Label(cut_frame, text="Cut").grid(row=0, column=0, padx=5, pady=5, sticky='w')
    cut_entries = {}

    cut_entries['col'] = ttk.Entry(cut_frame, width=15)
    cut_entries['col'].insert(0, "Column name")
    cut_entries['col'].grid(row=0, column=1, padx=5, pady=5)
    cut_entries['col'].bind('<FocusIn>', lambda e: myapp_functions.on_focus_in_cut(e, cut_entries))
    cut_entries['col'].bind('<FocusOut>', lambda e: myapp_functions.on_focus_out_cut(e, cut_entries))

    cut_entries['bins'] = ttk.Entry(cut_frame, width=15)
    cut_entries['bins'].insert(0, "Bins (e.g., 0, 10, 20)")
    cut_entries['bins'].grid(row=0, column=2, padx=5, pady=5)
    cut_entries['bins'].bind('<FocusIn>', lambda e: myapp_functions.on_focus_in_cut(e, cut_entries))
    cut_entries['bins'].bind('<FocusOut>', lambda e: myapp_functions.on_focus_out_cut(e, cut_entries))

    cut_entries['labels'] = ttk.Entry(cut_frame, width=15)
    cut_entries['labels'].insert(0, "Labels (e.g., Low, High)")
    cut_entries['labels'].grid(row=0, column=3, padx=5, pady=5)
    cut_entries['labels'].bind('<FocusIn>', lambda e: myapp_functions.on_focus_in_cut(e, cut_entries))
    cut_entries['labels'].bind('<FocusOut>', lambda e: myapp_functions.on_focus_out_cut(e, cut_entries))

    ttk.Button(cut_frame, text="Apply", command=lambda: myapp_functions.apply_cut(cut_entries, tree, root), 
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

    tk.Button(root,text="Delete TView",command=lambda: myapp_functions.reset_treeView(tree)).pack()
    ttk.Button(root, text="Save Result to CSV", command=myapp_functions.save_result_to_csv,
            style='Accent.TButton').pack(pady=10)


    return tree