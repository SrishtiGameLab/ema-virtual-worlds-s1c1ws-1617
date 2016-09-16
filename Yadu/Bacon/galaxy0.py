import bacon 
import math
import random

bacon.window.resizable = True

class supstar(object):
	alpha=1
	alpha_value=0.5
	x = 0
	y = 0
	scale_x = 1
	scale_y = 1
	width = 10
	height = 10

	def __init__(self,x,y,scalex,scaley):
		self.x=x
		self.y=y
		self.scale_x=scalex
		self.scale_y=scaley

	def draw(self):


		bacon.push_transform()
		
		
		#bacon.translate(self.x,self.y)
		bacon.scale(self.scale_x,self.scale_y)
		bacon.push_color()

		if(self.alpha >= 1):
			self.alpha_value = -(self.alpha_value) # -0.5
		# if the supstar sprites alpha is lesser than 0 then set alpha value to positive
		elif(self.alpha < 0):
			self.alpha_value = abs(self.alpha_value) # 0.5


		# current alpha = current alpha + (0.5 * bacon.timestep)
		# or
		# current alpha = current alpha + (-0.5 * bacon.timestep)
		self.alpha += (self.alpha_value * bacon.timestep)

		


		bacon.set_color(1,1,1,self.alpha)
		bacon.fill_rect(self.x - self.width/6, self.y - self.height/2, self.x + self.width/6, self.y + self.height/2)
		bacon.set_color(0.3,0.5,0.9,self.alpha)
		bacon.fill_rect(self.x - self.width/2, self.y - self.height/6, self.x + self.width/2, self.y + self.height/6)
		bacon.pop_color()
		bacon.pop_transform()

class Game(bacon.Game):
	alpha_value=0.5


	stars=[]

	def on_init(self):

		for i in xrange(1,100):
			x = random.randint(0,bacon.window.width)
			y = random.randint(0,bacon.window.height)
			s = random.randint(1,3)
			self.stars.append(supstar(x, y,s,s))

	def on_tick(self):
		

		bacon.clear(0,0,0,1)
		bacon.set_blending(bacon.BlendFlags.src_alpha , bacon.BlendFlags.one_minus_src_alpha )
		
		'''
		bacon.translate(100,50)
		bacon.scale(10,10)

		bacon.set_color(0.7,0.5,0.8,1)
		bacon.fill_rect(3,0,6,9)
		bacon.set_color(0.3,0.5,0.9,1)
		bacon.fill_rect(0,3,9,6)
		'''
		

		for star in self.stars:
			star.draw()


bacon.run(Game())