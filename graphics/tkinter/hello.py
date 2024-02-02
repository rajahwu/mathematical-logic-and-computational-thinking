import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.title("Python GUI")

def click_me():
    action.configure(text='Hello ' + name.get())

ttk.Label(window, text="Enter a name:").grid(column=0, row=0)

name = tk.StringVar()
name_entered = ttk.Entry(window, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

action = ttk.Button(window, text="Click Me!", command=click_me)
action.grid(column=1, row=1)
action.configure(state='disabled')

name_entered.focus()

window.mainloop()
