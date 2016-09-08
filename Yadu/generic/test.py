# Assignment

import os 
import time 

def clear():
	tmp = os.system("cls")

def right_output(choice):
	if choice == 1:
		output = "Thank you for selecting Game Design. Hope you have fun."
	elif choice == 2:
		output = "Thank you for selecting Infoviz. Hope you have fun."
	elif choice == 3:
		output = "Thank you for selecting Programming. Hope you have fun."
	elif choice == 4:
		output = "Thank you for selecting Illustration. Hope you have fun."
	else:
		output = "Thank you for selecting Sculpting. Hope you have fun." 
	return output

def show_list():
	print "The courses available for this semester are:\n1. Game Design\n2. Infoviz\n3. Programming\n4. Illustration\n5. Sculpting"
	
	ri = raw_input("Please select a course (1-5) : ")
	choice = int(float(5.5))

	if choice > 0 and choice < 6 :
		print right_output(choice)
	else :
		print "The course you have selected is not on the list, please try again."
		time.sleep(3)
		clear()
		show_list()
	
show_list()