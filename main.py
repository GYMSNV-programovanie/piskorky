import tkinter as tk
import math
import pygame

pygame.init()
screen = pygame.display.set_mode((700, 700))

screen.fill("white")
def siet()->None:
        x1, y1 = 250,50
        x2, y2 = 50,250
        velkost_stvorceka= 200
       


        for i in range(2):
            pygame.draw.line(screen,(0,0,0), (x1,y1),(x1, y1+600),1 )
            x1+=velkost_stvorceka
            pygame.draw.line(screen,(0,0,0), (x2,y2),(x2+600, y2),1 )
            y2+=velkost_stvorceka

siet()

rad = 0
kruzka,kriziky,odpovede= [],[],[] 





running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            (x,y) = pygame.mouse.get_pos()
            x= math.floor(x/200)*200
            y= math.floor(y/200)*200  
            print(y)

            

            if y == 0:
                policko = x/200 + 1
            elif y / 200 == 1:
                policko = x/200 + 4
            elif y/200 == 2 :
                policko = x/200 + 7
            

            if rad %2== 0 and policko not in odpovede:
               pygame.draw.ellipse(screen,"green", (x+70,y+70,150,150),4 )
               rad= rad + 1
               kruzka.append(policko)
            elif rad %2== 1 and policko not in odpovede:
               pygame.draw.line(screen,"blue", (x+70,y+70),(x+220,y+220),4 )
               pygame.draw.line(screen,"blue", (x+70,y+220),(x+220,y+70),4 )
               rad= rad + 1
               kriziky.append(policko)
                    
            odpovede = kruzka + kriziky
            odpovede.sort()

           
            if all(item in kriziky for item in [1,2,3]) or all(item in kruzka for item in [1,2,3]):
                pygame.draw.line(screen , "red",(50,150),(650,150),4)
                break
            elif all(item in kriziky for item in [4,5,6]) or all(item in kruzka for item in [4,5,6]):
                pygame.draw.line(screen , "red",(50,350),(650,350),4)
            elif all(item in kriziky for item in [7,8,9]) or all(item in kruzka for item in [7,8,9]):
                pygame.draw.line(screen , "red",(50,550),(650,550),4)
            elif all(item in kriziky for item in [7,5,3]) or all(item in kruzka for item in [7,5,3]):
                pygame.draw.line(screen , "red",(50,650),(650,50),4)
            elif all(item in kriziky for item in [1,5,9]) or all(item in kruzka for item in [1,5,9]):
                pygame.draw.line(screen , "red",(50,50),(650,650),4)
            elif all(item in kriziky for item in [1,4,7]) or all(item in kruzka for item in [1,4,7]):
                pygame.draw.line(screen , "red",(150,50),(150,650),4)
            elif all(item in kriziky for item in [2,5,8]) or all(item in kruzka for item in [2,5,8]):
                pygame.draw.line(screen , "red",(350,50),(350,650),4)
            elif all(item in kriziky for item in [3,6,9]) or all(item in kruzka for item in [3,6,9]):
                pygame.draw.line(screen , "red",(550,50),(550,650),4)
            
            
        
                        
        
    

    pygame.display.flip()




pygame.quit()
