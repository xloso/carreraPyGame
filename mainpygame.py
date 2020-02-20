import pygame, sys
import random

class Runner():
    __customes = ('runner', 'runner1', 'runner2', 'runner3')
    
#dibujar corredor y moverlo por pantalla
#va a tener 2 metodos. el de la posicion, nombre, imagen y
# el del movimiento que se llama avanzar
    def __init__(self, x=0, y=0, custome = 'runner'):
        self.custome = pygame.image.load("assets/{}.png".format(custome))
        self.position = [x, y]
        self.name = custome
    
    def avanzar(self):
        #movemos por el eje X, por eso usamos la posicion 0
        self.position[0] += random.randint(1, 5)
    
    
    

class Game():
    runners = []
    __posY = (160, 200, 240, 280)
    __names = ('alonso', 'carlos', 'Speedy', 'Leo')
    __startLine = 5
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load("assets/Picture1.jpg")
        pygame.display.set_caption("Carrera de Bichos")
        
        #creo los corredores
        for i in range(4):
            theRunner = Runner(self.__startLine, self.__posY[i])
            theRunner.name = self.__names[i]
            self.runners.append(theRunner)
        #ahora tengo que dibujar el corredor
        #eso lo hago en competir
        
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True

#las variables que no llevan el self solo están activas en cada
#fucnion o "def"
#las self son propias de la clase.

            for runner in self.runners:
                runner.avanzar()
            #comprobar cuando llega a meta
                if runner.position >= self.__finishLine:
                    print("{} ha ganado".format(runner.name))
                    gameOver = True
            #esto actualiza la pantalla pero no la refresca
            self.__screen.blit(self.__background, (0,0))
            
            #dibujo los runners en su posicion y con su imagen(custome)
            for runner in self.runners:
               self.__screen.blit(runner.custome, runner.position) 
            
            #si no refresco pantalla no se ven los cambios
            #pygame.display.flip() también refresca
            pygame.display.update()
            
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = Game()
    pygame.init()
    game.competir()