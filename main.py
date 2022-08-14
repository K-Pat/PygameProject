import pygame

#Define keys for user input
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,

)

#initialize pygame
pygame.init()

#creating the screen (500 pixels X 500 pixels)
screen = pygame.display.set_mode([500,500])

#create game loop condition
running = True
while running: 

    #check to see if exit condition is met
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#if user trys to exit
            running = True
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running == False 
        elif event.type == QUIT:
            running = False
        
    
    screen.fill((0,0,0))#fill screen with color (RGB values)

    #update the display
    pygame.display.flip()

pygame.quit()
