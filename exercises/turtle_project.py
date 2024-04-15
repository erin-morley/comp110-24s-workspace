"""Turtle project titled 'A starry night with abduction'. It shows a person next to their house being abducted by an alien's spiral wavelength under the stars and the moon.

Above and beyond points: 
line 110 circle function used
lines 42-54 use a recursive 'spiral' function to create the abduction spiral.
"""
__author__ = "730670116"
from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    James: Turtle = Turtle()
    star(James, 70, 75, 20)
    star(James, 250, 200, 40)
    star(James, -100, 75, 20)
    star(James, -200, 125, 40)
    star(James, 0, 225, 40)
    house(James, -200, -200)
    person(James, 150, -250)
    moon(James, -225, 350)
    spiral(James, 150, 270, 100)
    done()


def star(star_turtle: Turtle, x: float, y: float, length: float) -> None:
    """Draws a star."""
    star_turtle.penup()
    star_turtle.goto(x, y)
    star_turtle.begin_fill()
    star_turtle.pencolor("black")
    star_turtle.fillcolor("yellow")
    idx: int = 0
    while idx < 6:
        star_turtle.forward(length)
        star_turtle.left(144)
        star_turtle.pendown()
        idx += 1
    star_turtle.end_fill()


def spiral(spiral_turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Draws a spiral. This is the alien abduction."""
    spiral_turtle.penup()
    spiral_turtle.pencolor("green")
    spiral_turtle.goto(x, y)
    spiral_turtle.pendown()
    spiral_turtle.circle(radius)
    y -= 20
    radius -= 7
    if radius > 1:
        spiral(spiral_turtle, x, y, radius)
    else: 
        return


def person(person_turtle: Turtle, x: float, y: float) -> None:
    """Draws a person."""
    person_turtle.penup()
    person_turtle.color("brown")
    person_turtle.goto(x, y)
    person_turtle.pendown()
    person_turtle.right(50)
    person_turtle.forward(50)
    person_turtle.left(30)
    person_turtle.forward(20)
    person_turtle.right(180)
    person_turtle.forward(20)
    person_turtle.left(120)
    person_turtle.forward(20)
    person_turtle.right(180)
    person_turtle.forward(20)
    person_turtle.left(30)
    person_turtle.forward(40)
    person_turtle.right(90)
    person_turtle.forward(20)
    person_turtle.right(180)
    person_turtle.forward(40)
    person_turtle.penup()
    person_turtle.goto(x, y + 20)
    person_turtle.pendown()
    person_turtle.circle(10)


def house(house_turtle: Turtle, x: float, y: float) -> None:
    """Draws a house."""
    house_turtle.penup()
    house_turtle.goto(x, y)
    house_turtle.begin_fill()
    house_turtle.fillcolor(177, 219, 217)
    house_turtle.pendown()
    idx: int = 0
    while idx < 4:
        house_turtle.forward(100)
        house_turtle.right(90)
        idx += 1
    house_turtle.left(40)
    house_turtle.forward(65)
    house_turtle.right(80)
    house_turtle.forward(65)
    house_turtle.end_fill()


def moon(moon_turtle: Turtle, x: float, y: float) -> None:
    """Draws a moon."""
    moon_turtle.penup()
    moon_turtle.goto(x, y)
    moon_turtle.begin_fill()
    moon_turtle.fillcolor("light yellow")
    moon_turtle.circle(75)
    moon_turtle.end_fill()
    moon_turtle.pendown()


if __name__ == "__main__":
    main()