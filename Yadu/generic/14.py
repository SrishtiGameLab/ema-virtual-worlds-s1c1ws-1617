def super_fun():
	print "this is super fun!!"

def not_fun():
	print "this is boring!! let me out of hear!!"



my_name = "Yadu Rajiv"

# print len(my_name)


'''
def square_me(num):
	squared = num ** 2
	return squared
'''

def square_me(num):
	return num ** 2

#print square_me(len(my_name))
#print square_me(5)

def mul(val1, val2):
	return val1 * val2

def complex_math(val1, val2):
	return mul(square_me(val1), square_me(val2))

print complex_math(100,20)
print complex_math(4,5)


