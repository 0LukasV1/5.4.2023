import tkinter as tk
import random
win = tk.Tk()
colors= ["red","orange","blue","green","turquoise"]
width= 300
height= 10
ux = 100
uy = 100
wires =[]
explosion = 0


def DrawWires():
    global wires,explosion
    for i in range(len(colors)):
        wires.append(canvas.create_rectangle(ux,uy+height*i,ux+width,uy+height*(i+1),fill=colors[i]))
    explosion = random.choice(wires)
    print(explosion)

def clicker(e):
    print("klikol")


canvas = tk.Canvas(win,height=500,width=500,bg="white")
canvas.pack()
canvas.bind("<Button-1>",clicker)
DrawWires()
win.mainloop()


