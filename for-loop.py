# A for loop actually takes a range of values and assigns
# them one by one to a variable.
# Then it executes a block of code once for each value.

for i in range (1,20):
	print("i is now {}".format(i))

number = "9,223,372,036,854,775,887"
for i in range(0, len(number)):
	print(number[i])
# "len" is a function which is an abbreviation for length
# and it actually returns the length of a string.
# So in our case, it actually returns 25 characters
# if (see number).
#
# The way we actually access individual characters in a
# string, they actually start from zero and end at whatever
# the length is minus one. So in this case, the length
# is 25-1 which is 24.
# #####################################
# Let's suppose that we are processing data,
# exported from someone else's spread sheet program.
# And let's say that the spreadsheet was set
# to display numbers with commas or some other
# seperators.

number = "9,223,372,036,854,775,887"
for i in range(0, len(number)):
	if number[i] in '0123456789': #"in" function; it returns true if whatever we have in left hand side is actually in whatever is in the right hand side.
		print(number[i],end='')#above we are skipping commas
