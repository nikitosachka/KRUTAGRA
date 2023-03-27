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

#налаштування гри
gameover = False
speed = 2
score = 0

#маркери гри
marker_width = 10
marker_height = 50

#зона дороги
road = (100, 0, 300, height)
left_edge_marker = (95, 0, marker_width, height)
right_edge_marker = (395, 0, marker_width, height)

#для перетинання ліній(анімація)
lane_marker_move_y = 0

#x координата лінії(білі які гравець перетинає)
left_lane = 150
center_lane = 250
right_lane = 350
lanes = [left_lane, center_lane, right_lane]