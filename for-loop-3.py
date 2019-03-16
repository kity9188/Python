# end='' => '\n'
number = "9,223,372,036,854,775,887" #Number -> String
cleanedNumber = '' #String -> Number
for i in range(0, len(number)):
	if number[i] in '0123456789':#removing commas
		cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))