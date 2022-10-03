import pygame
from main import screen, SCREEN_HEIGHT, SCREEN_WIDTH
class Sprite:

    #velocity variable
    x_change = 0
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT-100 
    Name= ''
    def __init__(self, name):
        Sprite.Name = name
    def load_image(self, image):
        sprite = pygame.image.load(image).convert_alpha()

    def move(self):
        screen.blit(Sprite.Name, (Sprite.x, Sprite.y))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_a:
                    x_change += -12
                if event.type == pygame.K_d:
                    x_change += 12
            if event.type == pygame.KEYUP:
                if event.type == pygame.K_a or event.type == pygame.K_d:
                    x_change = 0
        Sprite.x += x_change
        if Sprite.x <0:
            Sprite.x = 0
        if Sprite.x > 950:
            Sprite.x = 950