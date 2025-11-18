import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()

root.title("My App für Kreis")
root.geometry("500x400")


def kreis(r):
    if r > 10:
        return f"Fehler! {r} muss kleiner als 10 sein"
    else:
        theta = np.linspace(0, 2 * np.pi, 100)
        x = r * np.cos(theta) 
        y = r * np.sin(theta)
        fig1 = 1
        fig2 = 1
        # plt.figure(figsize=(r*fig1, r*fig2)) # Setzt die Figurgröße auf quadratisch
        # plt.plot(x, y, color='blue', linestyle='-')
        # plt.gca().set_aspect('equal', adjustable='box')
        # plt.grid()
        # plt.show()
    #return figure

def kreismachen():
    r = radius_entry.get()
    fig = kreis(int(r))
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()

    # r = float(r)
    # kreis(r)

tk.Label(root, text="Radius").grid(column=0, row=0,columnspan=2)
radius_entry = tk.Entry()
radius_entry.grid(column=0,row=1)

tk.Button(root, text="Click me for circle", command=kreismachen).grid(column=0, row=3)

root.mainloop()