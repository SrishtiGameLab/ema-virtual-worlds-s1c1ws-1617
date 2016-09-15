import bacon
import math

bacon.window.title = ""
bacon.window.width = 640
bacon.window.height = 480
bacon.window.resizable = True

class BaconSprite(object):
	image = None
	x = 0
	y = 0
	angle = 0
	xscale = 1
	yscale = 1
	alpha = 1

	def __init__(self, img):
		self.image = bacon.Image(img)

	def draw(self):
		bacon.push_transform()
		bacon.translate(self.x, self.y)
		bacon.scale(self.xscale, self.yscale)
		bacon.rotate(math.radians(self.angle))
		bacon.push_color()
		bacon.set_color(1, 1 , 1 , self.alpha)
		bacon.draw_image(self.image, -(self.image.width/2), -(self.image.height/2))
		bacon.pop_color()
		bacon.pop_transform()

	def center_image(self):
		self.x = bacon.window.width/2
		self.y = bacon.window.height/2

class BaconShape(object):
	x = 0
	y = 0
	angle = 0
	xscale = 1
	yscale = 1
	alpha = 1

	def __init__(self, img):
		self.image = bacon.Image(img)

	def draw(self):
		bacon.push_transform()
		bacon.translate(self.x, self.y)
		bacon.scale(self.xscale, self.yscale)
		bacon.rotate(math.radians(self.angle))
		bacon.push_color()
		bacon.set_color(1, 1 , 1 , self.alpha)

		bacon.pop_color()
		bacon.pop_transform()

	def center_image(self):
		self.x = bacon.window.width/2
		self.y = bacon.window.height/2
		

class SceneMenu(bacon.Game):

	def __init__(self):
		super(SceneMenu, self).__init__()
		print "menu::__init__"

	def on_init(self):
		print "menu::on_init"
		pass

	def on_tick(self):
		bacon.clear(0,0,0,1)
		pass

	def on_resize(self, w, h):
		pass

	def on_mouse_button(self, button, pressed):
		if pressed:
			print "onwards to game!"
			bacon.run(game)

	def on_key(self, key, pressed):
		if key == bacon.Keys.f and pressed == False:
			bacon.window.fullscreen = not bacon.window.fullscreen


class SceneGame(bacon.Game):

	def __init__(self):
		super(SceneGame, self).__init__()
		print "game::__init__"

	def on_init(self):
		print "game::on_init"
		pass

	def on_tick(self):
		bacon.clear(0,0,0,1)
		pass

	def on_resize(self, w, h):
		pass

	def on_key(self, key, pressed):
		if key == bacon.Keys.escape:
			print "back to menu"
			bacon.run(menu)

		if key == bacon.Keys.f and pressed == False:
			bacon.window.fullscreen = not bacon.window.fullscreen


menu = SceneMenu()
game = SceneGame()

bacon.run(menu)