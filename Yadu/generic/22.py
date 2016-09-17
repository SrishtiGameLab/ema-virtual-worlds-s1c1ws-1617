'''
try - except examples
'''


while True:
	try:
		something = int(raw_input("enter a number: "))
		break;
	except ValueError as err:
		print "Please enter a number!! Try again."
	except:
		exit()


print "thank you!"



while True:
	try:
		something = int(raw_input("enter a number: "))
		break;
	except:
		print "Please enter a number!! Try again."


print "thank you!"


try:
	print 100/0
except:
	print "div by 0!!"

print "potato!"