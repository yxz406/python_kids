import pygame, sys
import math
pygame.init()
secreen = pygame.display.set_mode([640, 480])
secreen.fill([255, 255,255])
for x in range(0,640):
    y = int(math.sin(x/640*4*math.pi)*200+240)
    pygame.draw.rect(secreen,[0,0,0],[x,y,1,1],1)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()