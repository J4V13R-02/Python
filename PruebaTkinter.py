from sys import prefix
from tkinter import *

window = Tk() #inicializa la ventana
window.geometry("300x300")
window.title("TKinter")
window.configure(background="blue")

clicks = 0

def clickar():
    global clicks
    clicks += 1
    label.config(text=f"Clicks: {clicks}")

button = Button(window, text="Pulsa")
button.pack()
button.place(x=150, y=200, anchor=S)
button.config(command=clickar)

label = Label(
    window,
    text=clicks,
    font=("Comic sans", 20),
    relief=RAISED,
    padx = 20,
    pady = 20
)
label.pack()
label.place(x=150, y=100, anchor=CENTER)

window.mainloop() #muestra la ventana