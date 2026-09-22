import pygame
from pygame.locals import *
from sys import exit

pygame.init() #initializing pygame

screen_size = (640, 480) #width and height

screen = pygame.display.set_mode(screen_size) #setting the screen

pygame.display.set_caption("Game") #changing the title of the screen

while True: #main loop
    for event in pygame.event.get(): #getting the events
        if event.type == QUIT: #event to close the screen 
            pygame.quit()
            exit()
    pygame.display.update() #screen update