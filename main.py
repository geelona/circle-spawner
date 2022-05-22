import sys
import pygame
from random import randint

pygame.init()
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h

win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

sand_l = []
sand_c = 500


class Sand:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sand_add(self):
        if pygame.mouse.get_pressed()[0] and\
                len(sand_l) <= sand_c:
            sand_l.append([self.x, self.y])
        if len(sand_l) >= sand_c:
            sand_l.pop(0)


def draw():
    sand_fall()
    win.fill((0, 0, 0))
    for el in sand_l:
        pygame.draw.circle(win, (255, 255, randint(1, 255)), (el[0], el[1]), 20)
    pygame.display.update()


def sand_fall():
    mx, my = pygame.mouse.get_pos()
    sand = Sand(mx, my)
    sand.sand_add()
    for j in sand_l:
        if j[1] <= HEIGHT - 1:
            j[1] += randint(1, 10)


def main():
    clock = pygame.time.Clock()
    while 1:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()
        draw()
        clock.tick(120)


if __name__ == "__main__":
    main()
