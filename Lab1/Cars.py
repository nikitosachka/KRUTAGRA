import pygame
from pygame.locals import *
import random

pygame.init()
#-------------------------------------------------Налаштування------------------------------------------------------
#створюємо вікно
width = 500
height = 500
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Need For Speed')