# Basic Operators
Operators are the constructs, which can manipulate the value of operands. 

## Types of Operator
Python language supports the following types of operators:
* Arithmetic Operators
* Comparison (Relational) Operators
* Assignment Operators
* Logical Operators
* Bitwise Operators
* Membership Operators
* Identity Operators

## Python Arithmetic Operators

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

## Python Comparison| Relational Operators

Operator  |   Description   |   Example   
---------- | --------------- | ----------
( == ) | If the values of two operands are equal, then the condition becomes true. | (a == b) is not true.
( != ) | If values of two operands are not equal, then condition becomes true. | (a!= b) is true.
( > ) | If the value of left operand is greater than the value of right operand, then condition becomes true. | (a > b) is not true.
( < ) | If the value of left operand is less than the value of right operand, then condition becomes true. | (a < b) is true.
( >= ) | If the value of left operand is greater than or equal to the value of right operand, then condition becomes true. | (a >= b) is not true.
( <= ) | If the value of left operand is less than or equal to the value of right operand, then condition becomes true. | (a <= b) is true.

Here a=10, b=20.

## Python Assignment Operators

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