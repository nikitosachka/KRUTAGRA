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
#-------------------------------------------------Класи-------------------------------------------------------------
#машина
class Car(pygame.sprite.Sprite):
          def __init__(self, image, x, y):
               pygame.sprite.Sprite.__init__(self)

               #маштабування машини щоб вона вміщалась у лінії
               image_scale = 45 / image.get_rect().width
               new_width = image.get_rect().width * image_scale
               new_height = image.get_rect().height * image_scale
               self.image = pygame.transform.scale(image, (new_width, new_height))

               self.rect = self.image.get_rect()
               self.rect.center = [x, y]

class PlayerCar(Car):
     def __init__(self, x, y):
          image = pygame.image.load('images/car.png')
          super().__init__(image, x, y)

#стартові координати гравця
player_x = 250
player_y = 400

#cтворення машини гравця
player_group = pygame.sprite.Group()
player = PlayerCar(player_x, player_y)
player_group.add(player)
#-------------------------------------------------Текстури----------------------------------------------------------
#завантаження інших машин
image_filenames = ['pickup_truck.png', 'semi_trailer.png', 'taxi.png', 'van.png']
vehicle_images = []
for image_flename in image_filenames:
     image = pygame.image.load('images/' + image_flename)
     vehicle_images.append(image)

#sprite група для машин
vehicle_group = pygame.sprite.Group()

#завантаження вибуху
crash = pygame.image.load('images/crash.png')
crash_rect = crash.get_rect()