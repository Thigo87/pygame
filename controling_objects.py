import pygame
from pygame.locals import *
from sys import exit


pygame.init()

screen_size = (640, 480)
object_size = (40, 60)

screen = pygame.display.set_mode(screen_size)

#Centralizing the object
x = (screen_size[0]/2) - (object_size[0]/2)
y = (screen_size[1]/2) - (object_size[1]/2)

pygame.display.set_caption("Game")

clock = pygame.time.Clock()

while True:
    screen.fill((0, 0, 0))
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        ''' if event.type == KEYDOWN: #pressing the key event
            if event.key == K_a:
                x -= 30
            elif event.key == K_d:
                x += 30
            elif event.key == K_w:
                y -= 30
            elif event.key == K_s:
                y += 30'''
    
    #Continuous pressing
    if pygame.key.get_pressed()[K_a]:
        x -= 10
    elif pygame.key.get_pressed()[K_d]:
        x += 10
    elif pygame.key.get_pressed()[K_w]:
        y -= 10
    elif pygame.key.get_pressed()[K_s]:
        y += 10
    
    pygame.draw.rect(screen, (0, 255, 0), (x, y, object_size[0], object_size[1]))
    
    if (x == screen_size[0] or x == 0) or (y == screen_size[1] or y == 0):
        x = (screen_size[0]/2) - (object_size[0]/2)
        y = (screen_size[1]/2) - (object_size[1]/2)
        
    
    pygame.display.update()
    