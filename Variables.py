#Creating variables has some rules which we should keep in mind.
#variable name  has to start with either a letter (upper or lower case) or an underscore(_).
#variable name can't be started with a number.
#We can also use numbers in variable names, just not as the first letter.
#We can declare same variable with Upper case and lower case letter as python will consider it distinct not same.

greeting = "Kumar"
Greeting = "There"
_myName = "Nicketa"
#1nicks= "Good"    starting with numeral will give error
nicks100= "Good" # but we can use numerals at any other position while declaring variables.
Nick_Was_16 = "Hello" #Another way of declaring a variable in Python

print(Nick_Was_16+" "+greeting)

#age = 24
#print(greeting + age) # This will give error that python can't convert int to string
#   "can only concatenate str (not "int") to str"
#   Instead we can write:
age = "24"  # now variable age is a string
print(greeting+' '+age)
print("******************")

a = 12
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)  #o/p will be floating point becz it's a division (use // if want to get a whole number as below)
print(a//b) #no of times b has been used to get a (o/p will be same but / gives floating point and // gives whole number)
print(a%b)  #remainder
print("******************")

for i in range (1,5):
    print(i)

#Python understands well operator precedence. The result is what it should be,
# not by what operator has been used first.
print(a + b / 3 - 4 * 12)
print(8 / 2 * 3)
print(8 * 3 / 2)
#Python actually need parenthesis. Below one will give the same output. Change value to see result.
print((((a + b)/3)-4)*12)

bun_price = 2.40 #if we change the value i.e., say 2.40 to 3 or 4; the data type will change from float to int.
money = 15
#print(money // bun_price)
#In order to change int/float data type into string
bun = str(money // bun_price)
print("The no of buns that can be purchased = "+ bun +" bun")

c = a + b
d = c /3
e = d -4
print (e * 12)