def gmeika3():
    import pygame
    import time
    import random
    import functions_for_snake
    from functions_for_snake import our_snake,our_snake1,input1,foodA,message,message2
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
    pygame.display.set_caption('Snake ')
    dis.fill(blue)
    pygame.display.update()
    snake_block = 10
    snake_speed = 10
    snake=[[600,500],[610,500]]
    snake2=[[500,500],[510,500]]
    x1_change=0
    y1_change=0
    x1_change1=0
    y1_change1=0
    foodx=(int(random.randint(0,1201))//10)*10
    foody=(int(random.randint(0,1001))//10)*10
    pygame.draw.rect(dis, green , [foodx, foody, snake_block, snake_block])
    pygame.display.update()
    sch=0
    sch2=0
    fghd=0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                if event.key == pygame.K_a:
                    x1_change1 = -snake_block
                    y1_change1 = 0
                elif event.key == pygame.K_d:
                    x1_change1 = snake_block
                    y1_change1 = 0
                elif event.key == pygame.K_w:
                    y1_change1 = -snake_block
                    x1_change1 = 0
                elif event.key == pygame.K_s:
                    y1_change1 = snake_block
                    x1_change1 = 0
        a=len(snake)-1
        y=snake[a][1]
        x=snake[a][0]
        y+=y1_change
        x+=x1_change
        a1=len(snake2)-1
        y1=snake2[a1][1]
        x1=snake2[a1][0]
        y1+=y1_change1
        x1+=x1_change1
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x)
        snake_Head.append(y)
        snake.append(snake_Head)
        if snake_Head[0]>dis_width:
            snake_Head[0]=0
        if snake_Head[0]<0:
            snake_Head[0]=dis_width
        if snake_Head[1]>dis_height:
            snake_Head[1]=0
        if snake_Head[1]<0:
            snake_Head[1]=dis_height
        if len(snake) > sch+2:
            del snake[0]
        snake_Head1 = []
        snake_Head1.append(x1)
        snake_Head1.append(y1)
        snake2.append(snake_Head1)
        if snake_Head1[0]>dis_width:
            snake_Head1[0]=0
        if snake_Head1[0]<0:
            snake_Head1[0]=dis_width
        if snake_Head1[1]>dis_height:
            snake_Head1[1]=0
        if snake_Head1[1]<0:
            snake_Head1[1]=dis_height
        if len(snake2) > sch2+2:
            del snake2[0]
        for i in snake[:-1]:
            if i ==  snake_Head1   and sch>0:
                game_over=True
                sch=0
                fghd=0
                message("You lose, viper!", collor1=white,collor2=red,a=vbf,b=400,c=400)
                message2("Press Q to exit or C to replay!", collor1=white,a=vbf,b=300,c=500)
                to_input="viper "+str(sch)
                input1(msg=to_input,collor=yellow,a=score_font,b=0,c=0)
                to_input="python "+str(sch2)
                input1(msg=to_input,collor=yellow,a=score_font,b=1000,c=0)
                pygame.display.update()
                while game_over:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                sch=0
                                pygame.quit()
                                quit()
                            if event.key == pygame.K_c:
                                sch=0
                                snake=[[600,500],[610,500]]
                                game_over=False
            elif i ==  snake_Head   and sch>0:
                game_over=True
                sch=0
                fghd=0
                message("You lose, viper!", collor1=white,collor2=red,a=vbf,b=400,c=400)
                message2("Press Q to exit or C to replay!", collor1=white,a=vbf,b=300,c=500)
                to_input="viper "+str(sch)
                input1(msg=to_input,collor=yellow,a=score_font,b=0,c=0)
                to_input="python "+str(sch2)
                input1(msg=to_input,collor=yellow,a=score_font,b=1000,c=0)
                pygame.display.update()
                while game_over:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                sch=0
                                pygame.quit()
                                quit()
                            if event.key == pygame.K_c:
                                sch=0
                                snake=[[600,500],[610,500]]
                                game_over=False
        for i in snake2[:-1]:
            if i ==  snake_Head1   and sch2>0:
                game_over=True
                sch2=0
                fghd=0
                message("You lose, python!", collor1=white,collor2=red,a=vbf,b=400,c=400)
                message2("Press Q to exit or C to replay!", collor1=white,a=vbf,b=300,c=500)
                to_input="viper "+str(sch)
                input1(msg=to_input,collor=yellow,a=score_font,b=0,c=0)
                to_input="python "+str(sch2)
                input1(msg=to_input,collor=yellow,a=score_font,b=1000,c=0)
                pygame.display.update()
                while game_over:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                sch2=0
                                pygame.quit()
                                quit()
                            if event.key == pygame.K_c:
                                sch2=0
                                snake2=[[600,500],[610,500]]
                                game_over=False
            elif i ==  snake_Head   and sch2>0:
                game_over=True
                sch2=0
                fghd=0
                message("You lose, python!", collor1=white,collor2=red,a=vbf,b=400,c=400)
                message2("Press Q to exit or C to replay!", collor1=white,a=vbf,b=300,c=500)
                to_input="viper "+str(sch)
                input1(msg=to_input,collor=yellow,a=score_font,b=0,c=0)
                to_input="python "+str(sch2)
                input1(msg=to_input,collor=yellow,a=score_font,b=1000,c=0)
                pygame.display.update()
                while game_over:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                sch2=0
                                pygame.quit()
                                quit()
                            if event.key == pygame.K_c:
                                sch2=0
                                snake2=[[600,500],[610,500]]
                                game_over=False                        
                    
                
        our_snake(snake_block, snake)
        our_snake1(snake_block, snake2)
        if x == foodx and y == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            sch += 1
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            sch2 += 1
        to_input="viper "+str(sch)
        input1(msg=to_input,collor=yellow,a=score_font,b=0,c=0)
        to_input="python "+str(sch2)
        input1(msg=to_input,collor=yellow,a=score_font,b=1000,c=0)
        fghd+=1
        if fghd%5==0:
            jklx=random.randint(0,3)
            jkly=random.randint(0,3)
            if jklx==0:
                foodx+=snake_block
            elif jklx==1:
                foodx-=snake_block
            else:
                foodx+=0
            if jkly==0:
                foody+=snake_block
            elif jkly==1:
                foody-=snake_block
            else:
                foody+=0 
            if foodx>dis_width:
                foodx=dis_width-snake_block
            elif foodx<0:
                foodx=0
            if foody>dis_height:
                foody=dis_height-snake_block
            elif foody<0:
                foody=0
        foodA(x=foodx,y=foody,collor=green)
        pygame.display.update()
        time.sleep(0.1)
    time.sleep(10)
    pygame.quit()
    quit()
gmeika3()










