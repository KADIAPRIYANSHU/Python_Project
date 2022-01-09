from tkinter import Tk
from tkinter import Label
import time

master = Tk()
master.title("Digital Clock")

def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200,get_time)

clock = Label(master,font=("Calibari",90),bg="grey",fg="white")
clock.pack()

get_time()

master.mainloop()
