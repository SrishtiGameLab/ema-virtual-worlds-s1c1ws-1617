'''
Get the flower names and colors from the user, create poem

____ are ____
____ are ____
In Soviet Russia
Poems write you
'''
flower_1 = raw_input("Name a flower: ")
color_1 = raw_input("What color is a %s: " % (flower_1))`
flower_2 = raw_input("Name another flower: ")
color_2 = raw_input("What color is a %s: " % (flower_2))

raw_input("Are you ready for my great poem?")

print "%s are %s\n%s are %s\nIn Soviet Russia\nPoems write you" % (flower_1, color_1, flower_2, color_2)