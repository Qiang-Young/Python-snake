import pygame
import sys
import time
import random
from pygame.locals import*
from collections import deque

#画横线和竖线
def DrawMp():
    window.fill(Light)
    for x in range(size, window_wid, size):
        pygame.draw.line(window,Black,(x,2*size),(x,window_hig),linewid)
    for y in range(size*2, window_hig, size):
        pygame.draw.line(window,Black,(0,y),(window_wid,y),linewid)
    pygame.display.flip()
    return

#蛇的初始位置
def InitSnake():
    snake = []
    snake.append([2,2])
    snake.append([1,2])
    snake.append([0,2])
    return snake

#键盘控制蛇的方向
def MoveDir(snake,pos):
    for event in pygame.event.get():
        if event.type == QUIT:
            print("您主动关闭了窗口！！")
            sys.exit()
        elif event.type == KEYDOWN:
            if pos == 3 or pos == 4:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    pos = 1
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    pos = 2
            elif pos == 1 or pos == 2:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    pos = 3
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    pos = 4
    return pos

#创建食物
def CreateFood(snake,food):
    food_x = random.randint(0,Max_X) * size
    food_y = random.randint(2,Max_Y) * size
    while (food_x,food_y) in snake:
        food_x = random.randint(0,Max_X) * size
        food_y = random.randint(2,Max_Y) * size
    food[0] = food_x
    food[1] = food_y
    return food

#判断游戏状态
def GameStatus(snake,win):
    i = len(snake)-1
    while i > 0:
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            return False
        i -= 1
    if snake[0][0] == Max_X + 1 or snake[0][0] == -1:
        return False
    elif snake[0][1] == Max_Y + 1 or snake[0][1] == 1:
        return False
    elif len(snake) == win:
        return 2
    else:
        return True
    
    
#蛇的移动
def MoveSnake(snake,pos,food,score):
    i = len(snake) - 1
    last = [snake[i][0],snake[i][1]]
    while i > 0:
        snake[i][0] = snake[i-1][0]
        snake[i][1] = snake[i-1][1]
        i -= 1
    snake[0][0] = snake[0][0] + move[pos-1][0]
    snake[0][1] = snake[0][1] + move[pos-1][1]
    #吃到食物
    if size * snake[0][0] == food[0] and size * snake[0][1] == food[1]:
        snake.append(last)
        food = CreateFood(snake,food)
        score += 1
    pygame.draw.rect(window,Dark,((food[0],food[1]),(size - linewid * 2,size - linewid * 2)))
    pygame.display.flip()
    return score

#画
def DrawSnake(snake,pos,food):
    DrawMp()
    for i in range(0,len(snake)):
        if i == 0:
            pygame.draw.rect(window,Red,((snake[i][0]*size+ linewid,snake[i][1]*size + linewid ),(size - linewid * 2,size - linewid * 2)))
        else:
            pygame.draw.rect(window,Dark,((snake[i][0]*size+ linewid,snake[i][1]*size + linewid ),(size - linewid * 2,size - linewid * 2)))
        pygame.display.flip()  
                     
if __name__ == "__main__":
    #初始化pygame函数
    pygame.init()
    #设置窗口大小、标题
    window_wid = 300
    window_hig = 340
    window = pygame.display.set_mode((window_wid,window_hig))
    pygame.display.set_caption("贪吃蛇")
    win = (window_wid/20) * (window_hig/20 -2) #判断游戏胜利的标准
    size = 20    #方格大小
    linewid = 1  #线宽
    move = [(0,-1),(0,1),(-1,0),(1,0)]   #上下左右移动参数
    pos = 4   #初始方向1，2，3，4分别代表上下左右
    #字体
    font1 = pygame.font.SysFont('SimHei',int(window_wid/20))
    font2 = pygame.font.SysFont('SimHei',int(window_hig/5))
    #游戏区域
    Max_X = window_wid/size -1
    Max_Y = window_hig/size -1
    #各颜色定义
    Green = (0,255,0)
    Black = (0,0,0)
    Light = (100,100,100)
    Dark = (200,200,200)
    Red = (200,30,30)
    BlackColor = (40,40,60)
    Blue = (0,0,128)
    #游戏参数
    game_status = True   #游戏开始的状态
    score = 0            #游戏分数

    food = [[],[]]
    snake = InitSnake()
    DrawMp()
    food = CreateFood(snake,food)
    while game_status:
        DrawSnake(snake,pos,food)
        pos = MoveDir(snake,pos)
        score = MoveSnake(snake,pos,food,score)
        text = ("分数：{}".format(score))
        textSurfaceObj = font1.render(text,True,Green)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center=(int(window_wid/8),15)
        window.blit(textSurfaceObj,textRectObj)
        pygame.display.update()
        game_status = GameStatus(snake,win)
        if game_status == False:
            textSurfaceObj = font2.render('GAME OVER',True,Blue)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center=(window_wid/2,window_hig/2)
            window.blit(textSurfaceObj,textRectObj)
            pygame.display.update()
            break
        if game_status == 2:
            textSurfaceObj = font2.render('YOU WIN',True,Blue)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center=(window_wid/2,window_hig/2)
            window.blit(textSurfaceObj,textRectObj)
            pygame.display.update()
            break
        time.sleep(0.2-score/120)
        DrawSnake(snake,pos,food)
        DrawSnake(snake,pos,food)
    

























