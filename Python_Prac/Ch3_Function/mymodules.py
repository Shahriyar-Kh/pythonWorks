"The doc string of mymodules"
def sum(x,y):
    c=x+y
    return print("Additon of two numbers: ",c)
def avg(x,y):
     return x+y/2
def power(x,y):
     return x**y
 
"""
1. __name__ is a special variable in Python. When a Python script is executed,
__name__ is set to "__main__" if the script is being run as the main program.
If the script is imported as a module into another script,
__name__ is set to the name of the module (not "__main__").

2. if __name__ == "__main__": checks if the script is being run as the main program.
If true, the code inside the block will be executed.

3. Inside the block, print("M_Sum: ", sum(4, 5)) is calling a function named sum with the arguments 4 and 5.
However, there's a potential issue here. The built-in sum function in 
Python takes an iterable (like a list) as its argument, not individual values.
If you want to sum these two values, 
you might want to use the + operator instead:"""

if __name__=="__main__":
    print("M_Sum: ",sum(4,5))
    
 