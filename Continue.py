shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
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
