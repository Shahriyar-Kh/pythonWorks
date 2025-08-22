# Define a class named 'singleton'
class singleton:
    # Class variable to hold the single instance of the class
    _instance = None
    
    # Define a special method '__new__' which is called to create a new instance of the class
    def __new__(cls):
        # Check if the class variable '_instance' is None (indicating no instance has been created yet)
        if cls._instance is None:
            print("Creating the object")
            # Create a new instance of the class using the super() function
            cls._instance = super(singleton, cls).__new__(cls)
            
        # Return the existing instance if it already exists, otherwise, return the new instance
        return cls._instance

# Create an instance of the 'singleton' class
obj1 = singleton()
# Print the instance (memory address) of the created object
print(obj1)

# Create another instance of the 'singleton' class
obj2 = singleton()
# Print the instance (memory address) of the second object
