from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Калькулятор")

mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))

calc = StringVar()
entry = ttk.Entry(mainframe, width = 7, textvariable = calc)
entry.grid(column =  2, row = 1, sticky = (W, E))

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        pass    
     

Button(root, text = "=", width = 18, height = 2, command = calculate).grid(row = 1, column = 0)
entry.focus()
root.mainloop()