# Python Casting
### Specify a Variable Type
There may be times when we want to specify a type on to a variable. This can be done with casting.

Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:
* ***int()*** - constructs an integer number from an integer literal, a float literal (by rounding down to the previous whole number), or a string literal (providing the string represents a whole number)
* ***float()*** - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
* ***str()*** - constructs a string from a wide variety of data types, including strings, integer literals and float literals

Examples:
* Integers:

 Input | print() | Output
-------- | -------- | --------
x = int(1)    | print(x) | 1 
y = int(2.8)  | print(y) | 2
z = int("3")  | print(z) | 3

* Floats:

 Input | print() | Output
-------- | -------- | --------
x = float(1)    | print(x) | 1.0 
y = float(2.8)  | print(y) | 2.8 
z = float("3")  | print(z) | 3.0 
w = float("4.2") | print(w) | 4.2 

* Strings:

 Input | print() | Output
-------- | -------- | --------
x = str("s1")    | print(x) | s1 
y = str(2)  | print(y) | 2 
z = str(3.0)  | print(z) | 3.0 

_in string 3.0 is just a string, not a numeric value_