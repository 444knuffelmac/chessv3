import pygame

import backend
from backend import *
class Vakje:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_game_pos(self):
        pass


class Bord:
    def __init__(self):
        self.bord = backend.default8()


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 640))
        self.clock = pygame.time.Clock()
        self.bg_color = (0, 0, 0)
        self.light_brown = pygame.image.load('PNGs/No shadow/1x/square brown light_1x_ns.png').convert()


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
