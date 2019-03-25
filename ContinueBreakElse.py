shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
print(shopping_list)
for item in shopping_list:
	print("Buy {}".format(item))

print('----- Continue ------')
for item in shopping_list:
	if item == 'spam':
		continue
	print("Buy {}".format(item))
print("continue skips the item")
# Now we can see, spam will not be printed in the list
# So what happens is, 'continue' actually stops processing any more lines
# in the block and forces the for loop to move on to the next value in the
# sequence.
# In other words, when there was an == match, it looked at that line,
# and bypassed print statement.
print('----- Break ------')
for item in shopping_list:
	if item == 'spam':
		break
	print("Buy {}".format(item))
print("break, terminates the program")
# we found our statement, now exit immediately from the loop.

print('-------------')
# meal = ['egg', 'beacon', 'spam', 'sausages']
meal = ['egg', 'beacon', 'beans', 'sausages']  # removed spam

# nasty_food_item = ''  # initializing here first.
for item in meal:
	if item == 'spam':  # if we remove spam from the list, it will give error because of this line
		nasty_food_item = item
		break
else:
	nasty_food_item = ''  # initializing here first.
	print("I'll have a plate for that, then, please")

if nasty_food_item:
	print("Can I have anything without having spam in it")
