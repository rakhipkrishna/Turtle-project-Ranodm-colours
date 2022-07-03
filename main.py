from turtle import Turtle,Screen
import random

tim = Turtle()
#Create a Turtle of red colour
#timmy_the_turtle.shape("turtle")
#timmy_the_turtle.color("red")
#Create a square
"""
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)
"""

#Create a dotted line
"""
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.penup()
"""

#draw different shapes

"""
for x in range(3):
    tim.forward(100)
    tim.right(120)

for x in range(4):
    tim.forward(100)
    tim.right(90)

for x in range(5):
    tim.forward(100)
    tim.right(72)

for x in range(6):
    tim.forward(100)
    tim.right(60)

for x in range(7):
    tim.forward(100)
    tim.right(51.43)

for x in range(8):
    tim.forward(100)
    tim.right(45)

for x in range(9):
    tim.forward(100)
    tim.right(40)

for x in range(10):
    tim.forward(100)
    tim.right(36)

"""
Colours = ['cyan','lime','red','blue','green','magenta','pink','gold','khaki']

def draw_shape(num_slide):
    angle = 360 / num_slide
    for sides in range(num_slide):
        tim.forward(100)
        tim.right(angle)

for shape_sides in range(3,11):
    tim.color(random.choice(Colours))
    draw_shape(shape_sides)



screen = Screen()
screen.exitonclick()
