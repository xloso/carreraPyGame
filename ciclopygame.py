import pygame, sys

width = 640
height = 480

screen = pygame.display.set_mode((width, height))
screen.fill((246, 147, 48))
pygame.display.set_caption("ciclo basico pygame")

pygame.init()

gameOver = False

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    #si no refresco pantalla no se ven los cambios
    pygame.display.update() 
     
pygame.quit()
#aseguramos que salimos si el juego es muy complejo
sys.exit()
    