import time

a = float(raw_input("gimme a number: "))

if a == 100:
	print "a is 100"



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


