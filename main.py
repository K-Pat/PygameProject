# Import the pygame module
import pygame
import random
import threading
import os
import time

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

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 667

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

# Define constants for the screen width and height

def score_display(text):
    smallText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, smallText)
    TextRect.center = ((950),(20))
    screen.blit(TextSurf, TextRect)

def crash():
    m =0 
    x = 0
    time.sleep(0.5)
    message_display("Crash")

running = True

RANDOM_X = random.randint(20, 980)
def game_loop(running):
    velocity = 12


    RANDOM_X = random.randint(20, 980)
    x_change = 0
    meteor_change = 0
    m = 0
    c = 0
    meteor_width = random.randint(80,350)
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 667
    bg = pygame.image.load("space.jpeg")

    sprite = pygame.image.load("rocket.jpeg")
    sprite = pygame.transform.scale(sprite, (50, 50))

    
    # Initialize pygame
    pygame.init()

    pygame.display.set_caption("Han Solo")

    # Create the screen object
    # The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT

    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT-100

    # Variable to keep the main loop running


    # Main loop
    score = 0
    while running:
        meteor = pygame.Surface((meteor_width,50))
        meteor.fill((110, 38, 14))
        screen.blit(bg, (0, 0))
        screen.blit(sprite, (x, y))
        screen.blit(meteor, (RANDOM_X, m))
        scoreString = str(score)
        score_display(scoreString)
        

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
            meteor_change = 10
        else:
            meteor_change = 0 
        
        if c == 97:
            c = 0
        
        m+=meteor_change
        c+=1

        if m>SCREEN_HEIGHT:
            m = 0-50
            RANDOM_X = random.randint(20, 700)
            meteor_width = random.randint(80,350)

        if y < 50+m:
            if x > RANDOM_X and x < RANDOM_X+meteor_width or x+50 > RANDOM_X and x + 50 < RANDOM_X+meteor_width:
                m =0 
                x = 0
                time.sleep(0.5)
                message_display("Crash")
                time.sleep(1)
                score = 0
                RANDOM_X = random.randint(20,700)
                meteor_width = random.randint(80, 350)

        pygame.display.update()
        score+=1
        clock.tick(60)

game_loop(running)