import pygame
pygame.init()
import time
WIDTH=800

HEIGHT=600

TITLE="BIRTHDAY_ANIMATION"

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)


run= True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    b1=pygame.image.load("background.birthday.jpg")
    b1=pygame.transform.scale(b1,(800,600))
    screen.blit(b1,(0,0))
    font=pygame.font.SysFont("Arial",40)
    message1=font.render("Happy Birthday", True,"black")
    screen.blit(message1,(280,300))
    pygame.display.update()
    time.sleep(5)
    
    cake=pygame.image.load("birthday_cake.jpg")
    cake=pygame.transform.scale(cake,(800,600))
    screen.blit(cake,(0,0))
    font=pygame.font.SysFont("Arial",40)
    message2=font.render("Have a nice day", True,"black")
    screen.blit(message2,(280,50))
    pygame.display.update()
    time.sleep(5)

    present=pygame.image.load("present.jpg")
    present=pygame.transform.scale(present,(800,600))
    screen.blit(present,(0,0))
    font=pygame.font.SysFont("Arial",40)
    message3=font.render("Hope you get lots of presents",True, "black")
    screen.blit(message3,(150,50))
    pygame.display.update()
    time.sleep(5)




    

    

    
    
    pygame.display.update()

    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

            
    pygame.display.update()