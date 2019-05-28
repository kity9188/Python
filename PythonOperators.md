# Python Operators

***Operators***: Operators are the constructs, which can manipulate the value of operands.

Python divides the operators in the following groups:
* Arithmetic Operators
* Comparison (Relational) Operators
* Assignment Operators
* Logical Operators
* Bitwise Operators
* Membership Operators
* Identity Operators

## 1. Python Arithmetic Operators

Operator | Description | Example
--------------- | ----------------------- | -------------
 ( + ) Addition | Adds values on either side of the operator. | a + b = 30
 ( - ) Subtraction | Subtracts right hand operand from left hand operand. | a – b = -10
 ( * ) Multiplication | Multiplies values on either side of the operator. | a * b = 200
 ( / ) Division | Divides left hand operand by right hand operand | b / a = 2.0
 ( % ) Modulus | Divides left hand operand by right hand operand and returns remainder | b % a = 0
 ( ** ) Exponent | Performs exponential (power) calculation on operators | a**b =10 to the power 20
 ( // ) Floor Division | The division of operands where the result is the quotient in which the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity) | 9//2 = 4 and 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0

Here a=10, b=20.

## 2. Python Comparison| Relational Operators

Operator  |   Description   |   Example   
---------- | --------------- | ----------
( == ) | If the values of two operands are equal, then the condition becomes true. | (a == b) is not true.
( != ) | If values of two operands are not equal, then condition becomes true. | (a!= b) is true.
( > ) | If the value of left operand is greater than the value of right operand, then condition becomes true. | (a > b) is not true.
( < ) | If the value of left operand is less than the value of right operand, then condition becomes true. | (a < b) is true.
( >= ) | If the value of left operand is greater than or equal to the value of right operand, then condition becomes true. | (a >= b) is not true.
( <= ) | If the value of left operand is less than or equal to the value of right operand, then condition becomes true. | (a <= b) is true.

Here a=10, b=20.

## 3. Python Assignment Operators

Operator  |  Description  |  Example  
---------- | ------------------ | ----------
( = ) |	Assigns values from right side operands to left side operand | c = a + b assigns value of a + b into c
( += ) Add AND | It adds right operand to the left operand and assign the result to left operand | c += a is equivalent to c = c + a
( -= ) Subtract AND | It subtracts right operand from the left operand and assign the result to left operand | c -= a is equivalent to c = c - a
( *= ) Multiply AND	| It multiplies right operand with the left operand and assign the result to left operand | c *= a is equivalent to c = c * a
( /= ) Divide AND |	It divides left operand with the right operand and assign the result to left operand | c /= a is equivalent to c = c / ac /= a is equivalent to c = c / a
( %= ) Modulus AND | It takes modulus using two operands and assign the result to left operand | c %= a is equivalent to c = c % a
( **= ) Exponent AND | Performs exponential (power) calculation on operators and assign value to the left operand | c **= a is equivalent to c = c ** a
( //= ) Floor Division | It performs floor division on operators and assign value to the left operand | c //= a is equivalent to c = c // a

## 4. Python Logical Operators
Logical operators are used to combine conditional statements:
Operator  |  Description  |  Example  
---------- | ------------------ | ----------
and | Returns True if both statements are true | x < 5 and  x < 10
or | Returns True if one of the statements is true | x < 5 or x < 4
not | Reverse the result, returns False if the result is true | not(x < 5 and x < 10)

~~~
x = 5

print(x > 3 and x < 10)

# returns True because 5 is greater than 3 AND 5 is less than 10
~~~

## 5. Python Bitwise Operators

Bitwise operator works on bits and performs bit-by-bit operation.
Say a = 60 and b = 13
=> in binary
* a = 0011 1100
* b = 0000 1101

So

* a&b (AND)= 0000 1100
* a|b (OR)= 0011 1101
* a^b (XNOR)= 0011 0001
* ~a (NOT)= 1100 0010 

Python's built-in function bin() can be used to obtain binary representation of an integer number.

Operator  |  Description  |  Example  
--------- | ------------- | ----------
( & ) Binary AND  |  Operator copies a bit, to the result, if it exists in both operands.  |  (a & b) (means 0000 1100)
( | ) Binary OR  |  It copies a bit, if it exists in either operand.  |  (a | b) = 61 (means 0011 1101)
( ^ ) Binary XOR  |  It copies the bit, if it is set in one operand but not both.  |  (a ^ b) = 49 (means 0011 0001)
( ~ ) Binary Ones Complement  |  It is unary and has the effect of 'flipping' bits.  |  (~a ) = -61 (means 1100 0011 in 2's complement form due to a signed binary number.
( << ) Binary Left Shift  |  The left operand's value is moved left by the number of bits specified by the right operand.  |  a << 2 = 240 (means 1111 0000)
( >> ) Binary Right Shift  |  The left operand's value is moved right by the number of bits specified by the right operand.  |  a >> 2 = 15 (means 0000 1111)

[Logic Gate](https://en.wikipedia.org/wiki/Logic_gate) | [Bitwise Operators](https://en.wikipedia.org/wiki/Bitwise_operations_in_C) | [Python Bitwise Operators](https://wiki.python.org/moin/BitwiseOperators) | [Logic Gate](https://whatis.techtarget.com/definition/logic-gate-AND-OR-XOR-NOT-NAND-NOR-and-XNOR)

## 6. Python Membership Operators
Membership operators are used to test if a sequence is presented in an object:
Operator  |  Description  |  Example  
--------- | ------------- | ----------
 in | Returns True if a sequence with the specified value is present in the object | x in y
 not in | Returns True if a sequence with the specified value is not present in the object | x not in y
 
~~~
x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list
~~~
.
~~~
x = ["apple", "banana"]

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list
~~~
## 7. Python Identity Operators
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
Operator  |  Description  |  Example  
--------- | ------------- | ----------
 is | Returns true if both variables are the same object | x is y
 is not | Returns true if both variables are not the same object | x is not y

~~~
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have thew same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
~~~

## Python Operators Precedence
![picture alt](https://i.stack.imgur.com/ne01T.png)