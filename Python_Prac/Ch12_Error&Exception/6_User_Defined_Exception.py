# Define a custom exception class named myException that inherits from the built-in Exception class
class myException(Exception):
    'invalid marks'
    pass

# Assign a value to the variable 'num'
num = 110

# Use a try-except block to handle potential exceptions
try:
    # Check if the value of 'num' is outside the valid range (less than 0 or greater than 100)
    if num < 0 or num > 100:
        # If the condition is met, raise the custom exception 'myException'
        raise myException
except myException as e:
    # Catch and handle the custom exception by printing an error message along with the invalid 'num' value
    print("invalid marks", num)
else:
    # If no exception is raised, execute this block and print a message indicating valid 'num' value
    print("Marks obtained", num)
