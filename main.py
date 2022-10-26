#IMPORTS
from cgitb import text
import pygame
import random
import threading
import os
import time
import Sprite
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

scores = []

#initialization
clock = pygame.time.Clock()
#Initialize Pygame
pygame.init()
#Setting a caption for the pygame screen
pygame.display.set_caption("Roaming In Space")
#opening highscores.txt with handle at the first 
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

def reset_scores():
    with open("highscores.txt", 'w') as scoresheet: 
        pass

#High Score Screen
def scores_screen():
    running = True
    screen.fill((0,0,0))
    scores=[]
    with open("highscores.txt") as scoresheet:
        for i in scoresheet:
            scores.append(int(i))
    largeText = pygame.font.Font('ARIALUNI.TTF',100)
    smallText = pygame.font.Font('ARIALUNI.TTF',25)
    mediumText = pygame.font.Font('ARIALUNI.TTF', 45)
    TextSurf, TextRect = text_objects("High Scores", largeText)
    TextRect.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2-250))
    screen.blit(TextSurf, TextRect)

    pygame.draw.rect(screen, (200,0,0), (SCREEN_HEIGHT/2+97.5,SCREEN_WIDTH/2-20, 150, 50))
    button_reset_collide = pygame.Rect((SCREEN_HEIGHT/2+97.5,SCREEN_WIDTH/2-20, 150, 50))

    pygame.draw.rect(screen, (0,200,0), (SCREEN_HEIGHT/2+97.5,SCREEN_WIDTH/2+40, 150, 50))
    button_main_collide = pygame.Rect((SCREEN_HEIGHT/2+97.5, ((SCREEN_WIDTH/4)+40), 150, 50))
    
    TextSurf_button1, TextRect_button1 = text_objects('"A"', smallText)
    TextRect_button1.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    TextRect_button1.center = ((SCREEN_HEIGHT/2+170,SCREEN_WIDTH/2+60))

    TextSurf_button2, TextRect_button2 = text_objects('"Reset"', smallText)
    TextRect_button2.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    TextRect_button2.center = ((SCREEN_HEIGHT/2+170,SCREEN_WIDTH/2+5))




    while running:
        if len(scores) >=1:
            TextSurf1, TextRect1 = text_objects(str(scores[0]), mediumText)
            TextRect1.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2-175))
            screen.blit(TextSurf1,TextRect1)
        if len(scores) >=2:
            TextSurf2, TextRect2 = text_objects(str(scores[1]), mediumText)
            TextRect2.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2-117.5))
            screen.blit(TextSurf2,TextRect2)
        if len(scores) >=3:
            TextSurf3, TextRect3 = text_objects(str(scores[2]), mediumText)
            TextRect3.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2-60))
            screen.blit(TextSurf3,TextRect3)
        if len(scores) >=4:
            TextSurf4, TextRect4 = text_objects(str(scores[3]), mediumText)
            TextRect4.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2-2.5))
            screen.blit(TextSurf4,TextRect4)
        if len(scores) >=5:
            TextSurf5, TextRect5 = text_objects(str(scores[4]), mediumText)
            TextRect5.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2+58))
            screen.blit(TextSurf5,TextRect5)
        pos = pygame.mouse.get_pos()

        screen.blit(TextSurf_button1,TextRect_button1)
        screen.blit(TextSurf_button2, TextRect_button2)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                #comment to test
            if event.type == pygame.KEYDOWN:
                if event.key == K_a:
                    pygame.draw.rect(screen, (0,255,0), (SCREEN_HEIGHT/2+97.5,SCREEN_WIDTH/2+40, 150, 50))
                if event.key == pygame.K_r:
                    pygame.draw.rect(screen, (255,0,0), (SCREEN_HEIGHT/2+97.5,SCREEN_WIDTH/2-20, 150, 50))
            if event.type==pygame.KEYUP:
                if event.key == K_a:
                    pygame.draw.rect(screen, (0,200,0), (SCREEN_HEIGHT/2+97.5,SCREEN_WIDTH/2+40, 150, 50))
                    start_menu("Roaming In Space")
                if event.key == pygame.K_r:
                    pygame.draw.rect(screen, (200,0,0), (SCREEN_HEIGHT/2+97.5,SCREEN_WIDTH/2-20, 150, 50))
                    reset_scores()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if its a left click and the pos of the mouse collides with the invisble RECT for the YES button then engage game loop
                if pygame.mouse.get_pressed()[0] and button_reset_collide.collidepoint(pos):
                    pygame.draw.rect(screen, (255,0,0), (SCREEN_HEIGHT/2+97.5,SCREEN_WIDTH/2-20, 150, 50))
                    reset_scores()
                #if its a left click and the pos of the mouse collides with the invisible RECT for the NO button then enngage quit sequence
                if pygame.mouse.get_pressed()[0] and button_main_collide.collidepoint(pos):
                    pygame.draw.rect(screen, (0,255,0), (SCREEN_HEIGHT/2+97.5,SCREEN_WIDTH/2+40, 150, 50))
                    start_menu("Roaming In Space")
        
        #update
        pygame.display.update()
        #lock FPS max at 15
        clock.tick(15)
        

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

    #text for the scores button
    TextSurf_button3, TextRect_button3 = text_objects('"S"', smallText)
    TextRect_button3.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    TextRect_button3.center = ((405+75, ((SCREEN_WIDTH/4)+175+25)))

    #fill both buttons. One is green, One is red. (RGB values) 
    #UNUSED
    button_yes.fill((255,0,0))
    button_no.fill((0,255,0))

    #Creates hidden hitboxes for the buttons
    button_yes_collide = pygame.Rect((SCREEN_HEIGHT/4,SCREEN_WIDTH/4+175), (150,50))
    button_no_collide =  pygame.Rect((650,((SCREEN_WIDTH/4)+175)), (150, 50))
    button_scores_collide = pygame.Rect((405, ((SCREEN_WIDTH/4)+175), 150, 50))

    #creates visuals for the buttons
    pygame.draw.rect(screen, (0,200,0), (SCREEN_HEIGHT/4,SCREEN_WIDTH/4+175, 150, 50))
    pygame.draw.rect(screen, (200,0,0), ((650),((SCREEN_WIDTH/4)+175), 150, 50))
    pygame.draw.rect(screen, (200,200,0), (405, ((SCREEN_WIDTH/4)+175), 150, 50))

    while running:
        time.sleep(0.5)
        #constantly updating live position of mouse 
        pos = pygame.mouse.get_pos()
        #screen.blit(button_no, (SCREEN_HEIGHT/4,SCREEN_WIDTH/4+175))
        #screen.blit(button_yes, (((650),((SCREEN_WIDTH/4)+175))))

        #BLIT the text that was defined earlier in the function
        screen.blit(TextSurf_button1, TextRect_button1)
        screen.blit(TextSurf_button2, TextRect_button2)
        screen.blit(TextSurf_button3, TextRect_button3)

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
                if event.key==pygame.K_s:
                    scores_screen()
            
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
                if pygame.mouse.get_pressed()[0] and button_scores_collide.collidepoint(pos):
                    pygame.draw.rect(screen, (255,255,0), (405, ((SCREEN_WIDTH/4)+175), 150, 50))
                    scores_screen()


        #update
        pygame.display.update()
        #lock FPS max at 15
        clock.tick(15)


