import pygame

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
            running = False
    
    screen.fill((255,255,255))#fill screen with color (RGB values)

    pygame.draw.circle(screen, #screen name
    (0,0,255), #rgb color
    (250,250), #center coordinate for circle
    75)#radius

    #update the display
    pygame.display.flip()

pygame.quit()
