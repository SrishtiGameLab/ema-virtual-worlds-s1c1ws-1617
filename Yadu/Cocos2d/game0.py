import cocos

class HelloWorld(cocos.layer.Layer):
	def __init__(self):
		super(HelloWorld, self).__init__()

		label = cocos.text.Label(
			'Hello World',
			font_name='Times New Roman',
			font_size=42,
			anchor_x='center', anchor_y='center'
		)

		label.position = 320, 240
		self.add(label)

cocos.director.director.init()
cocos.director.director.run(cocos.scene.Scene(HelloWorld()))