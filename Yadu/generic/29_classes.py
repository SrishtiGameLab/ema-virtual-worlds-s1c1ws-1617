'''
importing a pirate class from a file
'''
import pirate

n = raw_input("What do they call ye, you scallywag!!: ")

print pirate.PirateName(n).gen()