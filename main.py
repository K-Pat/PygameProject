# Import the pygame module
import pygame
import random
import threading
import os

clock = pygame.time.Clock()

# Import pygame.locals for easier access to key coordinates
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    KEYUP,
    QUIT,
    K_a,
    K_d, 
)

# Define constants for the screen width and height
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 667

RANDOM_X = random.randint(20, 980)

velocity = 12

meteor = pygame.Surface((50,50))
meteor.fill((110, 38, 14))
bg = pygame.image.load("space.jpeg")

sprite = pygame.image.load("rocket.jpeg")
sprite = pygame.transform.scale(sprite, (50, 50))

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
 
# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

x = SCREEN_WIDTH/2
y = SCREEN_HEIGHT-100

# Variable to keep the main loop running
running = True

# Main loop

x_change = 0
meteor_change = 0
m = 0
c = 0

def meteor_rain(x):
    while x:
        r = random.randint(20, 980)
        screen.blit(meteor, (r, m))
        if c%97:
            meteor_change = 5
        else:
            meteor_change = 0 
    
        if c == 97:
            c = 0
    
    m+=meteor_change
    c+=1

while running:
    screen.blit(bg, (0, 0))
    screen.blit(sprite, (x, y))
    screen.blit(meteor, (RANDOM_X, m))

    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
            # If the 'a' key is pressed: Move the sprite left:
            if event.key == K_a:
                x_change = -12 
            # If the 'd' key is pressed: Move the sprite left:
            if event.key == K_d:
                x_change = 12
        if event.type == KEYUP:
            if event.key == K_a or event.key == K_d:
                x_change = 0
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False
    
    x+=x_change

    if x<0:
        x=0
    elif x>950:
        x = 950
    
    if c%97:
        meteor_change = 5
    else:
        meteor_change = 0 
    
    if c == 97:
        c = 0
    
    m+=meteor_change
    c+=1
    # Update the display
    pygame.display.update()
    
    clock.tick(40)

