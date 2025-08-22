#Example 
class Employee:
    def __init__(self):
        self.var=10
        return
obj=Employee()
print("class of int",type(int))
print("class of list",type(list))
print("class of dict",type(dict))

print("class of Employee",type(Employee))

# 
anon=type('',(object,),{})
#To create an object of this anonymous class −
obj=anon()
#The result shows that the object is of anonymous class
print("types of obj:",type(obj))
#The result shows that the object is of anonymous class

#Example 2
"""
We can also add instance variables and instance methods dynamically. Take a look at this example −
    """
# Define a function getA to be used as an instance method
def getA(self):
    # Return the value of the 'a' attribute
    return self.a

# Use the type function to dynamically create a class
# Arguments: class name (''), base classes (object,), and a dictionary with attributes and methods
# This dynamically created class has attributes 'a', 'b', and 'c', and methods 'getA' and 'getB'
# The 'getA' method is defined using the getA function, and the 'getB' method is defined using a lambda function
obj1 = type('', (object,), {'a': 3, 'b': 5, 'c': 6, 'getA': getA, 'getB': lambda self: self.b})()

# Call the getA and getB methods of the dynamically created class and print the results
print(obj1.getA(), obj1.getB())
