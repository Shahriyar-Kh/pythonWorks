#Python - String Concatenation

"""
The "+" operator is well-known as an addition operator, 
returning the sum of two numbers. 
However, the "+" symbol acts as string concatenation operator in Python. 
It works with two string operands, and results in the concatenation of the two.

The characters of the string on the right of plus symbol are appended to the string on its left.
Result of concatenation is a new string.
"""
str1="Shahriyar"
str2=" Khan"
print("String 1:",str1)
print("String 2:",str2)
str3=str1+str2
print("String 3:",str3)

# Using (*) operator for repitation
"""
Another symbol *, which we normally use for multiplication of two numbers, 
can also be used with string operands. Here, * acts as a repetition operator in Python.
One of the operands must be an integer, and the second a string. 
The operator concatenates multiple copies of the string. """

#The "*" operator has a higher precedence over the "+" operator.
str4=str1+str2*3
print("String 4: ",str4)
str5=("\t"+str1+str2)*3
print("String 5:",str5.strip())


