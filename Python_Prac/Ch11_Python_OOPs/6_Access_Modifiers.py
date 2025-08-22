#Example 1
class Employee:
    "Common base class for all employee"
    #Create overload constructor
    def __init__(self,name="Shary",age=25):
        #Create instance variable
        self.name=name
        self.age=age
        
#Create instance 
obj1=Employee()#no arguments pass so using default parameters
obj2=Employee("Ali",25)#pass args so using this

#Output
#1st obj
print(f"Name: {obj1.name}")#shary
print(f"age: {obj1.age}")#24
#2nd obj
print(f"Name: {obj2.name}")#ali
print(f"age: {obj2.age}")#25

"""
Python doesn't enforce restrictions on accessing any instance variable or method. 
However, Python prescribes a convention of prefixing name of variable/method with 
single or double underscore to emulate behavior of protected and private access modifiers.

To indicate that an instance variable is private, prefix it with double underscore (such as "__age"). 
To imply that a certain instance variable is protected, prefix it with single underscore (such as "_salary")
        """


"""
Let us modify the Employee class. Add another instance variable salary. 
Make age private and salary as protected by prefixing double and single underscores respectively.
"""    
#Example 2 using Private and protected

class Employee:
    #Create overload constructor
    def __init__(self,name,age,salary):
        self.name=name #public varaible(anywhere acess with any pakage)
        self.__age=age #private variable private access within class and not access without pakage 
        self._salary=salary# variable protected no access out of class
    def displayEmployee(self):
        print(f"Name: {self.name} age: {self.__age} salary:{self._salary}")
        
obj3=Employee("Khan",25,1200)
print("\nPublic name",obj3.name)
print("protected salary",obj3._salary)#protected
#print(obj3.__age)#private not access out of class

# 6.1 Name Mangling
"""
Python doesn't block access to private data, it just leaves for the wisdom of the programmer,
not to write any code that access it from outside the class. 
You can still access the private members by Python's name mangling technique.

Name mangling is the process of changing name of a member with double underscore to the form object._class__variable. 
If so required, it can still be accessed from outside the class, 
but the practice should be refrained.

Sayntax :obj._class__privatevalue
"""
#We can access private value
print("(Private) age:",obj3._Employee__age)

#Example of getter and setter methods

class Employee:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    
    def set_name(self,name):
        self.__name=name
        return
    def set_age(self,age):
        self.__age=age
        
obj5=Employee("Shary",24)
print("get_Name:",obj5.get_name(),"get_age: ",obj5.get_age())

obj5.set_name("Ali")
obj5.set_age(25)
print("Get_Name:",obj5.get_name(),"Get_Age:",obj5.get_age())


#Example The complete program with property objects and their use is given below −

class Employee:
     
     def __init__(self,name,age):
         self.__name=name
         self.__age=age
     def get_n(self):
         return self.__name
     def get_a(self):
         return self.__age
     
     def set_n(self,name):
         self.__name=name
         return
     def set_a(self,age):
         self.__age=age
         return
     name=property(get_n,set_n,"name")
     age=property(get_a,set_a,"Age")
     
obj6=Employee("Sufyaan",40)
print("\nName:",obj6.name,"Age",obj6.age)

obj6.name='Changed name'
obj6.age=80
print("Name:",obj6.name,"Age:",obj6.age)
         
