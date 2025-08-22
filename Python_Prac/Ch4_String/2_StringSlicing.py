# 1.5 Python Slicing Strings

"""
In Python, a string is an ordered sequence of Unicode characters. 
Each character in the string has a unique index in the sequence. 
The index starts with 0. First character in the string has its positional index 0. 
The index keeps incrementing towards the end of string.
"""
string="Shahriyar"
print(string[0])#output 1st letter S

print(string[0:6])#output shahri 

print(string[6::-1])#output  yirhahS opposite the above

print(string[0:-1])#Shahriya 

#start from 0 to 6 but 6 not include
print(string[:6])#Shahri

#start from 6 to end of string
print(string[6:])#yar

"""
In Python, string is an immutable object. The object is immutable 
if it cannot be modified in-place, once stored in a certain memory location.
You can retrieve any character from the string with the help of its index, 
but you cannot replace it with another character. In our example,
character Y is at index 7 in HELLO PYTHON. Try to replace Y with y and see what happens.
"""
#string[0]='s' #str' object does not support item assignment
#print(string)

"""
The left operand must be smaller than the operand on right, 
for getting a substring of the original string. 
Python doesn't raise any error, 
if the left operand is greater, bu returns a null string.
"""
print(string[6:2])#empty
print("[:5][:2]: ",string[:5][:2])#Sh because using and op those show wich in both

