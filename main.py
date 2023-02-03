from tkinter import *
import random

# creation de la fenetre
fen = Tk()
fen.title("mon ecran enneigé")
fen.geometry("600x600")
canva = Canvas(fen, width=600, height=600, bg="black")
canva.place(x=0, y=0)
# creation des boules de neige
for i in range(200):
    d = random.randint(1, 25)
    x = random.randint(0, 600)
    y = random.randint(50, 600)
    canva.create_oval(x, y, x + d, y + d, fill="#33FFFF")

fen.mainloop()
