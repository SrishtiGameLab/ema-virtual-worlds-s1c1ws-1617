import pyglet

window = pyglet.window.Window()
window.set_size(800, 600)
image = pyglet.resource.image('res/kitten.jpg')

@window.event
def on_draw():
	window.clear()
	image.blit(0, 0)

pyglet.app.run()