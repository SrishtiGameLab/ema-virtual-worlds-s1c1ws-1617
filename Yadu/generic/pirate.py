# eg: "Yadu Rajiv"
# Source - https://en.wikipedia.org/wiki/List_of_fictional_pirates
# rule 1 - take second alphabet of frist name and select the first name list - eg: a_fname
# rule 1 - take length of first name - get len % count item from - eg: len(input_fname) % len(a_fname) and get that item from a_fname
# rule 2 - same for last name 
# rule 3 - take len of full name % len(profession_list)
# rule 4 - Add "Captain" if new first name starts with an A, B, C, D, M, J, R, S, W 

class PirateName(object):
	"""Find what your pirate name is!"""
	name = ""
	items = ["beard", "body", "booty", "nose"]
	features = ["one legged", "one eyed", "hawkeye", "mad", "scarface"]
	colors = ["Black", "Dark", "Grey", "Light", "Pink", "Red", "White", "Yellow"]
	a_fname = []
	b_fname = []
	c_fname = []

	def __init__(self, name):
		super(PirateName, self).__init__()
		self.name = name

	def gen(self):

		return self.name