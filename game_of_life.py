import pygame
import numpy as np

pygame.init()
pygame.font.init()
size = width, height =  800,600
life_size = 20
backgrond_color = (0,0,0)
life_color = (255,255,255)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

frame = np.random.randint(2, size=(int(width/life_size),int(height/life_size)))
# frame = np.zeros((int(width/life_size),int(height/life_size)))
# frame[0][0]=1
# frame[0][1]=1
# frame[1][0]=1
# frame[1][1]=1
# print(frame)

def draw_life(frame):
    for i in range(len(frame)):
        for j in range(len(frame[i])):
            if frame[i][j] == 1:
                pygame.draw.rect(screen,life_color,(i*life_size,j*life_size,life_size,life_size))

def check_life(frame):
    new_frame = frame.copy()

    for i in range(len(frame)):
        for j in range(len(frame[i])):

            neighbors=0
            for vx in range(i-1,i+2,1):
                for vy in range(j-1,j+2,1):
                    if 0<=vx<int(width/life_size) and 0<=vy<int(height/life_size) and not(vx==i and vy ==j):
                        if frame[vx][vy]==1:
                            neighbors+=1

            if 1<neighbors<4:
                new_frame[i][j]=1
            else:
                new_frame[i][j]=0
    return new_frame



while True:
    screen.fill(backgrond_color)

    draw_life(frame)
    frame = check_life(frame)
    pygame.display.update()
    pygame.display.flip()
    clock.tick(5)