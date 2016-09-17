'''
lists - loops, create, append, pop
'''

my_units = ["games", "viscom", "banana"]

my_units.append("cake")

for item in my_units:
	print item

print "----"

# list.pop(index) - 

print "we are removing the item - " + my_units.pop(len(my_units) - 1)

print "----"


for item in my_units:
	print item