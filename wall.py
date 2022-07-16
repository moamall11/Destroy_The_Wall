import pygame as pg
from pygame.sprite import Sprite

class SmallRectangle(Sprite):
    """represent each rectangle in the wall"""
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.settings = self.game.settings
        self.rect = pg.Rect(0,0,55,15)
        self.color = (200,0,0)

    def draw(self):
        pg.draw.rect(self.game.screen,self.color,self.rect)
