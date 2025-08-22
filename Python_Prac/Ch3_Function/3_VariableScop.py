#Python globals() Function
"""
Python's standard library includes a built-in function globals(). It returns a dictionary 
of symbols currently available in global namespace."""

name="Shary"
marks=69
result=True
def myfunction():
    a=10
    b=20
    return a+b

print(globals())
#show the usag of global variable in python

#global variable

x=5
y=10
def add():
    sum=x+y
    return sum

print(add())

#Python's standard library includes a built-in function locals(). 
"""
It returns a dictionary of symbols currently available in the local namespace of the function.

Modify the above script to print dictionary of 
global and local namespaces from within the function."""


name="Shary Khan"
marks=89
result=True
def myfunction1():
    a=10
    b=20
    c=a+b
    print("\n\nGlobals(): ",globals())
    print("\n\nLocals(): ",locals())
    print(locals().get('a'))#shows 10
    return c

myfunction1()
#USING get() method and index op for both global and locals function return
print(globals()["name"])#display shary

#Namespace Conflict in Python
"""
If a variable of same name is present in global as well as local scope,
Python interpreter gives priority to the one in local namespace."""

marks=50 #This is a gloabal variable
def myfunction2():
    marks=80 #this is a local variable
    print("\n\nLocal marks: ",marks) #print local marks
myfunction2()
print("Global marks:",marks) #print global marks

#Modify global variable
"""T
o modify a global variable, you can either update it with a dictionary syntax, 
or use the global keyword to refer it before modifying."""
var1=100 #global
var2=50
def myfunction3():
    #local=marks+30 #UnboundLocal error
    #so modify global values two methods
    globals()['var1']=globals()['var1']+20
    
    #also this
    global var2
    var2=var2+10
    
myfunction3()
print("var1: ",var1,"\nvar2: ",var2)#show global variables with modify values

    