import tkinter as tk
from tkinter.constants import X, Y
from turtle import title

from pip import main
mywindow = tk.Tk()
mywindow.title("ventana con tkinter")
mywindow.geometry("600x400")
mywindow.resizable(False,False)
mywindow.config(background="#2798FA")
main_title = tk.Label (text= "Parcial elaborado por: Juan Sebastian santanilla Bermeo :) ", font= ("tahoma",14), bg="#ff7763", fg="black", width="60", height="10")
main_title.place(x = 0, y = 50)
mywindow.tk.mainloop()