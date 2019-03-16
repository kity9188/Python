# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and under 31).
# If they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry.

n = (input("Please enter your name: "))
a = int(input("Please enter your age {}: ".format(n)))

if (a>17) and (a<31):
	print("Welcome to club 18-30 holidays {}".format(n))
else:
	print("Sorry {}, our holiday is package if for 18-30 age group only.".format(n))