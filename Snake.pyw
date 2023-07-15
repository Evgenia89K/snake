try:
    file = open('C:\Program Files\Python36\Lib\site-packages\pygame\__pyinstaller\__pycache__\hook-pygame.cpython-36.pyc')
except IOError as e:
    import subprocess
    module = "pygame"
    subprocess.run(["pip", "install", module, "--upgrade"])
import pygame
import os
from functions_for_snake import message,message2
pygame.init()
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
vbf = pygame.font.SysFont("comicsansms", 30)
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
violet=(225, 0, 180)
snake_collor11=(73,1,1)
snake_collor21=(30,11,6)
snake_collor12=(60,85,25)
snake_collor22=(15,40,25)
dis_width = 1200
dis_height = 1000
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Змейка ')
message("Click 'e' to select the English version or 'r' to select the Russian version.", collor1=blue,collor2=white,a=vbf,b=60,c=350)
message2("Нажмите 'e' чтобы выбрать англоязычную версию", collor1=blue,a=vbf,b=200,c=400)
message2("или 'r' для выбора рускоязычной версии.", collor1=blue,a=vbf,b=270,c=450)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                os.system('start Snake_E.pyw')
                pygame.quit()
                quit()
            elif event.key == pygame.K_r:
                os.system('start Snake_R.pyw')
                pygame.quit()
                quit()
