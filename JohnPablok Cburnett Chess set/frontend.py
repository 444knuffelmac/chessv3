import pygame

import backend
from backend import *
class Vakje:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.light_brown = pygame.image.load('PNGs/No shadow/1x/square brown light_1x_ns.png').convert()

    def getX(self):
        return self.x
    def getY(self):
        return self.y


class Bord:
    def __init__(self):
        self.bord = backend.default8()
        self.game_bord = self.bord.copy()

    def vakje_selector(self):
        for i in self.game_bord:
            for j in i:
                vakje = Vakje(j, i)
                vakje.getX()
                vakje.getY()




class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 640))
        self.clock = pygame.time.Clock()
        self.bg_color = (0, 0, 0)
        self.bord = Bord()


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.screen.fill(self.bg_color)

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.run()
