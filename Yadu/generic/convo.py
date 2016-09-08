b = raw_input ("Are you going upstairs?")

import time 

if b.lower() =="yes":
	c = raw_input("Can you do me a favor?")
	if c.lower() =="yes":
		print "Just take these books upstairs for me"
		time.sleep(2)
		print"sure"
else: 
	print "No. I'm not anything urgent?"