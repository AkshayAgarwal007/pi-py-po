

#------Importing modules---------#

import pygame
import sys
import time
import pygame.mixer
from pygame.locals import*
import random
from field import *
from main2 import *
from win import *

#------Screen size & other parameters--------------#

pygame.init()

 
SCREEN_HEIGHT=768
SCREEN_WIDTH=1366

size=(SCREEN_WIDTH,SCREEN_HEIGHT)



screen=pygame.display.set_mode((size),pygame.FULLSCREEN)

pygame.display.set_caption('TIC-TAC-TOE')

#--------function to obtain text----------------#
 
def text_display(text,color,size,font):
   FONT=pygame.font.SysFont(font,size)
   FONT.set_bold(True)
   SURFACEFONT=FONT.render(text,True,color)
   return SURFACEFONT





metro2(screen)                    #start screen

pygame.mouse.set_visible(True)

clr1=(22,122,211)                  #colors
clr2=(255,44,166)
clr3=(34,55,145)

red=(255,0,0)
white=(255,255,255)

p1,p2=0,0


text1=text_display(name.name1,white,30,'Arial')   
text2=text_display(name.name2,white,30,'Arial')
text3=text_display('%s-%s'%(p1,p2),white,50,'Arial')
text4=text_display('Press ESC To Return',white,30,'Arial')



text1_a=text1.get_rect()
text2_b=text2.get_rect()
text3_b=text3.get_rect()
text4_b=text3.get_rect()


FONT=pygame.font.SysFont('Arial',30)
FONT.set_bold(True)
u=FONT.size(name.name1)
text1_a.top=25
text1_a.left=SCREEN_WIDTH-88-u[0]-10
text2_b.top=25
text2_b.left=88+10
text3_b.center=(SCREEN_WIDTH/2,40)
text4_b.center=(SCREEN_WIDTH-265,750)
 
clock=pygame.time.Clock()                    
FPS=60
total_frames=0
width=260
height=195
xleft=300
ytop=110
turn=0
stat_of_turn=random.randint(1,2)
noft=0

list1=['0','0','0','0','0','0','0','0','0']
background1=pygame.image.load('back.jpg')

t=pygame.image.load('cross.gif')
r=pygame.image.load('cross2.gif')
q=pygame.image.load('circle2.gif')
p=pygame.image.load('circle.gif')
friend1=pygame.image.load('friend1.gif')
friend2=pygame.image.load('friend2.gif')
you=pygame.image.load('you.gif')

text5=text_display('Player %s wins'%(stat_of_turn),white,30,'Arial')
text5_b=text3.get_rect()
text5_b.center=(50,750)
wintext=''



