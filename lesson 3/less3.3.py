import turtle as t
import math
import time

x = -300
y = 0
a = 9.8
fi = 3*math.pi/7
V0 = 70
Vx = V0*math.cos(fi)
Vy = V0*math.sin(fi)
dt = 0.005
t.speed(150)
t.goto(300, 0)
while V0 > 0.01:
    t.goto(x, y)
    x += Vx*dt
    y += Vy*dt - (a*dt**2)/2
    Vy += -a*dt
    if y <= 0:
        V0 = V0/1.4
        Vy = V0 * math.sin(fi)
        Vx = V0 * math.cos(fi)