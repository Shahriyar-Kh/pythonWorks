# Define the Student class
class Student:
    # Constructor to initialize the student object with a name
    def __init__(self, name):
        # Assign the provided name to the 'name' attribute
        self.name = name
        # Create an instance of the subjects class and assign it to the 'subs' attribute
        self.subs = self.subjects()

    # Method to display the student's name and subjects
    def show(self):
        # Print the student's name and call the display method of the subjects class
        print(f"Name: {self.name} Subjects: {self.subs.display()}")

    # Inner class for representing subjects
    class subjects:
        # Constructor to initialize subjects (HCI and MAD)
        def __init__(self):
            # Assign the subject names to 'sub1' and 'sub2' attributes
            self.sub1 = "HCI"
            self.sub2 = "MAD"

        # Method to display subjects
        def display(self):
            # Return a formatted string representing the subjects
            return f"{self.sub1}, {self.sub2}"
# Create an instance of the Student class with the name "Shary"
obj1 = Student("Shary")
# Call the show method to display information about the student and subjects
obj1.show()
"""
It is quite possible to declare an object of outer class independently, 
and make it call its own display() method.
"""
sub=Student("Umair").subjects().display()
