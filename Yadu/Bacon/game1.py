import math
import bacon

class BaconSprite(object):
	image = None
	angle = 0
	x = 0
	y = 0
	origin_x = 0
	origin_y = 0

	def __init__(self, image, x = 0, y = 0, angle = 0):
		self.image = bacon.Image(image)
		self.x = x
		self.y = y
		self.angle = angle

	def draw(self):
		bacon.push_transform()
		bacon.translate(self.x, self.y)
		bacon.rotate(self.angle)
		bacon.draw_image(self.image, -(self.image.width/2), -(self.image.height/2))
		bacon.pop_transform()

cat = BaconSprite('res/island_pirate_1d1a.png', 100, 100, math.radians(45))

class Game(bacon.Game):
	def on_tick(self):
		cat.draw()

bacon.run(Game())