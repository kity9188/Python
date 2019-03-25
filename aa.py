number = "9,223,372,036,854,775,807"
cleanNumber = ''

for i in range(0, len(number)):
	if number[i] in '0123456789':
		cleanNumber = cleanNumber + number[i]
		# cleanNumber += number[i]

newNumber = int(cleanNumber)
print("The number is {}".format(newNumber))

x = 23
x += 1
print(x)

# now x = 24
x -= 4
print(x)

# now x = 20
x *= 5
print(x)

# now x = 100
x /= 4
print(x)

# now x = 25.0   ; x is taking the last value obtained from previous calculation
x **= 2   # x = x**2 , x**2 = x to the power 2
print(x)

x %= 60
print(x)

greeting = "Good"
greeting += "morning"
print(greeting)

greeting *= 5
print(greeting)
