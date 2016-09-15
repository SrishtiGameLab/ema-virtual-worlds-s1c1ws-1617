class PirateNameGenerator(object):
	"""docstring for PirateNameGenerator"""

	name = "Pirate Name Generator"

	def __init__(self):
		super(PirateNameGenerator, self).__init__()

	def generate(self, name):
		return name

class SuperHeroNamer(object):
	"""docstring for PirateNameGenerator"""

	name = "SuperHero Name Generator"

	def __init__(self):
		super(SuperHeroNamer, self).__init__()

	def generate(self, name):
		return name



generators = [PirateNameGenerator(),  SuperHeroNamer()]

print generators[0].name
print generators[1].name

