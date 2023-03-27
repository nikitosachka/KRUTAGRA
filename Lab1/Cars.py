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

#кольора
gray = (100, 100, 100)
green = (76, 208, 56)
red = (200, 0, 0)
white = (255, 255, 255)
yellow = (255, 232, 0)