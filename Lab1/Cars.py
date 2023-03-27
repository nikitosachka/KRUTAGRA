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
#-------------------------------------------------Головний-Цикл-------------------------------------------------------

#цикл гри
clock = pygame.time.Clock()
fps = 120
running = True
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        #переміщення гравця використовуючи праву/ ліву стрілку
        if event.type == KEYDOWN:
             if event.key == K_LEFT and player.rect.center[0] > left_lane:
                  player.rect.x -= 100
             elif event.key == K_RIGHT and player.rect.center[0] < right_lane:
                  player.rect.x += 100
        #перевірка чи є бокове зіткнення після зміни смуги руху
        for vehicle in vehicle_group:
             if pygame.sprite.collide_rect(player, vehicle):
               gameover = True
               #розмістити машину гравця поруч з іншою машиною
               #і визначити де розмістити зображення аварії
               if event.key == K_LEFT:
                    player.rect.left = vehicle.rect.right
                    crash_rect.center = [player.rect.left, (player.rect.center[1] + vehicle.rect.center[1]) / 2]
               elif event.key == K_RIGHT:
                    player.rect.right = vehicle.rect.left
                    crash_rect.center = [player.rect.right, (player.rect.center[1] + vehicle.rect.center[1]) / 2]
#-------------------------------------------------Малювання----------------------------------------------------------
    #малювання трави
    screen.fill(green)

    #малювання дороги
    pygame.draw.rect(screen, gray, road)

    #малювання жовтих меж
    pygame.draw.rect(screen, yellow, left_edge_marker)
    pygame.draw.rect(screen, yellow, right_edge_marker)

    #малювання білих ліній
    lane_marker_move_y += speed * 2
    if lane_marker_move_y >= marker_height * 2:
        lane_marker_move_y = 0
    
    for y in range(marker_height * -2, height, marker_height * 2):
        pygame.draw.rect(screen, white, (left_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
        pygame.draw.rect(screen, white, (center_lane + 45, y + lane_marker_move_y, marker_width, marker_height))

    #малювання машини гравця
    player_group.draw(screen)

    #додавання до двох машин
    if len(vehicle_group) < 2:
         #переконатися, що там достатньо місця
         add_vehicle = True
         for vehicle in vehicle_group:
              if vehicle.rect.top < vehicle.rect.height * 1.5:
                   add_vehicle = False

         if add_vehicle:
              #вибираємо рандомну лінію
              lane = random.choice(lanes)

              #вибираємо рандомну машину
              image = random.choice(vehicle_images)
              vehicle = Car(image, lane, height / -2)
              vehicle_group.add(vehicle)
         
    #логіка машин(перешкод)
    for vehicle in vehicle_group:
         vehicle.rect.y += speed

         #видалення машини, якщо вона за межами екрану
         if vehicle.rect.top >= height:
              vehicle.kill()
              # додавання рекорда
              score += 1
              
              #збільшення швидкості гри після минування 5 перешкод
              if score > 0 and score % 5 == 0:
                   speed += 1
                   
    #малювання машин(перешкод)
    vehicle_group.draw(screen)

    #малювання рекорду
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render('Score: ' + str(score), True, white)
    text_rect = text.get_rect()
    text_rect.center = (50, 450)
    screen.blit(text, text_rect)

    #перевірка чи є зіткнення
    if pygame.sprite.spritecollide(player, vehicle_group, True):
         gameover = True
         crash_rect.center = [player.rect.center[0], player.rect.top]

     #виведення GAMEOVER
    if gameover:
         screen.blit(crash, crash_rect)
         pygame.draw.rect(screen, red, (0, 50, width, 100))
         font = pygame.font.Font(pygame.font.get_default_font(), 16)
         text = font.render('GAMEOVER. Не буде з вас стрітрейсера!!! Грати ще раз? (Y/N)', True, white)
         text_rect = text.get_rect()
         text_rect.center = (width / 2, 100)
         screen.blit(text, text_rect)

    pygame.display.update()

    #перевірка чи гравець хоче грати ще?
    while gameover:
         clock.tick(fps)
         
         for event in pygame.event.get():
              if event.type == QUIT:
                   gameover = False
                   running = False
              #дати змогу гравцю натискати Y/N
              if event.type == KEYDOWN:
                   if event.key == K_y:
                        #перезапуск гри
                        gameover = False
                        speed = 2
                        score = 0
                        vehicle_group.empty()
                        player.rect.center = [player_x, player_y]
                   elif event.key == K_n:
                        #вихід з циклу
                        gameover = False
                        running = False
pygame.quit()
#POstavte good ocinku
