from random import randint
import turtle


number_of_turtles = 100
steps_of_time_number = 100
turtle.penup()
turtle.goto(-250, 250)
turtle.pendown()
turtle.goto(250, 250)
turtle.goto(250, -250)
turtle.goto(-250, -250)
turtle.goto(-250, 250)

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(10)
    unit.goto(randint(-230, 230), randint(-230, 230))


for i in range(steps_of_time_number):
    for unit in pool:
        if unit.xcor() >=250:
            unit.left(unit.heading()+180)
            unit.forward(20)
        if unit.xcor() <= -250:
            unit.right(unit.heading() + 180)
            unit.forward(20)
        if unit.ycor() >= 250:
            unit.left(unit.heading() + 180)
            unit.forward(20)
        if unit.ycor() <= -250:
            unit.left(unit.heading() - 180)
            unit.forward(20)
        unit.forward(10)
        unit.left(randint(-180, 180))