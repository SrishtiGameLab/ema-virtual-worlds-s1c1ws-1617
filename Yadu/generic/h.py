import os
import time
import random
import colorama 
from termcolor import colored, cprint

colorama.init() # initalising colorama 

r = random.Random()

player_grid = []			#player's grid (a list) empty in the beginning
AI_grid = []				#computer's grid (a list) empty in the beginning
player_targets_AI_grid = []	#grid shown on players screen to depict the hits it has made

player_count = 0
AI_count = 0

game_is_running = True
scene_menu = 0
scene_setup = 1
scene_game = 2
scene_end = 3
current_scene = scene_menu

#default values of the ships
ship_type_submarine = {"name" : "Submarine", "class" : "S", "size" : "2", "location" : ["A0", "B0"], "hitpoints":[0,0], "color" :"blue"}
ship_type_destroyer = {"name" : "Destroyer", "class" : "D", "size" : "3", "location" : ["A1", "B1", "C1"], "hitpoints":[0,0,0],"color" :"green"}
ship_type_carrier = {"name" : "Carrier", "class" : "C", "size" : "5", "location" : ["A2", "B2", "C2", "D2", "E2"], "hitpoints":[0,0,0,0,0], "color" :"yellow"}


#helper functions for the game 

def bg_color():									#function to change background colour
	try:
		os.system('color 82')
	except:
		pass
								
def clear():									#function to clear the screen
	os.system("cls")

def pause():									#function to create a 2 second pause on screen
	time.sleep(2)

def get_alphabets(n):							#funtion to generate a string of 'n' number of alphabets which goes
	result = ""
	index = 0 
	for index in xrange(n):
		result += "  %s " % (chr(65 + index))
	return result

def get_char_int(n):
	return chr(65 + n)

def make_grid(xcount, ycount, char = "X"):			#function that creates the grid with default data of "X"
	grid = []
	for y in xrange(ycount):
		grid.append([])
		for x in xrange(xcount):
			grid[y].append(char)
	return grid

def grid_size():									#function that takes the input of the size of grid to play
	global player_grid
	global AI_grid
	global player_targets_AI_grid 
	
	clear()
	print "\n\n"
	xcount = int(raw_input("\tEnter the number of rows for your grid (max. 10): "))
	if (xcount%10) == 0:
		xcount = 10
	else:
		xcount = xcount % 10
	print "\n"
	ycount = int(raw_input("\tEnter the number of columns for your grid (max. 10): "))
	if (ycount%10) == 0:
		ycount = 10
	else:
		ycount = ycount % 10
	
	if xcount < 5 or ycount < 5:
		print "This grid is too small to play with. Enter values bigger than 5."
		pause()
		clear()
		grid_size()
		return
	else:
		pass
	
	player_grid = make_grid(xcount, ycount)				#making player's grid - entering default data
	AI_grid = make_grid(xcount, ycount)					#making computer's grid - entering default data
	player_targets_AI_grid = make_grid(xcount, ycount)

def get_col(s):											#function to get index value of x coordinate of the grid
	for index in xrange(10):
		if s[0] == chr(65+index):
			return index
	return 0

def get_row(s):											#function to get index value of y coordinate of the grid
	return int(s[1])

def del_wrong_ship(ship_type, new_grid):				#function to delete the ship if it is placed on a wrong position 
	a = 0
	b = 0
	while a < len(new_grid):
		while b < len(new_grid[0]):
			if new_grid[a][b] == ship_type["class"]:
				new_grid[a][b] = "X"
			b += 1
		a += 1
		b = 0

