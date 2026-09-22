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
    pygame.draw.rect(screen, (0, 255, 0), (200, 300, 50, 70)) #drawing a rectangle, (where will be displayed, color(RGB), position(initial_x, initial_y, width, height))
    pygame.draw.circle(screen, (0, 0, 255), (300, 450), 25) #drawing a circle (where will be displayed, color(RGB), center(x, y), radius)
    pygame.draw.line(screen, (255, 255, 0), (150, 0), (150, 600), 5) #drawing a line (where will be displayed, color(RGB), (Xa, Ya), (Xb, Yb), width)
    
    pygame.display.update()