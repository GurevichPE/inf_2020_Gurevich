from random import random
from random import randint
import turtle

turtle.shape('turtle')
for i in range (100):
    a = int(360*random())
    l = randint(20, 80)
    turtle.forward(l)
    turtle.left(a)