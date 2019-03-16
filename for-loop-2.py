# Let's suppose that we are processing data,
# exported from someone else's spread sheet program.
# And let's say that the spreadsheet was set
# to display numbers with commas or some other
# seperators.

number = "9,223,372,036,854,775,887"
for i in range(0, len(number)):
	if number[i] in '0123456789': #"in" function; it returns true if whatever we have in left hand side is actually in whatever is in the right hand side.
		print(number[i],end='')#above we are skipping commas