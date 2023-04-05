import tkinter as tk
win = tk.Tk()

WIDTH = 500
HEIGHT = 500
x = 0
y = 0


def clicker(e):
    global x,y
    zoz= canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if ob1 in zoz:
        x= e.x
        y= e.y

def mover(e):
    global x,y
    print("som stlaceny a ma taha")
    if x!=0 and y!=0:
        dx = e.x - x
        dy = e.y - y
        canvas.move(ob1,dx,dy)
        x = e.x
        y = e.y

def releaser(e):
    global x,y
    x,y=0,0


canvas = tk.Canvas(win,height=HEIGHT,width=WIDTH,bg="white")
canvas.pack()

ob1 = canvas.create_polygon(10,10,50,80,140,82, fill="green")
canvas.bind("<Button-1>", clicker)
canvas.bind("<B1-Motion>",mover)
canvas.bind("<ButtonRelease>",releaser)

win.mainloop()


