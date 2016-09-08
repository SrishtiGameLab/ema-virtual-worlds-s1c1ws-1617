import os
import time
import colorama 
from termcolor import colored, cprint

colorama.init() # initalising colorama 

player_grid = []
enemy_grid = []

def bg_color():
	try:
		os.system('color 82')
	except:
		pass

def clear():
	os.system("cls")

def pause():
	time.sleep(2)

def get_alphabets(n):
	result = ""
	index = 0 
	for index in xrange(n):
		result += "  %s " % (chr(65 + index))
	return result

def make_grid(xcount, ycount, char = "X"):
	grid = []
	for y in xrange(ycount):
		grid.append([])
		for x in xrange(xcount):
			grid[y].append(char)
	return grid

def grid_size():
	
	xcount = int(raw_input("Enter the number of rows for your grid (max. 10): "))
	xcount = xcount % 10
	ycount = int(raw_input("Enter the number of columns for your grid (max. 10): "))
	ycount = ycount % 10
	
	if xcount < 5 or ycount < 5:
		print "This grid is too small to play with. Enter values bigger than 5."
		pause()
		clear()
		grid_size()
		return
	else:
		pass
	
	global player_grid, enemy_grid
	player_grid = make_grid(xcount, ycount)
	enemy_grid = make_grid(xcount, ycount)


#default values
ship_type_submarine = {"name" : "Submarine", "class" : "S", "size" : "2", "location" : ["A0", "B0"]}
ship_type_destroyer = {"name" : "Destroyer", "class" : "D", "size" : "3", "location" : ["A1", "B1", "C1"]}
ship_type_carrier = {"name" : "Carrier", "class" : "C", "size" : "5", "location" : ["A2", "B2", "C2", "D2", "E2"]}


#assigning default to player
player_submarine = ship_type_submarine
player_destroyer = ship_type_destroyer
player_carrier = ship_type_carrier


def get_col(s):
	for index in xrange(10):
		if s[0] == chr(65+index):
			return index
	return 0

def get_row(s):
	return int(s[1])

def del_wrong_ship(ship_type):
	a = 0
	b = 0
	while a < len(player_grid):
		while b < len(player_grid[0]):
			if player_grid[a][b] == ship_type["class"]:
				player_grid[a][b] = "X"

def update_grid(ship_type):
	for item in xrange(int(ship_type["size"])):
		new_sub = raw_input("Enter coordinate %s for placing your %s : " % (item+1, ship_type["name"]))
		x = get_col(new_sub)
		y = get_row(new_sub)

		if item == 0:
			old_x = x
			old_y = y
		
		if y >= 0 and x >= 0 and y < len(player_grid) and x < len(player_grid[0]):						#checking unavailable coordinates
			if (x == old_x and (y ==  (old_y + 1) or y == (old_y - 1) or y == old_y)) or (y == old_y and (x ==  (old_x + 1) or x == (old_x - 1) or x == old_x)):											#checking if such placement is logically possible
				if player_grid[y][x] == "X":										#checking for unoccupied coordinates
					player_grid[y][x] = (ship_type["class"])
				else:
					print "This coordinate is occupied. Please try entering the coordinates again." 
					del_wrong_ship(ship_type)			
					update_grid(ship_type)
	
			else:
				print "This placement of your %s is not possible. Please try entering the coordinates again." % (ship_type["name"])
				del_wrong_ship(ship_type)
				update_grid(ship_type)

		else:
			print "This coordinate doesn't exist. Please try entering the coordinates again."
			del_wrong_ship(ship_type)
			print "1"
			update_grid(ship_type)
		print_grid(player_grid)

	clear()
	


def print_grid(grid):
	clear()
	#bg_color()
	h = len(grid)											   #xcount
	w = len(grid[0])										   #ycount
	row_index = 0
	print colored("\n\n\n\t\t  %s" % (get_alphabets(w)), "white")           #for printing alphabets at the top of the grid 
	for row in grid:
		row_text = "" #reset row text
		print colored("\t\t  -" + ("----" * w), "white")        #for printing top line of the grid
		for item in row:                                      #for each column in a row
			if item == "X":
				row_text += colored(" X |", "white")
			else:
				row_text += colored(" %s |" % (item), "white")
		print colored("\t\t%s |%s" % (row_index, row_text), "white")
		row_index += 1
	print colored("\t\t  -" + ("----" * w), "white")           #for printing the bottom line of the grid
	print "\n\n"



grid_size()
pause()
clear(),
print_grid(player_grid)
pause()
pause()
update_grid(player_submarine)
update_grid(player_destroyer)
update_grid(player_carrier)
