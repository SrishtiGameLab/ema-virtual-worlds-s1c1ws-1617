def mul(argument1, argument2):
	return argument1 * argument2

def respond(a, b):
	return "multiply %s and %s and you get %s" % (a, b, mul(a,b)) 

print respond(5, 10)