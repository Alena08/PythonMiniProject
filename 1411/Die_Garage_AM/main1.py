from parkhaus import Parkhaus
from car import Car
from moto import Moto
import tkinter as tk
from tkinter import ttk, messagebox

autos = []

def submit():
    # Parkhaus erstellen
    anzahl_etagen = int(num_etagen.get())
    parkplases = int(plaetze_pro_etage.get())
    global parkhaus_vence
    parkhaus_vence = Parkhaus(anzahl_etagen, parkplases)
    #messagebox.showinfo("Garage Konfig", parkhaus_vence)

def submit_auto():
    id = auto_id.get()
    auto = Car(id) 
    autos.append(auto)

def submit_moto():
    m_id = moto_id.get()
    moto = Moto(m_id) 
    autos.append(moto)

def parken_auto():
    ind=0
    f_id = fahrzeug_id.get()
    for i, auto in enumerate(autos):
        if auto.id == f_id:
            ind = i
            break    
    parkhaus_vence.parken(autos[ind])

def ausparken():
    f_id_aus = fahrzeug_id_aus.get()
    parkhaus_vence.verlassen(f_id_aus)

def submit_status(): 
    info_message = parkhaus_vence.getStatus()
    info_area.config(text=info_message)

def getPosition():
    f_status = fahrzeug_id_status.get()
    info_status = parkhaus_vence.get_position(f_status)
    info_area.config(text=info_status)


root = tk.Tk()
root.title("Daten Garage")
root.geometry("700x400")
tk.Label(root, text="Interaktive Konfiguration").grid(column=0, row=0, columnspan=4)

tk.Label(root, text="Anzahl der Etagen").grid(column=0, row=1)
num_etagen = ttk.Entry()
num_etagen.grid(column=0, row=2)
#num_etagen.insert(0, "Anzahl der Etagen")

tk.Label(root, text="Anzahl der Parkplätze").grid(column=1, row=1)
plaetze_pro_etage = ttk.Entry()
plaetze_pro_etage.grid(column=1, row=2)
#plaetze_pro_etage.insert(0, "Anzahl der Parkplätze")

submit_btn = tk.Button(root, text="Einlegen", command=submit)
submit_btn.grid(column=2, row=2)

tk.Label(root, text="Fahrzeuge Daten").grid(column=1, row=3, columnspan=3)

tk.Label(root, text="Kennzeichen").grid(column=0, row=4)
auto_id = ttk.Entry()
auto_id.grid(column=0, row=5)
#auto_id.insert(0, "Kennzeichen")

submit_btn_auto = tk.Button(root, text="Auto Einlegen", command=submit_auto)
submit_btn_auto.grid(column=1, row=5)

tk.Label(root, text="Kennzeichen").grid(column=2, row=4)
moto_id = ttk.Entry()
moto_id.grid(column=2, row=5)
#moto_id.insert(0, "Kennzeichen")

submit_btn_moto = tk.Button(root, text="Moto Einlegen", command=submit_moto)
submit_btn_moto.grid(column=3, row=5)

# Operationen
tk.Label(root, text="Operationen").grid(column=0, row=6, columnspan=5)

fahrzeug_id = ttk.Entry()
fahrzeug_id.grid(column=0, row=7)

parken_btn = tk.Button(root, text="Parken", command=parken_auto)
parken_btn.grid(column=1, row=7)

fahrzeug_id_aus = ttk.Entry()
fahrzeug_id_aus.grid(column=0, row=8)

ausparken_btn = tk.Button(root, text="AusParken", command=ausparken)
ausparken_btn.grid(column=1, row=8)

fahrzeug_id_status = ttk.Entry()
fahrzeug_id_status.grid(column=0, row=9)

ausparken_btn = tk.Button(root, text="GetPosition", command=getPosition)
ausparken_btn.grid(column=1, row=9)

phStatus_btn = tk.Button(root, text="PH Status", command=submit_status)
phStatus_btn.grid(column=2, row=7, columnspan=2)

info_frame = tk.Frame(root, width=100, height=150, background="white")
info_frame.grid(column=2, row=8, rowspan=5)
info_area = ttk.Label(info_frame,text="Click the button to see information here.")
info_area.pack(padx=5, pady=5)



root.mainloop()