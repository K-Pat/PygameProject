# Import the pygame module
import pygame
import random
import threading
import os
import time

clock = pygame.time.Clock()

pygame.init()

pygame.display.set_caption("Roaming In Space")

pos = pygame.mouse.get_pos()

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
    largeText = pygame.font.Font('ARIALUNI.TTF',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

# Define constants for the screen width and height

def score_display(text):
    smallText = pygame.font.Font('ARIALUNI.TTF',20)
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

def start_menu(Display):
    running = True
    screen.fill((0,0,0))
    largeText = pygame.font.Font('ARIALUNI.TTF',100)
    smallText = pygame.font.Font('ARIALUNI.TTF',25)
    TextSurf, TextRect = text_objects(Display, largeText)
    TextRect.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    screen.blit(TextSurf, TextRect)
    button_no = pygame.Surface((150,50))
    button_no.fill((0,255,0))
    button_yes = pygame.Surface((150,50))
    button_yes.fill((255,0,0))
    
    TextSurf_button1, TextRect_button1 = text_objects('"A"', smallText)
    TextRect_button1.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    TextRect_button1.center = ((SCREEN_HEIGHT/4+75,SCREEN_WIDTH/4+175+25))


    TextSurf_button2, TextRect_button2 = text_objects('"ESC"', smallText)
    TextRect_button2.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    TextRect_button2.center = ((650+75,SCREEN_WIDTH/4+175+25))
    button_yes.fill((255,0,0))
    button_no.fill((0,255,0))

    button_yes_collide = pygame.Rect((SCREEN_HEIGHT/4,SCREEN_WIDTH/4+175), (150,50))
    pygame.draw.rect(screen, (0,200,0), (SCREEN_HEIGHT/4,SCREEN_WIDTH/4+175, 150, 50))
    pygame.draw.rect(screen, (200,0,0), ((650),((SCREEN_WIDTH/4)+175), 150, 50))

    while running:
        #screen.blit(button_no, (SCREEN_HEIGHT/4,SCREEN_WIDTH/4+175))
        #screen.blit(button_yes, (((650),((SCREEN_WIDTH/4)+175))))
        screen.blit(TextSurf_button1, TextRect_button1)
        screen.blit(TextSurf_button2, TextRect_button2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_a:
                    pygame.draw.rect(screen, (0,255,0), (SCREEN_HEIGHT/4,SCREEN_WIDTH/4+175, 150, 50))
                if event.key == K_ESCAPE:
                    pygame.draw.rect(screen, (255,0,0), ((650),((SCREEN_WIDTH/4)+175), 150, 50))
            if event.type == pygame.KEYUP:
                if event.key == K_a:
                    pygame.draw.rect(screen, (0,200,0), (SCREEN_HEIGHT/4,SCREEN_WIDTH/4+175, 150, 50))
                    game_loop(True)
                if event.key==K_ESCAPE:
                    pygame.quit()
                    quit()
        pygame.display.update()
        clock.tick(15)


def score_dodged(count):
    font = pygame.font.SysFont("ARIALUNI.TTF", 25)
    s = "Dodged: " + str(count)
    x = font.render(s, True, (255,255,255))
    smallText = pygame.font.Font('ARIALUNI.TTF',20)
    TextSurf, TextRect = text_objects(x, smallText)
    TextRect.center = ((15,15))
    screen.blit(TextSurf, TextRect)

def game_loop(running):
    velocity = 12


    RANDOM_X = random.randint(20, 980)
    x_change = 0
    meteor_change = 0
    m = 0
    c = 0
    meteor_width = random.randint(80,350)
    meteor_height = random.randint(30,75)
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 667
    bg = pygame.image.load("space.jpeg").convert_alpha()

    sprite = pygame.image.load("rocket.jpeg").convert_alpha()
    sprite = pygame.transform.scale(sprite, (50, 50))

    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT-100

    score = 0
    dodged = 0
    while running:
        #score_dodged(dodged)
        meteor = pygame.Surface((meteor_width,meteor_height))
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
            meteor_height = random.randint(30,75)
            dodged+=1


        if y < 50+m:
            if x > RANDOM_X and x < RANDOM_X+meteor_width or x+50 > RANDOM_X and x + 50 < RANDOM_X+meteor_width:
                m =0 
                x = 0
                #time.sleep(0.5)
                message_display("Crash")
                time.sleep(1)
                score = 0
                RANDOM_X = random.randint(20,700)
                meteor_width = random.randint(80, 350)
                start_menu("Play Again?")
                meteor_height = random.randint(30,75)
                

        pygame.display.update()
        score+=1
        print(pos)
        clock.tick(75)

start_menu("Roaming In Space")
