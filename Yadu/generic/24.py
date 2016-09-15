import os
import sys
import colorama
from termcolor import colored, cprint
from msvcrt import getch, getche

# init the colorama module
colorama.init()

def set_bg_color():
	# set bg color if possible to blue!
	if(os.name == 'nt'):
		try:
			os.system('color 1f') # 1 = blue, f = bright white - via: http://ss64.com/nt/color.html
		except:
			pass 
	elif(os.name == 'posix'):
		try:
			os.system('setterm -term linux -back $blue -fore white -clear')
		except:
			pass 

'''
game variables
'''
game_is_running = True
SCENE_MENU = 0
SCENE_SETUP = 1
SCENE_GAME = 2
SCENE_END = 3
current_scene = SCENE_MENU

SHIP_TYPE_SUB = {"name": "sub", "class": colored('S', 'red', 'on_grey', attrs=['reverse', 'blink']), "size": 2, "location": ["A0", "B0"]}
SHIP_TYPE_DESTROYER = {"name": "destroyer", "class": colored('D', 'white', 'on_magenta', attrs=['reverse', 'blink']), "size": 3, "location": ["A1", "B1", "C1"]}
SHIP_TYPE_CARRIER = {"name": "carrier", "class": colored('C', 'red', 'on_white', attrs=['reverse', 'blink']), "size": 3, "location": ["A2", "B2", "C2", "D2", "E2"]}


grid_player = []
grid_enemy = []

# setup screen vars
player_sub = SHIP_TYPE_SUB
player_destroyer = SHIP_TYPE_DESTROYER
player_carrier = SHIP_TYPE_CARRIER
setup_current_ship = "sub"
setup_active = False

'''
Helper functions
'''

def clear():
	''' clear the screen '''
	if(os.name == 'nt'):
		tmp = os.system("cls")
	elif(os.name == 'posix'):
		tmp = os.system("clear")
	else:
		pass # not handling anything else right now!
#-- end function clear

def p(txt):
	''' prints colored using a specific fore/bgcolor '''
	print colored(txt, 'white', 'on_blue')

def b(txt):
	''' prints colored using a specific fore/bgcolor '''
	print colored(txt, "white", "on_magenta")

def get_alphabets(n):
	''' takes a number and returns a sequence of alphabets in that length - 1 = A, 2 = B ... 26 = Z, 27 = AA, 28 == BB '''
	result = ""
	multiplier = 1
	index = 0
	for x in xrange(n):
		if(index >= 26): # Z
			index = 0
			multiplier += 1

		result += ("  %s " % (chr(65 + index) * multiplier))
		index += 1
	#-- end for
	return result
#-- end function get_alphabets

def make_grid(xcount, ycount, char = "~"):
	''' make ycount number of lists with xcount of char in them - X x Y grid '''
	g = []
	for y in xrange(ycount):
		g.append([]) # i append a list 
		for x in xrange(xcount):
			g[y].append(char)
	return g
#-- end function make_grid

def get_col(s):
	for index in xrange(26):
		if(s[0] == chr(65 + index)):
			return index
	return 0

def get_row(s):
	return int(s[1])

def update_ship_position(grid, ship):
	for item in ship["location"]:
		grid[get_row(item)][get_col(item)] = ship["class"]

def draw_grid(g):
	''' draws a grid made with make_grid '''
	h = len(g)
	w = len(g[0])
	row_index = 0

	clear()
	set_bg_color()
	
	print colored("\t  " + get_alphabets(w) + "  \t", "white", "on_blue")

	# for each row in grid
	for row in g:
		row_text = "" # reset grid row text

		# top bar of grid
		print colored("\t  +" + ("---+" * w) + "  \t", 'white', 'on_blue')

		# for each item in the row
		for item in row:
			if(item == "~"):
				row_text += colored(" %s |" % (item), 'white', 'on_blue')
			else:
				row_text += (colored(" ", 'white', 'on_blue') + item + colored(" |", 'white', 'on_blue'))
			#-- end for loop

		row_text = "\t%d |%s" % (row_index, row_text)
		row_text += colored(" " + str(row_index) + "\t", 'white', 'on_blue')
		print colored(row_text, 'white', 'on_blue')
		row_index += 1
		#-- end for loop

	# bottom bar of grid
	print colored("\t  +" + ("---+" * w) + "  \t", 'white', 'on_blue')
	print colored("\t  " + get_alphabets(w) + "  \t", "white", "on_blue")
