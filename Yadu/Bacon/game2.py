import bacon
import math

# window title
bacon.window.title = "Hello"

# window width and height
bacon.window.width = 800
bacon.window.height = 600

# can you resize it or not!
bacon.window.resizable = True

# A easy to use sprite class
class BaconSprite(object):
	# image to be loaded
	image = None
	
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

	#
	def __init__(self, img):
		# loads the image
		self.image = bacon.Image(img)

	# draw callback
	def draw(self):
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
		bacon.set_color(self.color[0], self.color[1] , self.color[2] , self.alpha)
		
		# draw image
		bacon.draw_image(self.image, -(self.image.width/2), -(self.image.height/2))
		
		# reset color
		bacon.pop_color()
		# reset transform
		bacon.pop_transform()

	# utility function to center the image to window
	def center_image(self):
		self.x = bacon.window.width/2
		self.y = bacon.window.height/2


# create some sprites and center them on window
pirate = BaconSprite("res/island_pirate_1d1a.png")
kitten = BaconSprite("res/kitten.jpg")

class myGame(bacon.Game):

	# we use this value to increment and decrement our pirate sprite's alpha value
	alpha_value = 0.5

	# update function
	def on_tick(self):
		# always clear the screen
		bacon.clear(1,1,1,1)

		# draw the kitten sprite
		kitten.draw()

		# if the pirate sprites alpha is greater than or equal to 1 then set alpha value to negatie
		if(pirate.alpha >= 1):
			self.alpha_value = -(self.alpha_value) # -0.5
		# if the pirate sprites alpha is lesser than 0 then set alpha value to positive
		elif(pirate.alpha < 0):
			self.alpha_value = abs(self.alpha_value) # 0.5

		# current alpha = current alpha + (0.5 * bacon.timestep)
		# or
		# current alpha = current alpha + (-0.5 * bacon.timestep)
		pirate.alpha += (self.alpha_value * bacon.timestep)

		# draw the scallywag
		pirate.draw()

	# called by bacon when the window is resized
	def on_resize(self, w, h):
		# when the window is resized, center our sprites
		kitten.center_image()
		pirate.center_image()

	# called when the mouse wheel is scrolled
	def on_mouse_scroll(self, dx, dy):
		pirate.scale_x += dy
		pirate.scale_y += dy

	# called when a key is down/up
	def on_key(self, key, pressed):
		# if the F key was pressed and then released
		# Note: (pressed == False) happens once when a key is pressed and released
		if key == bacon.Keys.f and pressed == False:
			# toggle fullscreen value
			bacon.window.fullscreen = not bacon.window.fullscreen

		
# run the bacon scene
bacon.run(myGame())
