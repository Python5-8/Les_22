import pygame as pg
from random import randint

pg.init()

# Создаем класс окружности
class Circle:

    # Определяем конструктор
    def __init__(self, x, y, rad, color):
        self.x = x
        self.y = y
        self.x_speed = 3
        self.rad = rad
        self.color = color

    # Метод отрисовки
    def draw(self, win):
        pg.draw.circle(win, self.color, (self.x, self.y), self.rad)

    # Метод автоматического движения
    def move(self):
        # Реализовать движение по горизонтали
        pass

    # Метод для изменения направления движения при соударении со стенкой
    def change_of_dir(self, w_sc):
        # Реализовать проверку
        pass


h_sc = 500
w_sc = 500

FPS = 120
# Создаем окно
win = pg.display.set_mode((w_sc, h_sc))
clock = pg.time.Clock()

# Нужно создать ОБЪЕКТ окружности

# Главный цикл программы
while True:
    # Проверка на нажатие крестика
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
            
    win.fill((255, 255, 255))

    # Отрисовываем созданый объект
    # Двигаем объект
    # Проверяем соударение со стенкой

    pg.display.update()
    clock.tick(FPS)