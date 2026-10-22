import pygame

import backend
from backend import *
class Vakje:
    def __init__(self, x, y, kleur):
        self.x = x
        self.y = y
        self.kleur_is_zwart = kleur
        self.light_brown = pygame.image.load('PNGs/No_shadow/1x/square_brown_light_1x_ns.png').convert()
        self.dark_brown = pygame.image.load('PNGs/No_shadow/1x/square_brown_dark_1x_ns.png').convert()
        self.dark_gray = pygame.image.load('PNGs/No_shadow/1x/square_gray_dark_1x_ns.png').convert()
        self.light_gray = pygame.image.load('PNGs/No_shadow/1x/square_gray_light_1x_ns.png').convert()
        self.assigned_color = None
        self.bevat_stuk = False
        self.stuk = None

        if self.kleur_is_zwart:
            self.assigned_color = self.dark_brown
        else:
            self.assigned_color = self.light_brown

    def select(self):
        if self.assigned_color == self.light_brown:
            self.assigned_color = self.light_gray
        elif self.assigned_color == self.dark_brown:
            self.assigned_color = self.dark_gray

    def deselect(self):
        if self.assigned_color == self.light_gray:
            self.assigned_color = self.light_brown
        elif self.assigned_color == self.dark_gray:
            self.assigned_color = self.dark_brown


    def set_kleur(self, kleur):
        self.assigned_color = kleur


    def get_kleur_rect(self):
        if self.kleur_is_zwart:
            return self.dark_brown.get_rect()
        else:
            return self.light_brown.get_rect()

    def setStuk(self, stuk):
        self.stuk = stuk
        self.bevat_stuk = True

    def getStuk(self):
        return self.stuk

    def unassignStuk(self):
        self.stuk = None
        self.bevat_stuk = False


    def get_assigned_color(self):
        return pygame.transform.scale(self.assigned_color, (80,80))


    def GetX(self):
        return self.x
    def GetY(self):
        return self.y


class Bord:
    def __init__(self):
        self.bord = backend.default8()
        self.game_bord = [[None for _ in range(8)] for _ in range(8)]
        self.vakje_generatie()


    def vakje_generatie(self):
        i = 0
        for row_idx, row in enumerate(self.game_bord):
            if i == 0: i += 1
            else: i -= 1
            for col_idx in range(len(row)):
                if i == 0:
                    self.game_bord[row_idx][col_idx] = Vakje(col_idx, row_idx, True)
                    i += 1
                else:
                    self.game_bord[row_idx][col_idx] = Vakje(col_idx, row_idx, False)
                    i -= 1


    def getGame_bord(self):
        return self.game_bord




class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 640))
        self.clock = pygame.time.Clock()
        self.bg_color = (0, 0, 0)
        self.bord = Bord()
        self.game_bord =self.bord.getGame_bord()



    def mouse_pos_on_board(self):
        for row_idx, row in enumerate(self.game_bord):
            for col_idx in range(len(row)):
                vakje = self.game_bord[row_idx][col_idx]
                pos = pygame.mouse.get_pos()
                vakje_x, vakje_y = vakje.GetX(), vakje.GetY()

                if vakje_x*80 < pos[0] < vakje_x*80+80:
                    if vakje_y*80 < pos[1] < vakje_y*80+80:
                        if pygame.mouse.get_pressed()[0]:

                            return vakje


    def vakje_selector(self, vakje1: Vakje, vakje2: Vakje):
        print(vakje1)

    def run(self):
        first_vakje = None
        second_vakje = None
        presses = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and first_vakje == None:
                    first_vakje = self.mouse_pos_on_board()
                    first_vakje.select()
                    print(f"first_vakje: {first_vakje}")
                    presses += 1
                elif event.type == pygame.MOUSEBUTTONDOWN and first_vakje != None:
                    second_vakje = self.mouse_pos_on_board()
                    second_vakje.select()
                    print(f"second_vakje: {second_vakje}")
                    presses += 1
                if presses > 2:
                    presses = 0
                    first_vakje.deselect()
                    second_vakje.deselect()
                    first_vakje = None
                    second_vakje = None





            self.screen.fill(self.bg_color)
            #self.set_vakjes()
            for row_idx, row in enumerate(self.game_bord):
                for col_idx in range(len(row)):
                    vakje = self.game_bord[row_idx][col_idx]
                    x, y, rect, image = vakje.GetX(), vakje.GetY(), vakje.get_kleur_rect(), vakje.get_assigned_color()
                    self.screen.blit(image, (x*80, y*80), rect)







            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.run()
