choice = 0

while True:
	try:
		choice = int(raw_input("input number: "))
		break;
	except:
		print "Please input a valid number! Error"

print "thank you for selecting " + str(choice)