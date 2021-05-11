import pygame 
import sys 
  
pygame.init() 
   
res = (1920,1080)  
screen = pygame.display.set_mode(res) 
   
color = (255,255,255) 
color_light = (170,170,170) 
color_dark = (100,100,100) 
  
width = screen.get_width() 
height = screen.get_height() 
  
fond_combat = pygame.image.load('fond.jpg')
screen.blit(fond_combat , (0, 0))

smallfont = pygame.font.SysFont('Corbel',35) 

def Texte(texte) :
    text = smallfont.render(texte , True , color) 
    return text
  
while True: 
      
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
              
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            if 720 <= mouse[0] <= 720+480 and 180 <= mouse[1] <= 180+72: 
                print("mot 1")
            if 720 <= mouse[0] <= 720+480 and 252 <= mouse[1] <= 252+72: 
                print("mot 2")
            if 720 <= mouse[0] <= 720+480 and 324 <= mouse[1] <= 324+72: 
                print("mot 3")
            if 720 <= mouse[0] <= 720+480 and 396 <= mouse[1] <= 396+72:
                print("mot 4")
            if 720 <= mouse[0] <= 720+480 and 468 <= mouse[1] <= 468+72: 
                print("mot 5")
            if 720 <= mouse[0] <= 720+480 and 540 <= mouse[1] <= 540+72: 
                print("mot 6")
            if 720 <= mouse[0] <= 720+480 and 612 <= mouse[1] <= 612+72: 
                print("mot 7")
            if 720 <= mouse[0] <= 720+480 and 684 <= mouse[1] <= 684+72: 
                print("mot 8")
            if 720 <= mouse[0] <= 720+480 and 756 <= mouse[1] <= 756+72: 
                print("mot 9")
            if 720 <= mouse[0] <= 720+480 and 828 <= mouse[1] <= 828+72: 
                print("mot 10")
      
    mouse = pygame.mouse.get_pos() 
    
    pygame.draw.rect(screen,color_dark,[81,64,240,60]) #Nom 1
    pygame.draw.rect(screen,color_dark,[81,180,472,835]) #Sprite 1

    pygame.draw.rect(screen,color_dark,[1599,64,240,60]) #Nom 2
    pygame.draw.rect(screen,color_dark,[1367,180,472,835]) #Sprite 2

    #Tableau Mot

    if 720 <= mouse[0] <= 720+480 and 180 <= mouse[1] <= 180+72: 
        pygame.draw.rect(screen,color_light,[720,180,480,72]) 
    else : pygame.draw.rect(screen,color_dark,[720,180,480,72]) #Mot 1

    if 720 <= mouse[0] <= 720+480 and 252 <= mouse[1] <= 252+72: 
        pygame.draw.rect(screen,color_light,[720,252,480,72]) 
    else : pygame.draw.rect(screen,color_dark,[720,252,480,72]) #Mot 2

    if 720 <= mouse[0] <= 720+480 and 324 <= mouse[1] <= 324+72: 
        pygame.draw.rect(screen,color_light,[720,324,480,72])     
    else : pygame.draw.rect(screen,color_dark,[720,324,480,72]) #Mot 3

    if 720 <= mouse[0] <= 720+480 and 396 <= mouse[1] <= 396+72: 
        pygame.draw.rect(screen,color_light,[720,396,480,72]) 
    else : pygame.draw.rect(screen,color_dark,[720,396,480,72]) #Mot 4

    if 720 <= mouse[0] <= 720+480 and 468 <= mouse[1] <= 468+72: 
        pygame.draw.rect(screen,color_light,[720,468,480,72]) 
    else : pygame.draw.rect(screen,color_dark,[720,468,480,72]) #Mot 5

    if 720 <= mouse[0] <= 720+480 and 540 <= mouse[1] <= 540+72: 
        pygame.draw.rect(screen,color_light,[720,540,480,72]) 
    else : pygame.draw.rect(screen,color_dark,[720,540,480,72]) #Mot 6

    if 720 <= mouse[0] <= 720+480 and 612 <= mouse[1] <= 612+72: 
        pygame.draw.rect(screen,color_light,[720,612,480,72]) 
    else : pygame.draw.rect(screen,color_dark,[720,612,480,72]) #Mot 7

    if 720 <= mouse[0] <= 720+480 and 684 <= mouse[1] <= 684+72: 
        pygame.draw.rect(screen,color_light,[720,684,480,72]) 
    else : pygame.draw.rect(screen,color_dark,[720,684,480,72]) #Mot 8

    if 720 <= mouse[0] <= 720+480 and 756 <= mouse[1] <= 756+72: 
        pygame.draw.rect(screen,color_light,[720,756,480,72]) 
    else : pygame.draw.rect(screen,color_dark,[720,756,480,72]) #Mot 9

    if 720 <= mouse[0] <= 720+480 and 828 <= mouse[1] <= 828+72: 
        pygame.draw.rect(screen,color_light,[720,828,480,72]) 
    else : pygame.draw.rect(screen,color_dark,[720,828,480,72]) #Mot 10


    if 840 <= mouse[0] <= 840+240 and 955 <= mouse[1] <= 955+60: 
        pygame.draw.rect(screen,color_light,[840,955,240,60]) 
    else : pygame.draw.rect(screen,color_dark,[840,955,240,60]) #Bouton finir phrase


    # Texte
    screen.blit(Texte("Nom 1") , (81, 64)) #Nom 1
    screen.blit(Texte("Nom 2") , (1599, 64)) #Nom 2

    screen.blit(Texte("Mot 1") , (720, 180)) #Mot 1
    screen.blit(Texte("Mot 2") , (720, 252)) #Mot 2
    screen.blit(Texte("Mot 3") , (720, 324)) #Mot 3
    screen.blit(Texte("Mot 4") , (720, 396)) #Mot 4
    screen.blit(Texte("Mot 5") , (720, 468)) #Mot 5
    screen.blit(Texte("Mot 6") , (720, 540)) #Mot 6
    screen.blit(Texte("Mot 7") , (720, 612)) #Mot 7
    screen.blit(Texte("Mot 8") , (720, 684)) #Mot 8
    screen.blit(Texte("Mot 9") , (720, 756)) #Mot 9
    screen.blit(Texte("Mot 10") , (720, 828)) #Mot 10

    screen.blit(Texte("Finir phrase"), (840, 955)) #Finir phrase
      
    # updates the frames of the game 
    pygame.display.update() 