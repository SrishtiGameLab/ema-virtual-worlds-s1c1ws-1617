'''

1. game design
2. infoviz
3. prgramming
4. illustration
5. sculpting

Please select a course (select from 1 - 5): 

-- not on the list
The course you have selected is not on the list, please try again.
<show list>

-- on the list
Thank you for selecting <course title>. Hope you have fun.

exit.

'''

import os

def clear():
	if(os.name == 'nt'):
		tmp = os.system("cls")
	else:
		tmp = os.system("clear")


list_of_units = ["game design","infoviz","prgramming","illustration","sculpting"]	


def show_list(msg = None):
	clear()
	c = 1

	if(msg != None):
		print msg

	print "Please select one of the following units (1 - %d)\n" % (len(list_of_units))

	for unit in list_of_units:
		print "\t%d. %s" % (c, unit)
		c += 1

	ui = 0
	while(True):
		try:
			ui = int(raw_input("\n\tYour choice: "))
			break;
		except ValueError as err:
			print "\n\tWrong input, please try again!"
		except:
			exit()

	validate_user_input(ui)


def validate_user_input(user_input):
	if(user_input > 0 and user_input <= len(list_of_units)):
		print "Thank you for selecting %s, we hope you have a great time!" % (list_of_units[user_input])
	else:
		show_list("Unknown unit selected, please try again!")

show_list()
