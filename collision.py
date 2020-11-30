import pygame
import random
 
# Define some colors
black = (  0,   0,   0)
white = (255, 255, 255)
red   = (255,   0,   0)
blue = (0,0,255)
green = (0,255,0)
w=0

pygame.init()

screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode([screen_width, screen_height])


#bloc=[masse,vitesse,posx,largeur,hauteur,couleur]

bloc1=[1,0,10,20,20,black]
bloc2=[1,1,980,20,20,red]
bloc3=[1,0,500,20,20,blue]
bloc4=[1,-2,340,20,20,green]

blocs=[bloc1,bloc2,bloc3,bloc4]

def update(bloc):
    global w
    bloc[2]+=bloc[1]
    if bloc[2]<0:
       bloc[1]=bloc[1]*-1
       bloc[2]=0
       #w+=1
       #print("collision  : "+str(w))
    if bloc[2]>980:
       bloc[1]=bloc[1]*-1
       bloc[2]=980



def collision(bloc1,bloc2):
    x1=(2*bloc2[0]*bloc2[1]+bloc1[1]*(bloc1[0]-bloc2[0]))
    x2=(2*bloc1[0]*bloc1[1]+bloc2[1]*(bloc2[0]-bloc1[0]))
    bloc1[1]=x1/(bloc1[0]+bloc2[0])
    bloc2[1]=x2/(bloc1[0]+bloc2[0])
    update(bloc1)
    update(bloc2)




def check_collision(bloc1):
    global w
    x=blocs.index(bloc1)
    for i in range(len(blocs)):
        if i == x:
            continue


      
        if blocs[x][2]-blocs[i][2]>0:
            if blocs[x][2]-blocs[i][2]<blocs[x][3]:
                #if abs(blocs[x][0]*blocs[x][1])>abs(blocs[i][0]*blocs[i][1]):
                    #blocs[i][2]-=blocs[x][2]-blocs[i][2]
                #else :
                    #blocs[x][2]+=blocs[x][2]-blocs[i][2]
                collision(blocs[i],blocs[x])
                #print("collision  : "+str(w))
                #w+=1

        if blocs[x][2]-blocs[i][2]<0:
            if blocs[i][2]-blocs[x][2]<blocs[i][3]:
                #if blocs[i][0]>blocs[x][0]:
                    #blocs[x][2]-=blocs[i][2]-blocs[x][2]
                #else :
                    #blocs[i][2]+=blocs[i][2]-blocs[x][2]
                collision(blocs[i],blocs[x])
                #print("collision  : "+str(w))
                #w+=1

running=True
while running:
    pygame.time.delay(10)
    screen.fill(white)
    pygame.draw.line(screen,black,(0,400),(1000,400))
    for bloc in blocs:
        pygame.draw.rect(screen,bloc[5],[bloc[2],400-bloc[4],bloc[3],bloc[4]])
        update(bloc)
        check_collision(bloc)
    pygame.display.flip()