import pygame
import sys
from helpnew import*
from field import *



class stat:
   loc=1

def text_display(text,color,size,font):
   FONT=pygame.font.SysFont(font,size)
   FONT.set_bold(True)
   SURFACEFONT=FONT.render(text,True,color)
   return SURFACEFONT

'''def rext_display(text,color):
   FONT=pygame.font.SysFont('monospace',15)
   FONT.set_bold(True)
   SURFACEFONT=FONT.render(text,True,color)
   return SURFACEFONT'''

def metro2(screen):
 
 white=(255,255,255)
 red=(191,20,214)
 pink=(239,174,248)

 yellow = (255,255,0)
 green = (0,176,80)
 black=(0,0,0)
 sky=(37,198,255)

 frame=0
 SCREEN_HEIGHT=768
 SCREEN_WIDTH=1366
 size=(SCREEN_WIDTH,SCREEN_HEIGHT)
 
 z=text_display('PI-PY-PO',green,120,'Omega Ruby')
 a=text_display('Start',red,70,'Omega Ruby')
 b=text_display('Help',pink,70,'Omega Ruby')
 c=text_display('Exit',pink,70,'Omega Ruby')
 d=text_display('PiABLE | Pi Accessible Learning Environment',white,25,'Times New Roman')
 
 


 SURFACER_a=a.get_rect()
 SURFACER_b=b.get_rect()
 SURFACER_c=c.get_rect()
 SURFACER_d=d.get_rect()
 SURFACER_z=z.get_rect()
 
 SURFACER_z.center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/4.7)
 SURFACER_a.center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/1.7-130)
 SURFACER_b.center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/1.7)
 SURFACER_c.center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/1.7+130)
 SURFACER_d.center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/1.1)

 background1= pygame.image.load('back.jpg')
 background1= pygame.transform.scale(background1,(1366,768))
 


 while True:
    

    
    screen.blit(background1,(0,0))
    

    screen.blit(z,SURFACER_z)
    screen.blit(a,SURFACER_a)
    screen.blit(b,SURFACER_b)
    screen.blit(c,SURFACER_c)
    screen.blit(d,SURFACER_d)

   
    pos = pygame.mouse.get_pos()
  
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
         
        if event.type==pygame.KEYDOWN:

            if event.key==pygame.K_DOWN:
               stat.loc=stat.loc+1
               if stat.loc==4:
                    stat.loc=1

            if event.key==pygame.K_UP:
               stat.loc=stat.loc-1
               if stat.loc==0:
                    stat.loc=3
            if event.key==pygame.K_RETURN:
                if stat.loc==3:
                    pygame.quit()
                    sys.exit()
                if stat.loc==1:
                    uy=inputt(screen)
                    if uy==0:
                       continue;
                    elif uy==1:
                       return
                    
                    
                
                if stat.loc==2:
                    txt_display(screen)
           
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if SURFACER_c.collidepoint(pos):
                    pygame.quit()
                    sys.exit()
                if SURFACER_a.collidepoint(pos):
                   return
                
                if SURFACER_b.collidepoint(pos):
                    txt_display(screen)
                    
    
    if SURFACER_a.collidepoint(pos):
         stat.loc=1
            
               
    elif SURFACER_b.collidepoint(pos):
         stat.loc=2
         
         
    elif SURFACER_c.collidepoint(pos):
         stat.loc=3
    
               
                
    a=text_display('Start',pink,70,'Omega Ruby')                
    b=text_display('Help',pink,70,'Omega Ruby')
    c=text_display('Exit',pink,70,'Omega Ruby')            
    if stat.loc==1:
        
            a=text_display('Start',red,70,'Omega Ruby')
       
       
    elif stat.loc==2:
            b=text_display('Help',red,70,'Omega Ruby')
        
        
    elif stat.loc==3:
     
            c=text_display('Exit',red,70,'Omega Ruby')
        
        
    pygame.display.flip()
    pygame.display.update()


   
    


