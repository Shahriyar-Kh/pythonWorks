# 1.6 Python - Modify Strings
"""
In Python, a string (object of str class) is of immutable type.
An immutable object is the one which can be modified in place,
one created in the memory. Hence, unlike a list, any character in the sequence cannot be overwritten, 
nor can we insert or append characters to it unless we use certain string method that returns a new string object.
"""

#tricks as a workaround to modify a string.
"""
Converting a String to a List
Since both string and list objects are sequences, they are interconvertible. 
Hence, if we cast a string object to a list, modify the list either by 
insert(), append() or remove() methods and convert the list back to a string, 
to get back the modified version."""

s1="Shahriyar Khan"
print("Orignal String ",s1)

# 1.6.1 convert string to list then modify string
list1=list(s1)
print("convert string to list :",list1)

list1.insert(0,'s')
print("Modify list: ",list1)

s1=''.join(list1)
print("modify String is: ",s1)

#1.6.2 Using Uppercase and lower case

#String in upper case
print(f"{string} is in Upper case: ",string.upper())

#String in lower case
print(f"{string} is in lower case: ",string.lower())

# 1.6.3 Using the Array Module
"""
To modify a string, construct an array object. Python standard library includes array module.
We can have an array of Unicode type from a string variable."""

#   Example 
import array as ar
s1="Word"
sAr=ar.array('u',s1)

"""perform array operations such as append, insert, remove etc. Let us insert L before the character D"""
sAr.insert(3,'L')
print("Modified array: ",sAr)

"""Now, with the help of tounicode() method, get back the modified string"""
print("Orignal string: ",s1)
s1=sAr.tounicode()
print("Modified String: ",s1)

# 1.6.4 Using the StringIO Class
"""
Python's io module defines the classes to handle streams. 
The StringIO class represents a text stream using an in-memory text buffer. 
A StringIO object obtained from a string behaves like a File object. 
Hence we can perform read/write operations on it. 
The getvalue() method of StringIO class returns a string."""

import io
s2="Shahriyar"
print("Orignal String :",s2)
sIO=io.StringIO(s2)#Convert string to Io class
sIO.seek(9)
sIO.write("Khan")
s2=sIO.getvalue()

print("Modified String: ",s2)

