'''
datetime and conditions
'''

from datetime import datetime

now = datetime.now()
i = raw_input("what do you want? (date or time): ")

if i.lower() == "time":
	print "The time is %s:%s" % (now.hour, now.minute)
elif i.lower() == "date":
	print "The date is %s/%s/%s" % (now.day, now.month, now.year)
else:
	print "I don't know what " + i + " means."
