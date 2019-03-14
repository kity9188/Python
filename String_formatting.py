age = 24
#print("My age is " + age + " years")
# this will give error as only string can concatenate
#So let's change int to string
print("My age is " + str(age) + " years")
#str is a method
print("My age is {0} years".format(age))
#here {} is the replacement field/field to be formatted.
#second way to convert "int" to "string".

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31, "January", "March", "May",
     "July", "August", "October", "December"))
#passing the values in string formats

#OR

print("""January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28,30,31))

#From python2
print("My age is %d years" %age)
print("My age is %d %s, %d %s" %(age, "years", 6, "months"))
#for passing multiple values, put them all into bracket.
#d for interger data type, s for string.

#******************************************************
# Q: My question is how comma(,) is different from concatenation(+) and what are the pros and cons of using the same?
# A: When you use a comma, you're just telling the print function that there are several things to print. It's fine
#   for printing things when debugging (or to a log file), but very limited when displaying information to the user.
#******************************************************


for i in range(1,12):
    print("No %2d squared is %4d and cubed is %4d" %(i, i ** 2, i ** 3))
print("**************")
for i in range(1,5):
    print("No %2d squared is %d and cubed is %d" %(i, i ** 2, i ** 3))
    # ** means square, *** means cube. i.e., no of * = no of power to (2 ** 2 = 2 square)
    #value of d is passed from i

print("*************")

for i in range(1,12):
    print("No {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print("*************")

for i in range(1,12):
    print("No {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

print("**************")
#Precision of numbers
print("Pi is approximately %12f" %(22/7))#upto six decimal palces
print("Pi is approximately %12.50f" %(22/7))#upto 50 decimal points

print("****NNNN*****")
print("Pi is approximately {0:12.50f}".format(22/7))
# it is .50 not :50

#{} is the replacement field in python 5.


