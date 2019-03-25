shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shopping_list:
	print("Buy {}".format(item))

for item in shopping_list:
	if item == 'spam':
		break
	print("Buy {}".format(item))
print("break, terminates the program")
# we found our statement, now exit immediately from the loop.
