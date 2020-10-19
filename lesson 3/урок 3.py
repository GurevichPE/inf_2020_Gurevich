f = open("test.txt", 'r')
lines = f.readlines()
import turtle as t

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

for i in range(len(lines)):
    lines[i] = lines[i].rstrip()
    lines[i] = lines[i].split()
    for j in range(len(lines[i])):
        lines[i][j] = int(lines[i][j])
       # lines[i][j+2] = int(lines[i][j+2])
        #lines[i][j+1] = (lines[i][j+1], lines[i][j+2])
    for k in range(1, len(lines[i])-(len(lines[i])-1)//2):
        lines[i][k] = (lines[i][k], lines[i][k+1])
        lines[i].pop(k+1)

index = [1, 1, 4, 7, 1, 0, 0]
for i in range(len(index)):
    for j in range(len(lines)):
        if lines[j][0] == index[i]:
            index[i] = lines[j][1:]

t.penup()
num(index)


