import turtle as t
import math

t.shape('turtle')
def num(ind):
    x0 = 0
    y = 0
    d = 30
    for i in range(len(ind)):
        for j in range(len(ind[i])):
            if j == 1:
                t.pendown()
            x, y = ind[i][j]
            x += x0
            t.goto(x, y)
        t.penup()
        x0 += d
        t.goto(x0, 0)

zer = [(0, 0), (0, -40), (20, -40), (20, 0), (0, 0)]
one = [(0, -20), (20, 0), (20, -40), (20, 0)]
fou = [(0, 0), (0, -20), (20, -20), (20, -40), (20, 0)]
sev = [(0, 0), (20, 0), (0, -20), (0, -40)]
t.penup()
ind = [one, fou, one, sev, zer, zer]
num(ind)
t.done()