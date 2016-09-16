import bacon
import math
import random

bacon.window.title = ""
bacon.window.resizable = True
bacon.window.width = 640
bacon.window.height = 480
#bacon.window.target = bacon.Image(width=200, height=200, atlas=0)

def_font = bacon.Font(None, 10)
font = bacon.Font('res/Aero.ttf', 18)
		

# A easy to use sprite class
class BaconObject(object):
	# position of sprite
	x = 0.0
	y = 0.0

	# angle
	angle = 0

	# scale x and y
	scale_x = 1.0
	scale_y = 1.0

	# color r,g,b - 1,1,1 - is no tint!!
	color = (1.0, 1.0, 1.0)

	# alpha/opacity
	alpha = 1.0

	is_blinking = False
	blink_speed = 0

	velocity = (0.0, 0.0)

	wrap_object_movement = True

	def __init__(self, arg):
		super(BaconObject, self).__init__()

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
		# scale
		bacon.scale(self.scale_x, self.scale_y)
		# rotate
		bacon.rotate(math.radians(self.angle))		
		# move
		self.x += (self.velocity[0] * bacon.timestep)
		self.y += (self.velocity[1] * bacon.timestep)

		if(self.wrap_object_movement):
			if(self.x < 0):
				self.x = bacon.window.width
			elif(self.x > bacon.window.width):
				self.x = 0

			if(self.y < 0):
				self.y = bacon.window.height
			elif(self.y > bacon.window.height):
				self.y = 0

		bacon.translate(self.x, self.y)


		# save current rgba values
		bacon.push_color()
		# set new color + alpha value

		if self.is_blinking:
			# if sprites alpha is greater than or equal to 1 then set alpha value to negatie
			if(self.alpha >= 1):
				self.alpha = 1
				self.blink_speed = -(self.blink_speed) # -0.5
			# if the pirate sprites alpha is lesser than 0 then set alpha value to positive
			elif(self.alpha < 0):
				self.alpha = 0
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
class BaconSprite(BaconObject):
	# image to be loaded
	image = None

	def __init__(self, img, x = 0, y = 0):
		# loads the image
		super(BaconSprite, self).__init__()
		self.image = bacon.Image(img)
		self.x = x
		self.y = y

	# draw callback
	def draw_object(self):
		# draw image
		bacon.draw_image(self.image, -(self.image.width/2), -(self.image.height/2))


# A easy to use Rect class
class BaconShapeRect(BaconObject):
	image = None

	# init
	def __init__(self, x = 0, y = 0, w = 32, h = 32, color = (1.0, 1.0, 1.0), alpha = 1.0):
		super(BaconShapeRect, self).__init__()
		self.x = x
		self.y = y
		self.width = w
		self.height = h
		self.color = color
		self.alpha = alpha

	# draw callback
	def draw_object(self):
		bacon.fill_rect(-self.width/2, -self.height/2, self.width/2, self.height/2)


class SceneMenu(bacon.Game):

	box = BaconShapeRect(195,60,4,32)

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
		bacon.draw_string(font, "Starship ready.", 10, 30)
		bacon.draw_string(font, "click to initiate", 10, 72)
		#bacon.draw_string(def_font, "(" + str(bacon.mouse.x) + ", " + str(bacon.mouse.y) + ")", bacon.mouse.x, bacon.mouse.y)
		

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

	star_layer_count = 5
	stars = []
	star_count = 0
	marker = BaconShapeRect(100, 100, 10, 10, (1,0,0))
	img = BaconSprite("res/island_pirate_1d1a.png", 100, 100)
	base_velocity = 10

	def __init__(self):
		super(SceneGame, self).__init__()
		print "game::__init__"
		print "setting up stars"
		self.generate_star_field()		

	def on_init(self):
		print "game::on_init"
		pass

	def on_tick(self):
		bacon.set_blending(bacon.BlendFlags.src_alpha , bacon.BlendFlags.one_minus_src_alpha )
		bacon.clear(0, 0, 0, 1)
		bacon.translate(0,0)

		for layer in self.stars:
			for star in layer:
				star.draw()

		bacon.draw_string(font, "star count: " + str(self.star_count), 10, 25	)


	def on_resize(self, w, h):
		self.generate_star_field()

	def on_key(self, key, pressed):
		if key == bacon.Keys.escape:
			print "back to menu"
			bacon.run(menu)

		if key == bacon.Keys.f and pressed == False:
			bacon.window.fullscreen = not bacon.window.fullscreen
			self.generate_star_field()

	def generate_star_field(self):
		del self.stars[:]
		print "purguing %d stars from %d layers" % (self.star_count, self.star_layer_count)
		c = 0
		for i in xrange(0,self.star_layer_count):
			s = self.create_stars((i + 10) * self.star_layer_count, (-(self.base_velocity*i), 0))
			self.stars.append(s)
			c += len(s)
		self.star_count = c
		print "created %d stars in %d layers" % (self.star_count, self.star_layer_count) 
		return c

	def create_stars(self, count, velocity):
		w = bacon.window.width
		h = bacon.window.height
		result = []
		for i in xrange(1,count):
			x = random.randint(0, w)
			y = random.randint(0, h)
			star = BaconShapeRect(x, y, 2, 2)
			bspeed = 1.5 * random.random()
			# a + (b-a) * random
			# 1 + (5 - 1) * rand()
			# 1 + 4 * rand()
			# 1 + 0 to 4
			# 1 + 4 = 5
			s = 0.1 + (1.1 * random.random())
			star.scale_x = s
			star.scale_y = s
			star.blink(True, bspeed)
			star.velocity = velocity
			result.append(star)

		return result


menu = SceneMenu()
game = SceneGame()

bacon.run(menu)