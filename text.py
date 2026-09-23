import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

screen_size = (640, 480)
object_size = (40, 60)

screen = pygame.display.set_mode(screen_size)

x = (screen_size[0]/2) - (object_size[0]/2)
y = (screen_size[1]/2) - (object_size[1]/2)

blue_x = randint(40, 600)
blue_y = randint(50, 430)

font = pygame.font.SysFont('colonna', 40, True, True) #setting the font

pygame.display.set_caption("Game")

clock = pygame.time.Clock()

points = 0

while True:
    screen.fill((0, 0, 0))
    clock.tick(60)
    
    msg = f"Points: {points}" #text
    
    formatted_text = font.render(msg, True, (255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    if pygame.key.get_pressed()[K_a]:
        x -= 10
    elif pygame.key.get_pressed()[K_d]:
        x += 10
    elif pygame.key.get_pressed()[K_w]:
        y -= 10
    elif pygame.key.get_pressed()[K_s]:
        y += 10
    
    green_rect = pygame.draw.rect(screen, (0, 255, 0), (x, y, object_size[0], object_size[1]))
    blue_rect = pygame.draw.rect(screen, (0, 0, 255), (blue_x, blue_y, object_size[0], object_size[1]))
    
    if (x == screen_size[0] or x == 0) or (y == screen_size[1] or y == 0):
        x = (screen_size[0]/2) - (object_size[0]/2)
        y = (screen_size[1]/2) - (object_size[1]/2)
        points -= 1
    
    if green_rect.colliderect(blue_rect):
        blue_x = randint(40, 600)
        blue_y = randint(50, 430)
        points += 1
        
    screen.blit(formatted_text, (450, 40))    
    pygame.display.update()