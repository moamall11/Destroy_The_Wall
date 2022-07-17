
class Settings:

	def __init__(self):
		self.screen_size = (1200,650)
		self.bg_color = (100,50,200)

		self.rectangle_color = (0,20,0)
		self.rectangle_speed = 1.5
		self.rectangle_width = 105

		self.ball_speed = 0.9

		self.lives = 3
		self.text_color = (0,200,0)

		#2 or 4.
		self.wall_number = 2

		#for AI player.
		self.rectangle_speed *= 4
		self.ball_speed *= 4
		self.wall_number *= 2
