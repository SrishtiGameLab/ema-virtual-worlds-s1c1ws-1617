

some_list = [1, 2, 3, 4, 5]

print some_list

for num in some_list:
	if(num % 2 == 0):
		some_list.remove(num)

some_other_list = [7, 9, 11]

# some_list = some_list + some_other_list
some_list.extend(some_other_list)

print some_list