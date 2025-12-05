import tkinter as tk
from myapp_gui import build_gui

if __name__ == "__main__":
    root = tk.Tk()
    tree = build_gui(root)
    root.mainloop()