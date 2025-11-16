
import tkinter

root_window = tkinter.Tk()

def printSomething():
    name = entry.get()
    #btn.config(text=name)
    btn['text'] = name
    print(f"Hello {name} from Tk!")

tkinter.Label(root_window,text="Enter Your name:").pack()
entry = tkinter.Entry(root_window)
entry.pack()
btn = tkinter.Button(root_window, text="Click Me!", command=printSomething)
btn.pack()


root_window.geometry("600x400")
root_window.title("Hello TK")

root_window.mainloop()
