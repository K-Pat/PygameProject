#IMPORTS
from cgitb import text
import pygame
import random
import threading
import os
import time
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

#initialization
clock = pygame.time.Clock()
#Initialize Pygame
pygame.init()
#Setting a caption for the pygame screen
pygame.display.set_caption("Roaming In Space")
#opening highscores.txt with handle at the first 
highscores = open('highscores.txt', 'a+')

#Variables 
#Screen Width
SCREEN_WIDTH = 1000
#Screen Height
SCREEN_HEIGHT = 667
running = True
#Finds a random digit between 20 and 980 to create the
RANDOM_X = random.randint(20, 980)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Text Functions
def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()
def message_display(text):
    #defining font
    largeText = pygame.font.Font('ARIALUNI.TTF',115)
    #creating text surface using text objects function
    TextSurf, TextRect = text_objects(text, largeText)
    #text center
    TextRect.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    #blit to screen
    screen.blit(TextSurf, TextRect)
    #update 
    pygame.display.update()

#Function to display the score NOT YET IMPLEMENTED
def score_display(text):
    #defining font but smaller
    smallText = pygame.font.Font('ARIALUNI.TTF',20)
    TextSurf, TextRect = text_objects(text, smallText)
    TextRect.center = ((950),(20))
    screen.blit(TextSurf, TextRect)

#High Score Screen
def scores_screen():
    running = True
    screen.fill((0,0,0))
    largeText = pygame.font.Font('ARIALUNI.TTF',100)
    smallText = pygame.font.Font('ARIALUNI.TTF',25)
    TextSurf,TextRect = text_objects("High Score", largeText)
    TextRect.center = ((10,10))
    screen.blit(TextSurf, TextRect)

#Start Menu Screen
def start_menu(Display):
    running = True
    screen.fill((0,0,0))
    largeText = pygame.font.Font('ARIALUNI.TTF',100)
    smallText = pygame.font.Font('ARIALUNI.TTF',25)
    TextSurf, TextRect = text_objects(Display, largeText)
    TextRect.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    screen.blit(TextSurf, TextRect)

    #Creating two surfaces. One yes button. One no button
    button_no = pygame.Surface((150,50))
    button_no.fill((0,255,0))
    button_yes = pygame.Surface((150,50))
    button_yes.fill((255,0,0))
    
    #Text for the yes button
    TextSurf_button1, TextRect_button1 = text_objects('"A"', smallText)
    TextRect_button1.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    TextRect_button1.center = ((SCREEN_HEIGHT/4+75,SCREEN_WIDTH/4+175+25))

    #text for the no button
    TextSurf_button2, TextRect_button2 = text_objects('"ESC"', smallText)
    TextRect_button2.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    TextRect_button2.center = ((650+75,SCREEN_WIDTH/4+175+25))

    #fill both buttons. One is green, One is red. (RGB values) 
    #UNUSED
    button_yes.fill((255,0,0))
    button_no.fill((0,255,0))

    #Creates hidden hitboxes for the buttons
    button_yes_collide = pygame.Rect((SCREEN_HEIGHT/4,SCREEN_WIDTH/4+175), (150,50))
    button_no_collide =  pygame.Rect((650,((SCREEN_WIDTH/4)+175)), (150, 50))

    #creates visuals for the buttons
    pygame.draw.rect(screen, (0,200,0), (SCREEN_HEIGHT/4,SCREEN_WIDTH/4+175, 150, 50))
    pygame.draw.rect(screen, (200,0,0), ((650),((SCREEN_WIDTH/4)+175), 150, 50))

    while running:
        time.sleep(0.5)
        #constantly updating live position of mouse 
        pos = pygame.mouse.get_pos()
        #screen.blit(button_no, (SCREEN_HEIGHT/4,SCREEN_WIDTH/4+175))
        #screen.blit(button_yes, (((650),((SCREEN_WIDTH/4)+175))))

        #BLIT the text that was defined earlier in the function
        screen.blit(TextSurf_button1, TextRect_button1)
        screen.blit(TextSurf_button2, TextRect_button2)

        #monitoring for events
        for event in pygame.event.get():

            #if event type is a QUIT event then quit the program
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #if event type is someone pressing a key
            if event.type == pygame.KEYDOWN:
                #if it's A then change color of yes button to something more bright to simulate it being clicked
                if event.key == K_a:
                    pygame.draw.rect(screen, (0,255,0), (SCREEN_HEIGHT/4,SCREEN_WIDTH/4+175, 150, 50))
                #same as YES button but instead with the ESC key
                if event.key == K_ESCAPE:
                    pygame.draw.rect(screen, (255,0,0), ((650),((SCREEN_WIDTH/4)+175), 150, 50))
            
            #When someone lifts their finger of a key
            if event.type == pygame.KEYUP:
                #if it's A then go back to normal color and initiate game loop. 
                if event.key == K_a:
                    pygame.draw.rect(screen, (0,200,0), (SCREEN_HEIGHT/4,SCREEN_WIDTH/4+175, 150, 50))
                    game_loop(True)
                #If key ESC is brought back up then initiate quit sequence
                if event.key==K_ESCAPE:
                    pygame.quit()
                    quit()
            
            #if someone clicks a mouse button. 
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if its a left click and the pos of the mouse collides with the invisble RECT for the YES button then engage game loop
                if pygame.mouse.get_pressed()[0] and button_yes_collide.collidepoint(pos):
                    pygame.draw.rect(screen, (0,255,0), (SCREEN_HEIGHT/4,SCREEN_WIDTH/4+175, 150, 50))
                    game_loop(True)
                #if its a left click and the pos of the mouse collides with the invisible RECT for the NO button then enngage quit sequence
                if pygame.mouse.get_pressed()[0] and button_no_collide.collidepoint(pos):
                    pygame.draw.rect(screen, (255,0,0), ((650),((SCREEN_WIDTH/4)+175), 150, 50))
                    pygame.quit()
                    quit()

        #update
        pygame.display.update()
        #lock FPS max at 15
        clock.tick(15)


