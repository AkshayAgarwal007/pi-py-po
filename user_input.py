import pygame
import sys
from pygame.locals import *
import string



class name:
   name1=''
   name2=''
def get_key(screen,left,top):

  frame=0
  img=pygame.image.load('text.gif')
  img1=pygame.image.load('text2.gif')
  clock=pygame.time.Clock()                    
  FPS=20
  while 1:
    if frame==10:
       screen.blit(img,(left,top))
       pygame.display.update()
    elif frame==20:
       screen.blit(img1,(left,top))
       pygame.display.update()
       frame=0
      
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass
    frame=frame+1

    clock.tick(FPS)
   
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

def inputt(screen):
 
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
 
 z=text_display('ENTER DETAILS',green,70,'Omega Ruby')
 a=text_display('Enter Player1 Name :',red,50,'Arial')
 b=text_display('Enter Player2 Name :',pink,50,'Arial')
 c=text_display(name.name2,white,40,'Arial')
 d=text_display(name.name1,white,40,'Arial')
 e=text_display('The maximum word size of your name can be 8 alphabets. ',white,25,'Times New Roman')
 
 cursor=pygame.image.load('cur116.png')
 cursor= pygame.transform.scale(cursor,(120,120))
 pygame.mouse.set_visible(False)


 SURFACER_a=a.get_rect()
 SURFACER_b=b.get_rect()
 SURFACER_c=c.get_rect()
 SURFACER_d=d.get_rect()
 SURFACER_z=z.get_rect()
 SURFACER_e=e.get_rect()
 
 SURFACER_z.center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/4.7)
 SURFACER_a.center=(SCREEN_WIDTH/3+60,SCREEN_HEIGHT/1.7-130)
 SURFACER_b.center=(SCREEN_WIDTH/3+60,SCREEN_HEIGHT/1.7)
 SURFACER_c.center=(SCREEN_WIDTH/2+110,SCREEN_HEIGHT/1.7-130+3)
 SURFACER_d.center=(SCREEN_WIDTH/2+110,SCREEN_HEIGHT/1.7+3)
 SURFACER_e.center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/1.1)

 background1= pygame.image.load('back.jpg')
 background1= pygame.transform.scale(background1,(1366,768))
 field=1
 current_string=[]


 while True:
    

    
    screen.blit(background1,(0,0))
    

    screen.blit(z,SURFACER_z)
    screen.blit(a,SURFACER_a)
    screen.blit(b,SURFACER_b)
    screen.blit(c,SURFACER_c)
    screen.blit(d,SURFACER_d)
    screen.blit(e,SURFACER_e)

    pygame.display.flip()
    
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
         
        
    if field==1:
       fv=SURFACER_c.left+len(name.name2)*28
       sv=SURFACER_c.top
    elif field==2:
       fv=SURFACER_d.left+len(name.name1)*28
       sv=SURFACER_d.top
                    
    inkey = get_key(screen,fv,sv)
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
      
    elif inkey==pygame.K_ESCAPE:
            name.name1=''
            name.name2=''
            return 0
       
    elif inkey == K_RETURN:
      if field==1 and name.name2!='':
         field=2
         current_string=[]
      elif field==2 and name.name1!='':
         field=3  
    elif inkey == K_MINUS:
      current_string.append("_")
    elif inkey <= 127:

       if field==1 and len(name.name2)<=7:
          
          current_string.append(chr(inkey))
          
       elif field==2 and len(name.name1)<=7:
          
          current_string.append(chr(inkey))

    e=text_display('The maximum word size of your name can be 8 alphabets. ',white,25,'Times New Roman')
 
    yi=string.join(current_string,"")
    yi=yi.upper()
    if field==1:
      name.name2=yi
      if len(name.name2)==8:
         e=text_display('The maximum word size of your name can be 8 alphabets. ',red,25,'Times New Roman')
 
      
    elif field==2:
      name.name1=yi
      if len(name.name1)==8:
        e=text_display('The maximum word size of your name can be 8 alphabets. ',red,25,'Times New Roman')
 
    elif field==3:
      return 1
   
    if field==2:
      a=text_display('Enter Player1 Name :',pink,50,'Arial')
      b=text_display('Enter Player2 Name :',red,50,'Arial')
  
       
      
    c=text_display(name.name2,white,40,'monospace')
    d=text_display(name.name1,white,40,'monospace')
       


   
    


