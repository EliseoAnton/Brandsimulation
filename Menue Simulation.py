import pygame
import sys
import time
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()
#all_fonts = pygame.font.get_fonts()
#Font = pygame.font.SysFont('arial', 20)
W = 600
H = 400

Surface = pygame.display.set_mode((W,H), 0, 32)
pygame.display.set_caption('Python Menus')

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)



##def text_print(text,color1,color2,left,top,Font=basicFont):
##    text = Font.render(text,True,color1,color2)
##    text_rect = text.get_rect()
##    text_rect.top = top
##    text_rect.left = left
##    Surface.blit(text, text_rect)
game = True
mouse_pos = (0,0)
mouse_click = (0,0)
text1_bool = False
text2_bool = False
text3_bool = False
output = '?'

while game == True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit(0)
        if event.type == MOUSEMOTION:
            mouse_pos = event.pos
        if event.type == MOUSEBUTTONUP:
            mouse_click = event.pos




    

    Surface.fill(BLACK)
    color = WHITE
    Font = pygame.font.SysFont('arial', 40)
    if text1_bool:
        color = RED
    text = Font.render('Simulation',True,color)
    text_rect = text.get_rect()
    text_rect.center = (W / 2,H / 5)
    if text_rect.collidepoint(mouse_click):
        output = '1'
    if text_rect.collidepoint(mouse_pos):
        text1_bool = True
    else:
        text1_bool = False
    Surface.blit(text, text_rect)

    bg = pygame.image.load("simulationsmenue_export.jpg")

    color = WHITE
    if text2_bool:
        color = RED
    
    Font = pygame.font.SysFont('arial', 40)
    text = Font.render('Bedienung',True,color)
    text_rect = text.get_rect()
    text_rect.center = (W / 2,H * 2 / 5)
    if text_rect.collidepoint(mouse_click):
        output = '2'
    if text_rect.collidepoint(mouse_pos):
        text2_bool = True
    else:
        text2_bool = False
    Surface.blit(text, text_rect)

    color = WHITE
    if text3_bool:
        color = RED
    
    Font = pygame.font.SysFont('arial', 40)
    text = Font.render('Hinweise',True,color)
    text_rect = text.get_rect()
    text_rect.center = (W / 2,H * 3 / 5)
    if text_rect.collidepoint(mouse_click):
        output = '3'
    if text_rect.collidepoint(mouse_pos):
        text3_bool = True
    else:
        text3_bool = False
    Surface.blit(text, text_rect)





    pygame.display.flip()
    mainClock.tick(100000)