def update_grid_player(ship_type, new_grid):			#function that updates the player's grid with ship coordinates

	for item in xrange(int(ship_type["size"])):

		new_ship = raw_input("\tEnter coordinate %s for placing your %s (for eg. A0, B6) : " % (item+1, ship_type["name"]))

		x = get_col(new_ship)
		y = get_row(new_ship)

		if item == 0:
			old_x = x
			old_y = y
		
		if y >= 0 and x >= 0 and y < len(new_grid) and x < len(new_grid[0]):						#checking for availability of coordinates
			
			if (x == old_x and (y ==  (old_y + item) or y == (old_y - item) or y == old_y)) or (y == old_y and (x ==  (old_x + item) or x == (old_x - item) or x == old_x)):											#checking if such placement is logically possible
				
				if new_grid[y][x] == "X":										#checking for unoccupied coordinates
					new_grid[y][x] = (ship_type["class"])
				else:
					print "\n\t This coordinate is occupied. Please try entering the coordinates \n\t again."
					pause() 
					del_wrong_ship(ship_type, new_grid)		
					print_grid(new_grid)	
					update_grid_player(ship_type, new_grid)
					return()
	
			else:
				print "\n\t This placement of your %s is not possible. Please try \n\t entering the coordinates again." % (ship_type["name"])
				pause()
				del_wrong_ship(ship_type, new_grid)
				print_grid(new_grid)
				update_grid_player(ship_type, new_grid)
				return()

		else:
			print "\n\tThis coordinate doesn't exist. Please try entering the coordinates \n\t again."
			pause()
			del_wrong_ship(ship_type, new_grid)
			print_grid(new_grid)
			update_grid_player(ship_type, new_grid)
			return()
		print_grid(new_grid)

	clear()
	print_grid(new_grid)

def update_grid_AI(ship_type, new_grid):				#function that upgrades computer's grid with ship coordinates

	for item in xrange(int(ship_type["size"])):

		if item == 0:
			y = r.randint(0, (len(new_grid) - 1))
			x = r.randint(0, (len(new_grid[0]) - 1))
			old_y = y
			old_x = x
		else:
			if ship_type["class"] == 'S' or ship_type["class"] == "D":
				x =  old_x + item
				y = old_y
			else:
				x = old_x
				y = old_y + item

		if y >= 0 and x >= 0 and y < len(new_grid) and x < len(new_grid[0]):						#checking for availability of coordinates
			if new_grid[y][x] == "X":										#checking for unoccupied coordinates
				new_grid[y][x] = (ship_type["class"])
			else:
				del_wrong_ship(ship_type, new_grid)			
				update_grid_AI(ship_type, new_grid)
				return()
	
		else:
			del_wrong_ship(ship_type, new_grid)
			update_grid_AI(ship_type, new_grid)
			return()			
		
def player_shoots(new_grid):							#function to check whether player's shot is a hit or a miss
	global player_targets_AI_grid
	global current_scene
	global scene_end

	clear()
	print_grid(player_targets_AI_grid)
	target = raw_input("\n\n\tEnter the coordinates of your target (for eg. D4, C2) : ")

	x = get_col(target)
	y = get_row(target)

	if y >= 0 and x >= 0 and y < len(new_grid) and x < len(new_grid[0]):        #checking for avability of the entered coordinates

		if new_grid[y][x] == "X":
			index = ["3", y, x]
			print_grid(new_grid, index)
			print "\n\n\n\t\t\t          MISS"
		else:
			if new_grid[y][x] == "S":
				try:
					val = player_submarine["location"].index(get_char_int(x) + str(y));
					print player_submarine["hitpoints"]
					player_submarine["hitpoints"][val] = 1
					print player_submarine["hitpoints"]
				except ValueError:
					print player_submarine["location"]

			index = ["2", y, x]
			print_grid(new_grid, index)
			print "\n\n\n"
			print "\t\t\t            HIT"
			print "\t\t\tYou just hit enemy's ship."
			global player_count 
			player_count += 1

		if player_count == 10:
			pause()
			clear()
			print "\n\n\n\n\n\n\t\t\tYou win."
			pause()
			pause()
			current_scene = scene_end

	else:
		print "\t\t This coordinate doesn't exist. Please try entering the coordinates \t\t again."
		pause()
		player_shoots(new_grid)
		return()

	pause()						



