#Example 1
import math
print("Square root of 100: ",math.sqrt(100))

#create module
def hello(name):
     print("Hi {}! how are you? ".format(name))
     return
           
#The import Statement
"""
In Python, the import keyword has been provided to load a Python object from one module. 
The object may be a function, class, a variable etc. 
If a module contains multiple definitions, 
all of them will be loaded in the namespace.
"""

#import modules as alies

import mymodules as md
print("Sum: ",md.sum(10,10))
print("average: ",md.avg(10,10))
print("power: ",md.power(10,2))

#list all the function names (or variable names) in a module. The dir() function:
x=dir(md)
print("The all function names (or variable names) in mymodules: ",x)

#The from ... import Statement
"""
The import statement will load all the resources of the module in the current namespace. 
It is possible to import specific objects from a module by using this syntax
"""
#Example From ... import statement
from mymodules import  sum,avg
print("Sum : ",sum(10,40))
print("Average: ",avg(10,40))
"""
Note: When importing using the from keyword, do not use the module name when referring to elements in the module
"""
#Example Module Attributes 
import mymodules
print("\n******************************************")
#1. __file__ returns the physical name of the module.
print("__file__attribute: ",mymodules.__file__)# c:\Users\Shahriyar Khan\Desktop\Python_Prac\Ch3_Function\mymodules.py

#2. __package__ returns the package to which the module belongs.
print("__package__attribute: ",mymodules.__package__)#

#3. __doc__ returns the docstring at the top of the module if any
print("__doc__attribute: ",mymodules.__doc__)#The doc string of mymodules

#4. __dict__ returns the entire scope of the module
#print("__dict__attribute: ",mymodules.__dict__)

#5. __name__ returns the name of the module
print("__name__attribute: ",mymodules.__name__)#The doc string of mymodules
print("\n******************************************")

#The reload() Function
"""
Sometimes you may need to reload a module, especially when working with the interactive interpreter session of Python.

Even if you edit the test.py file and save it, the function loaded in the memory won't update.
You need to reload it, using reload() function in imp module.

"""
import imp
imp.reload(mymodules)
mymodules.sum(5,6)

