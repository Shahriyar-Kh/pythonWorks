#Example 1 
num=20
print (type(num))
num1=55.50
print (type(num1))
s="TutorialsPoint"
print (type(s))
dct={'a':1,'b':2,'c':3}
print (type(dct))
def SayHello():
   print ("Hello World")
   return
print (type(SayHello))

"""In Python, the Object class is the base or parent class for all the classes, 
built-in as well as user defined.
The class keyword is used to define a new class"""
class Classname:
    "Optional class documentation string"
    class_suite
    
"""
The class has a documentation string, which can be accessed via ClassName.__doc__.

The class_suite consists of all the component statements defining class members, data attributes and functions.
        """

#Example 2
class Emp(obj):
    "Common base class for all employee"
    pass

"""
Any class in Python is a subclass of object class, 
hence object is written in parentheses. 
However, later versions of Python don't require object to be put in parentheses.
        """
class Emp:
        "Common base class for all employee"
        pass
#To define an object of this class, use the following syntax −
obj=Emp()#create Emp class instance or object
    