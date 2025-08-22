# 1.7 String Formatting Operator
# 1.7.1 Using % operator for substitution

"""
One of Python's coolest features is the string format operator %. This operator is unique to strings and makes up for the pack of having functions from C's printf() family. 
Format specification symbols (%d %c %f %s etc) 
used in C language are used as placeholders in a string."""

#Using %s for string and d% or %i for sin
print("My name is %s and weight is %o  kg! height is %d"%('Shary',64,34))

#using %u for (unsigned decimal integer base10) and %o for (Octal integer base 8)
print("width :%u and height is: %o (Octal integer base 8)"%(42,42))

#Using %x for (Hexadecimal int lowercase letter) and %X for uppercase
print("{42} in Hexadecimal integer in lowercase:%x\n {50} in Hexadecimal intger in Uppercase :%X"%(42,50))

#using %e and %E: Exponential notation (with lowercase 'e' or uppercase 'E')
print("{12345.67} is:%e {12345678.543} is:%E"%(12345.67,12345678.543))

#%f: Floating point real number
print("{12.4567} in float round 2 decimal point:%.2f"%(12.4567))


# 1.7.2 Using the format() Method

"""Python 3.0, introduced format() method to str class for handling complex string formatting more efficiently."""
"""The string itself contains placeholders {} in which values of variables are successively inserted."""
name="Shary"
age=23
print("My name is {} and age is {} years".format(name,age))

"""You can use variables as keyword arguments to format() method and use the variable name as the placeholder in the string."""
print("My name is {name} and age is {age} years".format(name="SharyKhan",age=25))

"""You can also specify C style formatting symbols. Only change is using ":" instead of %. For example, instead of %s use {:s} and instead of %d use (:d}"""
print("My name is {:s} and age is {:d} years".format(name,age))

# 1.7.3 Using f-string Formatting

"""
With the version 3.6, Python introduced a new string formatting method,
f-strings or Literal String Interpolation. 
With this formatting method you can use embedded Python expressions inside string constants. 
Python f-strings are a faster, more readable, more concise, and less error prone.

The string starts with a 'f' prefix, and one or more place holders are inserted in it,
whose value is filled dynamically."""
name1="Umair"
height="5.6 cm"
fstring=f"My name is {name} and height is {height}"
print(fstring)

"""The placeholders can be populated by dictionary values."""
user={'name':"Fahad",'age':40}
print(f"your name is {user['name']} and age is {user['age']}")

"""The = character is used for self debugging the expression in f-string."""

price=20
quantity=5
print(F"Total: {price*quantity=}")

"""The f-strings can display numbers with hexadecimal, octal and scientific notation"""
num=30
print(f"Hexadecimal: {num:x}")
print(f"Octal: {num:o}")
print(f"Scientific notation :{num:e}")


# 1.7.4 Using String Template Class

"""
Python's standard library has string module.
It provides functionalities to perform different string operations.

The Template class in string module provides an alternative method to format the strings dynamically.
One of the benefits of Template class is to be able to customize the formatting rules."""

from string import Template
temp_str="My name is $name and i am $age years old "
temp_obj=Template(temp_str)
ret=temp_obj.substitute(name="Ali",age=34)
print(ret)

"""We can also unpack the key-value pairs from a dictionary to substitute the values."""

names={'name':"Muhammad",'age':25,"height":"5.6 cm"}
temp_str="My name is $name and i am $age years old and $height "
temp_obj=Template(temp_str)
ret1=temp_obj.substitute(**names)
print(ret1)
