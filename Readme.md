# Continuous, Break & Else statements

## Continue
Continue actually stops processing any more lines
in the block and forces the for loop to move on to the next value in the
sequence.

In other words, when there was an == match, it looked at that line,
and bypassed print statement.

```python
shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

for item in shopping_list:
	if item == 'spam':
		continue
	print("Buy {}".format(item))
print("continue skips the item")
```
## Break
This is used to terminate the statement, once we found our code. i.e., _we found our statement, now exit immediately from the loop._
```python
shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

for item in shopping_list:
	if item == 'spam':
		break
	print("Buy {}".format(item))
print("break, terminates the program")
```
## Else
If the condition is not available in the code, it will print the result.
```python
food = ['egg', 'beacon', 'beans', 'sausages']
for item in food:
	if item == 'spam':
		nasty_food_item = item
		break
else:
	nasty_food_item = ''
	print("I'll have a plate for that, then, please")
#  As spam is not present in the food list, else statement will be printed. 
```