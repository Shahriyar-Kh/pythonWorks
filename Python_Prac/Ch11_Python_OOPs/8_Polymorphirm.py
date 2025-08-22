#Example 1  Different classes with the same method:
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Drive!")
class Boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Sail!")
class Plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Fly!")
        
#create Car instance
car1=Car("Ford","Mustang")

#create Boat instance
boat1=Boat("Ibiza","Touring 20")

#Create Plane instance
plane1=Plane("Boeing","747")

for i in (car1,boat1,plane1):
    i.move()
#Output
# Drive!
#Sail!
#Fly!
#Note : Look at the for loop at the end. Because of polymorphism we can execute the same method for all three classes.

# 8.1 Inheritance Class Polymorphism
"""
What about classes with child classes with the same name? Can we use polymorphism there?

Yes. If we use the example above and make a parent class called Vehicle, 
and make Car, Boat, Plane child classes of Vehicle, the child classes inherits the Vehicle methods, but can override them:
    """

#Example 2
class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Move!")
        
class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail")
class Plane(Vehicle):
    def move(self):
        print("Fly!")
car2=Car("NE","Mustang")
boat2=Boat("Ibiza2","Touring 30")
plane2=Plane("Boeing2","700")

for j in (car2,boat2,plane2):
    print("\n",i.brand)
    print(j.model)
    j.move()
    
    
#Example 3
"""
As an example of polymorphism given below, we have shape which is an abstract class.
It is used as parent by two classes circle and rectangle. Both classes overrideparent's draw() method in different ways."""   

# Import the ABC (Abstract Base Class) and abstractmethod from the abc module
from abc import ABC, abstractmethod
# Define an abstract class 'shape' that inherits from ABC (Abstract Base Class)
class shape(ABC):
    # Define an abstract method 'draw'
    @abstractmethod
    def draw(self):
        "Abstract method"
        return
# Define a concrete class 'circle' that inherits from the 'shape' class
class circle(shape):
    # Implement the 'draw' method for the 'circle' class
    def draw(self):
        #super().draw()  # Call the 'draw' method of the base class (shape) if it exists
        print("Draw a circle")  # Print a message indicating drawing a circle
        return
# Define a concrete class 'rectangle' that inherits from the 'shape' class
class rectangle(shape):
    # Implement the 'draw' method for the 'rectangle' class
    def draw(self):
        #super().draw()  # Call the 'draw' method of the base class (shape) if it exists
        print("Draw a rectangle")  # Print a message indicating drawing a rectangle
        return
# Create a list 'shapes' containing instances of 'circle' and 'rectangle'
shapes = [circle(), rectangle()]
# Iterate through each shape in the 'shapes' list and call the 'draw' method
for shp in shapes:
    shp.draw()
