import pygame
import os

pygame.font.init()

FPS = 60

BLACK = (0, 0, 0)
RED = (235, 105, 105)
BLUE = (105, 118, 235)
WHITE = (255, 255, 255)

WIDTH, HEIGHT = 900, 550
BUTTON_WIDTH, BUTTON_HEIGHT = 303, 92

BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background.jpg")), (WIDTH, HEIGHT))
CONNECT_FOUR_FONT = pygame.font.SysFont("comicsans", 90)
START_FONT = pygame.font.SysFont("comicsans", 25)