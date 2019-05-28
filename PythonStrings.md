# Python Strings
### String Literals
String literals in python are surrounded by either single quotation marks, or double quotation marks.
`'hello'` is the same as `"hello"`

Strings can be output to screen using the print function. For example: `print("hello")`

Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters. 
However, Python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string.

Example:
Get the character at position 1 (remember that in python, position starts from 0. Say: 0,1,2,...):
~~~
a = "Hello, World!"
print(a[1])
~~~
Substring. Get the characters from position 2 to position 5 (not included):
~~~
b = "Hello, World!"
print(b[2:5])
~~~
The strip() method removes any whitespace from the beginning or the end:
~~~
a = " Hello, World        !      "
print(a.strip())
~~~
The upper() method returns the string in upper case:
~~~
a = "Hello, World!"
print(a.upper())
~~~
The len() method returns the length of a string:
~~~
a = "Hello, World!"
print(len(a))
~~~
The replace() method replaces a string with another string:
~~~
a = "Hello, World!"
print(a.replace("H", "J"))
~~~
The split() method splits the string into substrings if it finds instances of the separator:
~~~
a = "Hello, World!"
print(a.split(","))
~~~
 Input | Output
-------- | --------
print(a[1]) #for a = "Hello, World!"| e
print(b[2:5]) #for b = "Hello, World!" | llo
print(a.strip()) #for a = " Hello, World        !      " | Hello, World        !
print(len(a)) #for a = "Hello, World!" | 13
print(a.lower()) #for a = "Hello, World!" | hello, world!
print(a.upper()) #for a = "Hello, World!" | HELLO, WORLD!
print(a.replace("H", "J")) #for a = "Hello, World!" | Jello, World!
print(a.split(",")) #for a = "Hello, World!" | ['Hello', ' World!']

