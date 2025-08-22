#Example 1
#Creating class
class Employee:
    #This is emp doc
    "Abasyn employees"
    #Create class constructor(Overload)
    def __init__(self,name="Shary",age=24):
        #Create instance (object) variable
         self.name1=name
         self.age1=age
    #create function
    def displayEmp(self):
        print("Name: ",self.name1,"\tAge: ",self.age1)
        
#print the output
print("Employee.__doc__:",Employee.__doc__)
print("Employee.__name__(Class_name):",Employee.__name__)
print("Employee.__module__:",Employee.__module__)
print("Employee.__bases__:",Employee.__bases__)
print("Employee.__dict__:",Employee.__dict__)

"""
name and age are instance variables, as their values may be different for each object. 
A class attribute or variable whose value is shared among all the instances of a in this class. 
A class attribute represents common attribute of all objects of a class.

Class attributes are not initialized inside __init__() constructor. 
They are defined in the class, but outside any method. 
"""
#Example 2
"""
Let us add a class variable called empCount in Employee class. 
For each object declared, the __init__() method is automatically called. 
This method initializes the instance variables as well as increments the empCount by 1."""

class Emp:
    #create class variable 
    empCount=0
    #create constructor
    def __init__(self,name,age):
        self.name1=name
        self.age1=age
        Emp.empCount+=1
        print("Name :",self.name1,"\tAge: ",self.age1)
        print("Employee number: ",Emp.empCount)

#Create instances of class
e1=Emp("Shary",24)
e2=Emp("Umair",23)
e3=Emp("Fahad",22)
        
        
    