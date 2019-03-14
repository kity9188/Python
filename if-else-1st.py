name = input("Please input your name: ")
Age= int(input("How old are you, {0}?: ".format(name))) #Conversion: string => int

if Age >= 18:
	print("You're old enough to vote.")
	print("Please go ahead and vote.")
else:
	print("Please come back in {0}".format(18 - Age),"yrs")
	print("Please come back in {0} years".format(18 - Age))