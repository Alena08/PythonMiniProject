### schreiben Sie Ihren Code hier ###
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def kreis(r):
    wb = np.linspace(0, 2*np.pi,100)
    cps = r * np.cos(wb) #+ r
    sp = r * np.sin(wb) #+ r

    figure,axes = plt.subplots(1)

    axes.plot(cps, sp)
    axes.set_aspect(1)

    plt.title(f"Kreis mit {r}")
    plt.grid()
    return figure
    #plt.show()

canvas = None
def mal_kreis():
    global canvas
    radius = entry.get()
    #kreis(int(radius))
    if canvas:
        canvas.get_tk_widget().destroy()
        canvas = None
    fig = kreis(int(radius))
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

root= tk.Tk()

root.geometry("400x500")
root.title("Kreis Zeichnen")
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Zeichne Kreis", command=mal_kreis).pack()

root.mainloop()
### Hauptprogramm ###
#####################
#kreis(1)