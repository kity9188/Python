greeting = "Hello"
name = input("Please enter your name: ")
print(greeting+' '+name)

print("*************")

splitString = "This string has been \nsplit over \nseveral\nlines"
print(splitString)

anotherSplitString = """This has been
slpit over 
several lines"""
print(anotherSplitString)
print("*************")

tabbedString = "1\t2\t3\t4\t5\t6\t"
print(tabbedString)
print("*************")
#If we want to use '' as the outer one, then we have to use \ where ever
#we are using ' again. Same goes for ".
print('The pet shop owner said "No, no, \'e\'s uh,.....he\'s resting"')
print("The pet shop owner said \"No, no, 'e's uh,.....he's resting\"")
print('''The pet shop owner said "No, no, 'e's uh,.....he's resting"''')
print("""The pet shop owner said "No, no, 'e's uh,.....he's resting" """)