def AI_shoots(new_grid):							#function to check whether computer's shot is a hit or a miss
	global player_grid
	global scene_end
	global current_scene

	y = 0 # r.randint(0, (len(new_grid) - 1))
	x = 0 # r.randint(0, (len(new_grid[0]) - 1))

	clear()
	print_grid(player_grid)
	pause()
	if new_grid[y][x] == "X":
		#print_grid(new_grid)
		print "\t\t                  MISS"
		print "\t\tEnemy tried to hit your ship, but failed."
		pause()
	else:
			
		index = ["1", y, x]
		print_grid(new_grid, index)
		print "              HIT"
		print "Enemy just hit one of your ships."
		pause()
		global AI_count 
		AI_count += 1

		if AI_count == 10:
			clear()
			print "\n\n\n\n\n\n\t\t\tComputer wins."
			pause()
			pause()
			current_scene = scene_end

def print_grid(grid, index = [0, 0, 0]):			#function that prints the grid
 
	clear()
	#bg_color()
	h = len(grid)											   #xcount
	w = len(grid[0])										   #ycount
	row_index = 0
	print colored("\n\n\n\t\t  %s" % (get_alphabets(w)), "white")           #for printing alphabets at the top of the grid 
	print colored("\t\t  -" + ("----" * w), "white")        #for printing top line of the grid
	
	if index[0] == "1":								#print the grid where a ship is detsroyed in red

		a = 0
		b = 0
		row_text = ""
		while a < len(grid):
			while b < len(grid[0]):
				if a == index[1] and b == index[2]:
					row_text += colored(" %s " % (grid[a][b]), "red")
					row_text += colored("|", "white")
				elif grid[a][b] == "S":
					row_text += colored(" %s " % (grid[a][b]), "blue")
					row_text += colored("|", "white")
				elif grid[a][b] == "D":
					row_text += colored(" %s " % (grid[a][b]), "green")
					row_text += colored("|", "white")
				elif grid[a][b] == "C":
					row_text += colored(" %s " % (grid[a][b]), "yellow")
					row_text += colored("|", "white")
				else:
					row_text += colored(" X |", "white")
				b += 1
			print colored("\t\t%s |%s" % (row_index, row_text), "white")
			print colored("\t\t  -" + ("----" * w), "white")
			a += 1
			b = 0
			row_index += 1
			row_text = ""
			
	elif index[0] == "2":								#print the grid where player shoots at the ship and hits 
		a = 0
		b = 0
		row_text = ""
		while a < len(grid):
			while b < len(grid[0]):
				if a == index[1] and b == index[2]:
					row_text += colored(" X ", "green")
					row_text += colored("|", "white")
				else:
					row_text += colored(" X |", "white")
				b += 1
			print colored("\t\t%s |%s" % (row_index, row_text), "white")
			print colored("\t\t  -" + ("----" * w), "white")
			a += 1
			b = 0
			row_index += 1
			row_text = ""

	elif index[0] == "3":								#print the grid where player shoots at the ship and misses
		a = 0
		b = 0
		row_text = ""
		while a < len(grid):
			while b < len(grid[0]):
				if a == index[1] and b == index[2]:
					row_text += colored(" X ", "red")
					row_text += colored("|", "white")
				else:
					row_text += colored(" X |", "white")
				b += 1
			print colored("\t\t%s |%s" % (row_index, row_text), "white")
			print colored("\t\t  -" + ("----" * w), "white")
			a += 1
			b = 0
			row_index += 1
			row_text = ""

	else:										#print the grid with default values - 'S': blue, 'D': green, 'C': yellow, and rest in white

		for row in grid:
			row_text = "" #reset row text
				
			for item in row:                                      #for each column in a row
				if item == "X":
					row_text += colored(" X |", "white")
				elif item == "S":
					row_text += colored(" %s " % (item), "blue")
					row_text += colored("|", "white")
				elif item == "D":
					row_text += colored(" %s " % (item), "green")
					row_text += colored("|", "white")
				elif item == "C":
					row_text += colored(" %s " % (item), "yellow")
					row_text += colored("|", "white")
			print colored("\t\t%s |%s" % (row_index, row_text), "white")
			print colored("\t\t  -" + ("----" * w), "white")
			row_index += 1

	print "\n\n"


# core game functions

def main_selection():
	global game_is_running
	while(True):
		try:
			sel = int(raw_input("\n\t\t\tEnter your choice : "))
			break
		except ValueError:
			print "Invalid selection, please try again!"
		except:
			game_is_running = False
			break
	return sel

