# Welcome to the unit 

'''
Why python
	- Easy to learn
	- Verbose and easy to read and understand for beginners
	- Large amount of libraries extend it's functionality, all of which is open source like python itself
	- Uses outside this two weeks! You can build websites with python frameworks like flask or django, you can use it to talk to devices connected to your computer - like an arduino or anything else, you can automate a lot of tasks on your computer, you can talk to, automate and extend tools like 3DMax, Maya and Blender and 
	- <insert more reasons>

Start by downloading and installing Python 2.7 (https://www.python.org/) and your favourite text editor - Sublime Text (https://www.sublimetext.com/)
see if python was installed ok!? - terminal/cmd 
'''

# Python Syntax

# Welcome!
print "This is a start"

# Variables
my_variable = 42

# Booleans and data types!
my_int = 42
my_float = 4.2
my_bool = True

# Assigning values - case sensitive!
my_int = 42
my_int = 3
print my_int

# Whitespace - intends have meaning!
def explode():
	return "BOOM"

# Python is an interpreted language
'''
line by line!
checking for errors
'''

# Single line comments
# this is a single line comment

# Multi line comments
"""
multiline comment
is here
"""


# Math operations + - * /
# Exponentiation **
# Modulo %

# Exercise
'''
Create a variable called isRunning, set it to True.
Create a variable called answer, set it to 42
Create a variable called squared, set it to answer squared
'''

# Recap
# variables, 3 data types, assigning values, comments, math ops, exponentiation, modulo


# Strings
my_fname = "Yadu"
my_lname = "Rajiv"

# Escaping characters
my_response = "Yadu said: \"I can't leave now!\""

'''
# Access by Index
+---+---+---+---+---+---+
| P | O | T | A | T | O |
+---+---+---+---+---+---+
  0   1   2   3   4   5
'''
p = "POTATO"
# acecss strings via their index
print p[0] # prints P
print p[3] # prints A
print p[4] # prints T

# String methods - dot notation - lower(), upper()
# Everything in python is an object (can have - methods, attributes, subclassable)
print p.lower() # prints potato
print p.upper() # prints POTATO

# len() - length of a string
print len(my_fname)

# str() - converts non-strings to strings
pi = 3.14
print str(pi)

# Printing strings - Printing variables with strings
pi = "three point one four"
print pi

# String concatenation
my_fname = "Yadu"
my_lname = "Rajiv"
my_name = my_fname + " " + my_lname

# Explicit string conversion
# print "hello" + 10 # will throw an error
print "hello " + str(10)

# Formatting strings with %
my_fname = raw_input("Your first name: ")
my_lname = raw_input("Your last name: ")
print "Hello, %s %s! Welcome to the Parteh!" % (my_fname, my_lname)

# Bringing it together
'''
Get the flower names and colors from the user, create poem
____ are ____
____ are ____
In Soviet Russia
Poems write you
'''
flower_1 = raw_input("Name a flower: ")
color_1 = raw_input("What color is a %s: " % (flower_1))
flower_2 = raw_input("Name another flower: ")
color_2 = raw_input("What color is a %s: " % (flower_2))

raw_input("Are you ready for my great poem?")

print "%s are %s\n%s are %s\nIn Soviet Russia\nPoems write you" % (flower_1, color_1, flower_2, color_2)



# Datetime library - what are libraries, why libs
from datetime import datetime

# Current Date and Time
datetime.now()

# Extract more info from datetime.now() object
now = datetime.now()
# now.year
# now.month
# now.day
print '%s/%s/%s' % (now.month, now.day, now.year)

# Bring it all together
#from datetime import datetime
now = datetime.now()
print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)


# Comparators - 6 of them - all return True or False
'''
==
!=
<
<=
>
>=
'''
# Boolean Operators
'''
and
or
not
'''
my_v = 42
my_a = 54
# print my_a < 100 and my_v < 100
# print my_a < 50 and my_v < 50
print (my_a < 50 or (my_v < 50)) and (200 == (100/2)*4)


# Conditional statements
# if, elif and else
a = float(raw_input("gimme a number: "))

if a < 100:
	print "a is less than 100"
elif a > 100:
	print "a is much larger than 100"
else:
	print "a is 100"

res = raw_input("do you want to go? ")

if res.lower() == "yes":
	print "please don't go!!"
else:
	print "ok then"


# Bring it together
# Take user input, compare input and check if input was one of the items, print appropriate response

# Bringing it together - 2
# Generate a story or a poem after taking some user input

# Functions - are reusable bits of code

# define a function
def say_hello():
	return "Hello"

# Call a function
print say_hello()

# params/arguments
def mul(argument1, argument2):
	return argument1 * argument2

print mul(5, 10)

# functions can call functions
def respond(a, b):
	return "multiply %s and %s and you get %s" % (a, b, mul(a,b)) 

# generic imports and functions
from random import Random
r = Random()
r.random()

# builtins!
print max(10, 11, 122, 121212)
print min(-10, -20, 4, 5)
print abs(-42)
print type(my_name)
print type(mul)
print type(True)

# Python Standard Library
# visit: https://docs.python.org/2/library/

# Bringing it together - Bonus points if you do this.
# make a small game where you have to guess the number which the computer has thoguht of!!