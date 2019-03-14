####Quiz#########
meal1 = "spam" + "eggs" + "beans"
meal2 = "spam\neggs\nbeans"
meal3 = "spam, eggs, beans"
meal4 = """spam
eggs
beans"""
print(meal2)
print(meal4)

first_name = "John"
last_name = "Cleese"
age = 78
#print(first_name + last_name + age)


a = 45
b = 15
c = 3

print(a - b / c)



quantity = 10
price = 5.0
total = quantity * price
tax = total / 5

Total = total + tax

print(total)


days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])

data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
#print(data[::5]) #This slice starts at the first character and goes to the end
#of the string, extracting every 5th. The result will be 12345678


data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[1:5])
#This slice will start at position 1, which is the : after 1, up to (but not including) the 2. The result will be :A,

flower= "blue violet"
print(flower == 'blue')
print('blue' in flower)

flower= "rose"
colour= "red"
print("the {0} is {1}".format(flower,colour))
