# Python Variables

Variables are nothing but reserved memory locations to store values. It means that when we create a variable, we reserve some space in the memory.

Based on the data type of a variable, the interpreter allocates memory and decides what can be stored in the reserved memory. Therefore, by assigning different data types to the variables, we can store integers, decimals or characters in these variables.

Creating variables has some rules which we should keep in mind.
variable name  has to start with either a letter (upper or lower case) or an underscore(_).
variable name can't be started with a number.
We can also use numbers in variable names, just not as the first letter.
We can declare same variable with Upper case and lower case letter as python will consider it distinct not same.

### Assigning Values to Variables
* eg:1
```python
greeting = "Hello" #assigning variable
name = str(input("Please enter your name: ")) #assigning variable at runtime
print(greeting+''+name) # printing variables
```
* eg:2
```python
c = a + b
d = c /3
e = d -4
print (e * 12)
```