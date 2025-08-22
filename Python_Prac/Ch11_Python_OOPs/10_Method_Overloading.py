#Example 1
class Add:
    def add(self,a,b):
        result=a+b
        return result
    
    def add(self,a,b,c):
        result=a+b+c
        return result
    
obj1=Add()
print("Sum(three para): ",obj1.add(10,20,30))
#print("Sum(two para): ",obj1.add(10,20)) Show error
"""
Output
The first call to add() method with three arguments is successful. 
However, calling add() method with two arguments as defined in the class fails.
Python considers only the latest definition of add() method, discarding the earlier definitions.
"""

#Solve this issue
"""
To simulate method overloading, we can use a workaround by defining default value to method arguments as None, 
so that it can be used with one, two or three arguments.
"""  
class Add:
    def add(self,a=None,b=None,c=None):
        results=0
        if a!=None and b!=None and c!=None:
            results=a+b+c
        elif (a!=None and b!=None and c==None):
            results=a+b
        return results
obj2=Add()
print("Sum of Three number: ",obj2.add(10,20,30))
print("Sum of Two number: ",obj2.add(10,20))
#With this workaround, we are able to incorporate method overloading in Python class.

"""
Python's standard library doesn't have any other provision for implementing method overloading. 
However, we can use dispatch function from a third party module named MultipleDispatch for this purpose.

This module has a @dispatch decorator. It takes the number of arguments to be passed to the method to be overloaded. 
Define multiple copies of add() method with @dispatch decorator as below −
    """
#Example 3
from multipledispatch import dispatch
class Add:
    @dispatch(int,int)
    def add(self,a,b):
        result=a+b
        return result
    @dispatch(int,int,int)
    def add(self,a,b,c):
        result=a+b+c
        return result
    
obj1=Add()
print("\nSum(three para): ",obj1.add(10,20,30))
print("Sum(two para): ",obj1.add(10,20))