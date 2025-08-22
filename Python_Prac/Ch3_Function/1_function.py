#create function
def function_Name():
    "this is doc string of greetings function"
    print("Hello word!")
    return
function_Name()

#calling a function
def printme(str):
    "This prints a passed string into this function"
    print(str)
    return;
#now you can call printme function
printme("\ni am first call to user defined function!")
printme("Again second call to the same function")

#Pass by Reference vs Value
"""
The function calling mechanism of Python differs from that of C and C++. There are two main function calling mechanisms:
    Call by Value and Call by Reference."""
#Pass string variable
def testfunction(arg):
    print("Id inside the function: ",id(arg))
var="Hello"
print("\nId before passing: ",id(var))
testfunction(var)

#Pass numaric varaible
"""
The behaviour also depends on whether the passed object is mutable or immutable. Python numeric object is immutable. When a numeric object is passed, and then the function changes the value of the formal argument, it actually creates a new object in the memory, 
leaving the original variable unchanged."""

def testfuntion2(arg):
    print("Id inside the function: ",id(arg))
    arg=arg+1
    print("new object after increment",arg,id(arg))
var=10
print("\nId before passing: ",id(var))
testfuntion2(var)
print("value after function call: ", var)

#passing list or dictionary
def listFunction(arg):
    arg=arg.append(100)
    print("inside the function: ",arg)
    print("Inside and modify the list in function: ",id(arg))
    
list=[10,20,30,40]

print("\nList after function call :",list)
print("\nId before passing: ",id(list))

listFunction(list)

print("List after function call :",list)
print("Id after the function calling: ",id(list))

#Function Arguments
"""
The process of a function often depends on certain 
data provided to it while calling it. 
While defining a function, you must give a 
list of variables in which the data passed to it is collected. 
The variables in the parentheses are called formal arguments.

When the function is called, value to each of the formal arguments must be provided. 
Those are called actual arguments."""

def string(name):
    "This is docString of greetting function  "
    print(f"\nHello {name}")
    return
string("Shary ")
string("Khan  ")
string("jan")

#Function with Return Value
"""
The return keyword as the last statement in function 
definition indicates end of function block, 
and the program flow goes back to the calling function.
Although reduced indent after the last statement in the block also implies return 
but using explicit return is a good practice.

Along with the flow control, the function can also return value of an expression to the calling function. 
The value of returned expression can be stored in a variable for further processing."""

def add(a,b):#step 1,step5
    result=a+b#step 6
    return result#step 7
n1=10#step2
n2=20#step3
result=add(n1,n2)#step 4,8
print(f"Addition of {n1} + {n2} is = {result}")#step 9

