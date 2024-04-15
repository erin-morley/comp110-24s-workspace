"""Turtle tutorial."""
# TO RUN - python3 -m lessons.turtle_tutorial
from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
leo.speed(50)
leo.pencolor("pink")
leo.goto(-150, -100)
i: int = 1
while i < 3:
    leo.forward(300)
    leo.left(120)
    i = i + 1
done()

house_turtle.left(40)
    house_turtle.forward(65)
    house_turtle.right(80)
    house_turtle.forward(65)