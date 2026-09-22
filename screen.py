import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen_size = (640, 480)

screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("Game")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()