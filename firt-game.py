import pygame
import random


class Ball:
    def __init__(self, pos):
        self.pos = list(pos)
        self.radius = random.randrange(15, 45)
        self.color = (random.randrange(200, 255), random.randrange(30, 255), random.randrange(50, 255))
        self.right = True
        self.stop = False
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
            else:
                stop = False
    clock.tick(FPS)  # это нужно для того чтобы у тебя смена кадров происходила с какой-то скоростью fps
    for ball in spisok:
        ball.horizontal_move()
        ball.redraw()

    pygame.display.flip()  # это смена кадров
    screen.fill((235, 229, 221))
    clock.tick(FPS)

pygame.quit()  # переменная отвечающая за время
