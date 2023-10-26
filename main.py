
import math
import pygame

pygame.init()
screen = pygame.display.set_mode((700, 700))

white = (255, 255, 255)
black = (0, 0, 0)

# Define a font
font = pygame.font.Font(None, 36)

# Create a text surface
text = font.render("Vyhral si", True, black)

# Get the rectangle for the text surface
text_rect = text.get_rect()
text_rect.center = (400, 300)

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

            # Riadky a stlpce 
            for i in range(3):
                if all(item in kriziky for item in [1+i*3,2+i*3,3+i*3]) or all(item in kruzka for item in [1+i*3,2+i*3,3+i*3]):
                    screen.blit(text, text_rect)
                    pygame.draw.line(screen , "red",(50,150 + i*200),(650,150 +i*200),4)
                    for k in range(10):
                        odpovede.append(k)
                elif all(item in kriziky for item in [1 + i,4+ i,7+ i]) or all(item in kruzka for item in [1 + i,4+ i,7+ i]):
                    pygame.draw.line(screen , "red",(150 + i * 200,50),(150 + i* 200,650),4)
                    for k in range(10):
                        odpovede.append(k)
            # Diagonály 
            if all(item in kriziky for item in [7,5,3]) or all(item in kruzka for item in [7,5,3]):
                pygame.draw.line(screen , "red",(50,650),(650,50),4)
                for k in range(10):
                    odpovede.append(k)
            elif all(item in kriziky for item in [1,5,9]) or all(item in kruzka for item in [1,5,9]):
                pygame.draw.line(screen , "red",(50,50),(650,650),4)
                for k in range(10):
                    odpovede.append(k)
          
            
        
                        
        
    

    pygame.display.flip()




pygame.quit()
