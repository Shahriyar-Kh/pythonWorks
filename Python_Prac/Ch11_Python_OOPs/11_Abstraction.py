#Example 1 
from abc import ABC,abstractmethod
class demo(ABC):
    @abstractmethod
    def methed1(self):
        print("Abstact Method")
        return
    def methed2(self):
        print("Concrete Method")
#obj1=demo()    #TypeError: Can't instantiate abstract class demo with abstract method method1
"""
The demo class here may be used as parent for another class. However, the child class must override the abstract method in parent class. 
If not, Python throws this error −
TypeError: Can't instantiate abstract class concreteclass with abstract method met

"""
#the child class with the abstract method overridden is given in the following example 
from abc import ABC,abstractmethod
class demo(ABC):
    @abstractmethod
    def methed1(self):
        print("Abstact Method")
        return
    def methed2(self):
        print("Concrete Method")
        
class concreteClass(demo):
    def methed1(self):
        super().methed1()
        return
obj2=concreteClass()
obj2.methed1()
obj2.methed2()

