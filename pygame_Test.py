import pygame
import sys

pygame.init()
hintergrund = pygame.image.load("Grafiken/hintergrund.png")
screen=pygame.display.set_mode([1200,595])
clock=pygame.time.Clock()
pygame.display.set_caption("Pygame_Tutorial")



def zeichen():
    screen.blit(hintergrund, (0,0))
    pygame.draw.rect(screen, (0, 0, 255), (x,y,breite, hoehe))
    pygame.display.update()



x=300
y=440.0
geschw=5
breite=40
hoehe=80

linkeWand = pygame.draw.rect(screen, (0,0,0,), (-1,0,2,600), 0)

rechteWand = pygame.draw.rect(screen, (0,0,0,), (1199,0,2,600), 0)




go =True

sprungVar = -16
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    spielerRechteck = pygame.Rect(x,y, 40,80)
    gedrueckt = pygame.key.get_pressed()

    if gedrueckt[pygame.K_UP]and sprungVar == -16:
       sprungVar = 15
    
    if gedrueckt[pygame.K_RIGHT] and not spielerRechteck.colliderect(rechteWand):
        x += geschw
    
    #if gedrueckt[pygame.K_DOWN]:
     #   y += geschw
    
    if gedrueckt[pygame.K_LEFT]and not spielerRechteck.colliderect(linkeWand):
        x -= geschw

    if sprungVar >= -15.0:
        n = 1.0
        if sprungVar < 0:
            n=-1.0
        y -= (sprungVar**2)*0.17*n
        sprungVar -=1

    zeichen()
    
    clock.tick(120)
