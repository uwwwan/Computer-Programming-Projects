import turtle
from turtle import *
print("———————————————————————————————")
print("Available Shapes: Triangle, Square, Circle, Star, Pentagon ,Hexagon")
print("———————————————————————————————")
shapes = input("Choose A Shape: ") .lower()
def jump(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

shapesPos = input("Enter Position (x, y): ").split(',')
x, y = map(float, shapesPos)

fill = input("Enter color name: ").lower()

def star():
  jump(x, y)
  turtle.fillcolor(fill)
  turtle.begin_fill()
  for count in range(5):
      turtle.forward(100)
      turtle.left(144)
  turtle.end_fill()

def circle():
    jump(x, y)
    turtle.fillcolor(fill)
    turtle.begin_fill()
    for count in range(1):
        turtle.circle(50)
    turtle.end_fill()

def square():
    jump(x, y)
    turtle.fillcolor(fill)
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()

def triangle():
    jump(x, y)
    turtle.fillcolor(fill)
    turtle.begin_fill()
    for count in range(3):
        turtle.forward(100)
        turtle.left(120)
    turtle.end_fill()

def pentagon():
    jump(x, y)
    turtle.fillcolor(fill)
    turtle.begin_fill()
    for count in range(5):
        turtle.forward(100)
        turtle.left(72)
    turtle.end_fill()

def hexagon():
    jump(x, y)
    turtle.fillcolor(fill)
    turtle.begin_fill()
    for count in range(6):
        turtle.forward(100)
        turtle.left(60)
    turtle.end_fill()


if shapes == ("star"):
    star()
    turtle.done()
elif shapes == ("triangle"):
    triangle()
    turtle.done()
elif shapes == ("circle"):
    circle()
    turtle.done()
elif shapes == ("square"):
    square()
    turtle.done()
elif shapes == ("pentagon"):
    pentagon()
    turtle.done
elif shapes == ("hexagon"):
    hexagon()
    turtle.done
else:
    print("———————————————————————————————")
    print("Not Available, Try Other Shape")
    print("———————————————————————————————")


