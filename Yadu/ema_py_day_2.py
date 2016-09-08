'''
# Going aroud with loops!
# Loops are statements that interate over expressions till a condition is satisfied
'''

# our title
lab = "Awesome lab for awesome things!"

# a for loop has the following structureThis is awesome!! -  If you are making games, do check it out - https://www.humblebundle.com/gamemaker-bundle
'''
# here iterator_var will go in a linear fashion through each item in the sequence
for iterator_var in sequence:
	pass
'''
# also...
'''
# x will have a value from 0 to 9 - loops 10 times
for x in xrange(0,10):
	pass
'''

'''
break - is a statement used to break out of the loop at that point, useful when
you want to prematurely exit a loop

continue - is a statement used to skip the loop from that point on, useful when
you want to skip to the next item in the loop

pass is a special statement which does nothing! - It can be used when a statement
is required syntactically but the program requires no action. 

more on loops - http://www.tutorialspoint.com/python/python_loops.htm
'''

'''
# Here is a function that takes in a text, loops through all 
# the characters the text has and converts them to elite speak
# using a for loop
'''
def elite_text(txt):
	leet = ""
	# for each character in the given text, loop!
	for char in txt:
		if char == "A": # replace capital A with 4
			leet += "4"
		elif char.lower() == "e": # replace e with 3
			leet += "3"
		elif char.lower() == "s": # replace s with $
			leet += "$"
		elif char.lower() == "o": # replace o with 0
			leet += "0"
		elif char.lower() == "l": # replace l with 1
			leet += "1"
		else:
			leet += char # all other characters as is
	return leet # return new string once done!


'''
# display our fancy elite title!
'''
print elite_text(lab)


'''
# Lists []
# lists are types of variables that stores a list of different types of data in a sequence
# lists can be empty
# list_courses = [] or can values like below
'''
list_courses = ["games", "infoviz", "viscom"]

'''
# this function loops through the list of courses we have and prints them
# then takes an input from the user for the course number
# and returns it
'''
def print_courses():
	print "----------------------------------------"
	print "We offer %d of the following courses!" % len(list_courses) # did you notice the %d there?
	for x in xrange(0,len(list_courses)):
		# access lists via index
		print "%d. %s" % ((x+1), list_courses[x])
	c = int(float(raw_input("Select a course(enter 1-%d): " % len(list_courses))))
	return c

'''
# this function takes a course number and then checks if it is in the range of the list
# and thanks the user for selecting the course
# or show the course list again for invalid selections
'''
def validate(c):
	c = c - 1 # we need a 0 based array index!

	# is our index between 0 and 2 inclusive
	if c < len(list_courses) and c >= 0:
		print "Thank you for selecting %s. Your sign up is complete." % (list_courses[c]) # select course
		print "\n"
	else:
		print "The course you have selected is invalid, please try again!"
		validate(print_courses()) # reshow options and validate again!

'''
# display course list and get signup
'''
validate(print_courses())


'''
# we can directly access list items and change them - here changing viscom to potato
'''
list_courses[2] = "potato"


'''
# redisplay with new potato course in list
'''
validate(print_courses())



'''
# Manipulating lists using functions
'''

'''
#lets add a new course to our list! - append adds the new item to the end of the list
'''
list_courses.append('viscom') # viscom is back by popular demand

'''
# redisplay with new viscom course in list
'''
validate(print_courses())

'''
# Slicing a list - returns a part of a list
'''
print list_courses[0:2] # prints items 0 and 1 [start_index:end_index] - end, not inclusive

'''
# since strings behave like lists and can be accessed
# via their index, they can alsobe sliced the same way
'''

print "lab = " + lab
print "lab[:7] = " + lab[:7] # prints the first 7 letters from lab
print "lab[24:] = " + lab[24:] # prints 25 to the last letter from lab
print "lab[8:11] = " + lab[8:11] # prints 3 chars from 8 to 11 from lab

'''
# We can use insert(index, item) to insert an object at a particular index of a list
'''
#lets add a new course before potato - who's index is 2
list_courses.insert(2, "uxd")

# lets print our list and see what has changed.
print list_courses

# ok, that potato is out of place, lets remove it!
list_courses.remove("potato")
# list.remove(obj) - removes the object from the room
# list.remove(index) - removes the item at index
# list.pop(index) - removes and returns item at index
# del(list[index]) - removes item at index

print list_courses

''' 
# other useful list functions
list.extend(seq) # appends a list to another
list.count(obj) # finds the number of appearance of an obj in a list
list.index(obj) # finds the index of an object in a list
list.sort() # sorts the actual given list
list.reverse() # reverses the actual given list
'''

'''
# Dictionaries {}
# Dictionaries are like lists, but they are accessed using a key rather than an index.
Like lists, they are also used to store data
'''
#Empty lists can be defined using {}

student_count = {"games": 16, "infoviz": 10, "uxd": 12, "viscom": 22}

print student_count

print "Games have %s sign ups for game" % (student_count["games"])

# adding a new entry is as easy as accessing the list
print "adding potato to list with 0 sign ups!"
student_count["potato"] = 0

print student_count

print "remove potato since it has no sign ups"
del student_count["potato"]
# student_count.remove("potato")

print student_count

''' 
# range and xrange
# range is another useful function, like xrange, but returns a list instead of an object(xrange is an object) 
# range(5) # returns [0,1,2,3,4] - range(stop)
# range(1, 6) # returns [1,2,3,4,5] - range(start, stop)
# range(1,6,3) # returns [1,4] - range(start, stop, step)
'''

print "extra functions"
# also useful are
print student_count.keys() # return a list of all the keys
print student_count.values() # return a list of all the values
print student_count.items() # returns a list of tuples


'''
# Battleship! - build the classic battle ship game, with functions, lists and conditionals
'''