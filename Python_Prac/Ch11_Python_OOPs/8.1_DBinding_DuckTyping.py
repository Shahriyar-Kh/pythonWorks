#Example 1
class shape:
   def draw(self):
      print ("draw method")
      return
class circle(shape):
   def draw(self):
      print ("Draw a circle")
      return
class rectangle(shape):
   def draw(self):
      print ("Draw a rectangle")
      return
shapes = [circle(), rectangle()]
for shp in shapes:
   shp.draw()

# Example of Duck Typing in Python
# Define a class 'circle'
class Circle:
    def draw(self):
        print("Draw circle")
        return

# Define a class 'rectangle'
class Rectangle:
    def draw(self):
        print("Draw rectangle")
        return

# Define a class 'area'
class Area:
    def draw(self):
        print("Calculate area")
        return

# Define a function 'duck_Function' that takes any object with a 'draw' method
def duck_Function(obj):
    obj.draw()

# Create instances of the classes
objects = [Circle(), Rectangle(), Area()]

# Print a newline for better output readability
print("\n")

# Iterate through the list of objects
for obj in objects:
    # Call the 'duck_Function' on each object, which calls the 'draw' method of each object
    duck_Function(obj)
