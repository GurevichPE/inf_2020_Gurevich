import turtle
import math

turtle.shape('turtle')
def num(nmb):
    if nmb == 'zer':
        nmb = zer
        turtle.pendown()
        for i in range(len(nmb)):
            a, l = nmb[i]
            turtle.left(a)
            turtle.forward(l)
        turtle.penup()
        turtle.forward(60)
    elif nmb == 'one':
        nmb = one
        turtle.left(270)
        turtle.forward(30)
        turtle.pendown()
        for i in range (len(nmb)):
            a, l = nmb[i]
            turtle.left(a)
            turtle.forward(l)
        turtle.penup()
        turtle.backward(60)
        turtle.left(90)
        turtle.forward(30)
    elif nmb == 'two':
        nmb = two
        turtle.pendown()
        for i in range(len(nmb)):
            a, l = nmb[i]
            turtle.left(a)
            turtle.forward(l)
        turtle.penup()
        turtle.forward(30)
        turtle.left(90)
        turtle.forward(60)
        turtle.right(90)
    elif nmb == 'fou':
        nmb = fou
        turtle.pendown()
        for i in range(len(nmb)):
            a, l = nmb[i]
            turtle.left(a)
            turtle.forward(l)
        turtle.penup()
        turtle.right(90)
        turtle.forward(30)
    elif nmb == 'sev':
        nmb = sev
        turtle.pendown()
        for i in range(len(nmb)):
            a, l = nmb[i]
            turtle.left(a)
            turtle.forward(l)
        turtle.penup()
        turtle.backward(60)
        turtle.left(90)
        turtle.forward(60)

zer = [(270, 60), (90, 30), (90, 60), (90, 30), (180, 0)]
one = [(135, math.sqrt(1800)), (225, 60)]
two = [(0, 30), (270, 30), (315, math.sqrt(1800)), (135, 30)]
thr = [(0, 30), (315, math.sqrt(1800)), (135, 30), (315, math.sqrt(1800))]
fou = [(270, 30), (90, 30), (270, 30), (180, 60)]
sev = [(0, 30), (225, math.sqrt(1800)), (45, 30)]

turtle.penup()
ind = input().split()
for elem in ind:
    num(elem)
# for our task you should enter 'one fou one sev zer zer'