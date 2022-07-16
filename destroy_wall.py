import pygame as pg
import sys
from rectangle import Rectangle
from settings import Settings
from wall import SmallRectangle
from ball import Ball
from score_board import ScoreBoard

class DestroyWall:
    """the game"""
    def __init__(self):
        """initilize the attributes"""
        pg.init()
        self.settings = Settings()
        self.screen = pg.display.set_mode(self.settings.screen_size)
        self.screen_rect = self.screen.get_rect()
        pg.display.set_caption("Destroy the wall")
        self.rectangle = Rectangle(self) 
        self.wall = pg.sprite.Group()
        self._make_wall()
        self.number_rectangles = len(self.wall.sprites())
        self.ball = Ball(self)
        self.score_board = ScoreBoard(self)
        self.lost = False
        self.end_game = False


    def run_game(self):
        """the main method"""
        while True:
            self._check_events()
            if not self.end_game:
                self.rectangle.move()
                self.ball.move()
                self._check_lost()
                self._check_collision()
                self._update_screen()
                pg.display.flip()


    def _check_events(self):
        """check for any events"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self._check_key_down(event)
            elif event.type == pg.KEYUP:
                self._check_key_up(event)


    def _check_key_down(self,event):
        """check for any keys pressed by the user"""
        if event.key == pg.K_q:
            sys.exit()
        elif event.key == pg.K_RIGHT:
            self.rectangle.moving_right = True
        elif event.key == pg.K_LEFT:
            self.rectangle.moving_left = True

    def _check_key_up(self,event):
        """check for the release of any keys pressed"""
        if event.key == pg.K_RIGHT:
            self.rectangle.moving_right = False
        elif event.key == pg.K_LEFT:
            self.rectangle.moving_left = False

    def _make_wall(self):
        """make the wall"""
        #make an instance of the small rectangle 
        #so we can get it's dimensions.
        rectangle = SmallRectangle(self)
        width,height = rectangle.rect.size
        #get the available space horizontally on the x axis.
        available_space_x = self.screen_rect.width - width
        #same thing with the y axis.
        available_space_y = self.screen_rect.height - (14 * height)
        #now we will get the number of rectangles 
        #that we can put in the available space.
        number_rectangles_x = available_space_x // (2 * width)
        number_rows = available_space_y // (3 * height)
        for row_number in range(number_rows):
            for rectangle_number in range(int(number_rectangles_x)):
                self._create_small_rectangle(row_number,rectangle_number)

    def _create_small_rectangle(self,row_number,rectangle_number):
        """create a small rectangle and add it to the wall"""
        rectangle = SmallRectangle(self)
        width,height = rectangle.rect.size
        rectangle.rect.x = width + (2 * width * rectangle_number)
        rectangle.rect.y = height + (3 * height * row_number)
        green_color = 25 * row_number
        if green_color > 250:
            green_color = 250
        rectangle.color = (200,green_color,0)
        self.wall.add(rectangle)

    def _check_collision(self):
        """check for collisions between the ball and the rectangle"""
        if pg.sprite.collide_rect(self.ball,self.rectangle):
            self.ball.moving_down = False
            self.ball.moving_up = True
            if self.ball.rect.centerx <= self.rectangle.rect.left:
                self.ball.moving_left_alot = True
                self.ball.moving_left = True
                self.ball.moving_right = False
            elif self.ball.rect.centerx >= self.rectangle.rect.right:
                self.ball.moving_right_alot = True
                self.ball.moving_right = True
            elif self.rectangle.moving_right:
                self.ball.moving_right = True
                self.ball.bias = self.settings.ball_speed/2
            elif self.rectangle.moving_left:
                self.ball.moving_right = False
                self.ball.moving_left = True
                self.ball.bias = self.settings.ball_speed/2
            else:
                #if none of the above happened then we need to reduce 
                #the amount by which the ball goes right or left (the bias).
                self.ball.bias *= 0.8
        rectangle = pg.sprite.spritecollideany(self.ball,self.wall)
        if rectangle:
            if self.ball.rect.centery < rectangle.rect.top:
                self.ball.moving_down = False
            elif self.ball.rect.centery > rectangle.rect.bottom:
                self.ball.moving_down = True
            if self.ball.rect.centerx > rectangle.rect.right:
                self.ball.moving_right = True
            elif self.ball.rect.centerx < rectangle.rect.left:
                self.ball.moving_right = False
            if self.ball.moving_right_alot:
                self.ball.moving_right_alot = False
                self.ball.moving_right = True
            elif self.ball.moving_left_alot:
                self.ball.moving_left_alot = False
                self.ball.moving_left = True
            self.wall.remove(rectangle)

    def _check_lost(self):
        """when the ball gets out"""
        if self.lost:
            self.settings.lives -= 1
            self.score_board.prep_img()
            self.ball.center()
            self.rectangle.center()
            if self.settings.lives > 0:
                self.lost = False
            else:
                self.end_game = True


    def _update_screen(self):
        """update the screen"""
        self.screen.fill(self.settings.bg_color)
        self.rectangle.draw()
        for rectangle in self.wall.sprites():
            rectangle.draw()
        self.score_board.draw()
        self.ball.draw()


if __name__ == '__main__':
    game = DestroyWall()
    game.run_game()