import pygame as pg
import random
from pygame.sprite import Sprite
from time import sleep

class Ball(Sprite):
    """represent the ball"""
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.settings = game.settings
        self.center()
        #intialize values.
        self.red = True
        self.first_red_zone = True

    def draw(self):
        """draw the circle to the surface"""
        red = random.randint(0,250)
        green = random.randint(0,250)
        blue = random.randint(0,150)
        if len(self.game.wall.sprites()) <= self.game.number_rectangles/2:
            green = 100 
        if len(self.game.wall.sprites()) <= self.game.number_rectangles/4:
            blue = 0
            green = 0
            if self.first_red_zone:
                self.settings.ball_speed *= 1.5
                self.first_red_zone = False
            if self.red:
                red = 250
                self.red = False
            else:
                red = 0
                self.red = True

        color = (red,green,blue)
        pg.draw.circle(self.game.screen,color,(self.centerx,self.centery),15)

    def move(self):
        """move the ball"""
        if self.moving_down:
            self.centery += self.settings.ball_speed
        elif self.moving_up:
            self.centery -= self.settings.ball_speed
        if self.moving_right_alot:
            self.centerx += self.settings.ball_speed
        elif self.moving_right:
            self.centerx += self.bias
        elif self.moving_left_alot:
            self.centerx -= self.settings.ball_speed
        elif self.moving_left:
            self.centerx -= self.bias
        self.rect = pg.Rect(self.centerx - 15,self.centery - 15,30,30)
        if self.rect.top <= 0:
            self.moving_down = True
        elif self.rect.right >= self.game.screen_rect.right:
            self.moving_left = True
            self.moving_right = False
            if self.moving_right_alot:
                self.moving_right_alot = False
                self.moving_left_alot = True
        elif self.rect.left <= 0:
            self.moving_right = True
            if self.moving_left_alot:
                self.moving_right_alot = True
        elif self.rect.bottom > self.game.screen_rect.bottom:
            #you lose.
            self.game.lost = True
            sleep(0.6)

    def center(self):
        """put the ball in it's default position"""
        self.centerx = self.game.screen_rect.centerx
        self.centery = self.game.screen_rect.centery + 120
        self.moving_down = True
        self.moving_up = False
        self.moving_right = False
        self.moving_left = False
        self.moving_right_alot = False
        self.moving_left_alot = False
        self.bias = self.settings.ball_speed/2


        
        

