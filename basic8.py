import pygame 
import random
import sys 
from pygame.locals import *
import time 
pygame.mixer.init()
white=(255,255,255)
fps=32
x=pygame.init()
w1=380
h1=550
gndx1=0
gndy1=475
birdx1=50
birdy1=205
gnd_width=380
point=0
font=pygame.font.SysFont(None,55)

window=pygame.display.set_mode((w1,h1))
pygame.display.set_caption("Flappy Bird")
begin=pygame.image.load("flappy_back.png")
begin=pygame.transform.scale(begin,(w1,h1)).convert_alpha()
base=pygame.image.load("flappy_base.png").convert_alpha()
pipe_low=pygame.image.load("flappy_pipe.png").convert_alpha()
pipe_up=pygame.transform.rotate(pipe_low,180)
bird=[]
bird.append(pygame.image.load("flappy_birddown.png").convert_alpha())
bird.append(pygame.image.load("flappy_birdup.png").convert_alpha())
pipes=[]
clock = pygame.time.Clock()
fps=100
imagecounter=0
imagedisplay=0
def start_game():
    
    global gndx1,gndy1,birdx1,birdy1,gnd_width,pipes,point
    exit_game=False 
    gndx1=0
    gndy1=475
    birdx1=50
    birdy1=205
    gnd_width=380
    point=0 
    pipes=[]
    begin1={}
    begin1['start']=pygame.image.load("fluppy_start.jpg").convert_alpha()
    while  exit_game==False:
        window.fill(white)
        window.blit(begin1['start'],(0,0))
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.QUIT
                    quit()
                if event.type==pygame.KEYDOWN:
                     if event.key==pygame.K_RETURN:
                          return
        pygame.display.update()
def update_ground():
     global gnd_width,gndx1,gndy1
     gnd_width-=1
     gndx1-=1
     window.blit(base,(gndx1+375,gndy1))
     if(gnd_width<0):
          gndx1=0
          gnd_width=380


def update_pipe():
     global pipes  
     if(len(pipes)>3):
          for i in range(len(pipes)-3):
               if(pipes[i][0][0]<1):
                    del pipes[i]
               else:
                    pipes[i][0][0]-=0.02
                    pipes[i][1][0]-=0.02
          
     return pipes
def draw_pipe():
     global pipes
     for i in range(len(pipes)):
          x1=int(pipes[i][0][0])
          y1=int(pipes[i][0][1])
          x2=int(pipes[i][1][0])
          y2=int(pipes[i][1][1])
          rect_up=pipes[0][0]
          rect_down=pipes[0][1]
          window.blit(pipe_up,(x1,y1))
          window.blit(pipe_low,(x2,y2))
          
     
          
def add_pipe():
     rect_up=pipe_up.get_rect()
     rect_down=pipe_low.get_rect()
     rect_up.y=random.randint(260,380)
     rect_up.x=380
     rect_down.x=380
     rect_down.y=rect_up.y-95-rect_up.height
     return(rect_up,rect_down)
def update_bird():
     global birdx1,birdy1,imagecounter,imagedisplay
     if imagecounter==1:
         window.blit(bird[imagedisplay],(birdx1,birdy1))
         imagecounter=0
         if imagedisplay==0:
              imagedisplay=1
         else:
              imagedisplay=0
     birdy1+=1.15
     imagecounter+=1
def play_point():
     global point
     pygame.mixer.music.load("point.mp3")
     pygame.mixer.music.play()
     point+=1
     
     
def collision():

    pipeh=pipe_low.get_rect()
    if(len(pipes)>1):
        if((int(birdy1)<=int(pipes[0][1][1])+pipeh.height) and (birdx1-pipes[0][1][0])>-25) :
             return True
        elif(int(birdy1)>=int(pipes[0][0][1]) and (birdx1-pipes[0][0][0])>-25):
                return True
        elif(int(birdy1)>=gndy1):
            return True
        else:
             if(birdx1-pipes[0][0][0]>40):
               play_point()
               return False

def main_game():
    start_game=False
    counter=180
    global birdy1
    global pipes
    while  start_game==False:
        window.fill(white)
        window.blit(begin,(0,0))
        screen_text=font.render(str(point),True,white)
        window.blit(screen_text,(150,150))

        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.QUIT
                    quit()
                if event.type==pygame.KEYDOWN:
                     if event.key==pygame.K_RETURN:
                          return
                     elif event.key==pygame.K_SPACE or K_UP:
                          birdy1-=50
                          pygame.mixer.music.load("flap.mp3")        
                          pygame.mixer.music.play()
                          if(birdy1<0):
                               birdy1=0
        
        if counter>180:
             pipes.append(add_pipe())
             counter=0
        counter+=1
        draw_pipe()
        pipes=update_pipe()
        window.blit(base,(gndx1,gndy1))
        update_ground()
        update_bird()
        if(collision()):
             start_game=True        
        pygame.display.update()
        clock.tick(fps)


def end_game():
     global birdy1
     end=False
     pygame.mixer.music.load("die.mp3")
     pygame.mixer.music.play()
     while not end:
          if(birdy1<465):
               window.fill(white)
               window.blit(begin,(0,0))
               draw_pipe()
               window.blit(base,(gndx1,gndy1))
               window.blit(base,(gndx1+375,gndy1))
               window.blit(bird[1],(birdx1,birdy1))
               screen_text=font.render(str(point),True,white)
               window.blit(screen_text,(150,150))
               birdy1+=1
          else: 
               end=True
          pygame.display.update()
     pygame.mixer.music.load("hit.mp3")
     pygame.mixer.music.play() 
     
     


while True:
     start_game()
     main_game()
     end_game()

 