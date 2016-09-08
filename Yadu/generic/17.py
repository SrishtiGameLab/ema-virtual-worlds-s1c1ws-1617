

text = "this is a test"

count = len(text) # 14
index = 0

'''
# print each char in text
while index < count: # 0 - 13 - loops 14 times
	print text[index]
	index += 1

# same in for loop
for char in text:
	print char

'''

'''
index = 0
while index < count:
	if(text[index].lower() == "a"):
		break
	else:
		print text[index]

	index += 1
'''


for char in text:
	if(char.lower() == "a"):
		continue
	else:
		print char

	print "*"

