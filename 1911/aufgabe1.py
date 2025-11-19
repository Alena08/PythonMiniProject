import tkinter as tk
from tkinter import messagebox

def clear_main():
    for widget in info_frame.winfo_children():
        widget.destroy()
 

def login_function():
    clear_main()
    tk.Label(info_frame, text='Username', background='white').grid(column=0, row=0, pady=50, padx=20)
    tk.Label(info_frame, text='Password', background='white').grid(column=0, row=1, pady=30, padx=20)
    user_entry = tk.Entry(info_frame)
    user_entry.grid(column=1, row=0,padx=20, pady=10)

    password_entry = tk.Entry(info_frame, show='*')
    password_entry.grid(column=1, row=1,padx=20, pady=10)
    form_login = tk.Button(info_frame, text='Login', command=submit_form)
    form_login.grid(column=1, row=2)

def sign_function():
    clear_main()
    tk.Label(info_frame, text='Username', background='white').grid(column=0, row=0, pady=50, padx=20)
    tk.Label(info_frame, text='Password', background='white').grid(column=0, row=1, pady=30, padx=20)
    sign_user_entry = tk.Entry(info_frame)
    sign_user_entry.grid(column=1, row=0,padx=20, pady=10)

    sign_password_entry = tk.Entry(info_frame, show='*')
    sign_password_entry.grid(column=1, row=1,padx=20, pady=10)
    var_radio = tk.StringVar(value="Female2")
    radio1 = tk.Radiobutton(info_frame, text="Male", variable=var_radio, value="Male1")
    radio2 = tk.Radiobutton(info_frame, text="Female", variable=var_radio, value="Female2")
    radio1.grid(column=1, row=3)
    radio2.grid(column=1, row=4)

    sign_form_login = tk.Button(info_frame, text='Login', command=submit_signform)
    sign_form_login.grid(column=1, row=5, pady=20)


def about_function():
    clear_main()
    tk.Label(info_frame, text="It's the best programm ever ").grid(column=0, row=1, columnspan=2, padx=20, pady=20, sticky="nsew")
    # text_field = tk.Text(info_frame, width=300, height=300)
    # text_field.grid(column=0, row=1, columnspan=2, padx=20, pady=20, sticky="nsew")
    # inhalt = "It's the best programm ever " 
    # text_field.insert("1.0", inhalt)

def submit_form():
    messagebox.showinfo('Login info','User ist eingeloggt!')

def submit_signform():
    messagebox.showinfo('Sign info','User is regestered!')

root = tk.Tk()
root.title("Work with file")
root.geometry('400x350')

btn_frame = tk.Frame(root, background='red')
btn_frame.grid(column=0, row=0)

info_frame = tk.Frame(root, background='white', width=300, height=300)
info_frame.grid(column=1, row=0)

btn_login = tk.Button(btn_frame, text="Login", command=login_function)
btn_login.grid(column=0,row=0,padx=50, pady=10)

btn_sign = tk.Button(btn_frame, text="Signup", command=sign_function)
btn_sign.grid(column=0,row=1,padx=20, pady=10)

btn_about = tk.Button(btn_frame, text='About', command=about_function)
btn_about.grid(column=0, row=2, padx=20, pady=100)

login_function()






root.mainloop()