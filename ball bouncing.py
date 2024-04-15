# import pygame
# import sys
# import time
# pygame.init()
# w=900
# h=400
# window = pygame.display.set_mode((w,h))
# pygame.display.set_caption("boing")
# white=(255,255,255)
# g=(0,255,0)
# ball_x=w/2
# ball_y=h/2
# ball_r=20
# ball_speed_x=5
# ball_speed_y=5
# clock=pygame.time.Clock()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     ball_x+=ball_speed_x
#     ball_y+=ball_speed_y
#     if ball_x-ball_r<0 or ball_x+ball_r>w:
#         ball_speed_x=-ball_speed_x
#     if ball_y-ball_r<0 or ball_y+ball_r>h:
#         ball_speed_y=-ball_speed_y
#
#     window.fill(white)
#     pygame.draw.circle(window,g,(ball_x,ball_y),ball_r)
#     pygame.display.flip()
#     clock.tick(30)
import random

# import pygame
# import sys
# import time
# pygame.init()
# w=900
# h=400
# window = pygame.display.set_mode((w,h))
# pygame.display.set_caption("boing")
# white=(255,255,255)
# g=(0,255,0)
# def ball():
#     speed= [random.randint(1,10),random.randint(1,5)]
#     radius=random.randint(10,30)
#     colour=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
#     pos=[random.randint(radius,w-radius),random.randint(radius,h-radius)]
#     return {'radius':radius,'Colour':colour,'spood':speed,'position':pos}
# balls=[ball() for i in range(100) ]
# clock=pygame.time.Clock()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     for balle in balls:
#         balle['position'][0]+=balle['spood'][0]
#         balle['position'][1] += balle['spood'][1]
#         if balle['position'][0]<=0 or balle['position'][0]>=w:
#             balle['spood'][0]= -balle['spood'][0]
#         if balle['position'][1]<=0 or balle['position'][1]>=h:
#             balle['spood'][1]= -balle['spood'][1]
#
#
#     # window.fill(white)
#     for balle in balls:
#         pygame.draw.circle(window,balle['Colour'],(balle['position'][0],balle['position'][1]),balle['radius'])
#     pygame.display.flip()
#     clock.tick(30)

import random

import pygame
import sys
import time

pygame.init()
w = 900
h = 400
window = pygame.display.set_mode((w, h))
pygame.display.set_caption("boing")
white = (255, 255, 255)
g = (0, 255, 0)
ga=pygame.image.load('discord pfp.PNG')
gay=pygame.transform.scale(ga,(900,400))
pooos=pygame.mixer.Sound('cute-level-up-3-189853.mp3')
oos=pygame.mixer.Sound('cool_song.wav')
def ball():
    speed = [random.randint(1, 10), random.randint(1, 5)]
    radius = random.randint(10, 30)
    colour = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    pos = [random.randint(radius, w - radius), random.randint(radius, h - radius)]
    return {'radius': radius, 'Colour': colour, 'spood': speed, 'position': pos}


balls = [ball() for i in range(100 )]
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for balle in balls:
        balle['position'][0] += balle['spood'][0]
        balle['position'][1] += balle['spood'][1]
        if balle['position'][0] <= 0 or balle['position'][0] >= w:
            balle['spood'][0] = -balle['spood'][0]
            pooos.play()
        if balle['position'][1] <= 0 or balle['position'][1] >= h:
            balle['spood'][1] = -balle['spood'][1]
            oos.play()

    window.blit(gay,(0,0))
    for balle in balls:
        pygame.draw.circle(window, balle['Colour'], (balle['position'][0], balle['position'][1]), balle['radius'])
    pygame.display.update()
    clock.tick(30)


