import pygame
import numpy as np

pygame.init()
pygame.font.init()
size = width, height =  800,800
life_size = 20
backgrond_color = (0,0,0)
life_color = (255,255,255)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# frame = np.random.randint(2, size=(int(width/life_size),int(height/life_size)))
frame = np.zeros((int(width/life_size),int(height/life_size)))

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

            if frame[i][j]==1 and (neighbors<2 or 3<neighbors):
                new_frame[i][j]=0
            if frame[i][j]==0 and neighbors==3:
                new_frame[i][j]=1

    return new_frame


stop =False
while True:
    screen.fill(backgrond_color)
    for event in pygame.event.get():
        # handle MOUSEBUTTONUP
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                if stop:
                    stop=False
                else:
                    stop=True

        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            mx = int(x/life_size)
            my = int(y/life_size)
            if frame[mx][my]==1:
                frame[mx][my]=0
            else:
                frame[mx][my]=1

    draw_life(frame)
    if not stop:
        frame = check_life(frame)
    pygame.display.update()
    pygame.display.flip()
    clock.tick(2)