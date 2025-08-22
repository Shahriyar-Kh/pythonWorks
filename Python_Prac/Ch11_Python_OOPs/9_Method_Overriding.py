#Example 1
class Parent:#define parent class
    def mymethod(self):
        print("Calling Parent method")
        
class Child(Parent):#defin child class
    def mymethod(self):
        print("Calling child method")
c=Child()#instance of child Class
c.mymethod()#Child calls overriden method

# Example 2
"""To understand inheritance in Python, let us take another example.
We use the following Employee class as a parent class."""

# Define a class 'Employee' as the parent class
class Employee:
    # Constructor to initialize name and salary attributes
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Method to get the name of the employee
    def getname(self):
        return self.name

    # Method to get the salary of the employee
    def getsalary(self):
        return self.salary

# Define a class 'SalesOffice' that inherits from the 'Employee' class
class SalesOffice(Employee):
    # Constructor to initialize name, salary, and incentive attributes
    def __init__(self, name, salary, inc):
        # Call the constructor of the base class ('Employee') using super()
        super().__init__(name, salary)
        # Additionally, the child class has one more instance variable 'incentive'
        self.incentive = inc

    # Override the getsalary() method to add the incentive to the salary
    def getsalary(self):
        return self.salary + self.incentive

# Create an instance 'obj1' of the 'Employee' class
obj1 = Employee("Shary", 9000)
# Print the total salary for 'obj1' using getname() and getsalary() methods
print("Total salary for {} is Rs {}".format(obj1.getname(), obj1.getsalary()))

# Create an instance 'obj2' of the 'SalesOffice' class with an incentive of 500
obj2 = SalesOffice("Hamad", 10000, 500)
# Print the total salary for 'obj2' using getname() and getsalary() methods
print("Total salary for {} is Rs {}".format(obj2.getname(), obj2.getsalary()))
