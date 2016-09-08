'''
Take any string
replace chars with the following
A = 4
l = 1
e = 3
s = $
t = 7
'''



def leet_text_convert(txt):
	result = ""
	for char in txt:
		if(char == "A"):
			result += "4"
		elif(char.lower() == "l"):
			result += "1"
		elif(char.lower() == "e"):
			result += "3"
		elif(char.lower() == "s"):
			result += "$"
		elif(char.lower() == "t"):
			result += "7"
		else:
			result = result + char

	return result


print leet_text_convert("This is so frigging cool! I'm so leet!")