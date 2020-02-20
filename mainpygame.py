import pygame, sys


class Game():
    runners = []
    __starLine = 20
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load("assets/Picture1.jpg")
        pygame.display.set_caption("Carrera de Bichos")


    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
            #esto actualiza la pantalla pero no la refresca
            self.__screen.blit(self.__background, (0,0))
            #si no refresco pantalla no se ven los cambios
            #pygame.display.flip() también refresca
            pygame.display.update()
            
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = Game()
    pygame.init()
    game.competir()