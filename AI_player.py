from destroy_wall import DestroyWall
from random import randint

class AIPlayer:
    def __init__(self,game):
        self.game = game
        self.same_loops = 0
        self.previous_num_sprites = 0


    def run_game(self):
        """the main loop"""
        while True:
            self.game._check_events()
            if not self.game.end_game:
                self._move_rectangle()
                self.game.rectangle.move()
                self.game.ball.move()
                self.game._check_lost()
                self.game._check_collision()
                self.game._check_win()
                self.game._update_screen()

    def _move_rectangle(self):
        """apply the strategy to move the rectangle"""
        #follow the ball,when it goes left you go left.
        if self.game.ball.centerx < self.game.rectangle.rect.left:
            self.game.rectangle.moving_left = True
            self.game.rectangle.moving_right = False
        #when it goes right you go right.
        elif self.game.ball.centerx > self.game.rectangle.rect.right:
            self.game.rectangle.moving_right = True
            self.game.rectangle.moving_left = False
        #and when the ball is within your bounds 
        #stay when there are rectangles within the bounds of the ball
        #else move the ball to the right or to the left to find rectangles.
        elif self.game.ball.centerx > self.game.rectangle.rect.left and\
        self.game.ball.centerx < self.game.rectangle.rect.right:
            stuck = self._is_stuck()
            if not stuck:
                self._get_vertical()
                if len(self.vertical) == 0:
                    self._find_another_vertical()
                else: 
                    self.game.rectangle.moving_right = False
                    self.game.rectangle.moving_left = False
            else:
                if randint(0,100) >= 50:
                    self._move_right()
                else:
                    self._move_left()


    def _get_vertical(self):
        self.vertical = []
        for sprite in self.game.wall.sprites():
            if sprite.rect.right > self.game.ball.centerx - 10 and \
            sprite.rect.left < self.game.ball.centerx + 10:
                self.vertical.append(sprite)

    def _find_another_vertical(self):
        """move right or left to find another vertical"""
        number = randint(0,len(self.game.wall.sprites()) - 1)
        sprite = self.game.wall.sprites()[number]
        if self.game.ball.moving_down and \
            self.game.ball.centery >= self.game.rectangle.rect.top - 20:
            if sprite.rect.left > self.game.rectangle.rect.right:
                self._move_right
            elif sprite.rect.right < self.game.rectangle.rect.left:
                self._move_left

    def _move_right(self):
        self.game.rectangle.moving_left = False
        self.game.rectangle.moving_right = True

    def _move_left(self):
        self.game.rectangle.moving_right = False
        self.game.rectangle.moving_left = True


    def _is_stuck(self):
        """returns True when the number of sprites 
        stays the same for a long time"""
        if len(self.game.wall.sprites()) == self.previous_num_sprites:
            self.same_loops += 1
        else:
            print(self.same_loops)
            self.same_loops = 0
            self.previous_num_sprites = len(self.game.wall.sprites())
        if self.same_loops > 600:
            return True
        else:
            return False
        



if __name__ == '__main__':
    game = DestroyWall()
    player = AIPlayer(game)
    player.run_game()