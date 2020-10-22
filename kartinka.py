import pygame
from pygame.draw import *

pygame.init()

FPS = 30
sc = pygame.display.set_mode((800, 800))
pi = 3.1415
black = (0, 0, 0)
grey = (231, 231, 231)
gr_hat = (228, 223, 220)
gr_cat = (220, 220, 220)
white = (255, 255, 255)
br0 = (173, 158, 148)
br1 = (146, 125, 112)
br2 = (108, 93, 82)
fish = (148, 173, 168)

rect(sc, (grey), (0, 0, 800, 400))
rect(sc, (white), (0, 300, 800, 700))

def draw_chukcha(scr, x, y, width, orientation):
    '''
    :param scr: объект pygame.Surface
    :param x: координата х левого верхнего угла
    :param y: координата у левого верхнего угла
    :param width: ширина изображения
    :param height:высота изображения
    :param orientation: "левый" = 0 и "правый" = 1 чукча
    :return: рисунок Чукчи
    '''
    height = (width*8)//5
    surf = pygame.Surface((width*11//10, height))
    surf.fill(white)
    surf.set_colorkey(white)
    #right hand
    sur = pygame.Surface((width * 7 // 20, height // 16))
    rect(sur, white, (0, 0, width * 7 // 20, height // 16))
    ellipse(sur, br1, (0, 0, width * 7 // 20, height // 16))
    sur_rot = pygame.transform.rotate(sur, -45)
    surf.blit(sur_rot, (width * 4 // 5, height * 5 // 16))
    #left hand
    ellipse(surf, br1, ((0, height * 9 // 32, width * 7 // 20, height // 16)))
    line(surf, black, ( width // 20, 0), ( width // 20, height * 11 // 16))

    ellipse(surf, gr_hat, (( width // 5, 0), (width * 7 // 10, height * 5 // 16))) # капюшон
    #body
    ellipse(surf, br1, ((width * 3 // 20, height * 3 // 16), (width * 4 // 5, height * 13 // 16)))
    rect(surf, white, (( width * 3 // 20, height * 19 // 32), (width * 4 // 5, height * 13 // 32)))
    rect(surf, br2, (( width * 2 // 5,  height // 4, width // 5, height * 6 // 18)))
    #legs
    ellipse(surf, br1, (width*3//10, height*19//32, width*3//20, height//8))
    ellipse(surf, br1, (width * 13 // 20, height * 19 // 32, width *3 // 20, height // 8))
    rect(surf, br2, (width * 3 // 20, height * 19 // 32, width * 4 // 5, height // 24))
    ellipse(surf, br1, (width//5, height*11//16, width*5//20, height//16))
    ellipse(surf, br1, (width * 13 // 20, height * 11 // 16, width * 5 // 20, height // 16))
    # head
    ellipse(surf, br0, (width*3//10, height//16, width//2, height*3//16))
    ellipse(surf, grey, (width*2//5, height//8, width*3//10, height*3//32))
    line(surf, black, (width*9//20, height*5//32), (width//2, height*11//64), 1)
    line(surf, black, (width*3//5, height*11//64), (width*13//20, height*5//32), 1)
    arc(surf, black, (width//2, height*3//16, width//10, height//32), pi/6, pi, 1)

    if orientation == 1:
        surf = pygame.transform.flip(surf, True, False)
    scr.blit(surf, (x, y))

def draw_chum(scr, x, y, width):
    height = (width * 9) // 10
    surf = pygame.Surface((width * 11 // 10, height))
    surf.fill(white)
    surf.set_colorkey(white)
    ellipse(surf, grey, (0, 0, width, height))
    ellipse(surf, black, (0, 0, width, height), 4)
    rect(surf, (255, 255, 254), (0, height//2, width, height//2))
    line(surf, black, (0, height//2), (width, height//2))
    line(surf, black, (width//20, height // 3), (width*19//20, height // 3))
    line(surf, black, (width * 3 // 20, height // 6), (width * 17 // 20, height // 6))
    line(surf, black, (width * 3 // 10, height // 18), (width * 7 // 10, height // 18))
    for i in range(5):
        line(surf, black, (width//10 + i*width//5, height//2), (width//10 + i*width//5, height//3))
        if i != 0 and i != 4:
            line(surf, black,
                 (width // 10 + i * width // 5, height // 6), (width // 10 + i * width // 5, height // 18)
                 )
    for i in range(4):
        line(surf, black, (width // 5 + i * width // 5, height // 3), (width // 5 + i * width // 5, height // 6))
        if i == 2:
            line(surf, black, (width // 5 + i * width // 5, height // 18), (width // 2, 0))
        if i == 1:
            line(surf, black, (width // 5 + i * width // 5, height // 18), (width // 2, 0))

    scr.blit(surf, (x, y))

def draw_cat(scr, x, y, width):
    height = width*3//8
    surf = pygame.Surface((width, height))
    surf.fill(white)
    #legs
    sur = pygame.Surface((width//4, height//6))
    sur.fill(white)
    surf.set_colorkey(white)
    sur.set_colorkey(white)
    ellipse(sur, gr_cat, (0, 0, width//4, height//8))
    leg1 = pygame.transform.rotate(sur, 5)
    leg2 = pygame.transform.rotate(sur, 15)
    leg3 = pygame.transform.rotate(sur, 145)
    leg4 = pygame.transform.rotate(sur, 150)
    surf.blit(leg1, (0, height*5//10))
    surf.blit(leg2, (width//20, height * 4//7))
    surf.blit(leg3, (width*17//48, height * 5 // 10))
    surf.blit(leg4, (width * 17 // 36, height * 5 // 10))
    #ears
    polygon(surf, gr_cat, ((width * 7 // 40 + width // 8, height * 5 // 27),
                           (width * 7 // 40 + width // 8, height // 3), (width // 4, height // 4)))
    polygon(surf, gr_cat, ((width * 7 // 40 + width // 13, height * 5 // 29),
                           (width * 7 // 40 + width // 13, height // 3), (width * 9 // 42, height // 4)))
    #body
    ellipse(surf, gr_cat, (width * 5 // 32, height * 5 // 12, width * 7 // 16, height // 3))
    # fish
    fx = width * 3 // 16
    fy = height * 3 // 10
    fsur = pygame.Surface((fx, fy))
    fsur.fill(white)
    fsur.set_colorkey(white)
    polygon(fsur, (220, 95, 95), ((fx * 2 // 7, fy // 3), (fx * 2 // 5, fy // 6), (fx * 2 // 5, fy // 2)))
    polygon(fsur, (220, 95, 95), ((fx * 2 // 7, fy * 2 // 3), (fx * 1 // 2, fy * 5 // 6), (fx * 2 // 5, fy // 2)))

    ellipse(fsur, fish, (0, fy // 3, width // 8, height // 10))
    ellipse(fsur, (135, 170, 155), (0, fy // 3, width // 8, height // 10), 1)
    circle(fsur, (0, 1, 209), (fx // 8, fy // 2), fy // 10)
    polygon(fsur, fish, ((width // 8, fy // 2), (fx * 9 // 10, fy // 3), (fx * 9 // 10, fy * 2 // 3)))
    polygon(fsur, (135, 170, 155), ((width // 8, fy // 2), (fx * 9 // 10, fy // 3), (fx * 9 // 10, fy * 2 // 3)), 1)

    fsur = pygame.transform.rotate(fsur, -25)
    surf.blit(fsur, (width // 9, height // 4))
    #head
    ellipse(surf, gr_cat, (width*7//40, height*4//18, width//7, height*2//7))
    ellipse(surf, white, (width*3//15, height*3//11, width//30, height//15))
    ellipse(surf, white, (width * 3 // 15, height * 3 // 11, width // 30, height * 2 // 45))
    circle(surf, black, (width*3//15 + width*3//120, height*3//11 + height//36), height//45)
    ellipse(surf, white, (width * 97 // 400, height * 3 // 10, width // 30, height * 3 // 45))
    circle(surf, black, (width*97//400 + width*3//120, height*3//10 + height//36), height//45)

    polygon(surf, black, ((width * 7 // 40 + width // 25, height * 110 // 300),
                           (width * 7 // 40 + width // 18, height * 110// 300), (width * 9 // 41, height * 120 // 300)))

    #tail
    tsur = pygame.Surface((width*3//8, height//6))
    tsur.fill(white)
    tsur.set_colorkey(white)
    ellipse(tsur, gr_cat, (0, 0, width*3//8, height//6))
    tsur = pygame.transform.rotate(tsur, 35)
    surf.blit(tsur, (width*13//26, 0))
    scr.blit(surf, (x, y))



draw_chum(sc, 20, 280, 120)
draw_chum(sc, 350, 320, 120)
draw_chum(sc, 50, 260, 320)
draw_chum(sc, 40, 380, 160)
draw_chum(sc, 150, 430, 160)
draw_chukcha(sc, 450, 350, 60, 1)
draw_chukcha(sc, 550, 280, 50, 0)
draw_chukcha(sc, 560, 300, 60, 1)
draw_chukcha(sc, 700, 310, 60, 0)
draw_chukcha(sc, 650, 400, 60, 0)
draw_chukcha(sc, 570, 380, 60, 1)
draw_chukcha(sc, 450, 440, 60, 1)
draw_chukcha(sc, 550, 450, 160, 0)

draw_cat(sc, -100, 500, 240)
draw_cat(sc, 160, 490, 240)
draw_cat(sc, 50, 560, 240)
draw_cat(sc, 290, 600, 240)
draw_cat(sc, 580, 620, 240)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
