from msvcrt import getch, getche

def move_up():
	# print "up"

def move_down():
	# print "Down"

def move_left():
	# print "Left"

def move_right():
	# print "right"

def select():
	#print "sel"

def escape():
	#print "escape"

def update_input:
    key = ord(getch())
    if key == 27: #ESC
        escape()
    elif key == 13 or key == 32: #Enter
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