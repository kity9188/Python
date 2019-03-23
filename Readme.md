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
a = 12
b = 3
c = a + b
d = c /3
e = d -4
print (e * 12)
```
- - - -
## Standard Data Types
Python has five standard data types −
* Numbers
* String
* List
* Tuple
* Dictionary

    1. Python Numbers:
        * var1 = 1
        * var2 = 10
        
        Python supports three different numerical types:
        * int (signed integers)
        * float (floating point real values)
        * complex (complex numbers)
        
       ```All integers in Python3 are represented as long integers. Hence, there is no separate number type as long.```
        
        Examples:
        
        int  | float | Complex
        ------------- | ------------- | -------------
        10  |    0.0     |  3.14j
        -786  | -21.9  |  -.6545+0J
        
        
        ```A complex number consists of an ordered pair of real floating-point numbers denoted by x + yj, where x and y are real numbers and j is the imaginary unit.```
        