# 1. Arguments
# Information can be passed into functions as arguments.

#Parameters or Arguments?
"""
The terms parameter and argument can be used for the same thing: information that are passed into a function.
From a function's perspective:
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called."""
# 1.1 Number argument
"""
By default, a function must be called with the correct number of arguments. 
Meaning that if your function expects 2 arguments, 
you have to call the function with 2 arguments, not more, and not less.
"""
def student(fname,lname):
    print(fname+ " " +lname)

#calling
student("Shary","Khan")

# 1.2 Default Aurguments
"""
Python allows to define a function with default value assigned to one or more formal arguments. 
Python uses the default value for such an argument if no value is passed to it. 
If any value is passed, the default value is overridden with the actual value passed.
"""
def printinf(name,age=35):
    " this prints a passed info this function  "
    print("Name: ",name)
    print("Age: ",age)
    return
#now calling function
printinf(name="Shary",age=17)#using passing age
printinf(name="Shahriyar")#when we dont pass age then using 35

#Example 2
def percent(phy,maths,maxmarks=200):
    var=(phy+maths)*100/maxmarks
    return var
#callin point 1
phy=60
maths=70
result=percent(phy,maths)#no pass maxmarks so use defaul
print("Percentage: ",result)
#calling point 2
phy=40
maths=46
result=percent(phy,maths,100)
print("Percentage: ",result)


# 1.3 Python - Keyword Arguments

"""
Python allows to pass function arguments in the form of keywords 
which are also called named arguments. 
Variables in the function definition are used as keywords. 
When the function is called, 
you can explicitly mention the name and its value."""

def keyword_arg(name,age):
    print("Name: ",name)
    print("Age: ",age)
#Now calling function by positional arguments
keyword_arg("S_Khan",30)

#calling with keyword arguments
keyword_arg(name="Shary",age=50)

#the positional arguments must be before the keyword arguments while using mixed calling.
#keyword_arg(name="Shary1",11)#error


# 1.4 Python - Keyword-Only Arguments

"""
You can use the variables in formal argument list as keywords to pass value.
Use of keyword arguments is optional. 
But, you can force the function be given arguments by keyword only.
You should put an 
astreisk (*) before the keyword-only arguments list."""

def inter(amt,*,rate):
    var=amt*rate/100
    return var
#intrest=inter(1000,10) error
inttrest=inter(1000,rate=10)
print(f"Intrest on {1000} is ={inttrest}")


# 1.5 Python - Positional Arguments

"""
The list of variables declared in the parentheses at 
the time of defining a function are the formal 
arguments. A function may be defined with any number of formal arguments.

While calling a function −

All the arguments are required

The number of actual arguments must be equal to the number of formal arguments.

Formal arguments are positional. They Pick up values in the order of definition.

The type of arguments must match.

Names of formal and actual arguments need not be same."""

def add(x,y):
   z=x+y
   print ("x={} y={} x+y={}".format(x,y,z))

a=10
b=20
add(a,b)

# 1.6 Python - Arbitrary Arguments

"""
You may want to define a function that is able to accept arbitrary or variable number of arguments.
Moreover, the arbitrary number of arguments might be positional or keyword arguments.

An argument prefixed with a single asterisk * for arbitrary positional arguments.

An argument prefixed with two asterisks ** for arbitrary keyword arguments."""

def add(*args):
    s=0
    for x in args:
        s=s+x
    return s
#calling and pass a tuple
result=add(10,20,30,40)
print("Sum of all items: ",result)
"""The args variable prefixed with "*" stores all the values passed to it. H
ere, args becomes a tuple. 
We can run a loop over its items to add the numbers."""
result=add(1,2,3,4,5)
print("Sum of all numbers: ",result)

#Example 2
def avg(first,*rest):
    second=max(rest)
    return (first+second)/2
result=avg(40,30,50,34)
print("average of first and best test: ",result)
#Explain  Example 2 
"""
Following call to avg() function passes first value to the required argument first,
and the remaining values to a tuple named rest. 
We then find the maximum and use it to calculate the average.
"""

#Example
"""
The following code is an example of a function with arbitrary keyword arguments.
The addr() function has an argument **kwargs which is able to accept any number 
of address elements like name, city, phno, pin, etc. 
Inside the function kwargs dictionary of kw:value pairs is traversed using items() method."""

def addr(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")
print("\n\nPassed two keyword args")
addr(Name="Jhon",City="Peshawer")

print("Passed four keywords args")
addr(Name="Shary",City="Charsadda",ph_no="1234456",pin="4455")


#Example
"""
Imagine a case where science and maths are mandatory subjects,
in addition to which student may choose any number of elective subjects.

The following code defines a percent() function where marks in science and marks are stored in required arguments, 
and the marks in variable number of elective subjects in **optional argument."""

def test(maths,sci,**Optional):
    print("\n\nMaths: ",maths)
    print("Sci: ",sci)
    #add maths and sci marks in S
    s=maths+sci
    #for loop for reaminning subject values
    for k,v in Optional.items():
        print(f"{k} : {v}")
        s=s+v
        return s/len(Optional)+2
    #call function with args
results=test(maths=80,sci=75,Eng=70,Hist=65,Geo=72)
print("Percentage: ",results)
