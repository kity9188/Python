meal = ['egg', 'beacon', 'spam', 'sausages']

nasty_food_item = ''  # initializing here first.
for item in meal:
	if item == 'spam':  # if we remove spam from the list, it will give error because of this line
		nasty_food_item = item
		break

if nasty_food_item:
	print("Can I have anything without having spam in it")

print('-------With else------------')
food = ['egg', 'beacon', 'beans', 'sausages']  # removed spam to print else statement.
# nasty_food_item = ''  # initializing here first.
for item in food:
	if item == 'spam':
		nasty_food_item = item
		break
else:
	nasty_food_item = ''  # initializing here first.
	print("I'll have a plate for that, then, please")

#  As spam is not present in the food list, else statement will be printed.
