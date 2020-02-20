import pygame
import sys

class runner():
    pass

class Game():
    
    corredores = []
    
    def __init__(self):
        #definicion pantalla
        self.__screen = pygame.display.set_mode((640, 480))
        #nombre de la pantalla
        pygame.display.set_caption("Carrera de bichos") 
        self.background = pygame.image.load("Picture1.jpg")
        
        self.runner = pygame.image.load('Tulipanes.jpg')
        
        
    def competir(self):
        
        x = 0
        hayGanador = False
        
        while not hayGanador:
#comprobacion de eventos en pygame, esto hay que hacerlo en pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    #paygame.quit no siempre funciona
                    #por eso ponemos esto
                    sys.exit() 
            
            #refrescar / renderizar la pantalla        
            self.__screen.blit(self.background, (0, 0))
            self.__screen.blit(self.runner, (x, 240))
            #hay que refrescar la memoria en pygame
            pygame.display.flip()
            
            x += 3
            if x >= 250:
                hayGanador == True
                
        pygame.quit()
        sys.exit() 
                    

if __name__ == '__main__':
    #en pygame hay que lanzarlo
    pygame.init() 
    game = Game()
    game.competir()
 
    
