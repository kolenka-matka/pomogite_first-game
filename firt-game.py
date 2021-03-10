import pygame
import random


class Ball:
    def __init__(self, pos):
        self.pos = list(pos)
        self.radius = random.randrange(15, 45)
        self.color = (random.randrange(200, 255), random.randrange(30, 255), random.randrange(50, 255))
        self.right = True
        self.stop = False
        self.dir = list(randome.choices(-4,5))
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

    def horizontal_move(self):
        if not self.stop:
            if self.pos[0] == 550:
                self.right = False
            if self.pos[0] == 50:
                self.right = True
            if self.right:
                self.pos[0] += 1
            else:
                self.pos[0] -= 1

    def ball_intersection(self, other):
        if ((self.pos[0] - other[0])**2 + (self.pos[1] - other[1])**2) < (2 * self.radius)**2:
            return True # пересекаются
        else:
            return False
        # разница меньше радиуса - пересекаются

    def redraw(self):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)


pygame.init()

screen = pygame.display.set_mode((600, 300))  # создаем экран размером (600, 300) и называем его screen
screen.fill((112, 146, 190))  # мы заливаем его цветом который в системе RGB записывается как (112, 146, 190)
x, y = 100, 100
running = True
right = True
circle_color = (236, 176, 199)
screen_color = (227, 218, 204)
clock = pygame.time.Clock()
stop = False  # для кликов мышкой
spisok = []
FPS = random.randrange(200, 500)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # это буквально означает "если пользователь нажал на крестик"
            running = False  # в этом случае переменная running становится false и соответственно игра заканчивается
        kol_balls = 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                koor = event.pos  # координаты точки где мы тыкнули левой кнопкой мыши
                ball = Ball(koor)
                spisok.append(ball)
            elif event.button == 3:
                stop = True
                del spisok[0]
    clock.tick(FPS)  # это нужно для того чтобы у тебя смена кадров происходила с какой-то скоростью fps
    for el in spisok:
        ball.horizontal_move()
        ball.redraw()

    koor = event.pos
    ball = Ball(koor)
    i = 0
    while i != (len(spisok) - 2):
        i += 1
        if ball.ball_intersection(spisok[i], spisok[i + 1]):
                del spisok[i]
                del spisok[i + 1]
    pygame.display.flip()  # это смена кадров
    screen.fill((235, 229, 221))
    clock.tick(FPS)

pygame.quit()  # переменная отвечающая за время
