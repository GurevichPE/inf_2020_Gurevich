# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
from  math import sqrt

WIDTH = 800
HEIGHT = 650
FPS = 30
time = 0
score = 0

# Задаем цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

name = input('Enter user`s name')

font_name = pygame.font.match_font('arial')


def table_top(i):
    return int(i[1])

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def record_table(name, score):
    f = open('records.txt', 'a')
    f.write(name + ' ' + str(score) + '\n')
    f.close()

def sort_table():
    f = open('records.txt', 'r')
    results = []
    while True:
        res = f.readline()
        if res == '':
            break
        results.append(res)

    for i in range(len(results)):
        results[i] = results[i].split()

    f.close()
    fw = open('records.txt', 'w')
    results.sort(key=table_top, reverse=True)
    for i in range(len(results)):
        fw.write(str(results[i][0]) + " " + str(results[i][1]) + "\n")
    fw.close()

class Ball(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        a = random.randint(30, 100)
        self.image = pygame.Surface((a, a))
        self.image.set_colorkey(BLACK)
        self.rad = a//2
        color = COLORS[random.randint(0, 5)]
        self.circle = pygame.draw.circle(self.image, color, (a//2, a//2), a//2)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(100, 700), random.randint(100, 500))
        self.speedx = random.randint(5, 10)
        self.speedy = random.randint(-10, 10)

    def update(self):

        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > WIDTH:
            self.speedx = random.randint(-10, 1)
        if self.rect.left < 0:
            self.speedx = random.randint(1, 10)
        if self.rect.bottom > HEIGHT:
            self.speedy = random.randint(-10, -1)
        if self.rect.top < 0:
            self.speedy = random.randint(1, 10)

class Square(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        a = random.randint(20, 80)
        self.width = a
        self.image = pygame.Surface((a, a))
        self.image.set_colorkey(BLACK)
        color = COLORS[random.randint(0, 5)]
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(100, 700), random.randint(100, 500))
        self.speedx = random.randint(5, 15)
        self.speedy = random.randint(-15, 15)

    def update(self):

        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > WIDTH:
            self.speedx = random.randint(-15, 1)
        if self.rect.left < 0:
            self.speedx = random.randint(1, 15)
        if self.rect.bottom > HEIGHT:
            self.speedy = random.randint(-15, -1)
        if self.rect.top < 0:
            self.speedy = random.randint(1, 15)



# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()
balls = pygame.sprite.Group()
squares = pygame.sprite.Group()
ball = Ball()
balls.add(ball)
all_sprites.add(ball)


# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    if time > 600:
        running = False
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for sprite in balls:
                if sqrt((sprite.rect.center[0] - pos[0])**2 + (pos[1] - sprite.rect.center[1])**2) < sprite.rad:
                    sprite.kill()
                    score += 1

            for sprite in squares:
                if sprite.rect.right > pos[0] > sprite.rect.x and sprite.rect.bottom > pos[1] > sprite.rect.y:
                    sprite.kill()
                    score += 2
    if running == False:
        record_table(name, score)
        sort_table()


    # Обновление
    time += 1
    if time%40 == 0:
        ball = Ball()
        balls.add(ball)
        all_sprites.add(ball)
    elif time%50 == 0:
        sq = Square()
        squares.add(sq)
        all_sprites.add(sq)
    all_sprites.update()


    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, WIDTH // 2, 10)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()