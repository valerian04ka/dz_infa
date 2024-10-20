from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        m = float(mass.get())
        h = float(height.get())
        i= int(m)/float(h)**2
        index.set(i)
        if i < 16:
            result.set("Выраженный дефицит массы тела")
        if i <= 18.5 and i > 16 :
            result.set("Недостаточная (дефицит) масса тела")
        if i <= 25 and i > 18.5 :
            result.set("Норма")
        if i <= 30 and i > 25 :
            result.set("Избыточная масса тела (предожирение)")
        if i <= 35 and i > 30 :
            result.set("Ожирение 1 степени")
        if i <= 40 and i > 35 :
            result.set("Ожирение 2 степени")
        if i > 40:
            result.set("Ожирение 3 степени")
        
    except ValueError:
        pass

root = Tk()
root.title("Body mass indeX")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


mass = StringVar()
mass_entry = ttk.Entry(mainframe, width=7, textvariable=mass)
mass_entry.grid(column=2, row=1, sticky=(W, E))

height = StringVar()
height_entry = ttk.Entry(mainframe, width=7, textvariable=height)
height_entry.grid(column=2, row=2, sticky=(W, E))

index = StringVar()
ttk.Label(mainframe, textvariable=index).grid(column=2, row=3,sticky=(W, E))

result = StringVar()
ttk.Label(mainframe, textvariable=result).grid(column=2, row=4, sticky=(W, E))


ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=4, row=3, sticky=W)

ttk.Label(mainframe, text="mass").grid(column=3, row=1, sticky=E)
ttk.Label(mainframe, text="height").grid(column=3, row=2, sticky=E)
ttk.Label(mainframe, text="your body mass index is").grid(column=1, row=3, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

mass_entry.focus()
root.bind("<Return>", calculate)
root.mainloop()