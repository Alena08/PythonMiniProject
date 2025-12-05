import tkinter as tk
from tkinter import ttk

import seaborn as sns

#print(sns.get_dataset_names())

df = sns.load_dataset("tips")

print(list(df.columns))

root = tk.Tk()
root.geometry("400x300")

df_columns = list(df.columns)
tree = ttk.Treeview(root, columns=df_columns, show='headings')

# Spalten Definieren (heading)
for col in df_columns:
    tree.heading(col,text=col)
    tree.column(col, width=100, anchor='center')

#Convertiere DataFrame in eine Liste von Listen
df_rows = df.astype(str).values.tolist()
for row in df_rows:
    tree.insert('',tk.END, values=row)

#Vertikal Scrollbar
vsb = ttk.Scrollbar(root,orient='vertical', command= tree.yview)
vsb.pack(side='right',fill='y')
tree.configure(yscrollcommand=vsb.set)

#Horizental Scrollbar
vsb = ttk.Scrollbar(root,orient='horizontal', command= tree.xview)
vsb.pack(side='bottom',fill='x')
tree.configure(xscrollcommand=vsb.set)

tree.pack(expand=True, fill='both')

def reset_treeView():
    global tree
    children = tree.get_children()
    if children:
        tree.delete(*children)

tk.Button(root,text="Delete TViewI",command=reset_treeView).pack()
root.mainloop()