import pygame as pg

class Rectangle:

    def __init__(self,game):
        """initialize the rectangle's attributes"""
        self.game = game
        from_top = game.screen_rect.bottom - 20
        width = self.game.settings.rectangle_width
        self.rect = pg.Rect(0,from_top,width,20)
        #put it in the middle of the x axis of the screen.
        self.center()
        #initialize values.
        self.moving_right = False
        self.moving_left = False


    def move(self):
        """move the rectangle to the right or to the left"""
        if self.moving_right and \
        self.rect.right < self.game.screen_rect.right:
            self.x += self.game.settings.rectangle_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.game.settings.rectangle_speed
        self.rect.x = self.x


    def draw(self):
        """draw the rectangle on the screen"""
        surface = self.game.screen 
        color = self.game.settings.rectangle_color
        pg.draw.rect(surface,color,self.rect)

    def center(self):
        self.rect.midbottom = self.game.screen_rect.midbottom
        self.x = float(self.rect.x)
