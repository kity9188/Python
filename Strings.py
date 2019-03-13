parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])
#3 means 3rd character starting from zero of parrot
# N o r w e g
# 0 1 2[3]   so it will print "w"
print(parrot[0])
print(parrot[9])
print(parrot[-1]) #to print from right to left
print(parrot[0:6]) #zero to 6th character
print(parrot[:6]) #same as previous
print(parrot[6:]) #after 6th position
print(parrot[-4:-2]) #it gone to 4th character from right and then from there to right so Bl
#Sometimes it skips character
print(parrot[0:6:2])
print(parrot[0:6:3])

number= "9,223,372,036,854,775,807"
print(number[1::4])
numbers= "1,2,3,4,5,6,7,8,9"
print(numbers[0::3])
string1= "he's "
string2= "probably "
print(string1 + string2)
print("he's ""probably ""pining")

#Multiply of strings
print("hello \n"*5)
print("hello "*5)
print("hello "*(5+4))
print("hello "*5+"4") #will append 4 at the end

today = "friday"
print("day" in today)
#in is an operator. day is a word in letter friday.
print("fri" in today)
print("thru" in today) #will be false
print("parrot" in "friday") #false