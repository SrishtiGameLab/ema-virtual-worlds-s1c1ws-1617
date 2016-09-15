import bacon
import math

bacon.window.title = ""
bacon.window.width = 640
bacon.window.height = 480
bacon.window.resizable = True


font = bacon.Font('res/Aero.ttf', 18)
		

# A easy to use sprite class
class BaconBase(object):
	# position of sprite
	x = 0
	y = 0

	# angle
	angle = 0

	# scale x and y
	scale_x = 1
	scale_y = 1

	# color r,g,b - 1,1,1 - is no tint!!
	color = (1, 1, 1)

	# alpha/opacity
	alpha = 1

	is_blinking = False
	blink_speed = 5

	def __init__(self, arg):
		super(BaconBase, self).__init__()

	def __init__(self):
		pass

	def pre_draw(self):
		pass

	def draw_object(self):
		pass

	def post_draw(self):
		pass

	# draw callback
	def draw(self):

		self.pre_draw()

		# save current transform
		bacon.push_transform()
		# move
		bacon.translate(self.x, self.y)
		# scale
		bacon.scale(self.scale_x, self.scale_y)
		# rotate
		bacon.rotate(math.radians(self.angle))

		# save current rgba values
		bacon.push_color()
		# set new color + alpha value

		if self.is_blinking:
			# if sprites alpha is greater than or equal to 1 then set alpha value to negatie
			if(self.alpha >= 1):
				self.blink_speed = -(self.blink_speed) # -0.5
			# if the pirate sprites alpha is lesser than 0 then set alpha value to positive
			elif(self.alpha < 0):
				self.blink_speed = abs(self.blink_speed) # 0.5
			# blink! 
			self.alpha += (self.blink_speed * bacon.timestep)

		bacon.set_color(self.color[0], self.color[1] , self.color[2] , self.alpha)
		
		self.draw_object()
		
		# reset color
		bacon.pop_color()
		# reset transform
		bacon.pop_transform()

		self.post_draw()

	# utility function to center the image to window
	def center_image(self):
		self.x = bacon.window.width/2
		self.y = bacon.window.height/2

	def blink(self, blink = True, blink_speed = 5):
		self.is_blinking = blink;
		self.blink_speed = blink_speed


# A easy to use sprite class
class BaconSprite(BaconBase):
	# image to be loaded
	image = None

	def __init__(self, img):
		# loads the image
		super(BaconSprite, self).__init__()
		self.image = bacon.Image(img)

	# draw callback
	def draw_object(self):
		# draw image
		bacon.draw_image(self.image, -(self.image.width/2), -(self.image.height/2))



# A easy to use Rect class
class BaconShapeRect(BaconBase):
	image = None

	# init
	def __init__(self, x = 0, y = 0, w = 32, h = 32, color = (1, 1, 1), alpha = 1):
		super(BaconShapeRect, self).__init__()
		self.x = x
		self.y = y
		self.width = w
		self.height = h
		self.color = color
		self.alpha = alpha

	# draw callback
	def draw_object(self):
		bacon.fill_rect(self.x - self.width/2, self.y - self.height/2, self.x + self.width/2, self.y + self.height/2)


class SceneMenu(bacon.Game):

	box = BaconShapeRect(92,15)

	def __init__(self):
		super(SceneMenu, self).__init__()
		print "menu::__init__"

	def on_init(self):
		print "menu::on_init"
		self.box.blink()
		pass

	def on_tick(self):
		bacon.set_blending(bacon.BlendFlags.src_alpha , bacon.BlendFlags.one_minus_src_alpha )
		bacon.clear(0, 0, 0, 1)
		self.box.draw()
		bacon.draw_string(font, "click to start", 10, 42)
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
		bacon.set_blending(bacon.BlendFlags.src_alpha , bacon.BlendFlags.one_minus_src_alpha )
		bacon.clear(0, 0, 0, 1)
		bacon.set_color(1, 0, 0, 1)
		bacon.fill_rect(50, 50, 150, 150)
		bacon.set_color(0, 1, 0, 0.1)
		bacon.fill_rect(100, 100, 200, 200)
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