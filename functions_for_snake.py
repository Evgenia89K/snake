import pygame
import time
import random
import datetime

pygame.init()
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
dis.fill(blue)
pygame.display.update()
    
snake_block = 10
snake_speed = 10
snake=[[600,500],[610,500]]
snake2=[[500,500],[510,500]]
    
def message(msg, collor1=(0,0,0),collor2=(255,255,255),a=vbf,b=dis_width / 6,c=dis_height / 3):
    dis.fill(collor2)
    pygame.display.update()
    mesg = a.render(msg, True, collor1)
    dis.blit(mesg, [b,c])
    pygame.display.update()
def message2(msg, collor1=(0,0,0),a=vbf,b=dis_width / 6,c=dis_height / 3):
        
        
    mesg = a.render(msg, True, collor1)
    dis.blit(mesg, [b,c])
    pygame.display.update()
def foodA(x,y,collor=green):
    pygame.draw.rect(dis, collor , [x, y, snake_block, snake_block])
    
def input1(msg, collor=(0,0,0),a=score_font,b=dis_width / 6,c=dis_height / 3):
    mesg = a.render(msg, True, collor)
    dis.blit(mesg, [b,c])
        
def our_snake(snake_block, snake_list):
    fgf=0
    for x in snake_list:
           
        if len(snake_list)-1==fgf:
            collor=snake_collor21
        else:
            collor=snake_collor11
        fgf+=1 
        pygame.draw.rect(dis, collor , [x[0], x[1], snake_block, snake_block])
            
def our_snake1(snake_block, snake_list):
    fgf=0
    for x in snake_list:
           
        if len(snake_list)-1==fgf:
            collor=snake_collor22
        else:
            collor=snake_collor12
        fgf+=1 
        pygame.draw.rect(dis, collor , [x[0], x[1], snake_block, snake_block])
            
            
    
