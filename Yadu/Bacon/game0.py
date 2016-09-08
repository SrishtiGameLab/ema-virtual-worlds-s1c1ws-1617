import bacon

kitten = bacon.Image('res/kitten.jpg')
font = bacon.Font('res/dejavu-sans.extralight.ttf', 42)
message = "Have you see me?"

bacon.window.width = 800
bacon.window.height = 600

class Game(bacon.Game):
	offset_x = 0
	offset_y = 0

	def on_tick(self):
		bacon.clear(0, 0, 0, 1)
		bacon.set_color(1, 0, 0, 1)
		bacon.draw_image(kitten, self.offset_x, self.offset_y)

		bacon.draw_string(font, message, 30, 60)

		self.offset_x += bacon.mouse.x/100
		self.offset_y += bacon.mouse.y/100

	def on_mouse_button(self, button, pressed):
		print('bacon.MouseButtons.%s was %s' % (bacon.MouseButtons.tostring(button), 'pressed' if pressed else 'released'))
		print(message)



bacon.run(Game())