#Main game loop
def game_loop(running):
    global scores
    #Velocity of the meteors
    velocity = 12
    #list for the highest scores
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
    scores.clear()
    with open("highscores.txt") as scoresheet:
        for i in scoresheet:
            scores.append(i)
    scoresheet = open('highscores.txt', 'w')
    while running:
        #score_dodged(dodged)
        
        #define the surface for the meteor
        meteor = pygame.Surface((meteor_width,meteor_height))
        #meteor_TWO = pygame.Surface((meteor_width_TWO, meteor_height_TWO))

        #fill the meteor with brown
        meteor.fill((110, 38, 14))

        #BLIT the starry sky backgroudn
        screen.blit(bg, (0, 0))
        
        spriteTest = Sprite.Sprite("Rocket")
        spriteTest.load_image("rocket.jpeg")

        #BLIT the sprite at postion (x,y)
        screen.blit(sprite, (x, y))

        #BLIT the meteor at a Random X value and at m which is the variable designated for the Y positon of the meteor
        screen.blit(meteor, (RANDOM_X, m))

        #screen.blit(meteor_TWO, (RANDOM_X, m_TWO))

        #convert score value to a string so it can be displayed with the score_display function
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
        
        #add the position change to the actual position value
        x+=x_change

    #if the x-coordinate of the sprite goes below 0 (Off the screen) then we reset to 0 to bring it back. 
        if x<0:
            x=0
    #same prinicple as the comment above but this is for the other side
        elif x>950:
            x = 950
        
        #Variable C made to restrict the speed of the change for the y coordinate of the meteor
        if c%97:
            meteor_change = 10
        else:
            meteor_change = 0 
        if c == 97:
            c = 0
        
        #Adding the change in the y position for the meteor to the designated Y variable.
        m+=meteor_change
        m_TWO-=meteor_change
        c+=1

        #Once the meteor goes off the screen. Then redefine all the variables to make the next meteor
        if m>SCREEN_HEIGHT:
            m = 0-50
            RANDOM_X = random.randint(20, 700)
            meteor_width = random.randint(80,350)
            meteor_height = random.randint(30,75)
            RANDOM_X_TWO = random.randint(20, 700)
            #meteor_width_TWO = random.randint(80,350)
            #meteor_height_TWO = random.randint(30,75)
            dodged+=1

        #The next two if statments calculate if the sprite has collided with the meteor. 
        #HOWEVER this is a little archaic IMO maybe we can use the collidepoint functions to do this much more easily. 
        if y < 50+m:
            if x > RANDOM_X and x < RANDOM_X+meteor_width or x+50 > RANDOM_X and x + 50 < RANDOM_X+meteor_width:
                m =0 
                x = 0
                #time.sleep(0.5)
                #Once we have established we have crashed
                #display a crash message
                message_display("Crash")
                #keep displaying for one second
                time.sleep(1)
                #append the score to the scores list
                scores.append(score)
                #bubble sort the list to go from least to greatest
                for i in range(len(scores)-1):
                    scores[i] = int(scores[i])
                bubble_sort(scores)
                for i in scores:
                    scoresheet.write(str(i)+'\n')
                scoresheet.close()
                #reset score
                score = 0
                #redefne the variables for another run
                RANDOM_X = random.randint(20,700)
                meteor_width = random.randint(80, 350)
                #Go back to the start screen but with a different message this time.
                start_menu("Play Again?")
                meteor_height = random.randint(30,75)
                RANDOM_X_TWO = random.randint(20, 700)
                meteor_width_TWO = random.randint(80,350)
                meteor_height_TWO = random.randint(30,75)
                                                    
        #update
        pygame.display.update()
        #every iteration of the for loop increase the score by 1
        score+=1
        #limit fps to 75
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

#Bubble sort function
def bubble_sort(args):
    n = len(args)
    swapped = False
    for i in range(n-1):
        for j in range(0,n-i-1):
            if args[j] < args[j+1]:
                swapped = True
                args[j],args[j+1] = args[j+1],args[j]
        if not swapped:
            return

def get_scores(scoresheet):
    assert scoresheet.closed
    global scores
    with open("highscores.txt") as score_sheet:
        for i in score_sheet:
            scores.append(i)


#create a main function
if __name__ == "__main__":
    start_menu("Roaming In Space")