#-- end function draw_grid


def get_user_selection():
	global game_is_running
	while(True):
		try:
			sel = int(raw_input(colored("\n\tSelect: ", "red", "on_white")))
			break
		except ValueError:
			b("Invalid selection, please try again!")
		except:
			game_is_running = False
			break
	return sel

def move_up():
	# print "up"
	pass

def move_down():
	# print "Down"
	pass

def move_left():
	# print "Left"
	pass

def move_right():
	global setup_active
	# print "right"

def select():
	#print "sel"
	pass

def escape():
	global setup_active
	#print "escape"
	setup_active = False

def update_input():
    key = ord(getch())
    if key == 27: #ESC
        escape()
    elif key == 13 or key == 32: #Enter # Spacebar
        select()
    elif key == 224: #Special keys (arrows, f keys, ins, del, etc.)
        key = ord(getch())
        if key == 80: #Down arrow
            move_down()
        elif key == 72: #Up arrow
            move_up()
        elif key == 75: #Left arrow
        	move_left()
        elif key == 77: #Right arrow
        	move_right()
#-- end function update_input

'''
Core game functions
'''
def show_scene_menu():
	global game_is_running
	global current_scene
	if(game_is_running == False):
		return

	clear()
	set_bg_color()

	p("\n")
	p("                                       |__")
	p("                                       |\/")
	p("                                       ---")
	p("                                       / | [")
	p("                                !      | |||")
	p("                              _/|     _/|-++'")
	p("                          +  +--|    |--|--|_ |-")
	p("                       { /|__|  |/\__|  |--- |||__/")
	p("                      +---------------___[}-_===_.'____                 /\\")
	p("                  ____`-' ||___-{]_| _[}-  |     |_[___\==--            \/   _")
	p("  __..._____--==/___]_|__|_____________________________[___\==--____,------' .7")
	p("  |                                                                     BB-61/")
	p("  \_________________________________________________________________________|")
	p("\n")
	b("\tBATTLESHIP 2016  ")
	p("\t1. New Game")
	p("\t2. Exit Game")
	# ASCII art source: http://ascii.co.uk/art/battleship
	# Battleship by Matthew Bace - Removed Signature from obove  

	if(get_user_selection() == 1):
		current_scene = SCENE_SETUP;
	else:
		game_is_running = False

	return
#-- end function show_scene_menu

def show_scene_setup():
	global game_is_running
	global current_scene
	global grid_player
	global grid_enemy
	global setup_active
	global setup_current_ship
	if(game_is_running == False):
		return

	grid_player = make_grid(10, 10)
	grid_enemy = make_grid(10, 10)

	setup_active = True
	while(setup_active):
		update_input()

	# temp!
	game_is_running = False

#-- end function show_scene_game

def show_scene_game():
	pass
#-- end function show_scene_game

def show_scene_end():
	pass
#-- end function show_scene_end


'''
Main game loop
'''

while(game_is_running):
	if(current_scene == SCENE_MENU):
		show_scene_menu()
	elif(current_scene == SCENE_SETUP): 
		show_scene_setup()
	elif(current_scene == SCENE_GAME):
		show_scene_game()
	elif(current_scene == SCENE_END):
		show_scene_end()
	else:
		current_scene = SCENE_MENU
#-- end while

#bs_grid = make_grid(10,10)
#draw_grid(bs_grid)


#clear the screen before we quit

clear()

# awesome outro!
print("\n")	
print("                                                                 .---.")
print("                                                                /  .  \\")
print("                                                               |\_/|   |")
print("    .----------------------------------------------------------------' |")
print("   /  .-.                                                              |")
print("  |  /   \                                                             |")
print("  | |\_.  |                Thank you for playing                       |")
print("  | `---' |                =--._..-x0-0x-.._.--=                       |")
print("  |       |                                                           /")
print("  |       |----------------------------------------------------------'")
print("   \     /")
print("    `---'")