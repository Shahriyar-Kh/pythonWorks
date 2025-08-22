#Example 1 annotations
"""
Annotations are ignored at runtime, 
but are helpful for the IDEs and static type checker libraries such as mypy."""

def myfunction(a: int, b: int):
    c=a+b
    return c

print(myfunction(10,20))
print(myfunction("Hello ","Khan"))

#You can give annotation for the return data type as wel
def myfunction(a:int, b: int) ->int:
    c=a+b
    return c
"""
As using the data type as annotation is ignored at runtime, 
you can put any expression which acts as the metadata for the arguments.
"""
#arbitrary expression as annotation as in following example −
def total(x: 'marks in Physics', y:'marks in English'):
    return x+y

#The __annotations__ attribute itself is a dictionary in which arguments are keys and anootations their values.

def myfunction(a: "physics", b:"Maths" = 20) -> int:
   c = a+b
   return c
print (myfunction.__annotations__)


#You may have arbitrary positional and/or arbitrary keyword arguments for a function. Annotations can be given for them also.

def myfunction(*args:'arbitrary_args', **kwargs: 'arbitrary_keyword_args') -> int:
   pass
print (myfunction.__annotations__)

#import modules
import Moduls
Moduls.hello("Khan")
