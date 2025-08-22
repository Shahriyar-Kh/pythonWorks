#Example 1
class Employee:
   empCount = 0
   def __init__(self, name, age):
      self.__name = name
      self.__age = age
      Employee.empCount += 1
    
    #Create a static method using @static method decorator
   @staticmethod #tecnique 1
   def showCount():
       print("Total Eployees:",Employee.empCount)##It prints the current value of the class variable empCount.
       return
   #Also create from this tecnique 2
   counter=staticmethod(showCount)
   
#Create object
obj1=Employee("Shary",45)
obj2=Employee("Hamad",14)
#Calling Static Method using an Instance
obj1.counter()

#Calling Static Method using the Class:
Employee.counter()

#Also work
Employee.showCount()