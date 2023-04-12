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
time = 100
status ="true"


def DrawWires():
    global wires,explosion
    for i in range(len(colors)):
        wires.append(canvas.create_rectangle(ux,uy+height*i,ux+width,uy+height*(i+1),fill=colors[i]))
    explosion = random.choice(wires)
    print(explosion)

def clicker(e):
    print("klikol")

def change():
    global time
    time -=1
    canvas.itemconfig(t,text=time)
    canvas.after(100,change)
    if status:
        canvas.after(100,change)

canvas = tk.Canvas(win,height=500,width=500,bg="white")
canvas.pack()
t= canvas.create_text(10,10,text=time)
canvas.bind("<Button-1>",clicker)
change()
DrawWires()
win.mainloop()
