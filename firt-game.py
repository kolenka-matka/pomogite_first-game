import pygame



class Ball():
    def _init_(self, pos, color):
        self.pos = pos
        self.color = color
        self.right = True
        self.stop = False
        pygame.draw.circle(screen, self.color, self.pos, 50)

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
        pygame.draw.circle(screen, self.color, self.pos, 50)

pygame.init()

screen = pygame.display.set_mode((600, 300))  # создаем экран размером (600, 300) и называем его screen
screen.fill((112, 146, 190))  # мы заливаем его цветом который в системе RGB записывается как (112, 146, 190)
x, y = 100, 100
running = True
right = True
circle_color = (236, 176, 199)
screen_color = (112, 146, 190)
clock = pygame.time.Clock()
FPS = 500
stop = False # для кликов мышкой

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # это буквально означает "если пользователь нажал на крестик"
            running = False  # в этом случае переменная running становится false и соответственно игра заканчивается
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                stop = True
            else:
                stop = False
    if not stop:
        if x == 550:
            right = False
        if x == 50:
            right = True
        if right:
            x += 1
        else:
            x -= 1
    clock.tick(FPS)  # это нужно для того чтобы у тебя смена кадров происходила с какой-то скоростью fps
    pygame.draw.circle(screen, circle_color, (x, y),
                       50)  # (поверхность, на которой размещается фигура, цвет круга, (центр окружности), радиус)
    pygame.display.flip()  # это смена кадров
    screen.fill((112, 146, 190))
    clock.tick(FPS)

pygame.quit()  # переменная отвечающая за время
