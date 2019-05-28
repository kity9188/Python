# Python Numbers
Python has three types of numeric:
* int
* float
* complex

Variables of numeric types are created when we assign a value to them:
e.g.:
~~~
x = 1    # int
y = 2.8  # float
z = 1j   # complex
~~~
To verify the type of any object in Python, use the `type()` function:
~~~
print(type(x))
print(type(y))
print(type(z))
~~~
Output will be:
~~~
<class 'int'>
<class 'float'>
<class 'complex'>
~~~

## 1. Int
Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
E.g.:
~~~
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
~~~
## 2. Float
Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
E.g.:
~~~
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
~~~
_Float can also be scientific numbers with an "e" to indicate the power of 10._
e.g. 5e10 = 5 x 10<sup>10</sup>
```
x = 35e3 # 35 x 10^3
y = 12E4 # 12 x 10^4
z = -87.7e100 # -87.7 x 10^100

print(type(x))
print(type(y))
print(type(z))
```
print(value)|Output  | print(type)|Output
------------- | ------------- | ------------- | -------------
print(x)  | 35000.0 | print(type(x)) | <class 'float'>
print(y)  | 120000.0 | print(type(y)) | <class 'float'>
print(z)  | -8.77e+101 | print(type(z)) | <class 'float'>

## 3. Complex
Complex numbers are written with a "j" as the imaginary part:
E.g.,
~~~
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
~~~
