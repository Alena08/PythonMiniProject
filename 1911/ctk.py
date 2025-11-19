import customtkinter as ctk

root = ctk.CTk()
root.geometry("500x500")
root.title("Hello CTk")

root._set_appearance_mode("dark")
ctk.CTkButton(root, text="Click me!", bg_color="transparent", corner_radius=30).place(x=50, y=50)

root.mainloop()