import pygame as pg

class ScoreBoard:
    def __init__(self,game):
        self.font = pg.font.SysFont(None,100)
        self.game = game
        self.settings = game.settings
        self.prep_img()

        
    def prep_img(self):
        color = self.settings.text_color
        lives = str(self.settings.lives)
        self.img = self.font.render(
            lives,None,color)
        self.rect = self.img.get_rect()
        self.rect.topright = self.game.screen_rect.topright

    def draw(self):
        self.game.screen.blit(self.img,self.rect)

