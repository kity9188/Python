# name = input("Please input your name: ")
# age= input("How old are you, {0}? ".format(name))
# print("This is 'string' data type "+age)
#
# #If we want age to represent a number, rather than a string,
# #we need to actually convert it.
# #We do that using the int function.
#
# Age= int(input("How old are you again, {0}?: ".format(name))) #Conversion: string => int
# #print("This is in 'int' data type " + Age) => This will give error of
# # concatenation as int + string data types has been used.
#
# if Age >= 18:  #int value 'Age' has been called out. not string 'age'.
# 	#Hence, case sensitive.
# 	print("You're old enough to vote.")
# 	print("Please go ahead and vote.")
# else:
# 	print("Please come back in {0}".format(18 - Age),"yrs")
# 	print("Please come back in {0} years".format(18 - Age))

######Phase II ###################

# print("Please guess a number between 1 and 10: ")
# guess = int(input())
# #here no to be guessed is 5
# if guess <5:
# 	print("Please guess higher")
# 	guess = int(input())
# 	if guess == 5:
# 		print("Well done, you guesses it!")
# 	else:
# 		print("Sorry, you haven't guessed correctly.")
# #elif stands for else if
# elif guess > 5:
# 	print("Please guess lower.")
# 	guess = int(input())
# 	if guess == 5:
# 		print("Well done, you guessed it!")
# 	else:
# 		print("Sorry, you haven't guessed correctly.")
# else:
# 	print("You got it first time.")

