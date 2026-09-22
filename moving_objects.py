import pygame
from pygame.locals import *
from sys import exit


pygame.init()

screen_size = (640, 480)

screen = pygame.display.set_mode(screen_size)

x = (screen_size[0]/2) - 20 #initial x
y = 0 #initial y

pygame.display.set_caption("Game")

clock = pygame.time.Clock() #setting the clock

while True:
    screen.fill((0, 0, 0)) #cleaning the screen
    clock.tick(60) #framerate
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    pygame.draw.rect(screen, (0, 255, 0), (x, y, 40, 60)) #variable position
    
    if y == screen_size[1]: #moving and returning to the initial point
        y = 0
    else:
        y += 1
    
    pygame.display.update()
    