#Main game loop
def game_loop(running):
    #Velocity of the meteors
    velocity = 12
    #list for the highest scores
    scores = []
    #random X value for the positioning of the meteor
    RANDOM_X = random.randint(20, 980)
    #random X value for the second meteor position on the X plane. 
    RANDOM_X_TWO = random.randint(20,980)
    #Change for the X position of the sprite. ADDED ONTO X which is used to BLIT the sprite
    x_change = 0
    #change for the y position of the meteor. ADDED ONTO M which is then used to BLIT the meteor
    meteor_change = 0
    #The variable used to blit the meteor's Y position on the screen
    m = 0
    #The variable used to blit the second meteor's positon on the Y screen 
    m_TWO = 667
    #used as a dummy value to slow down the movement of the meteor to be seen by the user
    c = 0
    #Random Height for the meteor
    meteor_width = random.randint(80,350)
    #Random width for the meteor
    meteor_height = random.randint(30,75)
    #Loading the background image for the game screen
    bg = pygame.image.load("space.jpeg").convert_alpha()
    #Loading in the sprite image for the rocket
    sprite = pygame.image.load("rocket.jpeg").convert_alpha()
    #scaling the sprite down to 50 by 50 pixels
    sprite = pygame.transform.scale(sprite, (50, 50))

    #middle of the screen (x-position of the sprite)
    x = SCREEN_WIDTH/2

    #y-position of the sprite
    y = SCREEN_HEIGHT-100

    #initial score
    score = 0
    #initial amount of meteor's dodged
    dodged = 0

    while running:
        #score_dodged(dodged)
        
        #define the surface for the meteor
        meteor = pygame.Surface((meteor_width,meteor_height))
        #meteor_TWO = pygame.Surface((meteor_width_TWO, meteor_height_TWO))

        #fill the meteor with brown
        meteor.fill((110, 38, 14))
        screen.blit(bg, (0, 0))
        screen.blit(sprite, (x, y))
        screen.blit(meteor, (RANDOM_X, m))
        #screen.blit(meteor_TWO, (RANDOM_X, m_TWO))
        scoreString = str(score)
        score_display(scoreString)
        
        # for loop through the event queue
        for event in pygame.event.get():
            # Check for KEYDOWN event
            if event.type == KEYDOWN:
                # If the Esc key is pressed, then exit the main loop
                if event.key == K_ESCAPE:
                    start_menu("Continue?")
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
        m_TWO-=meteor_change
        c+=1

        if m>SCREEN_HEIGHT:
            m = 0-50
            RANDOM_X = random.randint(20, 700)
            meteor_width = random.randint(80,350)
            meteor_height = random.randint(30,75)
            RANDOM_X_TWO = random.randint(20, 700)
            meteor_width_TWO = random.randint(80,350)
            meteor_height_TWO = random.randint(30,75)
            dodged+=1


        if y < 50+m:
            if x > RANDOM_X and x < RANDOM_X+meteor_width or x+50 > RANDOM_X and x + 50 < RANDOM_X+meteor_width:
                m =0 
                x = 0
                #time.sleep(0.5)
                message_display("Crash")
                time.sleep(1)
                scores.append(score)
                bubble_sort(scores)
                score = 0
                RANDOM_X = random.randint(20,700)
                meteor_width = random.randint(80, 350)
                start_menu("Play Again?")
                meteor_height = random.randint(30,75)
                RANDOM_X_TWO = random.randint(20, 700)
                meteor_width_TWO = random.randint(80,350)
                meteor_height_TWO = random.randint(30,75)
                
        pygame.display.update()
        score+=1
        clock.tick(75)

#Algorithm Functions
def score_dodged(count):
    font = pygame.font.SysFont("ARIALUNI.TTF", 25)
    s = "Dodged: " + str(count)
    x = font.render(s, True, (255,255,255))
    smallText = pygame.font.Font('ARIALUNI.TTF',20)
    TextSurf, TextRect = text_objects(x, smallText)
    TextRect.center = ((15,15))
    screen.blit(TextSurf, TextRect)

def bubble_sort(args):
    n = len(args)
    swapped = False
    for i in range(n-1):
        for j in range(0,n-i-1):
            if args[j] > args[j+1]:
                swapped = True
                args[j],args[j+1] = args[j+1],args[j]
        if not swapped:
            return



if __name__ == "__main__":
    start_menu("Roaming In Space")