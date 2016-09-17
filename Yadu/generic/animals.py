'''
animals class - used in 30_classes.py
'''
class Animal(object):
	voice = ""
	def __init__(self):
		pass

	def speak(self):
		print self.voice

	def doSomething(self):
		print "I am doing something!"


class Cat(Animal):
	voice = "Meow"

class Dog(Animal):
	voice = "BowBow"

	def speak(self):
		print "I am a dog and I go " + self.voice
		self.doSomething()

class Lab(Dog):
	voice = "Give me the ball!!"

	def goFetch(self):
		print "gets you a news paper"
