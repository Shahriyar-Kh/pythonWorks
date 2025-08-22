#Example 1
from abc import ABC,abstractmethod

class demointerface(ABC):
    
    @abstractmethod
    def method1(self):
        print("Abstract method1")
        return
    @abstractmethod
    def method2(self):
        print("Abstract method2")
        return
    
class ConcreteClass(demointerface):
    def method1(self):
        #super().method1()
        print("concrete Method1")
        return
    def method2(self):
        #super().method2()
        print("concrete Method2")
        return
    
# obj1=demo() TypeError: Can't instantiate abstract class demo with abstract methods method1, method2
obj2=ConcreteClass()
obj2.method1()
obj2.method2()