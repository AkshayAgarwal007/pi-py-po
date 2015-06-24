import pygame
import sys
from pygame.locals import*





def text_display(text,color,size):
   FONT=pygame.font.SysFont('monospace',size)
   FONT.set_bold(True)
   SURFACEFONT=FONT.render(text,True,color)
   return SURFACEFONT


def win(screen,name):
  white=(255,255,255)
  red=(255,0,0)
  green=(0,255,0)
  x,y,z=255,0,0
  clr=(x,y,z)
  SCREEN_HEIGHT=768
  SCREEN_WIDTH=1366

  

  a=text_display(name,clr,110)

  d=text_display('Press ESC To Return',white,30)

  SURFACER_a=a.get_rect()

  SURFACER_a.center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
  SURFACER_d=d.get_rect() 
  SURFACER_d.center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/1.1)
 
  background1=pygame.image.load('back.jpg')

  


  while True:
 
    screen.blit(background1,(0,0))
    screen.blit(a,SURFACER_a)
    screen.blit(d,SURFACER_d)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
      
        if event.type==pygame.KEYDOWN:

            if event.key==K_ESCAPE:
                
                return
    z+=1
    clr=(x,y,z)
    
    if z==255:
        z=0
    a=text_display(name,clr,110)
        
    
    pygame.display.update()