while True:

   
    
    
    if p1==p2:
       wintext='Game Draw'
    elif p1>p2:
       wintext=name.name2+' Wins'
    elif p2>p1:
       wintext=name.name1+' Wins'
       
       
    a=pygame.draw.rect(screen,white,(xleft,ytop,width,height))
    b=pygame.draw.rect(screen,white,(xleft+width,ytop,width,height))
    c=pygame.draw.rect(screen,white,(xleft+width*2,ytop,width,height))
    d=pygame.draw.rect(screen,white,(xleft,ytop+height,width,height))
    e=pygame.draw.rect(screen,white,(xleft+width,ytop+height,width,height))
    f=pygame.draw.rect(screen,white,(xleft+width*2,ytop+height,width,height))
    g=pygame.draw.rect(screen,white,(xleft,ytop+height*2,width,height))
    h=pygame.draw.rect(screen,white,(xleft+width,ytop+height*2,width,height))
    i=pygame.draw.rect(screen,white,(xleft+width*2,ytop+height*2,width,height))

    screen.blit(background1,(0,0))
   

    if stat_of_turn==1:
       screen.blit(you,(SCREEN_WIDTH-88,0))
       screen.blit(friend1,(0,0))
       screen.blit(text1,text1_a)
       screen.blit(text3,text3_b)
       screen.blit(text2,text2_b)
    elif stat_of_turn==2:
        screen.blit(friend2,(0,0))
        screen.blit(friend1,(SCREEN_WIDTH-88,0))
        screen.blit(text2,text2_b)
        screen.blit(text3,text3_b)
        screen.blit(text1,text1_a)

    pygame.draw.line(screen, white, (xleft,ytop+height), (xleft+width*3,ytop+height),5)
                     
    pygame.draw.line(screen, white, (xleft,ytop+height*2), (xleft+width*3,ytop+height*2),5)
    
    pygame.draw.line(screen, white, (xleft+width,ytop), (xleft+width,ytop+height*3),5)
    
    pygame.draw.line(screen, white, (xleft+width*2,ytop), (xleft+width*2,ytop+height*3),5)
    
    screen.blit(text4,text4_b)
    pos = pygame.mouse.get_pos()
   

    if stat_of_turn==1:
      text5=text_display('%s wins'%(name.name2),white,30,'Arial')
      
    else:
      text5=text_display('%s wins'%(name.name1),white,30,'Arial')
       
    
    if(list1[0]==list1[1]==list1[2]) and list1[0]!='0': 

       if stat_of_turn==1:
          p1=p1+1
          
       elif stat_of_turn==2:
          p2=p2+1
      
       if list1[1]=='1':
        x=screen.blit(r,a)
        y=screen.blit(r,b)
        z=screen.blit(r,c)

       elif list1[1]=='2':
        x=screen.blit(q,a)
        y=screen.blit(q,b)
        z=screen.blit(q,c)
      
       pygame.display.update(x)
       pygame.display.update(y)
       pygame.display.update(z)

       qw=screen.blit(text5,text5_b)
       pygame.display.update(qw)
      
  
       time.sleep(2)
       
       
       list1=['0','0','0','0','0','0','0','0','0']
       stat_of_turn=random.randint(1,2)
       noft=0
       
       continue;
       
       
       
    elif(list1[0]==list1[3]==list1[6]) and list1[0]!='0':

       if stat_of_turn==1:
          p1=p1+1
       elif stat_of_turn==2:
          p2=p2+1

      
       if list1[0]=='1':
        x=screen.blit(r,a)
        y=screen.blit(r,d)
        z=screen.blit(r,g)

       elif list1[0]=='2':
        x=screen.blit(q,a)
        y=screen.blit(q,d)
        z=screen.blit(q,g)
       pygame.display.update(x)
       pygame.display.update(y)
       pygame.display.update(z)
       qw=screen.blit(text5,text5_b)
       pygame.display.update(qw)
       
       time.sleep(2)
       
       list1=['0','0','0','0','0','0','0','0','0']
       stat_of_turn=random.randint(1,2)
       noft=0
       
       continue;

   
    elif(list1[0]==list1[4]==list1[8]) and list1[0]!='0':       

       if stat_of_turn==1:
          p1=p1+1
       elif stat_of_turn==2:
          p2=p2+1
       
       
      
       if list1[0]=='1':
        x=screen.blit(r,a)
        y=screen.blit(r,e)
        z=screen.blit(r,i)

       elif list1[0]=='2':
        x=screen.blit(q,a)
        y=screen.blit(q,e)
        z=screen.blit(q,i)
       pygame.display.update(x)
       pygame.display.update(y)
       pygame.display.update(z)
       qw=screen.blit(text5,text5_b)
       pygame.display.update(qw)
       
       time.sleep(2)
       list1=['0','0','0','0','0','0','0','0','0']
       stat_of_turn=random.randint(1,2)
       noft=0
       continue;
       
     
    elif(list1[6]==list1[7]==list1[8]) and list1[8]!='0': 
       
       if stat_of_turn==1:
          p1=p1+1
       elif stat_of_turn==2:
          p2=p2+1
       
       if list1[6]=='1':
        x=screen.blit(r,g)
        y=screen.blit(r,h)
        z=screen.blit(r,i)

       elif list1[6]=='2':
        x=screen.blit(q,g)
        y=screen.blit(q,h)
        z=screen.blit(q,i)
       pygame.display.update(x)
       pygame.display.update(y)
       pygame.display.update(z)
       qw=screen.blit(text5,text5_b)
       pygame.display.update(qw)
       
       time.sleep(2)

       list1=['0','0','0','0','0','0','0','0','0']
       stat_of_turn=random.randint(1,2)
       noft=0
       
       continue;
    elif(list1[2]==list1[5]==list1[8]) and list1[8]!='0':
       
       if stat_of_turn==1:
          p1=p1+1
       elif stat_of_turn==2:
          p2=p2+1
       

      
       if list1[2]=='1':
        x=screen.blit(r,c)
        y=screen.blit(r,f)
        z=screen.blit(r,i)

       elif list1[2]=='2':
        x=screen.blit(q,c)
        y=screen.blit(q,f)
        z=screen.blit(q,i)
        
       pygame.display.update(x)
       pygame.display.update(y)
       pygame.display.update(z)
       qw=screen.blit(text5,text5_b)
       pygame.display.update(qw)
       time.sleep(2)
       list1=['0','0','0','0','0','0','0','0','0']
       stat_of_turn=random.randint(1,2)
       noft=0
       
       continue;

    elif(list1[6]==list1[4]==list1[2]) and list1[6]!='0':
       
       if stat_of_turn==1:
          p1=p1+1
       elif stat_of_turn==2:
          p2=p2+1
       


       if list1[6]=='1':
        x=screen.blit(r,c)
        y=screen.blit(r,e)
        z=screen.blit(r,g)

       elif list1[6]=='2':
        x=screen.blit(q,c)
        y=screen.blit(q,e)
        z=screen.blit(q,g)
       pygame.display.update(x)
       pygame.display.update(y)
       pygame.display.update(z)
       qw=screen.blit(text5,text5_b)
       pygame.display.update(qw)
       
       time.sleep(2)
       list1=['0','0','0','0','0','0','0','0','0']
       stat_of_turn=random.randint(1,2)
       noft=0
       
       continue;
      
    elif(list1[3]==list1[4]==list1[5]) and list1[3]!='0':
       
       if stat_of_turn==1:
          p1=p1+1
       elif stat_of_turn==2:
          p2=p2+1
       
      
       if list1[3]=='1':
        x=screen.blit(r,d)
        y=screen.blit(r,e)
        z=screen.blit(r,f)

       elif list1[3]=='2':
        x=screen.blit(q,d)
        y=screen.blit(q,e)
        z=screen.blit(q,f)
       pygame.display.update(x)
       pygame.display.update(y)
       pygame.display.update(z)
       qw=screen.blit(text5,text5_b)
       pygame.display.update(qw)
       
       
       time.sleep(2)

       list1=['0','0','0','0','0','0','0','0','0']
       stat_of_turn=random.randint(1,2)
       noft=0
       
       continue;
      
    elif(list1[1]==list1[4]==list1[7]) and list1[1]!='0':
       
       if stat_of_turn==1:
          p1=p1+1
       elif stat_of_turn==2:
          p2=p2+1
       

      
       if list1[1]=='1':
        x=screen.blit(r,b)
        y=screen.blit(r,e)
        z=screen.blit(r,h)

       elif list1[1]=='2':
        x=screen.blit(q,b)
        y=screen.blit(q,e)
        z=screen.blit(q,h)
       pygame.display.update(x)
       pygame.display.update(y)
       pygame.display.update(z)
       qw=screen.blit(text5,text5_b)
       pygame.display.update(qw)
       time.sleep(2)
       list1=['0','0','0','0','0','0','0','0','0']
       stat_of_turn=random.randint(1,2)
       noft=0
       
       continue;

    if noft==9:
       list1=['0','0','0','0','0','0','0','0','0']
       stat_of_turn=random.randint(1,2)
       noft=0
       
       continue;
    
   
    
    text3=text_display('%s - %s'%(p1,p2),white,50,'Arial')
    
    

    

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type==pygame.KEYDOWN:

            if event.key==pygame.K_ESCAPE:
               list1=['0','0','0','0','0','0','0','0','0']
               stat_of_turn=random.randint(1,2)
               noft=0
               name.name1=''
               name.name2=''
               p1=0
               p2=0
               win(screen,wintext)
               metro2(screen)
               text1=text_display(name.name1,white,30,'Arial')   
               text2=text_display(name.name2,white,30,'Arial')
               FONT=pygame.font.SysFont('Arial',30)
               FONT.set_bold(True)
               u=FONT.size(name.name1)
               text1_a.top=25
               text1_a.left=SCREEN_WIDTH-88-u[0]-10
               pygame.mouse.set_visible(True)
               continue;
            
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
              
                   
                if a.collidepoint(pos) and list1[0]=='0':
                   
                   if stat_of_turn==2:
                      stat_of_turn=1
                      list1[0]='2'
                   elif stat_of_turn==1:
                      stat_of_turn=2
                      list1[0]='1'
                   noft=noft+1
                if b.collidepoint(pos)and list1[1]=='0':
                   
                   if stat_of_turn==2:
                      stat_of_turn=1
                      list1[1]='2'
                   elif stat_of_turn==1:
                      stat_of_turn=2
                      list1[1]='1'
                   noft=noft+1
                if c.collidepoint(pos)and list1[2]=='0':
                   
                   if stat_of_turn==2:
                      stat_of_turn=1
                      list1[2]='2'
                   elif stat_of_turn==1:
                      stat_of_turn=2
                      list1[2]='1'
                   noft=noft+1
                if d.collidepoint(pos)and list1[3]=='0':
                   
                   if stat_of_turn==2:
                      stat_of_turn=1
                      list1[3]='2'
                   elif stat_of_turn==1:
                      stat_of_turn=2
                      list1[3]='1'
                   noft=noft+1
                if e.collidepoint(pos)and list1[4]=='0':
                   
                   if stat_of_turn==2:
                      stat_of_turn=1
                      list1[4]='2'
                   elif stat_of_turn==1:
                      stat_of_turn=2
                      list1[4]='1'
                   noft=noft+1
                if f.collidepoint(pos)and list1[5]=='0':
                   
                   if stat_of_turn==2:
                      stat_of_turn=1
                      list1[5]='2'
                   elif stat_of_turn==1:
                      stat_of_turn=2
                      list1[5]='1'
                   noft=noft+1
                if g.collidepoint(pos)and list1[6]=='0':
                   
                   if stat_of_turn==2:
                      stat_of_turn=1
                      list1[6]='2'
                   elif stat_of_turn==1:
                      stat_of_turn=2
                      list1[6]='1'
                   noft=noft+1
                if h.collidepoint(pos)and list1[7]=='0':
                   
                   if stat_of_turn==2:
                      stat_of_turn=1
                      list1[7]='2'
                   elif stat_of_turn==1:
                      stat_of_turn=2
                      list1[7]='1'
                   noft=noft+1
                if i.collidepoint(pos)and list1[8]=='0':
                   
                   if stat_of_turn==2:
                      stat_of_turn=1
                      list1[8]='2'
                   elif stat_of_turn==1:
                      stat_of_turn=2
                      list1[8]='1'
                   noft=noft+1
    if list1[0]=='1':
       screen.blit(t,a)
    elif list1[0]=='2':
       screen.blit(p,a)
    if list1[1]=='1':
       screen.blit(t,b)
    elif list1[1]=='2':
       screen.blit(p,b)
    if list1[2]=='1':
       screen.blit(t,c)
    elif list1[2]=='2':
       screen.blit(p,c)
    if list1[3]=='1':
       screen.blit(t,d)
    elif list1[3]=='2':
       screen.blit(p,d)
    if list1[4]=='1':
       screen.blit(t,e)
    elif list1[4]=='2':
       screen.blit(p,e)
    if list1[5]=='1':
       screen.blit(t,f)
    elif list1[5]=='2':
       screen.blit(p,f)
    if list1[6]=='1':
       screen.blit(t,g)
    elif list1[6]=='2':
       screen.blit(p,g)
    if list1[7]=='1':
       screen.blit(t,h)
    elif list1[7]=='2':
       screen.blit(p,h)
    if list1[8]=='1':
       screen.blit(t,i)
    elif list1[8]=='2':
       screen.blit(p,i)
     
    z=0
    pygame.display.flip()
    clock.tick(FPS)





    
