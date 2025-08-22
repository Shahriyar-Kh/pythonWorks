#1.9.1 Case Conversion Methods

#Example 1 Capitalize() method
"""The capitalize() method returns a string with only its first character capitalized."""
var="hi how are you"
mvar=var.capitalize()
print("Orignal String: ",var)
print("Modify String: ",mvar)

#Example 2 casefold() Method
"""
The casefold() method is a new addition to string methods. The .casefold() method returns a copy of a string with all characters in lowercase. 
It is similar to .lower(), but whereas that method deals purely with ASCII text, .casefold() can also convert Unicode characters"""

var="I AM LIVING IN PAKISTAN"
mvar=var.casefold()
print("\nOrignal String: ",var)
print("Modify String: ",mvar)

#Example 3 lower() Method
mvar=var.lower()
print("\nOrignal String: ",var)
print("Modify String: ",mvar)

#Example 4 swapcase() Method
var2="This Is Python Practices"
mvar1=var2.swapcase()
print("\nOrignal String: ",var2)
print("Modify String: ",mvar1)

#Example 5 title and upper()

# 1.9.2 Alignment Methods

"""Following methods in the str class control the alignment of characters within the string object.
Syntax
Following is the syntax for center() method −
"""
#Example 1 center(width[, fillchar])

var = "This Is String Example....WOW!!!"
var1 = var.center(40, '*')
print ("original string:", var)
print ("Centered string:", var1)

#Example 2 ljust(width[, fillchar]) Method
var = "This Is String Example....WOW!!!"
var1 = var.ljust(40, '*')

print ("\noriginal string:", var)
print ("Left justified string:", var1)

#Example 3 rjust(width[, fillchar]) Method
var = "This Is String Example....WOW!!!"
var1 = var.rjust(40, '*')

print ("\noriginal string:", var)
print ("Rigth justified string:", var1)

#Example 4 expandtabs(tabsize = 8) Method
var = "this is\tstring example....wow!!!"
var1 = var.expandtabs()
var2 = var.expandtabs(24)
print ("\noriginal string:", var)
print ("string with default expanded tab:", var1)
print ("string with tripple expanded tab:", var2)

#Example zfill (width) Method
var="Hello python"
var1=var.center(40)
var2=var.ljust(40, '*')
var3=var.rjust(40, '*')
print ("original string: ", var)
print ("centered:", var1)
print ("left justified: ", var2)
print ("right justified:", var3)
var="Hello\tPython"
var4=var.expandtabs(16)
print ("capitalized:",var4)
var=-1234.50
var5=str(var).zfill(10)
print ("zfilled:", var5)

# 1.9.3 Split and join method
#usign strip() for remove the white spases of start working of lstrip() and rstrip()
Svar="         Shahriyar khan"
Rvar=Svar.strip()
print("Orignal   String: ",Svar)
print("Istripped string: ",Rvar)

#using lstrip(remove spaces from start) and rstrip(from end)
num="0001234400"
num2=num.lstrip('0')
num3=num.rstrip('0')
print("Orignal String : ",num)
print("lStripped String: ",num2)
print("rStripped String: ",num3)

#using Split() This method returns a list of strings.

name="My name is shahriyar khan"
print("Orignal string: ",name)
print("list of split strings: ",name.split())
print("First three word split :",name.split(" ",3))

#using splitlines() This method returns a list of lines in the string
name1='''my
name
is 
shahriyar
khan'''
splitline=name1.splitlines()
print("Orignal string: ",name1)
print("Splitlinse String in list: ",splitline)

#also use this
print("Splitlinse String in list: ",name1.splitlines(True))
#using removesuffic and removeprifex

print("Remove prefix 'my': ",name.removeprefix('My'))

# 1.9.6  Find and Replace Methods

#Example using count(sub,start,end)
uni="Abasyn university"
print("Orignal string: ",uni)
print(f"Count i {uni}: ",uni.count('i'))
print(f"Count 'i' in first 10 character {uni}: ",uni.count('i',0,10))

#Example find() Method
print("i is found at: ",uni.find('i'))
print("sity is found at: ",uni.find('sity',0,10))

#example replace() method
print("sity is replace with city:",uni.replace('sity','city'))

# 1.9.7 Translation Methods

# maketrans()
"""
The maketrans() method returns a mapping table. 
It maps each character from astr to a character at same index in bstr. 
The mapping table returned by this method may be used by translate() method to replace the characters.

Syntax
var.maketrans(astr, bstr, cstr)"""

name3="Explicit is better than implicit "

#translation table creation 
table=name3.maketrans({"i":"I"})#his line creates a translation table using the maketrans method. The dictionary {"i": "I"} specifies that every occurrence of the letter 'i' in the string should be replaced with 'I'. The resulting table variable holds the translation table.

#Printing Original String and Translation Table:
print("\nOrignal String :",name3)
print("Translation table: ",table)

#String Translation:
var3=name3.translate(table)#This line applies the translation table to the original string using the translate method. It replaces every 'i' with 'I' according to the specified translation rule.
print("Translated string: ",var3)

#Second example
table1=name3.maketrans("than","THEN")
print("Tranlation table: ",table1)
var4=name3.translate(table1)
print("Translated string: ",var4)

#Third Example
#where 'i' is mapped to 'a', and 's' is removed.
tableone = name3.maketrans("is","as", "s") 
print ("original string:", name3)
print ("translation table:", tableone)#This line uses the translate method to apply the translation table to the original string (var). It replaces 'i' with 'a' and removes 's' based on the specified translation rules."""
var5=name3.translate(tableone)
print ("Translated string", var5)


#1.9.5 Join()
"""
The join() method takes all items in an iterable and joins them into one string.
A string must be specified as the separator."""
list=['S','h','a','h','r','y']
print(''.join(list))# Output Shahry