def show_scene_menu():
	global game_is_running
	global current_scene
	global scene_setup

	if game_is_running == False:
		return

	clear()

	print "\n\n\n"
	print "                                       |__"
	print "                                       |\/"
	print "                                       ---"
	print "                                       / | ["
	print "                                !      | |||"
	print "                              _/|     _/|-++'"
	print "                          +  +--|    |--|--|_ |-"
	print "                       { /|__|  |/\__|  |--- |||__/"
	print "                      +---------------___[}-_===_.'____                 /\\"
	print "                  ____`-' ||___-{]_| _[}-  |     |_[___\==--            \/   _"
	print "  __..._____--==/___]_|__|_____________________________[___\==--____,------' .7"
	print "  |                                                                     BB-61/"
	print "  \_________________________________________________________________________|"
	print "\n\n\n"
	print colored("\t\t\tBATTLESHIP", "red")
	print "\t\t\t1. New Game"
	print "\t\t\t2. Exit"

	if(main_selection() == 1):
		current_scene = scene_setup
	else:
		game_is_running = False

	return

def show_scene_setup():
	global game_is_running
	global current_scene
	global scene_game
	global player_grid
	global player_submarine
	global player_destroyer
	global player_destroyer
	global AI_grid
	global AI_submarine
	global AI_destroyer
	global AI_carrier

	if game_is_running == False:
		return

	grid_size()
	print_grid(player_grid)
	print "\t\t    This is your default grid."
	pause()

	#assigning default values to player's ships
	player_submarine = ship_type_submarine
	player_destroyer = ship_type_destroyer
	player_carrier = ship_type_carrier

	#assigning default values to computer's ships
	AI_submarine = ship_type_submarine
	AI_destroyer = ship_type_destroyer
	AI_carrier = ship_type_carrier

	clear()
	print_grid(player_grid)

	update_grid_player(player_submarine, player_grid)
	update_grid_player(player_destroyer, player_grid)
	update_grid_player(player_carrier, player_grid)
	print "\t\t    This is your grid with the ships."
	pause()
	pause()
	update_grid_AI(AI_submarine, AI_grid)
	update_grid_AI(AI_destroyer, AI_grid)
	update_grid_AI(AI_carrier, AI_grid)
	print_grid(AI_grid)
	print "\t\t    This is computer's grid with ships."
	pause()
	pause()

	current_scene = scene_game

def show_scene_game():
	global game_is_running
	global player_grid
	global AI_grid

	if game_is_running == False:
		return

	clear()

	while(current_scene == scene_game):

		clear()
		print "\n\n\n\n\n\n\t\t\t\tIts your turn."
		pause()
		player_shoots(AI_grid)
		pause()
		if player_count == 10:
			break
		clear()
		print "\n\n\n\n\n\n\n\t\t\t\tIts computer's turn."
		pause()
		AI_shoots(player_grid)
		if AI_count == 10:
			break

def show_scene_end():
	global current_scene
	global scene_menu
	global game_is_running

	clear()
	print "\n\n\n\n\n\n\t\t\t1. New Game"
	print "\t\t\t2. Exit"

	if(main_selection() == 1):
		current_scene = scene_menu
	else:
		game_is_running = False


# main game

while(game_is_running):
	if current_scene == scene_menu:
		show_scene_menu()
	elif current_scene == scene_setup:
		show_scene_setup()
	elif current_scene == scene_game:
		show_scene_game()
	elif current_scene == scene_end:
		show_scene_end()
	else:
		current_scene = scene_menu

clear()

print "\n"
print "                                                                    .---."
print "                                                                   /  .  \\"
print "                                                                  |\_/|   |"
print "       .----------------------------------------------------------------' |"
print "      /  .-.                                                              |"
print "     |  /   \                                                             |"
print "     | |\_.  |                Thank you for playing                       |"
print "     | `---' |                =--._..-x0-0x-.._.--=                       |"
print "     |       |                                                           /"
print "     |       |----------------------------------------------------------'"
print "      \     /"
print "       `---'"






