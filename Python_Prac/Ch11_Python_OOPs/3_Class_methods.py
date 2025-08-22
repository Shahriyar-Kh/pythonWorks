#Example 1
class Employee:
    #  Create class variable initialized to 0
    empCount=0
    #The __init__ method is the constructor that gets called when an object of the class is created.
    def __init__(self,name,age):
        #Instance variables value passed during obj creation
        self.name1=name
        self.age1=age
        #It increments the class variable empCount by 1, indicating the creation of a new employee.
        Employee.empCount+=1
    
    #Class method
    def showCount(self):
        #This is an instance method named showcount that prints the current value of the class variable empCount
        print("Total Employees: ",self.empCount)
        """
        This line creates a class method named counter using the classmethod decorator.
        The counter class method is associated with the showcount instance method.
        """
    #Class method  using classmethod decorator
    Counter=classmethod(showCount)
    
#Creates instanses or object
obj1=Employee("Shary",25)
obj2=Employee("Fahad",23)

#Calling instance method
obj1.showCount()#This calls the showcount instance method for the e1 object, which prints the current value of empCount.

#Calling class method
Employee.Counter()#It also prints the current value of empCount because the class method has access to the class variables.
"""
Using @classmethod() decorator is the prescribed way to define 
a class method as it is more convenient than first declaring 
an instance method and then transforming to a class method.
"""
@classmethod
def showCount1(cls):
        print(cls.empCount)
        return
@classmethod
def newemployee(cls,name,age):
        return cls(name,age)

obj3=Employee("Shary",34)
obj3=Employee("Umair",24)
obj4=Employee.newemployee("Khan",10)
Employee.showCount1()


#important points
"""
Class Methods and Variables:
Class Variables:
Class variables are shared among all instances of a class. They are defined outside any method in the class and are accessed using the class name.

python
Copy code
class MyClass:
    class_variable = 0

obj1 = MyClass()
obj2 = MyClass()

MyClass.class_variable = 10

print(obj1.class_variable)  # Output: 10
print(obj2.class_variable)  # Output: 10

Class Methods:
Class methods are defined using the @classmethod decorator. They take the class as the first parameter (cls) instead of the instance (self). Class methods can access and modify class variables.
class MyClass:
    class_variable = 0

    @classmethod
    def update_class_variable(cls, new_value):
        cls.class_variable = new_value

obj1 = MyClass()
obj2 = MyClass()

print(obj1.class_variable)  # Output: 0

MyClass.update_class_variable(20)

print(obj1.class_variable)  # Output: 20
print(obj2.class_variable)  # Output: 20
    """
    
    