'''
battleship part - making a grid, getting an alphabet list
'''

def make_grid(xcount, ycount, char = "~"):
	''' make ycount number of lists with xcount of char in them - X x Y grid '''
	g = []
	for y in xrange(ycount):
		g.append([]) # i append a list 
		for x in xrange(xcount):
			g[y].append(char)
	return g
#-- end function make_grid

test = make_grid(10, 10)

def get_alphabets(n):
	''' takes a number and returns a sequence of alphabets in that length - 1 = A, 2 = B ... 26 = Z, 27 = AA, 28 == BB '''
	result = ""
	multiplier = 1
	index = 0
	for x in xrange(n):
		if(index >= 26): # Z
			index = 0
			multiplier += 1

		result += ("  %s " % (chr(65 + index) * multiplier))
		index += 1
	#-- end for
	return result
#-- end function get_alphabets

print get_alphabets(142)