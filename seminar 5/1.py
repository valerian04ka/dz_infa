from tkinter import *
from tkinter import ttk


root = Tk()     
root.title("Приложение на Tkinter")    
root.geometry("300x300")    
 
label = Label(text="Hello") 
label.pack()   

btn = ttk.Button(text="Click") # создаем кнопку из пакета ttk
btn.pack()  

def finish():
    root.destroy()  # ручное закрытие окна и всего приложения. обратите внимание, что к root обращаемся как к глобальной переменной
    print("App closed")
root.protocol("WM_DELETE_WINDOW", finish)

root.mainloop()