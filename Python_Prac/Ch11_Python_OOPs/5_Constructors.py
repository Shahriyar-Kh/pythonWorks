#Example 1
class Employee:
    "Common base class for all employees"
    #Create Constructors(defult)
    def __init__(self):
        self.name1="Shary"
        self.age1=25
#Create instanse
obj1=Employee()
print(f"Name: {obj1.name1}")
print(f"Age: {obj1.age1}")

#Create 2nd object
obj2=Employee()
print(f"Name: {obj2.name1}")
print(f"Age: {obj2.age1}")

#Note bydefult constructor each object we declare will have same value for its instance variables name and age.

#Example 2
class Employee:
    "Common base class for all employees"
    #Create Parameterized Constructor
    def __init__(self,name,age):
        self.name1=name
        self.age1=age
        
#Create instances and pass arguments
obj1=Employee("Ali",20)       
print(f"Name: {obj1.name1}")
print(f"Age: {obj1.age1}")

#Create 2nd object
obj2=Employee("Fahad",30)
print(f"Name: {obj2.name1}")
print(f"Age: {obj2.age1}")

"""
You can assign defaults to the formal arguments in the constructor 
so that the object can be instantiated with or without passing parameters.
        """
        
#Example 3
class Employee:
    "Common base class for all employees"
    #Create Parameterized Constructor
    def __init__(self,name="Umair",age=40):
        self.name1=name
        self.age1=age
        
#Create instances and pass arguments
obj1=Employee("Ali",20)       
print(f"Name: {obj1.name1}")
print(f"Age: {obj1.age1}")

#Create 2nd object without parameter so its using the above defult values
obj2=Employee()
print(f"Name: {obj2.name1}")
print(f"Age: {obj2.age1}")

#1.5.2  Python - Instance Methods
"""
In addition to the __init__() constructor, there may be one or more instance methods defined in a class. 
A method with self as one of the formal arguments is called instance method, as it is called by a specific object."""
#Example 5
"""In the following example a displayEmployee() method has been defined. It returns the name and age attributes of the Employee object that calls the method."""
class Employee:
    "Common base class for all employees"
    #Create Parameterized Constructor
    def __init__(self,name="Umair",age=40):
        self.name1=name
        self.age1=age
    def displayEmp(self):
        print(f"Name: {self.name1} Age:{self.age1}")
        
#Create objects
obj3=Employee()
obj4=Employee("Ayan",10)

#calling displayEmp using obj
obj3.displayEmp()
obj4.displayEmp()

#You can add, remove, or modify attributes of classes and objects at any time
obj3.salary=700 #Add a salary attribute
print(f"Name: {obj3.name1} Age:{obj3.age1} Salary: {obj3.salary}")
obj3.name1="Umair khan"#Modify name attribute
print(f"Name: {obj3.name1} Age:{obj3.age1} Salary: {obj3.salary}")
del obj3.salary #delete salary attribute
#print(f"Name: {obj3.name1} Age:{obj3.age1} Salary: {obj3.salary}")
#AttributeError: 'Employee' object has no attribute 'salary' 


"""
Instead of using the normal statements to access attributes, you can use the following functions −

The getattr(obj, name[, default]) − to access the attribute of object.

The hasattr(obj,name) − to check if an attribute exists or not.

The setattr(obj,name,value) − to set an attribute. If attribute does not exist, then it would be created.

The delattr(obj, name) − to delete an attribute.
        """
print(hasattr(obj3,'salary'))# Returns true if 'salary' attribute exists
setattr(obj3,'salary',8000)# Set attribute 'salary' at 8
print(getattr(obj3,'salary'))# Returns value of name attribute
delattr(obj3,'salary')# Returns value of name attribute

