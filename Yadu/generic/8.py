my_fname = "Yadu"
my_lname = "Rajiv"

msg = "He said: \"what is the meaning of this!?\""

another_msg = "and then I said: \'lolwut\'"

print msg
print another_msg


print my_fname.lower()
print my_lname.upper()

print "hello! how are you".upper()

print len(my_fname)
print len(my_lname)
print len("hello! how are you")

my_value = 42 ** 42

print str(my_value)

my_name = my_fname + " " + my_lname
print my_name

print "Hello " + str(42)

user_fname = raw_input("What is your first name? ")
user_lname = raw_input("What is your last name? ")
user_color = raw_input("What is yor fav color? ")

# Hello lname, fname. I hear you like color
print "Hello %s, %s.\nI hear you like %s" % (user_lname, user_fname, user_color)