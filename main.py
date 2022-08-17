# Import the pygame module
import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_a,
    K_d, 
)

# Define constants for the screen width and height
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 667

velocity = 12

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
y = SCREEN_HEIGHT/2

# Variable to keep the main loop running
running = True

# Main loop
while running:
    screen.blit(bg, (0, 0))
    screen.blit(sprite, (x, y))

    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
            if event.key == pygame.K_a:
                x-=velocity
            if event.key == pygame.K_d:
                x+=velocity
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False


    

    # Draw the player on the screen


    # Update the display
    pygame.display.update()

