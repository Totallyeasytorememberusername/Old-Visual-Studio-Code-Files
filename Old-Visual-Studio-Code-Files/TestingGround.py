import tkinter as tk
from turtle import RawTurtle, TurtleScreen, ScrolledCanvas

root = tk.Tk()
root.attributes("-alpha", 0.3)

canvas = ScrolledCanvas(root)
canvas.pack()

screen = TurtleScreen(canvas)

turtle = RawTurtle(screen)
turtle.width(10)

turtle.penup()
turtle.sety(-100)
turtle.pendown()
turtle.circle(100)

screen.mainloop()