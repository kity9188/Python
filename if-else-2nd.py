print("Please guess a number between 1 and 10: ")
guess = int(input())
#here no to be guessed is 5
if guess != 5 :
	if guess <5:
		print("Please guess higher")
	else: #guess must be greater than 5
		print("Please guess lower.")

	guess = int(input())
	if guess == 5:
		print("Well done, you guessed it!")
	else:
		print("Sorry, you haven't guessed correctly.")
else:
	print("You got it first time.")
